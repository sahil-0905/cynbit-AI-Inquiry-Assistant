
import sqlite3
import os
import json

# Database location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "cynbit_inquiries.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


# --------------------------------
# CREATE DATABASE TABLE
# --------------------------------

def initialize_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inquiries (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            inquiry TEXT NOT NULL,

            category TEXT,

            budget INTEGER,

            timeline TEXT,

            urgency TEXT,

            project_scope TEXT,

            lead_score INTEGER,

            priority TEXT,

            recommended_services TEXT,

            ai_response TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


# --------------------------------
# SAVE CUSTOMER INQUIRY
# --------------------------------

def save_inquiry(inquiry, analysis, recommendations, ai_response):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inquiries (
            inquiry,
            category,
            budget,
            timeline,
            urgency,
            project_scope,
            lead_score,
            priority,
            recommended_services,
            ai_response
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        inquiry,
        analysis.get("category"),
        analysis.get("budget"),
        analysis.get("timeline"),
        analysis.get("urgency"),
        analysis.get("project_scope"),
        analysis.get("lead_score"),
        analysis.get("priority"),
        json.dumps(recommendations),
        ai_response
    ))

    conn.commit()
    conn.close()


# --------------------------------
# GET ALL CUSTOMER INQUIRIES
# --------------------------------

def get_all_inquiries():

    conn = get_connection()
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM inquiries
        ORDER BY created_at DESC
    """)

    records = cursor.fetchall()
    conn.close()

    return [dict(record) for record in records]


# --------------------------------
# GET TOTAL INQUIRY COUNT
# --------------------------------

def get_inquiry_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM inquiries")

    count = cursor.fetchone()[0]

    conn.close()

    return count


# --------------------------------
# TEST DATABASE
# --------------------------------

if __name__ == "__main__":

    initialize_db()

    print("Cynbit database initialized successfully!")
    print("Total saved inquiries:", get_inquiry_count())
