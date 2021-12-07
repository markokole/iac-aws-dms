import mysql.connector
from datetime import datetime

user = "foo"
password = "foobarbaz"
host = ""
port = "3306"
database = "mydb"

transactions = (
    "CREATE TABLE `transactions` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tdate` date NOT NULL,"
    "  `customer` varchar(14) NOT NULL,"
    "  `amount` decimal(12,2) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user=user, password=password, host=host)
cursor = cnx.cursor(buffered=True)

# cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))

cursor.execute("USE {}".format(database))

cursor.execute(transactions)


timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
insert = "INSERT INTO {} (tdate, customer, amount) VALUES (NOW(), 'Marko', 12345678.90)".format("transactions")
cursor.execute(insert)


cursor.execute("SELECT * FROM {}".format("transactions"))
rows = cursor.fetchall()

cursor.close()
cnx.close()