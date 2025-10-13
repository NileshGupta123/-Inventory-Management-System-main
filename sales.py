# from tkinter import*
# from PIL import Image,ImageTk
# from tkinter import ttk,messagebox
# import sqlite3
# import os

# class salesClass:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1100x500+320+220")
#         self.root.title("Inventory Management System | Nishant Gupta")
#         self.root.config(bg="white")
#         self.root.resizable(False,False)
#         self.root.focus_force()

#         self.blll_list=[]
#         self.var_invoice=StringVar()
#         #--------------- title ---------------------
#         lbl_title=Label(self.root,text="View Customer Bills",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
#         lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="white").place(x=50,y=100)
#         txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)

#         btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
#         btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=490,y=100,width=120,height=28)

#         #----------------- bill list -------------------
#         sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
#         sales_Frame.place(x=50,y=140,width=200,height=330)

#         scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
#         self.Sales_List=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
#         scrolly.pack(side=RIGHT,fill=Y)
#         scrolly.config(command=self.Sales_List.yview)
#         self.Sales_List.pack(fill=BOTH,expand=1)
#         self.Sales_List.bind("<ButtonRelease-1>",self.get_data)

#         #--------------- bill area ----------------------
#         bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
#         bill_Frame.place(x=280,y=140,width=410,height=330)
        
#         lbl_title2=Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)
        
#         scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
#         self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2.set)
#         scrolly2.pack(side=RIGHT,fill=Y)
#         scrolly2.config(command=self.bill_area.yview)
#         self.bill_area.pack(fill=BOTH,expand=1)

#         #------------- image -----------------
#         self.bill_photo=Image.open("Inventory-Management-System/images/cat2.jpg")
#         self.bill_photo=self.bill_photo.resize((450,300))
#         self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

#         lbl_image=Label(self.root,image=self.bill_photo,bd=0)
#         lbl_image.place(x=700,y=110)
        
#         self.show()
# #----------------------------------------------------------------------------------------------------
#     def show(self):
#         del self.blll_list[:]
#         self.Sales_List.delete(0,END)
#         for i in os.listdir('Inventory-Management-System/bill'):
#             if i.split('.')[-1]=='txt':
#                 self.Sales_List.insert(END,i)
#                 self.blll_list.append(i.split('.')[0])

#     def get_data(self,ev):
#         index_=self.Sales_List.curselection()
#         file_name=self.Sales_List.get(index_)
#         self.bill_area.delete('1.0',END)
#         fp=open(f'Inventory-Management-System/bill/{file_name}','r')
#         for i in fp:
#             self.bill_area.insert(END,i)
#         fp.close()

#     def search(self):
#         if self.var_invoice.get()=="":
#             messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
#         else:
#             if self.var_invoice.get() in self.blll_list:
#                 fp=open(f'Inventory-Management-System/bill/{self.var_invoice.get()}.txt','r')
#                 self.bill_area.delete('1.0',END)
#                 for i in fp:
#                     self.bill_area.insert(END,i)
#                 fp.close()
#             else:
#                 messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

#     def clear(self):
#         self.show()
#         self.bill_area.delete('1.0',END)


# if __name__=="__main__":
#     root=Tk()
#     obj=salesClass(root)
#     root.mainloop()

#mongodb code
# from tkinter import *
# from tkinter import ttk, messagebox
# from pymongo import MongoClient
# import os

# class salesClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sales Management")
#         self.root.geometry("1000x500+220+130")
#         self.root.config(bg="white")
#         self.root.focus_force()

#         # === MongoDB Connection ===
#         self.client = MongoClient("mongodb://localhost:27017/")
#         self.db = self.client["ims"]
#         self.collection = self.db["sales"]

#         # === Title ===
#         title = Label(self.root, text="View Customer Bills", font=("goudy old style", 20), bg="#0f4d7d", fg="white")
#         title.pack(side=TOP, fill=X)

#         # === Bill Search Area ===
#         self.var_invoice = StringVar()
#         lbl_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white")
#         lbl_invoice.place(x=50, y=70)

#         txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15), bg="lightyellow")
#         txt_invoice.place(x=160, y=70, width=180)

#         btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white")
#         btn_search.place(x=360, y=70, width=100, height=28)

#         btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white")
#         btn_clear.place(x=470, y=70, width=100, height=28)

#         # === Bill List Frame ===
#         sales_frame = Frame(self.root, bd=3, relief=RIDGE)
#         sales_frame.place(x=50, y=120, width=200, height=330)

#         scrolly = Scrollbar(sales_frame, orient=VERTICAL)
#         self.sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
#         scrolly.pack(side=RIGHT, fill=Y)
#         scrolly.config(command=self.sales_list.yview)
#         self.sales_list.pack(fill=BOTH, expand=1)
#         self.sales_list.bind("<ButtonRelease-1>", self.get_data)

#         # === Bill Display Area ===
#         bill_frame = Frame(self.root, bd=3, relief=RIDGE)
#         bill_frame.place(x=280, y=120, width=680, height=330)

#         lbl_bill_area = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 15), bg="orange")
#         lbl_bill_area.pack(side=TOP, fill=X)

#         scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
#         self.txt_bill_area = Text(bill_frame, yscrollcommand=scrolly2.set, font=("goudy old style", 13), bg="lightyellow")
#         scrolly2.pack(side=RIGHT, fill=Y)
#         scrolly2.config(command=self.txt_bill_area.yview)
#         self.txt_bill_area.pack(fill=BOTH, expand=1)

#         self.show()

#     def show(self):
#         self.sales_list.delete(0, END)
#         bill_dir = os.path.join(os.path.dirname(__file__), "bill")  # ✅ Absolute path
#         if os.path.exists(bill_dir):
#             for file in os.listdir(bill_dir):
#                 if file.endswith(".txt"):
#                     self.sales_list.insert(END, file.replace(".txt", ""))
#         else:
#             messagebox.showwarning("Warning", f"Bill directory not found at:\n{bill_dir}")

#     def get_data(self, ev):
#         selected = self.sales_list.curselection()
#         if selected:
#             filename = self.sales_list.get(selected[0])
#             self.show_bill(filename)

#     def show_bill(self, invoice):
#         try:
#             self.txt_bill_area.delete("1.0", END)
#             bill_path = os.path.join(os.path.dirname(__file__), "bill", f"{invoice}.txt")  # ✅ Absolute path
#             if os.path.exists(bill_path):
#                 with open(bill_path, "r") as f:
#                     self.txt_bill_area.insert(END, f.read())
#             else:
#                 messagebox.showerror("Error", f"Bill not found:\n{bill_path}")
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

#     def search(self):
#         invoice = self.var_invoice.get().strip()
#         if invoice == "":
#             messagebox.showerror("Error", "Invoice no. is required", parent=self.root)
#         else:
#             if invoice in self.sales_list.get(0, END):
#                 self.show_bill(invoice)
#             else:
#                 messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)

#     def clear(self):
#         self.var_invoice.set("")
#         self.show()
#         self.txt_bill_area.delete("1.0", END)

# if __name__ == "__main__":
#     root = Tk()
#     obj = salesClass(root)
#     root.mainloop()


#new mongodb code
# from tkinter import *
# from tkinter import ttk, messagebox
# from pymongo import MongoClient

# class salesClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sales Management")
#         self.root.geometry("1000x500+220+130")
#         self.root.config(bg="white")
#         self.root.focus_force()

#         # === MongoDB Connection ===
#         self.client = MongoClient("mongodb://localhost:27017/")
#         self.db = self.client["ims"]
#         self.collection = self.db["sales"]

#         # === Title ===
#         title = Label(self.root, text="Sales Records", font=("goudy old style", 20), bg="#0f4d7d", fg="white")
#         title.pack(side=TOP, fill=X)

#         # === Search Area ===
#         self.var_invoice = StringVar()
#         lbl_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white")
#         lbl_invoice.place(x=50, y=70)

#         txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15), bg="lightyellow")
#         txt_invoice.place(x=160, y=70, width=180)

#         btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white")
#         btn_search.place(x=360, y=70, width=100, height=28)

#         btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white")
#         btn_clear.place(x=470, y=70, width=100, height=28)

#         # === Bill List Frame ===
#         sales_frame = Frame(self.root, bd=3, relief=RIDGE)
#         sales_frame.place(x=50, y=120, width=200, height=330)

#         scrolly = Scrollbar(sales_frame, orient=VERTICAL)
#         self.sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
#         scrolly.pack(side=RIGHT, fill=Y)
#         scrolly.config(command=self.sales_list.yview)
#         self.sales_list.pack(fill=BOTH, expand=1)
#         self.sales_list.bind("<ButtonRelease-1>", self.get_data)

#         # === Sales Display Area ===
#         bill_frame = Frame(self.root, bd=3, relief=RIDGE)
#         bill_frame.place(x=280, y=120, width=680, height=330)

#         lbl_bill_area = Label(bill_frame, text="Sales Details", font=("goudy old style", 15), bg="orange")
#         lbl_bill_area.pack(side=TOP, fill=X)

#         scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
#         self.txt_bill_area = Text(bill_frame, yscrollcommand=scrolly2.set, font=("goudy old style", 13), bg="lightyellow")
#         scrolly2.pack(side=RIGHT, fill=Y)
#         scrolly2.config(command=self.txt_bill_area.yview)
#         self.txt_bill_area.pack(fill=BOTH, expand=1)

#         self.show()

#     def show(self):
#         self.sales_list.delete(0, END)
#         sales = self.collection.find()
#         for sale in sales:
#             if "invoice_no" in sale:
#                 self.sales_list.insert(END, sale["invoice_no"])

#     def get_data(self, ev):
#         selected = self.sales_list.curselection()
#         if selected:
#             invoice_no = self.sales_list.get(selected[0])
#             self.show_bill(invoice_no)

#     def show_bill(self, invoice_no):
#         self.txt_bill_area.delete("1.0", END)
#         sale = self.collection.find_one({"invoice_no": invoice_no})
#         if not sale:
#             messagebox.showerror("Error", "Sale record not found")
#             return

#         self.txt_bill_area.insert(END, "\tXYZ-Inventory\n")
#         self.txt_bill_area.insert(END, "\tPhone No. 9899459288 , Delhi-110053\n")
#         self.txt_bill_area.insert(END, "="*50 + "\n")
#         self.txt_bill_area.insert(END, f"Customer Name: {sale.get('customer_name', 'N/A')}\n")
#         self.txt_bill_area.insert(END, f"Ph. no. : {sale.get('contact', 'N/A')}\n")
#         self.txt_bill_area.insert(END, f"Invoice No: {sale.get('invoice_no', 'N/A')}\tDate: {sale.get('timestamp', 'N/A')}\n")
#         self.txt_bill_area.insert(END, "="*50 + "\n")
#         self.txt_bill_area.insert(END, f"Product Name\t\tQTY\tPrice\n")
#         self.txt_bill_area.insert(END, "="*50 + "\n")

#         for item in sale.get("items", []):
#             name = item.get("name", "")
#             qty = item.get("qty", 0)
#             price = item.get("price", 0)
#             self.txt_bill_area.insert(END, f"{name}\t\t{qty}\tRs.{price*qty}\n")

#         total = sale.get("total", 0.0)
#         self.txt_bill_area.insert(END, "="*50 + "\n")
#         self.txt_bill_area.insert(END, f"Bill Amount\t\t\tRs.{total:.2f}\n")
#         self.txt_bill_area.insert(END, f"Discount\t\t\tRs.0.00\n")  # optional
#         self.txt_bill_area.insert(END, f"Net Pay\t\t\tRs.{total:.2f}\n")
#         self.txt_bill_area.insert(END, "="*50 + "\n")

#     def search(self):
#         invoice = self.var_invoice.get().strip()
#         if not invoice:
#             messagebox.showerror("Error", "Invoice number is required")
#             return
#         result = self.collection.find_one({"invoice_no": invoice})
#         if result:
#             self.show_bill(invoice)
#         else:
#             messagebox.showerror("Error", "Invoice not found in sales")

#     def clear(self):
#         self.var_invoice.set("")
#         self.txt_bill_area.delete("1.0", END)
#         self.show()

# if __name__ == "__main__":
#     root = Tk()
#     obj = salesClass(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Management")
        self.root.geometry("1000x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()

        # ✅ Update to match your billing DB
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["billing_system"]  # ✅ Make sure this matches billing.py
        self.collection = self.db["sales"]

        Label(self.root, text="Sales Records", font=("goudy old style", 20), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        self.var_invoice = StringVar()
        Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50, y=70)
        Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=160, y=70, width=180)

        Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=360, y=70, width=100, height=28)
        Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=470, y=70, width=100, height=28)

        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=120, width=200, height=330)

        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=120, width=680, height=330)

        Label(bill_frame, text="Sales Details", font=("goudy old style", 15), bg="orange").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        self.txt_bill_area = Text(bill_frame, yscrollcommand=scrolly2.set, font=("goudy old style", 13), bg="lightyellow")
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.txt_bill_area.yview)
        self.txt_bill_area.pack(fill=BOTH, expand=1)

        self.show()

    def show(self):
        self.sales_list.delete(0, END)
        for sale in self.collection.find():
            if "invoice_no" in sale:
                self.sales_list.insert(END, sale["invoice_no"])

    def get_data(self, ev):
        selected = self.sales_list.curselection()
        if selected:
            invoice_no = self.sales_list.get(selected[0])
            self.show_bill(invoice_no)

    def show_bill(self, invoice_no):
        self.txt_bill_area.delete("1.0", END)
        sale = self.collection.find_one({"invoice_no": invoice_no})
        if not sale:
            messagebox.showerror("Error", "Sale record not found")
            return

        self.txt_bill_area.insert(END, f"\tINVENTORY SYSTEM\n")
        self.txt_bill_area.insert(END, f"Customer: {sale.get('customer_name')}\n")
        self.txt_bill_area.insert(END, f"Contact: {sale.get('contact_no')}\n")
        self.txt_bill_area.insert(END, f"Invoice No: {sale.get('invoice_no')}\tDate: {sale.get('generated_at')}\n")
        self.txt_bill_area.insert(END, "="*50 + "\nProduct\tQty\tPrice\n" + "="*50 + "\n")

        for item in sale.get("products", []):
            self.txt_bill_area.insert(END, f"{item['name']}\t{item['quantity']}\tRs.{item['quantity'] * item['price']:.2f}\n")

        self.txt_bill_area.insert(END, "="*50 + f"\nTotal Amount:\tRs.{sale.get('total_amount'):.2f}\n" + "="*50)

    def search(self):
        invoice = self.var_invoice.get().strip()
        if invoice:
            self.show_bill(invoice)
        else:
            messagebox.showerror("Error", "Please enter Invoice Number")

    def clear(self):
        self.var_invoice.set("")
        self.txt_bill_area.delete("1.0", END)
        self.show()


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
