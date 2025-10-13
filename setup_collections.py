from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ims"]

# Drop existing collections (for clean setup - optional)
db.drop_collection("employee")
db.drop_collection("supplier")
db.drop_collection("category")
db.drop_collection("product")
db.drop_collection("sales")
db.drop_collection("billing")


# === Create & populate employee collection ===
db["employee"].insert_many([
    {
        "name": "John Doe",
        "email": "john@example.com",
        "gender": "Male",
        "contact": "1234567890",
        "dob": "1990-01-01",
        "doj": "2020-05-01",
        "pass": "admin123",
        "utype": "Admin",
        "address": "New York",
        "salary": "50000"
    },
    {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "gender": "Female",
        "contact": "9876543210",
        "dob": "1995-02-02",
        "doj": "2021-06-01",
        "pass": "emp456",
        "utype": "Employee",
        "address": "California",
        "salary": "40000"
    }
])

# === Create & populate supplier collection ===
db["supplier"].insert_many([
    {
        "invoice": "INV1001",
        "name": "ABC Traders",
        "contact": "9998887770",
        "desc": "Supplier of electronic parts"
    },
    {
        "invoice": "INV1002",
        "name": "XYZ Supplies",
        "contact": "8887776665",
        "desc": "Supplier of packaging items"
    }
])

# === Create & populate category collection ===
db["category"].insert_many([
    {"name": "Electronics"},
    {"name": "Stationery"},
    {"name": "Grocery"}
])

# === Create & populate product collection ===
db["product"].insert_many([
    {
        "category": "Electronics",
        "supplier": "ABC Traders",
        "name": "Power Bank",
        "price": 1200.00,
        "qty": 50,
        "status": "Active"
    },
    {
        "category": "Stationery",
        "supplier": "XYZ Supplies",
        "name": "Notebook",
        "price": 50.00,
        "qty": 200,
        "status": "Active"
    },
    {
        "category": "Grocery",
        "supplier": "XYZ Supplies",
        "name": "Rice (1kg)",
        "price": 60.00,
        "qty": 100,
        "status": "Inactive"
    }
])

# === Create empty sales collection ===
db.create_collection("sales")

print("✅ MongoDB collections created and sample data inserted.")

db.create_collection("billing")
print("✅ MongoDB collections created and sample data inserted.")

