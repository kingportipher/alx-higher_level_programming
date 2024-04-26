#!/usr/bin/python3

import MySQLdb
"""Lists states"""

def list_states(username, password, db_name):
    """Lists all states from the database hbtn_0e_0_usa.

    Args:
        username: MySQL username.
        password: MySQL password.
        db_name: Database name.
    """

    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(host="localhost",
                                     user=username,
                                     passwd=password,
                                     db=db_name)

        cursor = connection.cursor()

        # Get all states sorted by id
        sql = "SELECT * FROM states ORDER BY states.id ASC;"
        cursor.execute(sql)

        # Fetch results and print them
        for row in cursor:
            print(row[0])  # Print state name (assuming it's the first column)

    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")

    finally:
        # Close connection
        if connection:
            connection.close()


if __name__ == "__main__":
    # Script execution is disabled when imported
    pass
