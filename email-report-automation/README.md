# Email Report Automation

Generate a summary report from a CSV file and send it by email automatically.

## Features
- CSV-based report generation
- Plain-text email report body
- SMTP integration using environment variables

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Generate a report preview

```bash
python main.py --csv sales.csv --preview
```

### Send the report by email

```bash
set SMTP_HOST=smtp.example.com
set SMTP_PORT=587
set SMTP_USER=your_user
set SMTP_PASSWORD=your_password
set EMAIL_FROM=reports@example.com
python main.py --csv sales.csv --to manager@example.com --subject "Daily Sales Report"
```
