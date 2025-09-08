import sqlite3


class StudentDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT,
            branch TEXT,
            semester INTEGER,
            total_marks REAL
        )
        """)
        self.conn.commit()

    def return_data(self):
        self.cur.execute("SELECT * FROM students")
        return self.cur.fetchall()

    def search_data(self, search_term):
        """Search by ID (exact) or name/branch/semester (partial)"""
        search_term = str(search_term).lower()
        self.cur.execute(
            """
            SELECT * FROM students 
            WHERE id = ? 
               OR LOWER(name) LIKE ? 
               OR LOWER(branch) LIKE ? 
               OR CAST(semester AS TEXT) LIKE ?
            """,
            (search_term, f"%{search_term}%", f"%{search_term}%", f"%{search_term}%")
        )
        return self.cur.fetchall()  # return all matches

    def add_data(self, id, name, branch, semester, total_marks):
        # Check if exact ID already exists
        self.cur.execute("SELECT * FROM students WHERE id=?", (id,))
        if self.cur.fetchone():
            return "ID already exists."
        try:
            self.cur.execute(
                "INSERT INTO students (id, name, branch, semester, total_marks) VALUES (?, ?, ?, ?, ?)",
                (id, name, branch, semester, total_marks)
            )
            self.conn.commit()
            return True
        except Exception as e:
            return f"Error occurred while adding data: {e}"

    def update_data(self, id, new_name, new_branch, new_semester, new_total_marks):
        # Check if exact ID exists
        self.cur.execute("SELECT * FROM students WHERE id=?", (id,))
        if self.cur.fetchone():
            try:
                self.cur.execute(
                    "UPDATE students SET name=?, branch=?, semester=?, total_marks=? WHERE id=?",
                    (new_name, new_branch, new_semester, new_total_marks, id)
                )
                self.conn.commit()
                return True
            except Exception as e:
                return f"Error occurred while updating data: {e}"
        else:
            return "ID doesn't exist!"

    def delete_data(self, id):
        # Check if exact ID exists
        self.cur.execute("SELECT * FROM students WHERE id=?", (id,))
        if self.cur.fetchone():
            try:
                self.cur.execute("DELETE FROM students WHERE id=?", (id,))
                self.conn.commit()
                return True
            except Exception as e:
                return f"Error occurred while deleting data: {e}"
        else:
            return "ID doesn't exist!"
