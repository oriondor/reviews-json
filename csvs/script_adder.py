import csv
import psycopg2
import os

host = os.environ['host']
dbname = os.environ['dbname']
user = os.environ['user']
password = os.environ['password']
conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")
cur = conn.cursor()
with open('Products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO products (title,asin) VALUES (%s, %s)",
        row
    )
conn.commit()
with open('Reviews.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO reviews (asin,title,review) VALUES (%s, %s, %s)",
        row
    )
conn.commit()