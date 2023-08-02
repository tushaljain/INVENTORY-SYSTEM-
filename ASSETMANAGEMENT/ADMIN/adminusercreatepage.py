'''
Created on 06-Jul-2023

@author: tanvi
'''
from tkinter import messagebox, Toplevel, Label, Entry, Button,ttk
import psycopg2
def createuser():
    def save_user():
        # Get the entered user data\
        id=id_name_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        contact = contact_entry.get()
        department = department_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        try:
            conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
            cursor = conn.cursor()

            # Insert the user data into the 'users' table
            insert_query = f"INSERT INTO users (id,first_name, last_name, contact, department, email, password) VALUES ('{id}','{first_name}', '{last_name}', '{contact}', '{department}', '{email}', '{password}')"
            cursor.execute(insert_query)
            conn.commit()

            messagebox.showinfo("User Created", "New user has been created successfully.")
            
            conn.close()
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    # Create the new window for user input
    user_window = Toplevel()
    user_window.title("Create User")
    
    label_id_name = Label(user_window, text="USER_ID:")
    label_id_name.pack()
    id_name_entry = Entry(user_window,textvariable=label_id_name,font=("goud old style",15),bg="white")
    id_name_entry.pack()

    label_first_name = Label(user_window, text="First Name:")
    label_first_name.pack()
    first_name_entry = Entry(user_window,textvariable=label_first_name,font=("goud old style",15),bg="white")
    first_name_entry.pack()

    label_last_name = Label(user_window, text="Last Name:")
    label_last_name.pack()
    last_name_entry = Entry(user_window,textvariable=label_last_name,font=("goud old style",15),bg="white")
    last_name_entry.pack()

    label_contact = Label(user_window, text="Contact:")
    label_contact.pack()
    contact_entry = Entry(user_window,textvariable=label_contact,font=("goud old style",15),bg="white")
    contact_entry.pack()

    label_department = Label(user_window, text="Department:")
    label_department.pack()
    department_entry = Entry(user_window,textvariable=label_department,font=("goud old style",15),bg="white")
    department_entry.pack()

    label_email = Label(user_window, text="Email:")
    label_email.pack()
    email_entry = Entry(user_window,textvariable=label_email,font=("goud old style",15),bg="white")
    email_entry.pack()

    label_password = Label(user_window, text="Password:")
    label_password.pack()
    password_entry = Entry(user_window, show="*",textvariable=label_password,font=("goud old style",15),bg="white")
    password_entry.pack()

    save_button = Button(user_window, text="Save", command=save_user)
    save_button.pack()
def viewusers():
    
    user_window = Toplevel()
    user_window.geometry("700x700+0+0")
    user_window.title("ALL USERS")

    # Create the Treeview widget
    treeview = ttk.Treeview(user_window, columns=("ID","First Name", "Last Name", "Contact", "Department", "Email", "Password"))
    
    # Define the column headings
    treeview.heading("ID", text="User ID")
    treeview.heading("First Name", text="First Name")
    treeview.heading("Last Name", text="Last Name")
    treeview.heading("Contact", text="Contact")
    treeview.heading("Department", text="Department")
    treeview.heading("Email", text="Email")
    treeview.heading("Password", text="Password")

    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()
        query = f"SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()

        # Insert the data into the Treeview
        for row in result:
            treeview.insert("", "end", text="", values=row)

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

    # Pack the Treeview widget
    # style = ttk.Style()
    # style.configure("Custom.Treeview",
    #                 borderwidth=10,
    #                 relief="solid",
    #                 background="#ffffff",
    #                 fieldbackground="#ffffff",
    #                 foreground="#ffffff")
    # style.map("Custom.Treeview",
    #           background=[("selected", "#0078d7"), ("!selected", "#ffffff")],
    #           foreground=[("selected", "#ffffff"), ("!selected", "#ffffff")])
    #
    # # Configure gridlines
    # style.configure("Custom.Treeview.Treeview",
    #                 rowheight=24,
    #                 show="tree headings",
    #                 bd=4)
    # style.configure("Custom.Treeview.Heading",
    #                 background="#e0e0e0",
    #                 foreground="#ffffff",
    #                 relief="flat",
    #                 font=("Arial", 12, "bold"))
    # style.layout("Custom.Treeview.Treeview", [("Custom.Treeview.Treeview.treearea", {"sticky": "nswe"})])

    # Pack the Treeview widget
    treeview.pack(fill="both", expand=True)


   
def adminuserpage():
    new_window=Toplevel()
    new_window.title('WELCOME TO ADMIN-USER PAGE')  
    CREATE_USER=Button(new_window,text="CREATE ACCOUNT",command=lambda :createuser())
    CREATE_USER.pack()
   
    USER_ACCOUNT_DETAILS=Button(new_window,text="VIEW ALL USER",command=lambda:viewusers())
    USER_ACCOUNT_DETAILS.pack()