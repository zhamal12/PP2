# connect.py  –  Single place for psycopg2 connection creation.

import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG


def get_connection():
    """Return a new psycopg2 connection using DB_CONFIG."""
    return psycopg2.connect(**DB_CONFIG)


def get_cursor(conn):
    """Return a RealDictCursor (rows as dicts)."""
    return conn.cursor(cursor_factory=RealDictCursor)
