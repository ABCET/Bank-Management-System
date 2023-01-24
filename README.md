# Bank-Management-System
This script is for a simple bank account management system that connects to a MySQL database using the mysql-connector-python library. It allows users to create new bank accounts, as well as perform transactions (withdrawals and deposits) on existing accounts.

To use this script, you will need to have a MySQL server set up, and a database named "bank" with two tables: "customer" and "transaction". The "customer" table should have the following columns: "AccountNO", "Name", "PhoneNo", "EmailID", "Address", "AadharNO". The "transaction" table should have the following columns: "AccountNo", "Name", "date", "Deposit", "Withdraw", "currentbalance". You will also need to have the mysql-connector-python library installed.

The script defines several functions:

create(): This function creates a new bank account by inserting a new row into the "customer" table with the user's inputted name, phone number, email, address, and Aadhaar number. It also creates a new row in the "transaction" table with the user's account number, name, the current date, and an initial balance of 0.

trans(): This function allows the user to perform a transaction (withdraw or deposit) on their bank account. It first checks if the account number entered by the user is valid by checking if it exists in the "customer" table. If the account number is valid, it prompts the user to choose between withdraw and deposit, and then performs the corresponding transaction by updating the "transaction" table.

pr(listinp): This function writes the input list to a csv file.

datime(): This function writes the current date and time to a csv file

It also uses two global variables:

logdoc: a name of a csv file
mycon: a connection object to the bank database.
In order to use the script, you will need to replace the following line:

mycon = sql.connect(host='localhost', user='root', passwd='', database='bank')
with your database connection details.

Before running the script, make sure to set up the database and tables as described above.

Once you have set up the database and replaced the connection details, you can run the script and use the create() function to create new bank accounts, and the trans() function to perform transactions on existing accounts.

SOFTWARE REQUIREMENTS

1. OS
2. Python
3. MySQL
4. Python MySQL connector


