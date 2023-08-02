'''
Created on 07-Jul-2023

@author: tanvi
'''
from tkinter import messagebox, Toplevel, Label, Entry, Button
import psycopg2
import viewinventory
import editinventory
import ttkbootstrap
from ttkbootstrap.dialogs.dialogs import DatePickerDialog
import sqlite3
import tkinter as tk
from tkinter import ttk

def insertinventory():
    def save_inventory():
        # Get the entered inventory data
        serial_number=serial_number_entry.get()
        model_number = model_number_entry.get()
        model_name = model_name_entry.get()
        date_of_arrival = date_of_arrival_entry.get()
        quantity = quantity_entry.get()

        try:
            conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
            cursor = conn.cursor()

            # Insert the inventory data into the 'assets' table
            insert_query = f"INSERT INTO inventory (serialnumber,modelnumber, modelname, dateofarrival, quantity) VALUES ('{serial_number}','{model_number}', '{model_name}', '{date_of_arrival}', {quantity})"
            cursor.execute(insert_query)
            conn.commit()

            messagebox.showinfo("Inventory Inserted", "Inventory details have been inserted successfully.")
            
            conn.close()
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    inventory_window = Toplevel()
    inventory_window.title("INSERT PRODUCT DETAILS")
    
    label_serial_number = Label(inventory_window, text="SERIAL NUMBER:")
    label_serial_number.pack()
    serial_number_entry = Entry(inventory_window)
    serial_number_entry.pack()
    
    label_model_number = Label(inventory_window, text="Model Number:")
    label_model_number.pack()
    model_number_entry = Entry(inventory_window)
    model_number_entry.pack()

    label_model_name = Label(inventory_window, text="Model Name:")
    label_model_name.pack()
    model_name_entry = Entry(inventory_window)
    model_name_entry.pack()

    label_date_of_arrival = Label(inventory_window, text="Date of Arrival:")
    label_date_of_arrival.pack()
    date_of_arrival_entry = Entry(inventory_window)
    date_of_arrival_entry.pack()
    
    label_quantity = Label(inventory_window, text="Quantity:")
    label_quantity.pack()
    quantity_entry = Entry(inventory_window)
    quantity_entry.pack()

    save_button = Button(inventory_window, text="Save", command=save_inventory)
    save_button.pack()
def updateinventory(event):
    pass
def assigninventory():
    def assign_inventory_to_user():
        # Get the entered values from the input fields
        department = department_entry.get()
        mobile = mobile_entry.get()
        # contact = contact_entry.get()
        model_number = model_number_entry.get()
        quantity = int(quantity_entry.get())
        date_of_allotment = date_of_allotment_entry.get()
        empid = int(empid_entry.get())

        try:
            conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
            cursor = conn.cursor()

            # Check if the UID exists in the Users table
            check_uid_query = f"SELECT id FROM Users WHERE id = {empid}"
            cursor.execute(check_uid_query)
            result = cursor.fetchone()

            if result:
                # Decrement the quantity in the Asset table
                decrement_quantity_query = f"UPDATE inventory SET quantity = quantity - {quantity} WHERE modelnumber='{model_number}'"
                cursor.execute(decrement_quantity_query)

                # Insert the inventory assignment into the AssetAssign table
                insert_assignment_query = f"INSERT INTO AssetAssign (department, mobile,model_number, quantity, date_of_allotment, empid) VALUES ('{department}', '{mobile}','{model_number}', {quantity}, '{date_of_allotment}', {empid})"
                cursor.execute(insert_assignment_query)
                conn.commit()

                messagebox.showinfo("Inventory Assigned", "Inventory assigned successfully.")
                inventory_window.destroy()
            else:
                messagebox.showerror("Invalid UID", "Please enter a valid UID.")

            conn.close()
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    inventory_window = tk.Toplevel()
    inventory_window.title("Assign Inventory")

    # Create labels and entry fields for each input
    department_label = tk.Label(inventory_window, text="Department:",font=("goud old style",15))
    department_label.pack()
    department_entry = tk.Entry(inventory_window,textvariable=department_label,font=("goud old style",15),bg="white")
    department_entry.pack()

    mobile_label = tk.Label(inventory_window, text="Mobile:",font=("goud old style",15))
    mobile_label.pack()
    mobile_entry = tk.Entry(inventory_window,textvariable=mobile_label,font=("goud old style",15),bg="white")
    mobile_entry.pack()

    model_number_label = tk.Label(inventory_window, text="Model Number:",font=("goud old style",15))
    model_number_label.pack()
    model_number_entry = tk.Entry(inventory_window,textvariable=model_number_label,font=("goud old style",15),bg="white")
    model_number_entry.pack()

    quantity_label = tk.Label(inventory_window, text="Quantity:",font=("goud old style",15))
    quantity_label.pack()
    quantity_entry = tk.Entry(inventory_window,textvariable=quantity_label,font=("goud old style",15),bg="white")
    quantity_entry.pack()

    date_of_allotment_label = tk.Label(inventory_window, text="Date of Allotment:",font=("goud old style",15))
    date_of_allotment_label.pack()
    date_of_allotment_entry = tk.Entry(inventory_window,textvariable=date_of_allotment_label,font=("goud old style",15),bg="white")
    date_of_allotment_entry.pack()

    empid_label = tk.Label(inventory_window, text="Emp ID:",font=("goud old style",15))
    empid_label.pack()
    empid_entry = tk.Entry(inventory_window,textvariable=empid_label,font=("goud old style",15),bg="white")
    empid_entry.pack()

    assign_button = tk.Button(inventory_window, text="Assign",font=("times new roman",15,"bold"),bg="green",cursor="hand2", command=assign_inventory_to_user)
    assign_button.pack()
def assignviewinventory():
    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()

        # Fetch all the asset assignments from the 'AssetAssign' table
        query = "SELECT * FROM AssetAssign"
        cursor.execute(query)
        result = cursor.fetchall()

        # Create a new window for displaying the asset assignments
        window = tk.Toplevel()
        window.title("Asset Assignments")

        # Create a Treeview widget to display the asset assignments
        tree = ttk.Treeview(window)
        tree["columns"] = ("Department", "Mobile", "Contact", "Model Number", "Quantity", "Date of Allotment", "Emp ID")

        # Define the columns' headings
        tree.heading("Department", text="Department")
        tree.heading("Mobile", text="Mobile")
        tree.heading("Contact", text="Contact")
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
def inventorywindow():
    
    inventory_window = Toplevel()
    Insertinventorybutton = Button(inventory_window, text="INSERT NEW INVENTORY",font=("times new roman",15,"bold"),bg="magenta",cursor="hand2", command=lambda: insertinventory())
    Insertinventorybutton.pack()
    ViewInventory = Button(inventory_window, text="VIEW STOCK",font=("times new roman",15,"bold"),bg="blue",cursor="hand2",command=viewinventory.viewinventries)
    ViewInventory.pack()
    UpdateInventoryButton = Button(inventory_window, text="UPDATE EXISTING INVENTORY",font=("times new roman",15,"bold"),bg="green",cursor="hand2",command=editinventory.editinventries)
    UpdateInventoryButton.pack()
    Assigninventory=Button(inventory_window,text="ASSIGN INVENTORY",font=("times new roman",15,"bold"),bg="pink",cursor="hand2",command=lambda:assigninventory())
    Assigninventory.pack()
    Assignviewinventory=Button(inventory_window,text="VIEW ASSIGN INVENTORY",font=("times new roman",15,"bold"),bg="brown",cursor="hand2",command=lambda:assignviewinventory())
    Assignviewinventory.pack()
    