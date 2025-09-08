import Student_data as sd
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox  # for popups
import tkinter as tk  # for icon handling

# Database instance
data_base = sd.StudentDatabase()

# -------------------- Main Window --------------------
root = tb.Window(themename="darkly")
root.title("Student Management System")
root.geometry("1000x600")

# ✅ Fix hover/dock name (Linux/mac)
try:
    root.tk.call('wm', 'class', root._w, 'Student Management System')
except Exception as e:
    print("WM_CLASS not supported on this system:", e)

# -------------------- App Icon --------------------
try:
    # Windows
    root.iconbitmap("student.ico")
except Exception:
    try:
        # Linux/mac
        icon = tk.PhotoImage(file="student.png")
        root.iconphoto(True, icon)
    except Exception as e:
        print("⚠️ Could not load icon:", e)

# -------------------- Utility --------------------
def show_result(result, operation):
    if result is True:
        messagebox.showinfo("Success", f"Data {operation} successfully!")
    else:
        messagebox.showerror("Error", f"Data could not be {operation}!\nReason: {result}")

# -------------------- Functions --------------------
def add_data():
    id = id_entry.get()
    name = name_entry.get()
    branch = branch_entry.get()
    semester = sem_entry.get()
    marks = marks_entry.get()

    if not (id and name and branch and semester and marks):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        semester = int(semester)
        marks = float(marks)
    except:
        messagebox.showwarning("Input Error", "Semester must be integer and Marks must be number!")
        return

    result = data_base.add_data(id, name, branch, semester, marks)
    show_result(result, "added")

    # Clear entries
    id_entry.delete(0, tb.END)
    name_entry.delete(0, tb.END)
    branch_entry.delete(0, tb.END)
    sem_entry.delete(0, tb.END)
    marks_entry.delete(0, tb.END)

def delete_data():
    id = delete_entry.get().strip()
    if id:
        result = data_base.delete_data(id)
        if result is True:
            messagebox.showinfo("Success", "Student deleted successfully")
        else:
            messagebox.showerror("Error", result)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid ID")

def update_data():
    id = update_id_entry.get()
    new_name = update_name_entry.get()
    new_branch = update_branch_entry.get()
    new_sem = update_sem_entry.get()
    new_marks = update_marks_entry.get()

    if not (id and new_name and new_branch and new_sem and new_marks):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        new_sem = int(new_sem)
        new_marks = float(new_marks)
    except:
        messagebox.showwarning("Input Error", "Semester must be integer and Marks must be number!")
        return

    result = data_base.update_data(id, new_name, new_branch, new_sem, new_marks)
    show_result(result, "updated")

    update_id_entry.delete(0, tb.END)
    update_name_entry.delete(0, tb.END)
    update_branch_entry.delete(0, tb.END)
    update_sem_entry.delete(0, tb.END)
    update_marks_entry.delete(0, tb.END)

def search_data():
    search_term = search_entry.get().strip()
    result = data_base.search_data(search_term)

    result_text.config(state="normal")
    result_text.delete('1.0', tb.END)

    if result and isinstance(result, list):
        for student in result:
            if isinstance(student, tuple) and len(student) >= 5:
                result_text.insert(
                    tb.END,
                    f"ID: {student[0]}, Name: {student[1]}, Branch: {student[2]}, Semester: {student[3]}, Total marks: {student[4]}\n"
                )
            else:
                result_text.insert(tb.END, f"⚠️ Invalid row: {student}\n")
    else:
        result_text.insert(tb.END, "No students found.\n")

    result_text.config(state="disabled")

# -------------------- Add Data Frame --------------------
add_frame = tb.Labelframe(root, text="Add Student Data", padding=10)
add_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

id_label = tb.Label(add_frame, text="ID:")
id_label.grid(row=0, column=0, sticky="w")
id_entry = tb.Entry(add_frame)
id_entry.grid(row=0, column=1)

name_label = tb.Label(add_frame, text="Name:")
name_label.grid(row=1, column=0, sticky="w")
name_entry = tb.Entry(add_frame)
name_entry.grid(row=1, column=1)

branch_label = tb.Label(add_frame, text="Branch:")
branch_label.grid(row=2, column=0, sticky="w")
branch_entry = tb.Entry(add_frame)
branch_entry.grid(row=2, column=1)

sem_label = tb.Label(add_frame, text="Semester:")
sem_label.grid(row=3, column=0, sticky="w")
sem_entry = tb.Entry(add_frame)
sem_entry.grid(row=3, column=1)

marks_label = tb.Label(add_frame, text="Total Marks:")
marks_label.grid(row=4, column=0, sticky="w")
marks_entry = tb.Entry(add_frame)
marks_entry.grid(row=4, column=1)

add_button = tb.Button(add_frame, text="Add Data", bootstyle="success", command=add_data)
add_button.grid(row=5, column=0, columnspan=2, pady=5)

# -------------------- Delete Data Frame --------------------
delete_frame = tb.Labelframe(root, text="Delete Student Data", padding=10)
delete_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

delete_label = tb.Label(delete_frame, text="ID:")
delete_label.grid(row=0, column=0, sticky="w")
delete_entry = tb.Entry(delete_frame)
delete_entry.grid(row=0, column=1)

delete_button = tb.Button(delete_frame, text="Delete Data", bootstyle="danger", command=delete_data)
delete_button.grid(row=1, column=0, columnspan=2, pady=5)

# -------------------- Update Data Frame --------------------
update_frame = tb.Labelframe(root, text="Update Student Data", padding=10)
update_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

update_id_label = tb.Label(update_frame, text="ID:")
update_id_label.grid(row=0, column=0, sticky="w")
update_id_entry = tb.Entry(update_frame)
update_id_entry.grid(row=0, column=1)

update_name_label = tb.Label(update_frame, text="Name:")
update_name_label.grid(row=1, column=0, sticky="w")
update_name_entry = tb.Entry(update_frame)
update_name_entry.grid(row=1, column=1)

update_branch_label = tb.Label(update_frame, text="Branch:")
update_branch_label.grid(row=2, column=0, sticky="w")
update_branch_entry = tb.Entry(update_frame)
update_branch_entry.grid(row=2, column=1)

update_sem_label = tb.Label(update_frame, text="Semester:")
update_sem_label.grid(row=3, column=0, sticky="w")
update_sem_entry = tb.Entry(update_frame)
update_sem_entry.grid(row=3, column=1)

update_marks_label = tb.Label(update_frame, text="Total Marks:")
update_marks_label.grid(row=4, column=0, sticky="w")
update_marks_entry = tb.Entry(update_frame)
update_marks_entry.grid(row=4, column=1)

update_button = tb.Button(update_frame, text="Update Data", bootstyle="warning", command=update_data)
update_button.grid(row=5, column=0, columnspan=2, pady=5)

# -------------------- Search Frame --------------------
search_frame = tb.Labelframe(root, text="Search Student Data", padding=10)
search_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

search_label = tb.Label(search_frame, text="Enter ID or Name:")
search_label.grid(row=0, column=0, sticky="w")
search_entry = tb.Entry(search_frame)
search_entry.grid(row=0, column=1)

search_button = tb.Button(search_frame, text="Search", bootstyle="info", command=search_data)
search_button.grid(row=1, column=0, columnspan=2, pady=5)

result_text = tb.Text(search_frame, width=50, height=10, state="disabled")
result_text.grid(row=2, column=0, columnspan=2, pady=5)

# -------------------- Run App --------------------
root.mainloop()
