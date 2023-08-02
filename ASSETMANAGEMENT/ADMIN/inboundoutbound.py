from tkinter import messagebox, Toplevel, Label, Entry, Button
import psycopg2

def save_inbound_entry(date_of_issue_entry, reason_of_repair_entry, person_allotted_entry, model_number_entry, model_name_entry):
    # Get the entered data
    date_of_issue = date_of_issue_entry.get()
    reason_of_repair = reason_of_repair_entry.get()
    person_allotted = person_allotted_entry.get()
    model_number = model_number_entry.get()
    model_name = model_name_entry.get()

    try:
        conn = psycopg2.connect(
            database="assetmanagement",
            user="postgres",
            password="root2005417",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Insert the inbound entry into the database
        insert_query = f"INSERT INTO Inbound (date_of_issue, reason_of_repair, person_allotted, model_number, model_name) VALUES ('{date_of_issue}', '{reason_of_repair}', '{person_allotted}', '{model_number}', '{model_name}')"
        cursor.execute(insert_query)
        conn.commit()

        messagebox.showinfo("Inbound Entry Saved", "The inbound entry has been saved successfully.")

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

def save_outbound_entry(inbound_id_entry, date_of_issue_entry, date_of_receipt_entry, reason_of_repair_entry, person_allotted_entry, model_number_entry, model_name_entry):
    # Get the entered data
    inbound_id = inbound_id_entry.get()
    date_of_issue = date_of_issue_entry.get()
    date_of_receipt = date_of_receipt_entry.get()
    reason_of_repair = reason_of_repair_entry.get()
    person_allotted = person_allotted_entry.get()
    model_number = model_number_entry.get()
    model_name = model_name_entry.get()

    try:
        conn = psycopg2.connect(
            database="assetmanagement",
            user="postgres",
            password="root2005417",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Insert the outbound entry into the database
        insert_query = f"INSERT INTO Outbound (inbound_id, date_of_issue, date_of_receipt, reason_of_repair, person_allotted, model_number, model_name) VALUES ('{inbound_id}', '{date_of_issue}', '{date_of_receipt}', '{reason_of_repair}', '{person_allotted}', '{model_number}', '{model_name}')"
        cursor.execute(insert_query)
        conn.commit()

        messagebox.showinfo("Outbound Entry Saved", "The outbound entry has been saved successfully.")

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

def create_window():
    window = Toplevel()
    window.title("Save Entries")
    
    def destroy_other_window():
        if 'outbound_window' in globals():
            outbound_window.destroy()
        if 'inbound_window' in globals():
            inbound_window.destroy()

    def open_inbound_window():
        destroy_other_window()
        inbound_window = Toplevel(window)
        inbound_window.title("Inbound Entry")

        # Create labels and entry fields for inbound entry
        label_date_of_issue = Label(inbound_window, text="Date of Issue:")
        label_date_of_issue.pack()
        date_of_issue_entry = Entry(inbound_window)
        date_of_issue_entry.pack()

        label_reason_of_repair = Label(inbound_window, text="Reason of Repair:")
        label_reason_of_repair.pack()
        reason_of_repair_entry = Entry(inbound_window)
        reason_of_repair_entry.pack()

        label_person_allotted = Label(inbound_window, text="Person Allotted:")
        label_person_allotted.pack()
        person_allotted_entry = Entry(inbound_window)
        person_allotted_entry.pack()

        label_model_number = Label(inbound_window, text="Model Number:")
        label_model_number.pack()
        model_number_entry = Entry(inbound_window)
        model_number_entry.pack()

        label_model_name = Label(inbound_window, text="Model Name:")
        label_model_name.pack()
        model_name_entry = Entry(inbound_window)
        model_name_entry.pack()

        # Create a button to save the inbound entry
        save_inbound_button = Button(inbound_window, text="Save Inbound Entry", command=lambda: save_inbound_entry(date_of_issue_entry, reason_of_repair_entry, person_allotted_entry, model_number_entry, model_name_entry))
        save_inbound_button.pack()

    def open_outbound_window():
        destroy_other_window()
        outbound_window = Toplevel(window)
        outbound_window.title("Outbound Entry")

        # Create labels and entry fields for outbound entry
        label_inbound_id = Label(outbound_window, text="Inbound ID:")
        label_inbound_id.pack()
        inbound_id_entry = Entry(outbound_window)
        inbound_id_entry.pack()

        label_date_of_issue = Label(outbound_window, text="Date of Issue:")
        label_date_of_issue.pack()
        date_of_issue_entry = Entry(outbound_window)
        date_of_issue_entry.pack()

        label_date_of_receipt = Label(outbound_window, text="Date of Receipt:")
        label_date_of_receipt.pack()
        date_of_receipt_entry = Entry(outbound_window)
        date_of_receipt_entry.pack()

        label_reason_of_repair = Label(outbound_window, text="Reason of Repair:")
        label_reason_of_repair.pack()
        reason_of_repair_entry = Entry(outbound_window)
        reason_of_repair_entry.pack()

        label_person_allotted = Label(outbound_window, text="Person Allotted:")
        label_person_allotted.pack()
        person_allotted_entry = Entry(outbound_window)
        person_allotted_entry.pack()

        label_model_number = Label(outbound_window, text="Model Number:")
        label_model_number.pack()
        model_number_entry = Entry(outbound_window)
        model_number_entry.pack()

        label_model_name = Label(outbound_window, text="Model Name:")
        label_model_name.pack()
        model_name_entry = Entry(outbound_window)
        model_name_entry.pack()

        # Create a button to save the outbound entry
        save_outbound_button = Button(outbound_window, text="Save Outbound Entry", command=lambda: save_outbound_entry(inbound_id_entry, date_of_issue_entry, date_of_receipt_entry, reason_of_repair_entry, person_allotted_entry, model_number_entry, model_name_entry))
        save_outbound_button.pack()

    # Create buttons to open the inbound and outbound windows
    inbound_button = Button(window, text="Open Inbound Window", command=open_inbound_window)
    inbound_button.pack()

    outbound_button = Button(window, text="Open Outbound Window", command=open_outbound_window)
    outbound_button.pack()
