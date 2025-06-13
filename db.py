# db.py
import sqlite3

DB_FILE = "nodes.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS nodes (node_key TEXT PRIMARY KEY)")
        conn.commit()

def save_node(node_key):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO nodes (node_key) VALUES (?)", (node_key,))
        conn.commit()

def get_node_by_key(node_key):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT node_key FROM nodes WHERE node_key = ?", (node_key,))
        return c.fetchone()
