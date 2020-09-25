import csv
import psycopg2
conn = psycopg2.connect("host=ec2-52-213-173-172.eu-west-1.compute.amazonaws.com dbname=d4piu8k00a3slu user=ijppypsnabbvel")
cur = conn.cursor()
with open('Products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO products VALUES (%s, %s)",
        row
    )
conn.commit()
with open('Reviews.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO products VALUES (%s, %s, %s)",
        row
    )
conn.commit()