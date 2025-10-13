# from tkinter import*
# from PIL import Image,ImageTk
# from tkinter import ttk,messagebox
# import sqlite3

# class categoryClass:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1100x500+320+220")
#         self.root.title("Inventory Management System | Nishant Gupta")
#         self.root.config(bg="white")
#         self.root.resizable(False,False)
#         self.root.focus_force()

#         #------------ variables -------------
#         self.var_cat_id=StringVar()
#         self.var_name=StringVar()
#         #--------------- title ---------------------
#         lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
#         lbl_mame=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
#         txt_mame=Entry(self.root,textvariable=self.var_name,bg="lightyellow",font=("goudy old style",18)).place(x=50,y=170,width=300)

#         btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
#         btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)

#         #------------ category details -------------
#         cat_frame=Frame(self.root,bd=3,relief=RIDGE)
#         cat_frame.place(x=700,y=100,width=380,height=100)

#         scrolly=Scrollbar(cat_frame,orient=VERTICAL)
#         scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)\
        
#         self.CategoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
#         scrollx.pack(side=BOTTOM,fill=X)
#         scrolly.pack(side=RIGHT,fill=Y)
#         scrollx.config(command=self.CategoryTable.xview)
#         scrolly.config(command=self.CategoryTable.yview)
#         self.CategoryTable.heading("cid",text="C ID")
#         self.CategoryTable.heading("name",text="Name")
#         self.CategoryTable["show"]="headings"
#         self.CategoryTable.column("cid",width=90)
#         self.CategoryTable.column("name",width=100)
        
#         self.CategoryTable.pack(fill=BOTH,expand=1)
#         self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
#         self.show()

#         #----------------- images ---------------------
#         self.im1=Image.open("Inventory-Management-System/images/cat.jpg")
#         self.im1=self.im1.resize((500,250))
#         self.im1=ImageTk.PhotoImage(self.im1)
#         self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
#         self.lbl_im1.place(x=50,y=220)

#         self.im2=Image.open("Inventory-Management-System/images/category.jpg")
#         self.im2=self.im2.resize((500,250))
#         self.im2=ImageTk.PhotoImage(self.im2)
#         self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
#         self.lbl_im2.place(x=580,y=220)
# #----------------------------------------------------------------------------------
#     def add(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             if self.var_name.get()=="":
#                 messagebox.showerror("Error","Category Name must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from category where name=?",(self.var_name.get(),))
#                 row=cur.fetchone()
#                 if row!=None:
#                     messagebox.showerror("Error","Category already present",parent=self.root)
#                 else:
#                     cur.execute("insert into category(name) values(?)",(
#                         self.var_name.get(),
#                     ))
#                     con.commit()
#                     messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
#                     self.clear()
#                     self.show()
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")

#     def show(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             cur.execute("select * from category")
#             rows=cur.fetchall()
#             self.CategoryTable.delete(*self.CategoryTable.get_children())
#             for row in rows:
#                 self.CategoryTable.insert('',END,values=row)
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")

    
#     def clear(self):
#         self.var_name.set("")
#         self.show()

#     def get_data(self,ev):
#         f=self.CategoryTable.focus()
#         content=(self.CategoryTable.item(f))
#         row=content['values']
#         self.var_cat_id.set(row[0])
#         self.var_name.set(row[1])
    
#     def delete(self):
#         con=sqlite3.connect(database=r'ims.db')
#         cur=con.cursor()
#         try:
#             if self.var_cat_id.get()=="":
#                 messagebox.showerror("Error","Category name must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
#                 row=cur.fetchone()
#                 if row==None:
#                     messagebox.showerror("Error","Invalid Category Name",parent=self.root)
#                 else:
#                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
#                     if op==True:
#                         cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
#                         con.commit()
#                         messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
#                         self.clear()
#                         self.var_cat_id.set("")
#                         self.var_name.set("")
#         except Exception as ex:
#             messagebox.showerror("Error",f"Error due to : {str(ex)}")



# if __name__=="__main__":
#     root=Tk()
#     obj=categoryClass(root)
#     root.mainloop()

#mongodb code
from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Category Management")
        self.root.geometry("600x400+400+150")
        self.root.config(bg="white")
        self.root.focus_force()

        # === MongoDB Connection ===
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["ims"]
        self.collection = self.db["category"]

        # === Variables ===
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # === Title ===
        title = Label(self.root, text="Manage Product Category", font=("goudy old style", 20), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=30, y=60)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=30, y=100, width=300)

        btn_add = Button(self.root, text="Add", command=self.add, font=("goudy old style", 15), bg="#4caf50", fg="white")
        btn_add.place(x=340, y=100, width=100, height=30)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white")
        btn_delete.place(x=450, y=100, width=100, height=30)

        # === Category Table ===
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=0, y=150, relwidth=1, height=250)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(cat_frame, columns=("name",), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("name", text="Name")
        self.CategoryTable["show"] = "headings"
        self.CategoryTable.column("name", width=200)

        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self):
        name = self.var_name.get()
        if name == "":
            messagebox.showerror("Error", "Category name must be required", parent=self.root)
        else:
            try:
                if self.collection.find_one({"name": name}):
                    messagebox.showerror("Error", "Category already exists", parent=self.root)
                else:
                    self.collection.insert_one({"name": name})
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        self.CategoryTable.delete(*self.CategoryTable.get_children())
        for doc in self.collection.find():
            self.CategoryTable.insert("", END, values=(doc.get("name", ""),))

    def get_data(self, ev):
        selected = self.CategoryTable.focus()
        data = self.CategoryTable.item(selected)["values"]
        if data:
            self.var_name.set(data[0])

    def delete(self):
        name = self.var_name.get()
        if name == "":
            messagebox.showerror("Error", "Select category to delete", parent=self.root)
        else:
            try:
                result = self.collection.delete_one({"name": name})
                if result.deleted_count:
                    messagebox.showinfo("Success", "Category deleted successfully", parent=self.root)
                    self.show()
                else:
                    messagebox.showerror("Error", "Category not found", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
