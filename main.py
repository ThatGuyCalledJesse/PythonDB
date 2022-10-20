from database import *

db = DB()
print("LOADED DATABASE")
db.load('database.txt')
db.print()