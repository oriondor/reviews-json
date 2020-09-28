import csv
import psycopg2
import os

password = os.environ['password']
conn = psycopg2.connect(f"host=ec2-52-213-173-172.eu-west-1.compute.amazonaws.com dbname=d4piu8k00a3slu user=ijppypsnabbvel password={password}")
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