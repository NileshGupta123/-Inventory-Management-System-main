from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import os
import dashboard1  # This should be your dashboard file

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login | IMS")
        self.root.geometry("400x400+500+200")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # === MongoDB Setup ===
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["ims"]
        self.user_col = self.db["users"]

        # === UI ===
        title = Label(self.root, text="IMS Login", font=("times new roman", 25, "bold"), bg="white", fg="#010c48")
        title.pack(pady=30)

        lbl_user = Label(self.root, text="Username", font=("times new roman", 15), bg="white")
        lbl_user.pack(pady=(10, 0))
        self.txt_user = Entry(self.root, font=("times new roman", 15), bg="lightyellow")
        self.txt_user.pack(pady=(0, 10))

        lbl_pass = Label(self.root, text="Password", font=("times new roman", 15), bg="white")
        lbl_pass.pack(pady=(10, 0))
        self.txt_pass = Entry(self.root, font=("times new roman", 15), show="*", bg="lightyellow")
        self.txt_pass.pack(pady=(0, 20))

        btn_login = Button(self.root, text="Login", command=self.login, font=("times new roman", 15), bg="#4caf50", fg="white")
        btn_login.pack(pady=10)

    def login(self):
        username = self.txt_user.get().strip()
        password = self.txt_pass.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # === Authenticate ===
        user = self.user_col.find_one({"username": username, "password": password})
        if user:
            messagebox.showinfo("Success", f"Welcome {username}", parent=self.root)
            self.root.destroy()
            self.open_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)

    def open_dashboard(self):
        root_dash = Tk()
        app = dashboard1.IMS(root_dash)
        root_dash.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
