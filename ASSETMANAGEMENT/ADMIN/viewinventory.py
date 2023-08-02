from tkinter import messagebox, Toplevel, Label, Entry, Button
import psycopg2
import tkinter as tk
from tkinter import ttk

def viewinventries():
    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()

        # Fetch all the inventory data from the 'inventory' table
        query = "SELECT * FROM inventory"
        cursor.execute(query)
        result = cursor.fetchall()

        # Create a new window for displaying the inventory data
        inventory_window = Toplevel()
        inventory_window.title("View Inventory")

        # Create a Treeview widget to display the inventory data
        tree = ttk.Treeview(inventory_window)
        tree["columns"] = ("Serial Number", "Model Number", "Model Name", "Date of Arrival", "Quantity")

        # Define the columns' headings
        tree.heading("Serial Number", text="Serial Number")
        tree.heading("Model Number", text="Model Number")
        tree.heading("Model Name", text="Model Name")
        tree.heading("Date of Arrival", text="Date of Arrival")
        tree.heading("Quantity", text="Quantity")

        # Insert the fetched data into the Treeview widget
        for row in result:
            tree.insert("", "end", values=row)

        # Pack the Treeview widget
        tree.pack(fill="both", expand=True)

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
