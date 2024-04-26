#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Query to retrieve states from the database
    query = "SELECT * FROM states ORDER BY id ASC"

    try:
        # Execute the query
        cursor.execute(query)
        # Fetch all the results
        results = cursor.fetchall()
        # Display results
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        sys.exit(1)
    finally:
        # Close the database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)

