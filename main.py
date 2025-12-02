from inmemory_db import InMemoryDB
db = InMemoryDB()
print(db.get("A"))
try:
    db.put("A", 5)
except Exception as e:
    print("Error:",e)
db.begin_transaction()
db.put("A", 5)
print(db.get("A"))

db.put("A", 6)
db.commit()

print(db.get("A"))
try:
    db.commit()
except Exception as e:
    print("Error:", e)

db.begin_transaction()
db.put("B", 10)
db.rollback()

print(db.get("B"))
