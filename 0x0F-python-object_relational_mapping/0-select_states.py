import MySQLdb

def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the database connection
    db.close()

# Provide the MySQL username, password, and database name as arguments
username = "Festus1914"
password = "Myschool1914!"
database = "hbtn_0e_0_usa"

# Call the function to list states
list_states(username, password, database)
