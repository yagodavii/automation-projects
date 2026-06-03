# API Data Sync

Synchronize data between an API and a local SQLite database.

## Features
- Fetches JSON data from an API
- Stores synchronized records in SQLite
- Uses a configurable record ID field
- Keeps the latest version of each record

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Sync API data into SQLite

```bash
python main.py --source-url "https://jsonplaceholder.typicode.com/users" --db sync.db --table users --id-field id
```

The API response can be either a JSON array or an object containing an `items` array.
