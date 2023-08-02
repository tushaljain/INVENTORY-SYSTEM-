from tkinter import messagebox, Toplevel, Label, Entry, Button
import psycopg2
import tkinter as tk
from tkinter import ttk

tree = None  # Declare tree as a global variable

def editinventries():
    global tree  # Access the global variable

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

        # Function to handle the update window
        def update_inventory(event):
            selected_item = tree.focus()  # Get the selected item in the treeview
            item_values = tree.item(selected_item)['values']  # Get the values of the selected item

            # Create a new window for updating the inventory
            update_window = Toplevel()
            update_window.title("Update Inventory")

            # Create labels and entry fields for each inventory field
            label_serial_number = Label(update_window, text="Serial Number:")
            label_serial_number.pack()
            entry_serial_number = Entry(update_window, font=("goud old style", 15), bg="white")
            entry_serial_number.pack()
            entry_serial_number.insert(0, item_values[0])

            label_model_number = Label(update_window, text="Model Number:")
            label_model_number.pack()
            entry_model_number = Entry(update_window, font=("goud old style", 15), bg="white")
            entry_model_number.pack()
            entry_model_number.insert(0, item_values[1])

            label_model_name = Label(update_window, text="Model Name:")
            label_model_name.pack()
            entry_model_name = Entry(update_window, font=("goud old style", 15), bg="white")
            entry_model_name.pack()
            entry_model_name.insert(0, item_values[2])

            label_date_of_arrival = Label(update_window, text="Date of Arrival:")
            label_date_of_arrival.pack()
            entry_date_of_arrival = Entry(update_window, font=("goud old style", 15), bg="white")
            entry_date_of_arrival.pack()
            entry_date_of_arrival.insert(0, item_values[3])

            label_quantity = Label(update_window, text="Quantity:")
            label_quantity.pack()
            entry_quantity = Entry(update_window, font=("goud old style", 15), bg="white")
            entry_quantity.pack()
            entry_quantity.insert(0, item_values[4])

            # Function to update the inventory data
            def update_inventory_data():
                updated_serial_number = entry_serial_number.get()
                updated_model_number = entry_model_number.get()
                updated_model_name = entry_model_name.get()
                updated_date_of_arrival = entry_date_of_arrival.get()
                updated_quantity = entry_quantity.get()

                # Update the inventory data in the database
                update_query = f"UPDATE inventory SET modelnumber='{updated_model_number}', modelname='{updated_model_name}', dateofarrival='{updated_date_of_arrival}', quantity={updated_quantity} WHERE serialnumber='{updated_serial_number}'"
                cursor.execute(update_query)
                conn.commit()

                messagebox.showinfo("Update Inventory", "Inventory details have been updated successfully.")
                update_window.destroy()  # Close the update window

                # Update the treeview with the new values
                tree.item(selected_item, values=(updated_serial_number, updated_model_number, updated_model_name, updated_date_of_arrival, updated_quantity))

                # Close the cursor and connection
                cursor.close()
                conn.close()

            # Button to update the inventory
            button_update = Button(update_window, text="Update", command=update_inventory_data)
            button_update.pack()

        # Bind the double-click event on a row to the update_inventory function
        tree.bind('<Double-Button-1>', update_inventory)

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

def search_inventory():
    global tree  # Access the global variable

    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()

        serial_number = search_entry.get()

        # Clear the treeview
        tree.delete(*tree.get_children())

        # Fetch the inventory data based on the entered serial number
        query = f"SELECT * FROM inventory WHERE serialnumber = '{serial_number}'"
        cursor.execute(query)
        result = cursor.fetchall()

        # Insert the fetched data into the Treeview widget
        for row in result:
            tree.insert("", "end", values=row)

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

# Create the main window
def searching_inventory():
    
    update_window=Toplevel()
    search_label = Label(update_window, text="Enter Serial Number:")
    search_label.pack()
    search_entry = Entry(update_window, font=("goud old style", 15), bg="white")
    search_entry.pack()
    search_button = Button(update_window, text="Search", command=search_inventory)
    search_button.pack()
# Start the Tkinter event loop
