import argparse
import csv
import re
from pathlib import Path


def normalize_column_name(name):
    cleaned = name.strip().lower()
    cleaned = re.sub(r"[^a-z0-9]+", "_", cleaned)
    return cleaned.strip("_")


def clean_value(value):
    return " ".join(value.strip().split()) if isinstance(value, str) else value


def clean_csv(input_path, output_path, sort_by=None):
    with Path(input_path).open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = [normalize_column_name(name) for name in reader.fieldnames or []]

        rows = []
        seen = set()
        for raw_row in reader:
            cleaned_row = {
                normalize_column_name(key): clean_value(value)
                for key, value in raw_row.items()
            }
            signature = tuple(cleaned_row.get(field, "") for field in fieldnames)
            if signature not in seen:
                seen.add(signature)
                rows.append(cleaned_row)

    if sort_by:
        if sort_by not in fieldnames:
            raise SystemExit(f"Column not found: {sort_by}")
        rows.sort(key=lambda row: row.get(sort_by, ""))

    with Path(output_path).open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)


def main():
    parser = argparse.ArgumentParser(description="Clean and standardize CSV data.")
    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--output", required=True, help="Output CSV file.")
    parser.add_argument("--sort-by", help="Optional normalized column name used for sorting.")
    args = parser.parse_args()

    row_count = clean_csv(args.input, args.output, args.sort_by)
    print(f"Cleaned {row_count} rows into {args.output}.")


if __name__ == "__main__":
    main()
