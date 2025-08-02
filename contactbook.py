import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    clear_entries()
    update_contact_list()
    messagebox.showinfo("Success", "Contact added successfully.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        display = f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}"
        listbox_contacts.insert(tk.END, display)

def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone to search:")
    if not keyword:
        return

    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            messagebox.showinfo("Contact Found",
                f"Name: {contact['name']}\n"
                f"Phone: {contact['phone']}\n"
                f"Email: {contact['email']}\n"
                f"Address: {contact['address']}")
            return
    messagebox.showwarning("Not Found", "No contact matched.")

def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Select", "Select a contact to delete.")
        return

    index = selected[0]
    del contacts[index]
    update_contact_list()
    messagebox.showinfo("Deleted", "Contact deleted successfully.")

def update_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Select", "Select a contact to update.")
        return

    index = selected[0]
    contact = contacts[index]

    name = simpledialog.askstring("Update", f"Name ({contact['name']}):") or contact['name']
    phone = simpledialog.askstring("Update", f"Phone ({contact['phone']}):") or contact['phone']
    email = simpledialog.askstring("Update", f"Email ({contact['email']}):") or contact['email']
    address = simpledialog.askstring("Update", f"Address ({contact['address']}):") or contact['address']

    contacts[index] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    update_contact_list()
    messagebox.showinfo("Updated", "Contact updated successfully.")

# GUI Setup
root = tk.Tk()
root.title(" Contact Book ")
root.geometry("600x550")

# Entry Fields
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root, width=50)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root, width=50)
entry_address.pack()

tk.Button(root, text="Add Contact", command=add_contact, bg="lightgreen").pack(pady=5)

# Listbox
tk.Label(root, text="Contact List (Full Details)").pack()
listbox_contacts = tk.Listbox(root, width=80, height=10)
listbox_contacts.pack()

# Buttons
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=2)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=2)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=2)
tk.Button(root, text="Exit", command=root.quit, bg="salmon").pack(pady=10)

root.mainloop()
