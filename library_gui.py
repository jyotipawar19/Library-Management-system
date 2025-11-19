import tkinter as tk 
from tkinter import ttk, messagebox 
from backend.db_connection import connect 
 
# ---------------- FUNCTIONS ---------------- # 
 
def fetch_books(): 
    con = connect() 
    cur = con.cursor() 
    cur.execute("SELECT * FROM books") 
    rows = cur.fetchall() 
    for row in book_table.get_children(): 
        book_table.delete(row) 
    for row in rows: 
        book_table.insert("", tk.END, values=row) 
    con.close() 
 
def add_book(): 
    title = title_var.get() 
    author = author_var.get() 
    genre = genre_var.get() 
    year = year_var.get() 
    status = status_var.get() 
    if title == "" or author == "": 
        messagebox.showerror("Error", "All fields are required!") 
        return 
    con = connect() 
    cur = con.cursor() 
    cur.execute("INSERT INTO books (title, author, genre, year_published, status) 
VALUES (%s,%s,%s,%s,%s)", 
                (title, author, genre, year, status)) 
    con.commit() 
    con.close() 
    fetch_books() 
    messagebox.showinfo("Success", "Book added successfully!") 
 
def update_book(): 
    selected = book_table.focus() 
    if not selected: 
        messagebox.showwarning("Select Book", "Please select a record to update.") 
        return 
    data = book_table.item(selected, "values") 
    con = connect() 
    cur = con.cursor() 
    cur.execute(""" 
        UPDATE books 
        SET title=%s, author=%s, genre=%s, year_published=%s, status=%s 
        WHERE book_id=%s 
    """, (title_var.get(), author_var.get(), genre_var.get(), year_var.get(), 
status_var.get(), data[0])) 
    con.commit() 
    con.close() 
    fetch_books() 
    messagebox.showinfo("Updated", "Book details updated successfully!") 
 
def delete_book(): 
    selected = book_table.focus() 
    if not selected: 
        messagebox.showwarning("Select Book", "Please select a record to delete.") 
        return 
    data = book_table.item(selected, "values") 
    con = connect() 
    cur = con.cursor() 
    cur.execute("DELETE FROM books WHERE book_id=%s", (data[0],)) 
    con.commit() 
    con.close() 
    fetch_books() 
    messagebox.showinfo("Deleted", "Book deleted successfully!") 
 
def clear_fields(): 
    title_var.set("") 
    author_var.set("") 
genre_var.set("") 
year_var.set("") 
status_var.set("Available") 
# ---------------- GUI ---------------- # 
root = tk.Tk() 
root.title("Library Management System") 
root.geometry("900x600") 
root.configure(bg="#f0f4f7") 
tk.Label(root, text="Library Management System", font=("Arial", 22, "bold"), 
bg="#f0f4f7", fg="#333").pack(pady=15) 
frame = tk.Frame(root, bg="#f0f4f7") 
frame.pack(pady=10) 
title_var = tk.StringVar() 
author_var = tk.StringVar() 
genre_var = tk.StringVar() 
year_var = tk.StringVar() 
status_var = tk.StringVar(value="Available") 
labels = ["Title", "Author", "Genre", "Year", "Status"] 
variables = [title_var, author_var, genre_var, year_var, status_var] 
for i in range(5): 
tk.Label(frame, text=labels[i], bg="#f0f4f7").grid(row=i, column=0, padx=10, pady=5, 
sticky="w") 
tk.Entry(frame, textvariable=variables[i], width=40).grid(row=i, column=1, padx=10, 
pady=5) 
button_frame = tk.Frame(root, bg="#f0f4f7") 
button_frame.pack(pady=10) 
tk.Button(button_frame, text="Add", width=10, command=add_book, bg="#4CAF50", 
fg="white").grid(row=0, column=0, padx=10) 
tk.Button(button_frame, text="Update", width=10, command=update_book, 
bg="#2196F3", fg="white").grid(row=0, column=1, padx=10) 
tk.Button(button_frame, text="Delete", width=10, command=delete_book, 
bg="#f44336", fg="white").grid(row=0, column=2, padx=10) 
tk.Button(button_frame, text="Clear", width=10, command=clear_fields, 
bg="#9E9E9E", fg="white").grid(row=0, column=3, padx=10) 
columns = ("Book ID", "Title", "Author", "Genre", "Year", "Status") 
book_table = ttk.Treeview(root, columns=columns, show="headings", height=15) 
for col in columns: 
book_table.heading(col, text=col) 
book_table.column(col, width=130) 
book_table.pack(fill="x", pady=10) 
fetch_books() 
root.mainloop() 