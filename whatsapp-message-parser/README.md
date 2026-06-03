# WhatsApp Message Parser

Extract useful structured data from exported WhatsApp chat messages.

## Features
- Parses common WhatsApp export formats
- Extracts date, time, sender, and message text
- Exports structured data to CSV

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --input chat.txt --output messages.csv
```

The output CSV contains `date`, `time`, `sender`, and `message` columns.
