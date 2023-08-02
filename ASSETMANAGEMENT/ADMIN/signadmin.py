import ADMINPG
import USERPG
import enginnerpage
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from connection import test_connection
from flask import Flask
from threading import Thread

app = Flask(__name__)

def run_tkinter():
    root = Tk()
    root.geometry("1200x700+0+0")
    root.title("INVENTORY MANAGEMENT SYSTEM BY IRCON")
    title = Label(root, text="INVENTORY MANAGEMENT", font=("times new roman ", 40, "bold"), bg="#010c48",
                  fg="white").place(x=0, y=0, relwidth=1, height=70)
    root.configure(bg="#b1d2f0")
    # test_connection()

    frame = Frame(root, bg="white", width="400", height="900")
    frame.pack(pady=150, padx=20)

    TEXT_IRCON = Label(frame, text="MENU", height=5, width=40, bg="light green", fg="black")
    TEXT_IRCON.config(font=("TIMES NEW ROMAN", 20))
    TEXT_IRCON.pack()
    # irconlogo=Image.open("C:\\Users\\tanvi\\Desktop\\ASSETMANAGEMENT\\ADMIN\\irconback.png")
    # irconlogo=irconlogo.resize((100,100),Image.ANTIALIAS)
    # lbl_irconlogo=Label(frame,image=irconlogo)
    b1 = Button(frame, text="ADMIN", font=("times new roman", 15, "bold"), bg="red", cursor="hand2",
                command=ADMINPG.admin_button_clicked)
    b1.pack(pady=10)

    b2 = Button(frame, text="USER", font=("times new roman", 15, "bold"), bg="green", cursor="hand2",
                command=USERPG.user_button_clicked)
    b2.pack(pady=10)

    b3 = Button(frame, text="ENGINEER", font=("times new roman", 15, "bold"), bg="pink", cursor="hand2",
                command=enginnerpage.engineer_button_clicked)
    b3.pack(pady=10)

    root.resizable(0, 0)
    root.mainloop()

@app.route('/')
def signadmin():
    thread = Thread(target=run_tkinter)
    thread.start()
    return 'Signadmin module executed successfully!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8083)
