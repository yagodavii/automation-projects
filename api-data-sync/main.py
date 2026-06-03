import argparse
import json
import re
import sqlite3
from datetime import datetime, timezone
from urllib.request import Request, urlopen


def normalize_identifier(value):
    identifier = re.sub(r"[^a-zA-Z0-9_]+", "_", value.strip()).strip("_")
    if not identifier:
        raise ValueError("Identifier cannot be empty.")
    return identifier


def fetch_json(url):
    request = Request(url, headers={"User-Agent": "api-data-sync/1.0"})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("items"), list):
        return payload["items"]
    raise SystemExit("Expected a JSON array or an object with an 'items' array.")


def sync_to_database(items, db_path, table_name, id_field):
    safe_table = normalize_identifier(table_name)
    synced_at = datetime.now(timezone.utc).isoformat()

    with sqlite3.connect(db_path) as connection:
        connection.execute(
            f"""
            CREATE TABLE IF NOT EXISTS "{safe_table}" (
                id TEXT PRIMARY KEY,
                payload TEXT NOT NULL,
                synced_at TEXT NOT NULL
            )
            """
        )

        for item in items:
            if not isinstance(item, dict):
                continue
            record_id = item.get(id_field)
            if record_id is None:
                continue
            connection.execute(
                f"""
                INSERT INTO "{safe_table}" (id, payload, synced_at)
                VALUES (?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    payload = excluded.payload,
                    synced_at = excluded.synced_at
                """,
                (str(record_id), json.dumps(item, ensure_ascii=False), synced_at),
            )


def main():
    parser = argparse.ArgumentParser(description="Synchronize API data into a SQLite database.")
    parser.add_argument("--source-url", required=True, help="API endpoint that returns JSON data.")
    parser.add_argument("--db", required=True, help="SQLite database path.")
    parser.add_argument("--table", required=True, help="Target table name.")
    parser.add_argument("--id-field", default="id", help="Field used as the record identifier.")
    args = parser.parse_args()

    payload = fetch_json(args.source_url)
    items = extract_items(payload)
    sync_to_database(items, args.db, args.table, args.id_field)
    print(f"Synchronized {len(items)} records into {args.db}:{args.table}.")


if __name__ == "__main__":
    main()
