import sqlite3

DB_NAME = "healthcare.db"


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            heart_rate INTEGER,
            temperature REAL,
            spo2 INTEGER,
            timestamp TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)

    connection.commit()
    connection.close()


def register_patient(name, age, gender):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT patient_id FROM patients
        WHERE patient_name = ? AND age = ? AND gender = ?
    """, (name, age, gender))

    row = cursor.fetchone()

    if row:
        patient_id = row[0]
    else:
        cursor.execute("""
            INSERT INTO patients (patient_name, age, gender)
            VALUES (?, ?, ?)
        """, (name, age, gender))
        patient_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return f"P{patient_id:03d}"


def insert_patient_data(patient_id, heart_rate, temperature, spo2, timestamp):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    numeric_id = int(patient_id[1:])

    cursor.execute("""
        INSERT INTO patient_data
        (patient_id, heart_rate, temperature, spo2, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (numeric_id, heart_rate, temperature, spo2, timestamp))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("Healthcare Database Created Successfully!")