'''
Created on 10-Jul-2023

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
import inboundoutbound
def login_clicked(username_entry, password_entry):
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    try:
        conn = psycopg2.connect(database="assetmanagement", user="postgres", password="root2005417", host="localhost", port="5432")
        cursor = conn.cursor()
        query = f"SELECT * FROM engineer WHERE email = '{entered_username}' AND password= '{entered_password}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            messagebox.showinfo("Login Successful", "ENGINEER login successful.")
            # viewuserassetdetials()
            # login_window = Toplevel()
            # login_window.title("INBOUND-OUTBOUND")
            inboundoutbound.create_window()
            
            # Add code to open the next page or perform further actions
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
def engineer_button_clicked():
    login_window = Toplevel()
    login_window.title("ENGINEER Login")

    label_username = Label(login_window, text="ENGINEER USERNAME")
    label_username.pack()
    username_entry = Entry(login_window,textvariable=label_username,font=("goud old style",15),bg="white")
    username_entry.pack()

    label_password = Label(login_window, text="Password:")
    label_password.pack()
    password_entry = Entry(login_window, show="*",textvariable=label_password,font=("goud old style",15),bg="white")
    password_entry.pack()

    login_button = Button(login_window, text="Login",command=lambda:login_clicked(username_entry,password_entry))
    login_button.pack()
