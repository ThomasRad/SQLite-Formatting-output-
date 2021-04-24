# Import package.
import sqlite3

# Connect to the database. 
conn = sqlite3.connect('customer.db')

# Create a cursor.
c = conn.cursor()

# Query the Database. 
c.execute("SELECT * FROM customers")

#Lets get all entries 
names = c.fetchall()


# Format the data to look good when printed. 
print("Name " + "\t\tEMAIL")
print("----------" + "\t\t-----------")
for name in names:
	print(name[0] + " " + name[1] + "\t" + name[2])

# Commit the command 
conn.commit()

# Now we close the connection. 
conn.close()

