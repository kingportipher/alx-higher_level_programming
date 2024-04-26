#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

def list_states(username, password, database):
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    
    # Query to retrieve states from the database
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    
    # Display results
    for row in query_rows:
        print(row)
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        exit(1)
    
    username = argv[1]
    password = argv[2]
    database = argv[3]

    list_states(username, password, database)
