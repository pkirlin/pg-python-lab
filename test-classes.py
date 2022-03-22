import psycopg2

conn = psycopg2.connect(host="database.rhodescs.org", user="", password="", dbname="practice")
cur = conn.cursor()
