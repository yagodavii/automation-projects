import argparse
import csv
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path


def build_report(csv_path):
    path = Path(csv_path)
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        return f"Report for {path.name}\n\nNo rows found."

    columns = rows[0].keys()
    report_lines = [
        f"Report for {path.name}",
        "",
        f"Total rows: {len(rows)}",
        f"Columns: {', '.join(columns)}",
        "",
        "First records:",
    ]

    for row in rows[:5]:
        preview = ", ".join(f"{key}={value}" for key, value in row.items())
        report_lines.append(f"- {preview}")

    return "\n".join(report_lines)


def send_email(to_address, subject, body):
    host = os.environ["SMTP_HOST"]
    port = int(os.environ.get("SMTP_PORT", "587"))
    username = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASSWORD"]
    from_address = os.environ.get("EMAIL_FROM", username)

    message = EmailMessage()
    message["From"] = from_address
    message["To"] = to_address
    message["Subject"] = subject
    message.set_content(body)

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)


def main():
    parser = argparse.ArgumentParser(description="Generate and email a CSV summary report.")
    parser.add_argument("--csv", required=True, help="Path to the CSV file used for the report.")
    parser.add_argument("--to", help="Recipient email address.")
    parser.add_argument("--subject", default="Automated Report", help="Email subject.")
    parser.add_argument("--preview", action="store_true", help="Print the report without sending email.")
    args = parser.parse_args()

    report = build_report(args.csv)

    if args.preview:
        print(report)
        return

    if not args.to:
        raise SystemExit("--to is required unless --preview is used.")

    send_email(args.to, args.subject, report)
    print(f"Report sent to {args.to}.")


if __name__ == "__main__":
    main()
