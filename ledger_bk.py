import sqlite3

def create():
    con = sqlite3.connect("minedatabase.db")  # Changed the database name to minedatabase.db
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY,name TEXT,user TEXT, password TEXT,category TEXT,cdate TEXT)")
    con.commit()
    con.close()

def viewall():
    con = sqlite3.connect("minedatabase.db")  # Changed the database name to minedatabase.db
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows

def search(search_value="", search_type=""):
    con = sqlite3.connect("minedatabase.db")
    cur = con.cursor()
    
    # Create the base query
    query = "SELECT * FROM account WHERE 1=1"  # Start with a true condition
    params = []

    # Adjust the query based on the search type
    if search_type == "name":
        query += " AND name=?"
        params.append(search_value)
    elif search_type == "user":
        query += " AND user=?"
        params.append(search_value)
    elif search_type == "password":
        query += " AND password=?"
        params.append(search_value)
    elif search_type == "category":
        query += " AND category=?"
        params.append(search_value)

    cur.execute(query, params)
    rows = cur.fetchall()
    con.close()
    return rows

def add(name, user, password, category, cdate):
    con = sqlite3.connect("minedatabase.db")  # Changed the database name to minedatabase.db
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL,?,?,?,?,?)", (name, user, password, category, cdate))
    con.commit()
    con.close()

def update(id, name, user, password, category, cdate):
    con = sqlite3.connect("minedatabase.db")  # Changed the database name to minedatabase.db
    cur = con.cursor()
    cur.execute("UPDATE account SET name=?, user=?, password=?, category=?, cdate=? WHERE id=?", (name, user, password, category, cdate, id))
    con.commit()
    con.close()

def delete(id):
    con = sqlite3.connect("minedatabase.db")  # Changed the database name to minedatabase.db
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?", (id,))
    con.commit()
    con.close()

create()  # This will create the minedatabase.db and the account table
