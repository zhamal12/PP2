from connect import get_connection


def call_upsert(name, surname, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s, %s)", (name, surname, phone))
    conn.commit()

    cur.close()
    conn.close()


def search(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def paginate(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete(name=None, surname=None, phone=None):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s, %s, %s)", (name, surname, phone))
    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":

    call_upsert("John", "Doe", "1234567890")
    call_upsert("Jane", "Smith", "9876543210")

    print("\nSearch:")
    search("John")

    print("\nPagination:")
    paginate(5, 0)

    print("\nDelete:")
    delete(phone="1234567890")