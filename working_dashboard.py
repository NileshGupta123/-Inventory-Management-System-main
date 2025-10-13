from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import sqlite3
import os

from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillingApp

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+110+80")
        self.root.title("Inventory Management System")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # ------------- Title with Logo --------------
        image_path = os.path.join(os.path.dirname(__file__), "images", "logo1.png")
        try:
            self.icon_title = PhotoImage(file=image_path)
            title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                          font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
            title.place(x=0, y=0, relwidth=1, height=70)
        except:
            title = Label(self.root, text="Inventory Management System",
                          font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
            title.place(x=0, y=0, relwidth=1, height=70)

        # ------------ Logout Button -----------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # ------------ Clock -----------------
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ---------------- Left Menu ---------------
        try:
            menu_path = os.path.join(os.path.dirname(__file__), "images", "menu_im.png")
            self.MenuLogo = Image.open(menu_path)
            self.MenuLogo = self.MenuLogo.resize((200, 200))
            self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

            LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
            LeftMenu.place(x=0, y=102, width=200, height=565)

            lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
            lbl_menuLogo.pack(side=TOP, fill=X)
        except:
            LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
            LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)

        try:
            side_path = os.path.join(os.path.dirname(__file__), "images", "side.png")
            self.icon_side = PhotoImage(file=side_path)
        except:
            self.icon_side = None

        # Create buttons
        btn_employee = Button(LeftMenu, text="Employee", command=self.employee,
                              compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                              bg="white", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)

        btn_supplier = Button(LeftMenu, text="Supplier", command=self.supplier,
                              compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                              bg="white", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)

        btn_category = Button(LeftMenu, text="Category", command=self.category,
                              compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                              bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)

        btn_product = Button(LeftMenu, text="Products", command=self.product,
                             compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                             bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)

        btn_sales = Button(LeftMenu, text="Sales", command=self.sales,
                           compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                           bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)

        btn_billing = Button(LeftMenu, text="Billing", command=self.billing,
                             compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                             bg="white", bd=3, cursor="hand2")
        btn_billing.pack(side=TOP, fill=X)

        btn_exit = Button(LeftMenu, text="Exit", command=self.root.quit,
                          compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"),
                          bg="white", bd=3, cursor="hand2")
        btn_exit.pack(side=TOP, fill=X)

        # ----------- Dashboard Labels ----------------
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE,
                                 bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE,
                               bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # ------------ Footer -----------------
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | For any Technical Issues Contact: 9899459288",
                           font=("times new roman", 12), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)

        self.update_content()

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillingApp(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n[ {str(len(supplier))} ]")
            
            bill_folder = os.path.join(os.path.dirname(__file__), "bill")
            if os.path.exists(bill_folder):
                bill = len(os.listdir(bill_folder))
            else:
                bill = 0
            self.lbl_sales.config(text=f"Total Sales\n[ {str(bill)} ]")

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
