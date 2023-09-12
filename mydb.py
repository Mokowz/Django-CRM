import mysql.connector


dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mokowz27@mysql",
)

# Preparing a cursor object
cursorObject = dataBase.cursor()

# Creating database
cursorObject.execute("CREATE DATABASE rekodi")

print("All Done")