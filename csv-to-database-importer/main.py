import argparse
import csv
import re
import sqlite3
from pathlib import Path


def normalize_identifier(value):
    identifier = re.sub(r"[^a-zA-Z0-9_]+", "_", value.strip()).strip("_")
    if not identifier:
        raise ValueError("Identifier cannot be empty.")
    return identifier


def validate_rows(rows, required_columns):
    for column in required_columns:
        if rows and column not in rows[0]:
            raise SystemExit(f"Required column not found: {column}")

    for index, row in enumerate(rows, start=1):
        for column in required_columns:
            if not row.get(column, "").strip():
                raise SystemExit(f"Missing value for '{column}' on row {index}.")


def import_csv(csv_path, db_path, table_name, required_columns):
    with Path(csv_path).open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        rows = list(reader)
        columns = reader.fieldnames or []

    validate_rows(rows, required_columns)

    safe_table = normalize_identifier(table_name)
    safe_columns = [normalize_identifier(column) for column in columns]
    column_sql = ", ".join(f'"{column}" TEXT' for column in safe_columns)
    placeholders = ", ".join("?" for _ in safe_columns)

    with sqlite3.connect(db_path) as connection:
        connection.execute(f'CREATE TABLE IF NOT EXISTS "{safe_table}" ({column_sql})')
        connection.executemany(
            f'INSERT INTO "{safe_table}" ({", ".join(f"""\"{column}\"""" for column in safe_columns)}) VALUES ({placeholders})',
            [[row.get(column, "") for column in columns] for row in rows],
        )

    return len(rows)


def main():
    parser = argparse.ArgumentParser(description="Import a CSV file into a SQLite database.")
    parser.add_argument("--csv", required=True, help="Input CSV file.")
    parser.add_argument("--db", required=True, help="SQLite database path.")
    parser.add_argument("--table", required=True, help="Target table name.")
    parser.add_argument("--required", nargs="*", default=[], help="Columns that must exist and contain values.")
    args = parser.parse_args()

    inserted = import_csv(args.csv, args.db, args.table, args.required)
    print(f"Imported {inserted} rows into {args.db}:{args.table}.")


if __name__ == "__main__":
    main()
