import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT,
    rating INTEGER,
    comment TEXT
)
""")

conn.commit()


def save_feedback(question, answer, rating, comment=""):
    cursor.execute(
        """
        INSERT INTO feedback(question, answer, rating, comment)
        VALUES(?,?,?,?)
        """,
        (question, answer, rating, comment)
    )

    conn.commit()