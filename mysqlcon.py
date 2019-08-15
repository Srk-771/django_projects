import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="srk@khan007",  # your password
                     db="test")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
mycursor = db.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
