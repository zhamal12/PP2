# PhoneBook Extended — TSIS 1

Extended contact-management console application built with **Python 3 + psycopg2 + PostgreSQL**.

Extends the work from Practice 7 (CRUD, CSV import, basic search) and Practice 8 (pattern-search function, upsert procedure, bulk-insert, paginated query function, delete procedure).

---

## Features added in TSIS 1

| # | Feature | File |
|---|---------|------|
| 3.1 | `phones` table, `groups` table, `email`, `birthday` columns | `schema.sql` |
| 3.2 | Filter by group, search by email, sort by name/birthday/date | `phonebook.py` |
| 3.2 | Paginated console navigation (next / prev / quit) | `phonebook.py` |
| 3.3 | Export all contacts → JSON | `phonebook.py` |
| 3.3 | Import contacts ← JSON with skip/overwrite on duplicate | `phonebook.py` |
| 3.3 | Extended CSV import (email, birthday, group, phone type) | `phonebook.py` |
| 3.4 | Procedure `add_phone(name, phone, type)` | `procedures.sql` |
| 3.4 | Procedure `move_to_group(name, group)` — creates group if absent | `procedures.sql` |
| 3.4 | Function `search_contacts(query)` — matches name, email, all phones | `procedures.sql` |

---

## Repository structure

```
TSIS1/
├── phonebook.py      # Main console application
├── config.py         # DB connection settings  ← edit this
├── connect.py        # psycopg2 connection helper
├── schema.sql        # CREATE TABLE statements (idempotent)
├── procedures.sql    # PL/pgSQL procedures & functions
└── contacts.csv      # Sample CSV with extended fields
```

---

## Quick start

### 1. Create the database

```bash
psql -U postgres -c "CREATE DATABASE phonebook;"
```

### 2. Configure connection

Edit `config.py` and set your password / host:

```python
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "phonebook",
    "user":     "postgres",
    "password": "your_password_here",
}
```

### 3. Install dependency

```bash
pip install psycopg2-binary
```

### 4. Run the application

```bash
python phonebook.py
```

The app will automatically execute `schema.sql` and `procedures.sql` on first run.

---

## CSV format

The extended CSV importer expects this header row:

```
name,phone,phone_type,email,birthday,group
```

Multiple rows with the **same name** are merged into one contact with multiple phones.

---

## JSON export / import format

```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice@gmail.com",
    "birthday": "1990-03-15",
    "group_name": "Friend",
    "created_at": "2025-01-01T10:00:00",
    "phones": [
      {"phone": "+1-555-0101", "type": "mobile"},
      {"phone": "+1-555-0102", "type": "work"}
    ]
  }
]
```

On import, if a contact with the same **name** already exists, the app asks:
- `[s]kip` — leave the existing record unchanged
- `[o]verwrite` — update email/birthday/group and replace all phones

---

## Stored procedures & functions (PL/pgSQL)

```sql
-- Add a phone number to an existing contact
CALL add_phone('Alice Johnson', '+1-555-9999', 'work');

-- Move a contact to a group (creates the group if it doesn't exist)
CALL move_to_group('Alice Johnson', 'VIP');

-- Search across name, email, and all phones
SELECT * FROM search_contacts('gmail');
SELECT * FROM search_contacts('+1-555');
```
