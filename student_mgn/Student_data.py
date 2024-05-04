import sqlite3

class Data:
    def __init__(self):
        conn = sqlite3.connect("data.db")
        self.conn = conn
        cur = conn.cursor()
        self.cur = cur
        cur.execute(
            """CREATE TABLE IF NOT EXISTS student_data(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    branch TEXT,
                    semester INTEGER,
                    total_marks REAL
                    )"""
        )
        conn.commit()

    def return_data(self):
        self.cur.execute("SELECT * FROM student_data")
        return self.cur.fetchall()

    def search_data(self, search_term):
        search_term = str(search_term)
        self.cur.execute(
            "SELECT * FROM student_data WHERE id LIKE ? OR name LIKE ?",
            ("%" + search_term + "%", "%" + search_term + "%"),
        )
        data = self.cur.fetchall()
        if data:
            return data
        else:
            return False

    def add_data(self, id, name, branch, semester, total_marks):
        if self.search_data(id):
            return "ID already exists."
        else:
            try:
                self.cur.execute(
                    "INSERT INTO student_data (id, name, branch, semester, total_marks) VALUES (?, ?, ?, ?, ?)",
                    (id, name, branch, semester, total_marks),
                )
                self.conn.commit()
                return True
            except Exception as e:
                return f"Error occurred while adding data: {e}: "

    def update_data(self, id, new_name, new_branch, new_semester, new_total_marks):
        if self.search_data(id):
            try:
                self.cur.execute(
                    "UPDATE student_data SET name=?, branch=?, semester=?, total_marks=? WHERE id=?",
                    (new_name, new_branch, new_semester, new_total_marks, id),
                )
                self.conn.commit()
                return True
            except Exception as e:
                return f"Error occurred while updating data: {e}:"
        else:
            return "ID doesn't exist!"

    def delete_data(self, id):
        if self.search_data(id):
            try:
                self.cur.execute("DELETE FROM student_data WHERE id=?", (id,))
                self.conn.commit()
                return True
            except Exception as e:
                return f"Error occurred while deleting data: {e}:"
        else:
            return "ID doesn't exist!"
