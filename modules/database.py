import sqlite3

DB_NAME = "vbcua.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            topic TEXT,
            semantic_score REAL,
            final_score REAL
        )
    """)

    conn.commit()
    conn.close()


def save_result(student_name, topic, semantic_score, final_score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO results(student_name, topic, semantic_score, final_score)
        VALUES (?, ?, ?, ?)
    """, (student_name, topic, semantic_score, final_score))

    conn.commit()
    conn.close()