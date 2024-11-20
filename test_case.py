import sqlite3

# Function to create and set up a simple database
def setup_database():
    conn = sqlite3.connect(':memory:')  # In-memory database for testing
    cursor = conn.cursor()
    
    # Create a table and insert some test data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS indexed_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
    
    # Insert some test data
    cursor.execute("INSERT INTO indexed_data (name) VALUES ('Apple')")
    cursor.execute("INSERT INTO indexed_data (name) VALUES ('Banana')")
    cursor.execute("INSERT INTO indexed_data (name) VALUES ('Orange')")
    conn.commit()
    
    return conn

# Function to search the database by name
def search_data(conn, keyword):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM indexed_data WHERE name LIKE ?', ('%' + keyword + '%',))
    return cursor.fetchall()

# Test Case with if-else structure to verify search functionality
def test_search_functionality():
    conn = setup_database()
    
    # Search for a known item
    search_result = search_data(conn, "Apple")
    
    # Check if search results are returned
    if len(search_result) > 0:
        print(f"Test Passed: Found {len(search_result)} result(s) for 'Apple'.")
        print("Details:", search_result)
    else:
        print("Test Failed: No results found for 'Apple'.")
    
    # Search for an item that doesn't exist
    search_result = search_data(conn, "Pineapple")
    
    # Check if no results are returned
    if len(search_result) == 0:
        print("Test Passed: No results found for 'Pineapple'.")
    else:
        print(f"Test Failed: Found unexpected results for 'Pineapple'.")
    
    # Close the connection
    conn.close()

test_search_functionality()
