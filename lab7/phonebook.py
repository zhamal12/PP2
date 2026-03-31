from connect import get_connection

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Added!")

def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search():
    name = input("Search name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s;",
        ('%' + name + '%',)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

def update():
    phone = input("Enter phone: ")
    new_name = input("New name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET name=%s WHERE phone=%s;",
        (new_name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Updated!")

def delete():
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM contacts WHERE phone=%s;", (phone,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")

import csv

def load_csv():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for name, phone in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV loaded!")

def menu():
    while True:
        print("\n1 Add")
        print("2 Show")
        print("3 Search")
        print("4 Update")
        print("5 Delete")
        print("6 Load CSV")
        print("0 Exit")

        choice = input(">> ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            load_csv()
        elif choice == "0":
            break

menu()