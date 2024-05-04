import tkinter as tk
import Student_data as sd
from tkinter import messagebox

data_base = sd.Data()

root = tk.Tk()

root.title("Student Management System")

def show_result(result, operation):
    if result == True:
        messagebox.showinfo("Success", f"Data {operation} successfully!")
    else:
        messagebox.showinfo("Error", f"Data could not be {operation}!\nReason: {result}")

def add_data():
    id = int(id_entry.get())
    name = name_entry.get()
    branch = branch_entry.get()
    semester = int(sem_entry.get())
    marks = float(marks_entry.get())
    result = data_base.add_data(id, name, branch, semester, marks)
    show_result(result, "added")
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    sem_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

def delete_data():
    id = int(delete_entry.get())
    result = data_base.delete_data(id)
    show_result(result, "deleted")
    delete_entry.delete(0, tk.END)

def update_data():
    id = int(update_id_entry.get())
    new_name = update_name_entry.get()
    new_branch = update_branch_entry.get()
    new_sem = int(update_sem_entry.get())
    new_marks = float(update_marks_entry.get())
    result = data_base.update_data(id, new_name, new_branch, new_sem, new_marks)
    show_result(result, "updated")
    update_id_entry.delete(0, tk.END)
    update_name_entry.delete(0, tk.END)
    update_branch_entry.delete(0, tk.END)
    update_sem_entry.delete(0, tk.END)
    update_marks_entry.delete(0, tk.END)

def search_data():
    search_term = search_entry.get().lower()
    result = data_base.search_data(search_term)
    if result:
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        for student in result:
            result_text.insert(tk.END, f"ID: {student[0]}, Name: {student[1]}, Branch: {student[2]}, Semester: {student[3]}, Total marks: {student[4]}\n")
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("No Results", "No students found matching the search criteria.")




# Add data Section
add_frame = tk.LabelFrame(root, text="Add student data", padx=10, pady=10)
add_frame.grid(row=0, column=0, padx=10, pady=10)

id_label = tk.Label(add_frame, text="Id:")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(add_frame)
id_entry.grid(row=0, column=1)

name_label = tk.Label(add_frame, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=1, column=1)

branch_label = tk.Label(add_frame, text="Branch:")
branch_label.grid(row=2, column=0)
branch_entry = tk.Entry(add_frame)
branch_entry.grid(row=2, column=1)

sem_label = tk.Label(add_frame, text="Semester:")
sem_label.grid(row=3, column=0)
sem_entry = tk.Entry(add_frame)
sem_entry.grid(row=3, column=1)

marks_label = tk.Label(add_frame, text="Total marks:")
marks_label.grid(row=4, column=0)
marks_entry = tk.Entry(add_frame)
marks_entry.grid(row=4, column=1)

add_button = tk.Button(add_frame, text="Add Data", command=add_data)
add_button.grid(row=5, column=0, columnspan=2)


# Delete data Section
delete_frame = tk.LabelFrame(root, text="Delete student data", padx=10, pady=10)
delete_frame.grid(row=1, column=0, padx=10, pady=10)

delete_label = tk.Label(delete_frame, text="ID:")
delete_label.grid(row=0, column=0)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=1)

delete_button = tk.Button(delete_frame, text="Delete data", command=delete_data)
delete_button.grid(row=1, column=0, columnspan=2)


# Update Book Section
update_frame = tk.LabelFrame(root, text="Update student data", padx=10, pady=10)
update_frame.grid(row=0, column=1, padx=10, pady=10)

update_id_label = tk.Label(update_frame, text="ID:")
update_id_label.grid(row=0, column=0)
update_id_entry = tk.Entry(update_frame)
update_id_entry.grid(row=0, column=1)

update_name_label = tk.Label(update_frame, text="Name:")
update_name_label.grid(row=1, column=0)
update_name_entry = tk.Entry(update_frame)
update_name_entry.grid(row=1, column=1)

update_branch_label = tk.Label(update_frame, text="Branch:")
update_branch_label.grid(row=2, column=0)
update_branch_entry = tk.Entry(update_frame)
update_branch_entry.grid(row=2, column=1)

update_sem_label = tk.Label(update_frame, text="Semester:")
update_sem_label.grid(row=3, column=0)
update_sem_entry = tk.Entry(update_frame)
update_sem_entry.grid(row=3, column=1)

update_marks_label = tk.Label(update_frame, text="Total marks:")
update_marks_label.grid(row=4, column=0)
update_marks_entry = tk.Entry(update_frame)
update_marks_entry.grid(row=4, column=1)

update_button = tk.Button(update_frame, text="Update data", command=update_data)
update_button.grid(row=5, column=0, columnspan=2)


# Search Books Section

search_frame = tk.LabelFrame(root, text="Search student data", padx=10, pady=10)
search_frame.grid(row=1, column=1, padx=10, pady=10)

search_label = tk.Label(search_frame, text="Search\n( You can view entire database by\nclicking on search button with no input):")
search_label.grid(row=0, column=0)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1)

search_button = tk.Button(search_frame, text="Search", command=search_data)
search_button.grid(row=1, column=0, columnspan=2)

result_text = tk.Text(search_frame, height=10, width=50, state=tk.DISABLED)
result_text.grid(row=2, column=0, columnspan=2)

root.mainloop()
