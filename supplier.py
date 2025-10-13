# from tkinter import*
# from PIL import Image,ImageTk
# from tkinter import ttk,messagebox
# import sqlite3

# class supplierClass:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1100x500+320+220")
#         self.root.title("Inventory Management System | Nishant Gupta")
#         self.root.config(bg="white")
#         self.root.resizable(False,False)
#         self.root.focus_force()

#         #------------ all variables --------------
#         self.var_searchby=StringVar()
#         self.var_searchtxt=StringVar()
#         self.var_sup_invoice=StringVar()
#         self.var_name=StringVar()
#         self.var_contact=StringVar()
        
        
#         #---------- Search Frame -------------
#         lbl_search=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",15))
#         lbl_search.place(x=700,y=80)

#         txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=850,y=80,width=160)
#         btn_search=Button(self.root,command=self.search,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

#         #-------------- title ---------------
#         title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

#         #-------------- content ---------------
#         #---------- row 1 ----------------
#         lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
#         txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
        
#         #---------- row 2 ----------------
#         lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
#         txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)
        
#         #---------- row 3 ----------------
#         lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
#         txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)
        
#         #---------- row 4 ----------------
#         lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
#         self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
#         self.txt_desc.place(x=180,y=200,width=470,height=120)
        
#         #-------------- buttons -----------------
#         btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
#         btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
#         btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
#         btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

#         #------------ supplier details -------------
#         sup_frame=Frame(self.root,bd=3,relief=RIDGE)
#         sup_frame.place(x=700,y=120,width=380,height=350)

#         scrolly=Scrollbar(sup_frame,orient=VERTICAL)
#         scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)\
        
#         self.SupplierTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
#         scrollx.pack(side=BOTTOM,fill=X)
#         scrolly.pack(side=RIGHT,fill=Y)
#         scrollx.config(command=self.SupplierTable.xview)
#         scrolly.config(command=self.SupplierTable.yview)
#         self.SupplierTable.heading("invoice",text="Invoice")
#         self.SupplierTable.heading("name",text="Name")
#         self.SupplierTable.heading("contact",text="Contact")
#         self.SupplierTable.heading("desc",text="Description")
#         self.SupplierTable["show"]="headings"
#         self.SupplierTable.column("invoice",width=90)
#         self.SupplierTable.column("name",width=100)
#         self.SupplierTable.column("contact",width=100)
#         self.SupplierTable.column("desc",width=100)
        
#         self.SupplierTable.pack(fill=BOTH,expand=1)
#         self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
#         self.show()
# #-----------------------------------------------------------------------------------------------------
#     def add(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             if self.var_sup_invoice.get()=="":
#                 messagebox.showerror("Error","Invoice must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
#                 row=cur.fetchone()
#                 if row!=None:
#                     messagebox.showerror("Error","Invoice no. is already assigned",parent=self.root)
#                 else:
#                     cur.execute("insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
#                         self.var_sup_invoice.get(),
#                         self.var_name.get(),
#                         self.var_contact.get(),
#                         self.txt_desc.get('1.0',END),
#                     ))
#                     con.commit()
#                     messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
#                     self.clear()
#                     self.show()
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")

#     def show(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             cur.execute("select * from supplier")
#             rows=cur.fetchall()
#             self.SupplierTable.delete(*self.SupplierTable.get_children())
#             for row in rows:
#                 self.SupplierTable.insert('',END,values=row)
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")

#     def get_data(self,ev):
#         f=self.SupplierTable.focus()
#         content=(self.SupplierTable.item(f))
#         row=content['values']
#         self.var_sup_invoice.set(row[0])
#         self.var_name.set(row[1])
#         self.var_contact.set(row[2])
#         self.txt_desc.delete('1.0',END)
#         self.txt_desc.insert(END,row[3])

#     def update(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             if self.var_sup_invoice.get()=="":
#                 messagebox.showerror("Error","Invoice must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
#                 row=cur.fetchone()
#                 if row==None:
#                     messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
#                 else:
#                     cur.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(
#                         self.var_name.get(),
#                         self.var_contact.get(),
#                         self.txt_desc.get('1.0',END),
#                         self.var_sup_invoice.get(),
#                     ))
#                     con.commit()
#                     messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
#                     self.show()
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")

#     def delete(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             if self.var_sup_invoice.get()=="":
#                 messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
#                 row=cur.fetchone()
#                 if row==None:
#                     messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
#                 else:
#                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
#                     if op==True:
#                         cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
#                         con.commit()
#                         messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
#                         self.clear()
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")

#     def clear(self):
#         self.var_sup_invoice.set("")
#         self.var_name.set("")
#         self.var_contact.set("")
#         self.txt_desc.delete('1.0',END)
#         self.var_searchtxt.set("")
#         self.show()

#     def search(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             if self.var_searchtxt.get()=="":
#                 messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
#             else:
#                 cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
#                 row=cur.fetchone()
#                 if row!=None:
#                     self.SupplierTable.delete(*self.SupplierTable.get_children())
#                     self.SupplierTable.insert('',END,values=row)
#                 else:
#                     messagebox.showerror("Error","No record found!!!",parent=self.root)
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")


# if __name__=="__main__":
#     root=Tk()
#     obj=supplierClass(root)
#     root.mainloop()

#mongodb code
from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient

from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Supplier Management")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()

        # === MongoDB Connection ===
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["ims"]
        self.collection = self.db["supplier"]

        # === Variables ===
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # === Title ===
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        lbl_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white")
        lbl_invoice.place(x=50, y=60)

        txt_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow")
        txt_invoice.place(x=180, y=60, width=180)

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=50, y=100)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=180, y=100, width=180)

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=50, y=140)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=180, y=140, width=180)

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white")
        lbl_address.place(x=50, y=180)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=180, y=180, width=300, height=60)

        # === Buttons ===
        btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white")
        btn_add.place(x=500, y=60, width=100, height=28)

        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white")
        btn_update.place(x=610, y=60, width=100, height=28)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white")
        btn_delete.place(x=720, y=60, width=100, height=28)

        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white")
        btn_clear.place(x=830, y=60, width=100, height=28)

        # === Table ===
        supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
        supplier_frame.place(x=0, y=260, relwidth=1, height=230)

        scrolly = Scrollbar(supplier_frame, orient=VERTICAL)
        scrollx = Scrollbar(supplier_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(supplier_frame, columns=("invoice", "name", "contact", "address"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Invoice No.")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("address", text="Address")

        self.SupplierTable["show"] = "headings"
        self.SupplierTable.column("invoice", width=100)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("address", width=200)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self):
        try:
            data = {
                "invoice": self.var_sup_invoice.get(),
                "name": self.var_name.get(),
                "contact": self.var_contact.get(),
                "address": self.txt_address.get("1.0", END).strip()
            }
            if self.collection.find_one({"invoice": data["invoice"]}):
                messagebox.showerror("Error", "Invoice No. already exists", parent=self.root)
            else:
                self.collection.insert_one(data)
                messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        self.SupplierTable.delete(*self.SupplierTable.get_children())
        for doc in self.collection.find():
            self.SupplierTable.insert("", END, values=(
                doc.get("invoice", ""),
                doc.get("name", ""),
                doc.get("contact", ""),
                doc.get("address", "")
            ))

    def get_data(self, ev):
        selected = self.SupplierTable.focus()
        data = self.SupplierTable.item(selected)['values']
        if data:
            self.var_sup_invoice.set(data[0])
            self.var_name.set(data[1])
            self.var_contact.set(data[2])
            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, data[3])

    def update(self):
        try:
            query = {"invoice": self.var_sup_invoice.get()}
            new_data = {
                "$set": {
                    "name": self.var_name.get(),
                    "contact": self.var_contact.get(),
                    "address": self.txt_address.get("1.0", END).strip()
                }
            }
            result = self.collection.update_one(query, new_data)
            if result.matched_count:
                messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                self.show()
            else:
                messagebox.showerror("Error", "Invoice No. not found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        try:
            query = {"invoice": self.var_sup_invoice.get()}
            result = self.collection.delete_one(query)
            if result.deleted_count:
                messagebox.showinfo("Success", "Supplier deleted successfully", parent=self.root)
                self.show()
            else:
                messagebox.showerror("Error", "Invoice No. not found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_address.delete("1.0", END)

if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
