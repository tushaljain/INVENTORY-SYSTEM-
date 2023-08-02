from tkinter import messagebox, Toplevel, Label, Entry, Button
import psycopg2
import adminusercreatepage
# from ADMIN.adminusercreatepage import adminuserpage
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle

import inventoryfeed  
import adminengineerpage 
def openadminpage():
   def logout_clicked():
        new_window.destroy()
        messagebox.showinfo("Logout", "You have been logged out.")
   new_window=Toplevel()
   # new_window.geometry("200X200")
   new_window.title('ADMIN PAGE')  
   ENGGACCOUNT = Button(new_window, text="ENGINEER ACCOUNT", font=("times new roman", 15, "bold"), bg="light green", cursor="hand2",command=adminengineerpage.engineer_account_page)
   ENGGACCOUNT.pack()
   
   USERACCOUNT=Button(new_window,text="USER ACCOUNT",font=("times new roman",15,"bold"),bg="blue",cursor="hand2",command=adminusercreatepage.adminuserpage)
   USERACCOUNT.pack()
   
   Inventory=Button(new_window,text="INVENTORY",font=("times new roman",15,"bold"),bg="pink",cursor="hand2",command=inventoryfeed.inventorywindow)
   Inventory.pack()
   
   logout_button = Button(new_window, text="Logout", font=("times new roman",15,"bold"),bg="red",cursor="hand2",command=lambda:logout_clicked())
   logout_button.pack()
   

def login_clicked(username_entry, password_entry):
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()
        query = f"SELECT * FROM admin WHERE username = '{entered_username}' AND password= '{entered_password}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            messagebox.showinfo("Login Successful", "Admin login successful.")
            openadminpage()

            
            # Add code to open the next page or perform further actions
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
def admin_button_clicked():
    login_window = Toplevel()
    login_window.title("Admin Login")

    label_username = Label(login_window, text="Username:",font=("goud old style",15),bg="black",fg="white")
    label_username.pack()
    username_entry = Entry(login_window,textvariable=label_username,font=("goud old style",15),bg="white")
    username_entry.pack()

    label_password = Label(login_window, text="Password:",font=("goud old style",15),bg="black",fg="white")
    label_password.pack()
    password_entry = Entry(login_window, show="*",textvariable=label_password,font=("goud old style",15),bg="white")
    password_entry.pack()

    login_button = Button(login_window, text="Login",font=("times new roman",15,"bold"),bg="green",cursor="hand2", command=lambda: login_clicked(username_entry, password_entry))
    login_button.pack()
    # login_window.destroy()
    