'''
Created on 05-Jul-2023

@author: tanvi
'''
from tkinter import messagebox, Toplevel, Label, Entry, Button
import tkinter as tk
from tkinter import ttk
import psycopg2
def viewuserassetdetials():
    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()

        # Fetch all the asset assignments from the 'AssetAssign' table
        # emplid=emplid.get()
        query = "SELECT model_number,quantity,date_of_allotment,empid FROM AssetAssign "
        cursor.execute(query)
        result = cursor.fetchall()

        # Create a new window for displaying the asset assignments
        window = tk.Toplevel()
        window.title("Asset Assignments")

        # Create a Treeview widget to display the asset assignments
        tree = ttk.Treeview(window)
        tree["columns"] = ("Model Number", "Quantity", "Date of Allotment", "Emp ID")

        # Define the columns' headings
        # tree.heading("Department", text="Department")
        # tree.heading("Mobile", text="Mobile")
        # tree.heading("Contact", text="Contact")
        tree.heading("Model Number", text="Model Number")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Date of Allotment", text="Date of Allotment")
        tree.heading("Emp ID", text="Emp ID")

        # Insert the fetched data into the Treeview widget
        for row in result:
            tree.insert("", "end", values=row)

        # Pack the Treeview widget
        tree.pack(fill="both", expand=True)

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
    pass
def login_clicked(username_entry, password_entry):
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE email = '{entered_username}' AND password= '{entered_password}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            messagebox.showinfo("Login Successful", "USER login successful.")
            viewuserassetdetials()
            
            # Add code to open the next page or perform further actions
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
def user_button_clicked():
    login_window = Toplevel()
    login_window.title("USER Login")

    label_username = Label(login_window, text="Username:")
    label_username.pack()
    username_entry = Entry(login_window,textvariable=label_username,font=("goud old style",15),bg="white")
    username_entry.pack()

    label_password = Label(login_window, text="Password:")
    label_password.pack()
    password_entry = Entry(login_window, show="*",textvariable=label_password,font=("goud old style",15),bg="white")
    password_entry.pack()

    login_button = Button(login_window, text="Login",font=("times new roman",15,"bold"),bg="red",cursor="hand2",command=lambda:login_clicked(username_entry,password_entry))
    login_button.pack()