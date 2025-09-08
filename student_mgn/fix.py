import sqlite3

def safe_search(db_path, search_term=""):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if search_term:
        cur.execute("SELECT * FROM students WHERE id=? OR name LIKE ?", (search_term, f"%{search_term}%",))
    else:
        cur.execute("SELECT * FROM students")

    results = cur.fetchall()

    if not results:
        print("⚠️ No matching student found.")
        return

    for idx, student in enumerate(results):
        # Error detection
        if not isinstance(student, tuple):
            print(f"❌ Error: Row {idx} is not a tuple -> {student}")
            continue

        if len(student) < 5:
            print(f"❌ Error: Row {idx} does not have enough columns -> {student}")
            continue

        try:
            print(f"✅ Row {idx}: ID={student[0]}, Name={student[1]}, Branch={student[2]}, Semester={student[3]}, Total Marks={student[4]}")
        except Exception as e:
            print(f"❌ Unexpected error in row {idx}: {e} -> {student}")

    conn.close()


# Example usage:
if __name__ == "__main__":
    safe_search("data.db", "Anil")   # You can pass empty string "" to view all
