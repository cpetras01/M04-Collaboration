#Supporting code for question 16.8 M04 Programming assingment

# Create a CSV file called books2.csv
def newCSV():
    import csv
    import os

    myCSV = [
        {'title': 'The Weirdstone of Brisingamen','author': 'Alan Garner','year': 1960},
        {'title': 'Perdido Street Station', 'author': 'China Mieville', 'year': 2000},
        {'title': 'Thud!', 'author': 'Terry Pratchett', 'year': 2005},
        {'title': 'The Spellman Files', 'author': 'Lisa Lutz', 'year': 2007},
        {'title': 'Small Gods', 'author': 'Terry Pratchett', 'year': 1992}
        ]

    # field names
    headers = ['title', 'author', 'year']

    # name of csv file
    directory = 'C:/Users/colem/Desktop/Coleman Programs/M04-Collaboration/'
    filename = os.path.join(directory, 'books2.csv')

    #writing to csv file
    with open(filename, 'w', newline='') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        # writing headers
        writer.writeheader()

        # writing data rows
        writer.writerows(myCSV)

# Create a new SQLite Database
def newSQL():
    import sqlite3
    import os

    directory = 'C:/Users/colem/Desktop/Coleman Programs/M04-Collaboration/'

    # Construct the full path to the SQLite database file
    db_file = os.path.join(directory, 'books.db')

    # Connect to sqlite
    connection = sqlite3.connect(db_file)

    # Creating a cursor object with cursor() method
    cursor = connection.cursor()

    # Creating table
    cursor.execute('''CREATE TABLE books
        (title TEXT,
        author TEXT,
        year INTEGER)'''
        );

    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

# Read the CSV into the database
def readCSVtoSQL():
    import sqlite3
    import csv
    import os

    # Connect to the SQLite database
    directory = 'C:/Users/colem/Desktop/Coleman Programs/M04-Collaboration/'

    # Construct the full path to the SQLite database file
    db_file = os.path.join(directory, 'books.db')

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    try:
        # Open the CSV file and read its contents
        with open('books2.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)

            # Extract headers and prepare for insertion
            headers = reader.fieldnames
            next(reader)  # Skip the header row

            # Prepare a list to store data rows
            data_rows = []
            for row in reader:
                data_rows.append((row['title'], row['author'], row['year']))

            # SQL query to insert data into the books table
            insert_records = "INSERT INTO books(title, author, year) VALUES(?,?,?)"

            # Import the contents of the file into the books table
            cursor.executemany(insert_records, data_rows)
    
        # Select all data from the books table to verify insertion 
        select_all = "SELECT * FROM books"
        cursor.execute(select_all)
        rows = cursor.fetchall()
    
        # Output to the console
        for r in rows:
            print(r)
    
        # Commit changes
        connection.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()
