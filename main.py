import tkinter as tk
from tkinter import messagebox
import datetime


vaccination_records = {}
appointments = {}


def add_child_record():
    name = name_entry.get()
    vaccine = vaccine_entry.get()
    date = date_entry.get()

    if name and vaccine and date:
        try:
            vaccination_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            if name not in vaccination_records:
                vaccination_records[name] = []
            vaccination_records[name].append({
                'vaccine_name': vaccine,
                'vaccination_date': vaccination_date
            })
            messagebox.showinfo("Success", f"Added record for {name}: {vaccine} on {date}")
            clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def schedule_appointment():
    name = name_entry.get()
    date = appointment_date_entry.get()

    if name and date:
        try:
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            if name not in appointments:
                appointments[name] = []
            appointments[name].append(appointment_date)
            messagebox.showinfo("Success", f"Scheduled appointment for {name} on {date}")
            clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def view_records():
    name = name_entry.get()
    if name in vaccination_records:
        records = vaccination_records[name]
        result = "\n".join([f"Vaccine: {rec['vaccine_name']}, Date: {rec['vaccination_date']}" for rec in records])
        messagebox.showinfo("Vaccination Records", result)
    else:
        messagebox.showinfo("No Records", "No records found for this child")

def view_appointments():
    name = name_entry.get()
    if name in appointments:
        dates = appointments[name]
        result = "\n".join([f"Appointment Date: {date}" for date in dates])
        messagebox.showinfo("Appointments", result)
    else:
        messagebox.showinfo("No Appointments", "No appointments found for this child")

def clear_entries():
    name_entry.delete(0, tk.END)
    vaccine_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    appointment_date_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Child Vaccination Management System")
tk.Label(root, text="Child's Name").grid(row=0, column=0)
tk.Label(root, text="Vaccine Name").grid(row=1, column=0)
tk.Label(root, text="Vaccination Date (YYYY-MM-DD)").grid(row=2, column=0)
tk.Label(root, text="Appointment Date (YYYY-MM-DD)").grid(row=3, column=0)

name_entry = tk.Entry(root)
vaccine_entry = tk.Entry(root)
date_entry = tk.Entry(root)
appointment_date_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
vaccine_entry.grid(row=1, column=1)
date_entry.grid(row=2, column=1)
appointment_date_entry.grid(row=3, column=1)


tk.Button(root, text="Add Record", command=add_child_record).grid(row=4, column=0, pady=10)
tk.Button(root, text="Schedule Appointment", command=schedule_appointment).grid(row=4, column=1, pady=10)
tk.Button(root, text="View Records", command=view_records).grid(row=5, column=0, pady=10)
tk.Button(root, text="View Appointments", command=view_appointments).grid(row=5, column=1, pady=10)


root.mainloop()
