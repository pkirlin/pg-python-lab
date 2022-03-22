import psycopg2

conn = psycopg2.connect(host="database.rhodescs.org", user="", password="", dbname="practice")
cur = conn.cursor()

def dump_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print("Here are the users:")
    for row in rows:
        print("Userid:", row[0], "Name:", row[1], row[2])

def add_user(firstname, lastname):
    cur.execute("INSERT INTO users (firstname, lastname) VALUES (%s, %s)", [firstname, lastname])
    conn.commit()  # mandatory to actually write the data to the db

def add_users_from_csv(filename):
    with open(filename, 'r') as file:
        next(file) # Skip the header row.
        cur.copy_from(file, 'users', sep=',')
    conn.commit()

def delete_all_users():
    cur.execute("DELETE FROM users") # careful! deletes everything.
    conn.commit()
    
def main():
    dump_users()


main()
