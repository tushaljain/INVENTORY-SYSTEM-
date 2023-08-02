from tkinter import messagebox, Toplevel, Label, Entry, Button, ttk
import psycopg2

def create_engineer():
    def save_engineer():
        # Get the entered engineer data
        emp_id = entry_emp_id.get()
        name = entry_name.get()
        contact = entry_contact.get()
        password = entry_password.get()
        email = entry_email.get()

        try:
            conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
            cursor = conn.cursor()

            # Insert the engineer data into the 'engineers' table
            insert_query = f"INSERT INTO engineer (emp_id, name, contact, password, email) VALUES ('{emp_id}', '{name}', '{contact}', '{password}', '{email}')"
            cursor.execute(insert_query)
            conn.commit()

            messagebox.showinfo("Engineer Created", "New engineer has been created successfully.")

            conn.close()
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    # Create the new window for engineer input
    engineer_window = Toplevel()
    engineer_window.title("Create Engineer")

    label_emp_id = Label(engineer_window, text="Employee ID:")
    label_emp_id.pack()
    entry_emp_id = Entry(engineer_window)
    entry_emp_id.pack()

    label_name = Label(engineer_window, text="Name:")
    label_name.pack()
    entry_name = Entry(engineer_window)
    entry_name.pack()

    label_contact = Label(engineer_window, text="Contact:")
    label_contact.pack()
    entry_contact = Entry(engineer_window)
    entry_contact.pack()

    label_password = Label(engineer_window, text="Password:")
    label_password.pack()
    entry_password = Entry(engineer_window, show="*")
    entry_password.pack()

    label_email = Label(engineer_window, text="Email:")
    label_email.pack()
    entry_email = Entry(engineer_window)
    entry_email.pack()

    save_button = Button(engineer_window, text="Save", command=save_engineer)
    save_button.pack()

def view_engineers():
    engineer_window = Toplevel()
    engineer_window.title("All Engineers")

    treeview = ttk.Treeview(engineer_window, columns=("Employee ID", "Name", "Contact", "Password", "Email"))

    treeview.heading("Employee ID", text="Employee ID")
    treeview.heading("Name", text="Name")
    treeview.heading("Contact", text="Contact")
    treeview.heading("Password", text="Password")
    treeview.heading("Email", text="Email")

    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()
        query = "SELECT * FROM engineer"
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            treeview.insert("", "end", text="", values=row)

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

    treeview.pack(fill="both", expand=True)

def engineer_account_page():
    engineer_window = Toplevel()
    engineer_window.title("Engineer Account")

    button_create_account = Button(engineer_window, text="Create Engineer Account", font=("times new roman", 15, "bold"), bg="light green", cursor="hand2", command=create_engineer)
    button_create_account.pack(pady=10)

    button_view_engineers = Button(engineer_window, text="View All Engineers", font=("times new roman", 15, "bold"), bg="light green", cursor="hand2", command=view_engineers)
    button_view_engineers.pack(pady=10)

# Rest of your code...


