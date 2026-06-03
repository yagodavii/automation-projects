import argparse
import csv
import re
from pathlib import Path


MESSAGE_PATTERNS = [
    re.compile(r"^\[(?P<date>\d{1,2}/\d{1,2}/\d{2,4}), (?P<time>\d{1,2}:\d{2}(?::\d{2})?)\] (?P<sender>.*?): (?P<message>.*)$"),
    re.compile(r"^(?P<date>\d{1,2}/\d{1,2}/\d{2,4}), (?P<time>\d{1,2}:\d{2}) - (?P<sender>.*?): (?P<message>.*)$"),
]


def parse_chat(input_path):
    messages = []
    current = None

    for line in Path(input_path).read_text(encoding="utf-8").splitlines():
        match = next((pattern.match(line) for pattern in MESSAGE_PATTERNS if pattern.match(line)), None)

        if match:
            current = match.groupdict()
            messages.append(current)
        elif current:
            current["message"] += "\n" + line

    return messages


def export_csv(messages, output_path):
    with Path(output_path).open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["date", "time", "sender", "message"])
        writer.writeheader()
        writer.writerows(messages)


def main():
    parser = argparse.ArgumentParser(description="Parse exported WhatsApp messages into CSV.")
    parser.add_argument("--input", required=True, help="WhatsApp exported .txt file.")
    parser.add_argument("--output", required=True, help="Output CSV file.")
    args = parser.parse_args()

    messages = parse_chat(args.input)
    export_csv(messages, args.output)
    print(f"Parsed {len(messages)} messages into {args.output}.")


if __name__ == "__main__":
    main()
