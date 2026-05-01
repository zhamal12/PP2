#!/usr/bin/env python3
"""
phonebook.py  –  PhoneBook Extended Console Application  (TSIS 1)

Builds on top of the CRUD / search / pagination work from Practice 7 & 8.
New features implemented here:
  • Extended schema (phones table, groups, email, birthday)
  • Filter by group, search by email, sort by name/birthday/date
  • Paginated console navigation (next / prev / quit)
  • Export contacts → JSON
  • Import contacts ← JSON  (with duplicate handling)
  • Extended CSV import  (email, birthday, group, phone type)
  • Stored procedures: add_phone, move_to_group
  • DB function:        search_contacts  (name + email + all phones)
"""

import csv
import json
import sys
from datetime import date, datetime

import psycopg2
from psycopg2.extras import RealDictCursor

from connect import get_connection, get_cursor

# ── pretty printing ────────────────────────────────────────────────────────────

DIVIDER = "─" * 72


def _fmt_row(row: dict) -> str:
    """Format a contact row (from v_contacts view) for display."""
    parts = [
        f"  ID      : {row['id']}",
        f"  Name    : {row['name']}",
        f"  Email   : {row.get('email') or '—'}",
        f"  Birthday: {row.get('birthday') or '—'}",
        f"  Group   : {row.get('group_name') or '—'}",
        f"  Phones  : {row.get('phones') or '—'}",
        f"  Added   : {row.get('created_at', '')!s:.19}",
    ]
    return "\n".join(parts)


def _print_contacts(rows):
    if not rows:
        print("  (no contacts found)")
        return
    for row in rows:
        print(DIVIDER)
        print(_fmt_row(row))
    print(DIVIDER)
    print(f"  {len(rows)} contact(s) shown.")


# ── low-level helpers ──────────────────────────────────────────────────────────

def _get_or_create_group(cur, group_name: str) -> int:
    """Return group id, creating the group if it doesn't exist."""
    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    row = cur.fetchone()
    if row:
        return row["id"]
    cur.execute(
        "INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,)
    )
    return cur.fetchone()["id"]


def _find_contact_by_name(cur, name: str):
    cur.execute("SELECT * FROM contacts WHERE name = %s LIMIT 1", (name,))
    return cur.fetchone()


def _list_groups(conn) -> list[dict]:
    with get_cursor(conn) as cur:
        cur.execute("SELECT id, name FROM groups ORDER BY name")
        return cur.fetchall()


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3.1 – Schema bootstrap  (called once at startup)
# ══════════════════════════════════════════════════════════════════════════════

def apply_schema(conn):
    """Run schema.sql and procedures.sql if the tables don't exist yet."""
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    for fname in ("schema.sql", "procedures.sql"):
        fpath = os.path.join(base, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as fh:
            sql = fh.read()
        try:
            with get_cursor(conn) as cur:
                cur.execute(sql)
            conn.commit()
            print(f"  [OK] Applied {fname}")
        except Exception as exc:
            conn.rollback()
            print(f"  [WARN] {fname}: {exc}")


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3.2 – Advanced Console Search & Filter
# ══════════════════════════════════════════════════════════════════════════════

def filter_by_group(conn):
    """Show contacts belonging to a chosen group."""
    groups = _list_groups(conn)
    if not groups:
        print("No groups in database.")
        return

    print("\nAvailable groups:")
    for g in groups:
        print(f"  [{g['id']}] {g['name']}")

    choice = input("Enter group ID (or name): ").strip()
    try:
        gid = int(choice)
    except ValueError:
        # looked up by name
        with get_cursor(conn) as cur:
            cur.execute("SELECT id FROM groups WHERE name ILIKE %s", (choice,))
            row = cur.fetchone()
        if not row:
            print(f"Group '{choice}' not found.")
            return
        gid = row["id"]

    with get_cursor(conn) as cur:
        cur.execute(
            """
            SELECT c.id, c.name, c.email, c.birthday,
                   g.name AS group_name,
                   STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones,
                   c.created_at
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            WHERE c.group_id = %s
            GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
            ORDER BY c.name
            """,
            (gid,),
        )
        _print_contacts(cur.fetchall())


def search_by_email(conn):
    """Partial-match search against the email field."""
    query = input("Email fragment to search: ").strip()
    if not query:
        return
    pattern = f"%{query}%"
    with get_cursor(conn) as cur:
        cur.execute(
            """
            SELECT c.id, c.name, c.email, c.birthday,
                   g.name AS group_name,
                   STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones,
                   c.created_at
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            WHERE c.email ILIKE %s
            GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
            ORDER BY c.name
            """,
            (pattern,),
        )
        _print_contacts(cur.fetchall())


def sort_contacts(conn):
    """Display all contacts sorted by user's choice."""
    sort_options = {
        "1": ("name",       "c.name ASC"),
        "2": ("birthday",   "c.birthday ASC NULLS LAST"),
        "3": ("date added", "c.created_at ASC"),
    }
    print("\nSort by:")
    for k, (label, _) in sort_options.items():
        print(f"  [{k}] {label}")
    choice = input("Choice [1-3]: ").strip()
    order = sort_options.get(choice, ("name", "c.name ASC"))[1]

    with get_cursor(conn) as cur:
        cur.execute(
            f"""
            SELECT c.id, c.name, c.email, c.birthday,
                   g.name AS group_name,
                   STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones,
                   c.created_at
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
            ORDER BY {order}
            """
        )
        _print_contacts(cur.fetchall())


# ── paginated navigation ───────────────────────────────────────────────────────

PAGE_SIZE = 5


def _fetch_page(conn, offset: int) -> list[dict]:
    with get_cursor(conn) as cur:
        cur.execute(
            """
            SELECT c.id, c.name, c.email, c.birthday,
                   g.name AS group_name,
                   STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones,
                   c.created_at
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
            ORDER BY c.name
            LIMIT %s OFFSET %s
            """,
            (PAGE_SIZE, offset),
        )
        return cur.fetchall()


def _total_contacts(conn) -> int:
    with get_cursor(conn) as cur:
        cur.execute("SELECT COUNT(*) AS n FROM contacts")
        return cur.fetchone()["n"]


def browse_paginated(conn):
    """Console loop: navigate contacts page by page."""
    total = _total_contacts(conn)
    if total == 0:
        print("No contacts in database.")
        return

    offset = 0
    while True:
        rows = _fetch_page(conn, offset)
        page_num = offset // PAGE_SIZE + 1
        total_pages = (total + PAGE_SIZE - 1) // PAGE_SIZE
        print(f"\n{'─'*72}")
        print(f"  Page {page_num} of {total_pages}  (total: {total} contacts)")
        _print_contacts(rows)

        nav_opts = []
        if offset > 0:
            nav_opts.append("[p] prev")
        if offset + PAGE_SIZE < total:
            nav_opts.append("[n] next")
        nav_opts.append("[q] quit")
        print("  " + "  |  ".join(nav_opts))
        cmd = input("  >> ").strip().lower()
        if cmd == "n" and offset + PAGE_SIZE < total:
            offset += PAGE_SIZE
        elif cmd == "p" and offset > 0:
            offset -= PAGE_SIZE
        elif cmd == "q":
            break
        else:
            print("  Invalid option.")


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3.3 – Import / Export
# ══════════════════════════════════════════════════════════════════════════════

# ── helpers for JSON serialisation ────────────────────────────────────────────

def _json_serial(obj):
    """JSON serialiser that handles date / datetime objects."""
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serialisable")


# ── Export to JSON ─────────────────────────────────────────────────────────────

def export_to_json(conn):
    """Write all contacts (with phones + group) to a JSON file."""
    filepath = input("Output JSON file path [contacts_export.json]: ").strip()
    if not filepath:
        filepath = "contacts_export.json"

    with get_cursor(conn) as cur:
        # Fetch each contact with its full phone list as structured data
        cur.execute(
            """
            SELECT c.id, c.name, c.email, c.birthday,
                   g.name AS group_name,
                   c.created_at
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            ORDER BY c.name
            """
        )
        contacts = [dict(r) for r in cur.fetchall()]

        for contact in contacts:
            cur.execute(
                "SELECT phone, type FROM phones WHERE contact_id = %s ORDER BY id",
                (contact["id"],),
            )
            contact["phones"] = [dict(r) for r in cur.fetchall()]

    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(contacts, fh, indent=2, default=_json_serial, ensure_ascii=False)

    print(f"  Exported {len(contacts)} contact(s) → {filepath}")


# ── Import from JSON ───────────────────────────────────────────────────────────

def import_from_json(conn):
    """Read contacts from a JSON file and insert into the DB.

    On duplicate name: ask user to skip or overwrite.
    """
    filepath = input("JSON file path to import: ").strip()
    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        print(f"  File not found: {filepath}")
        return
    except json.JSONDecodeError as exc:
        print(f"  Invalid JSON: {exc}")
        return

    inserted = skipped = updated = 0

    with get_cursor(conn) as cur:
        for item in data:
            name = item.get("name", "").strip()
            if not name:
                continue

            email    = item.get("email") or None
            birthday = item.get("birthday") or None
            group_nm = item.get("group_name") or None
            phones   = item.get("phones", [])  # list of {phone, type}

            # Resolve group
            group_id = _get_or_create_group(cur, group_nm) if group_nm else None

            # Check for duplicate
            existing = _find_contact_by_name(cur, name)
            if existing:
                print(f"\n  Duplicate found: '{name}'")
                choice = input("  [s]kip  or  [o]verwrite? ").strip().lower()
                if choice != "o":
                    skipped += 1
                    continue
                # overwrite
                cur.execute(
                    """
                    UPDATE contacts
                    SET email = %s, birthday = %s, group_id = %s
                    WHERE id = %s
                    """,
                    (email, birthday, group_id, existing["id"]),
                )
                # replace phones
                cur.execute("DELETE FROM phones WHERE contact_id = %s", (existing["id"],))
                for ph in phones:
                    cur.execute(
                        "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                        (existing["id"], ph.get("phone"), ph.get("type", "mobile")),
                    )
                updated += 1
            else:
                cur.execute(
                    """
                    INSERT INTO contacts (name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                    """,
                    (name, email, birthday, group_id),
                )
                cid = cur.fetchone()["id"]
                for ph in phones:
                    cur.execute(
                        "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                        (cid, ph.get("phone"), ph.get("type", "mobile")),
                    )
                inserted += 1

    conn.commit()
    print(f"\n  Import done — inserted: {inserted}, updated: {updated}, skipped: {skipped}")


# ── Extended CSV import ────────────────────────────────────────────────────────
# CSV columns: name, phone, phone_type, email, birthday, group

def import_from_csv(conn):
    """Extended CSV importer handling email, birthday, group, and phone type.

    Expected header row:
        name, phone, phone_type, email, birthday, group
    Multiple rows with the same name are collapsed into one contact
    with multiple phones.
    """
    filepath = input("CSV file path [contacts.csv]: ").strip()
    if not filepath:
        filepath = "contacts.csv"

    try:
        fh = open(filepath, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"  File not found: {filepath}")
        return

    reader = csv.DictReader(fh)
    # Group CSV rows by contact name first
    contact_map: dict[str, dict] = {}
    for row in reader:
        name = row.get("name", "").strip()
        if not name:
            continue
        if name not in contact_map:
            contact_map[name] = {
                "email":    row.get("email", "").strip() or None,
                "birthday": row.get("birthday", "").strip() or None,
                "group":    row.get("group", "").strip() or None,
                "phones":   [],
            }
        phone     = row.get("phone", "").strip()
        phone_type = row.get("phone_type", "mobile").strip() or "mobile"
        if phone:
            contact_map[name]["phones"].append({"phone": phone, "type": phone_type})
    fh.close()

    inserted = skipped = 0
    with get_cursor(conn) as cur:
        for name, info in contact_map.items():
            group_id = _get_or_create_group(cur, info["group"]) if info["group"] else None

            existing = _find_contact_by_name(cur, name)
            if existing:
                print(f"  Skipping existing contact: '{name}'")
                skipped += 1
                continue

            cur.execute(
                """
                INSERT INTO contacts (name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (name, info["email"], info["birthday"] or None, group_id),
            )
            cid = cur.fetchone()["id"]
            for ph in info["phones"]:
                cur.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (cid, ph["phone"], ph["type"]),
                )
            inserted += 1

    conn.commit()
    print(f"  CSV import done — inserted: {inserted}, skipped: {skipped}")


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3.4 – Stored Procedure Wrappers
# ══════════════════════════════════════════════════════════════════════════════

def call_add_phone(conn):
    """Console wrapper for the add_phone stored procedure."""
    name  = input("Contact name         : ").strip()
    phone = input("Phone number         : ").strip()
    ptype = input("Type (home/work/mobile) [mobile]: ").strip() or "mobile"
    try:
        with get_cursor(conn) as cur:
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        conn.commit()
        print(f"  Phone '{phone}' ({ptype}) added to '{name}'.")
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"  Error: {exc.pgerror or exc}")


def call_move_to_group(conn):
    """Console wrapper for the move_to_group stored procedure."""
    name  = input("Contact name : ").strip()
    group = input("Target group : ").strip()
    try:
        with get_cursor(conn) as cur:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()
        print(f"  '{name}' moved to group '{group}'.")
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"  Error: {exc.pgerror or exc}")


def call_search_contacts(conn):
    """Console wrapper for the search_contacts DB function."""
    query = input("Search query (name / email / phone): ").strip()
    if not query:
        return
    with get_cursor(conn) as cur:
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        _print_contacts(cur.fetchall())


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION – Basic Add Contact (with extended fields)
# ══════════════════════════════════════════════════════════════════════════════

def add_contact(conn):
    """Add a new contact with optional email, birthday, group, and multiple phones."""
    print("\n─── Add New Contact ───")
    name = input("Full name       : ").strip()
    if not name:
        print("  Name is required.")
        return

    email    = input("Email (optional): ").strip() or None
    birthday = input("Birthday (YYYY-MM-DD, optional): ").strip() or None

    groups = _list_groups(conn)
    print("Groups:", "  ".join(f"[{g['id']}] {g['name']}" for g in groups))
    group_input = input("Group (ID or name, optional): ").strip()

    with get_cursor(conn) as cur:
        group_id = None
        if group_input:
            try:
                group_id_candidate = int(group_input)
                cur.execute("SELECT id FROM groups WHERE id = %s", (group_id_candidate,))
                row = cur.fetchone()
                group_id = row["id"] if row else None
            except ValueError:
                group_id = _get_or_create_group(cur, group_input)

        # Check duplicate
        if _find_contact_by_name(cur, name):
            print(f"  Contact '{name}' already exists. Use 'add phone' to add numbers.")
            conn.rollback()
            return

        cur.execute(
            """
            INSERT INTO contacts (name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s) RETURNING id
            """,
            (name, email, birthday or None, group_id),
        )
        cid = cur.fetchone()["id"]

        # Collect phones
        while True:
            phone = input("Phone number (blank to stop): ").strip()
            if not phone:
                break
            ptype = input("  Type (home/work/mobile) [mobile]: ").strip() or "mobile"
            cur.execute(
                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                (cid, phone, ptype),
            )

    conn.commit()
    print(f"  Contact '{name}' saved (id={cid}).")


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════════════════════════════════════════

MENU = """
╔══════════════════════════════════════════════════════════════╗
║              PhoneBook Extended  —  TSIS 1                  ║
╠══════════════════════════════════════════════════════════════╣
║  [1]  Add contact                                           ║
║  [2]  Search contacts (name / email / phone)               ║
║  [3]  Filter by group                                       ║
║  [4]  Search by email                                       ║
║  [5]  Sort & list all contacts                             ║
║  [6]  Browse paginated                                      ║
║─────────────────────────────────────────────────────────────║
║  [7]  Add phone to existing contact                         ║
║  [8]  Move contact to group                                 ║
║─────────────────────────────────────────────────────────────║
║  [9]  Export contacts to JSON                               ║
║  [10] Import contacts from JSON                             ║
║  [11] Import contacts from CSV                              ║
║─────────────────────────────────────────────────────────────║
║  [0]  Exit                                                  ║
╚══════════════════════════════════════════════════════════════╝
"""


def main():
    print("Connecting to database…")
    try:
        conn = get_connection()
    except psycopg2.OperationalError as exc:
        print(f"Cannot connect: {exc}")
        sys.exit(1)

    print("Applying schema (if needed)…")
    apply_schema(conn)

    actions = {
        "1":  add_contact,
        "2":  call_search_contacts,
        "3":  filter_by_group,
        "4":  search_by_email,
        "5":  sort_contacts,
        "6":  browse_paginated,
        "7":  call_add_phone,
        "8":  call_move_to_group,
        "9":  export_to_json,
        "10": import_from_json,
        "11": import_from_csv,
    }

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        fn = actions.get(choice)
        if fn:
            try:
                fn(conn)
            except psycopg2.Error as exc:
                conn.rollback()
                print(f"  DB Error: {exc.pgerror or exc}")
            except KeyboardInterrupt:
                print("\n  Cancelled.")
        else:
            print("  Unknown option — try again.")

    conn.close()


if __name__ == "__main__":
    main()
