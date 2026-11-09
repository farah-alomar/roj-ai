import sqlite3
import uuid

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

# جدول المحادثات
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    title TEXT
)
""")

# جدول الرسائل
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    role TEXT,
    message TEXT
)
""")

conn.commit()


def create_session():

    session_id = str(uuid.uuid4())

    cursor.execute(
        "INSERT INTO sessions (id, title) VALUES (?, ?)",
        (session_id, "New Chat")
    )

    conn.commit()

    return session_id


def save(session_id, role, message):

    cursor.execute(
        "INSERT INTO messages (session_id, role, message) VALUES (?, ?, ?)",
        (session_id, role, message)
    )

    conn.commit()


def load_last(session_id, limit=10):

    cursor.execute(
        """
        SELECT role, message
        FROM messages
        WHERE session_id=?
        ORDER BY id DESC
        LIMIT ?
        """,
        (session_id, limit)
    )

    rows = cursor.fetchall()

    return [
        {
            "role": role,
            "content": message
        }
        for role, message in reversed(rows)
    ]


def get_sessions():

    cursor.execute(
        "SELECT id, title FROM sessions"
    )

    return cursor.fetchall()