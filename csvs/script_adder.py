import csv
import psycopg2
conn = psycopg2.connect("host=ec2-52-213-173-172.eu-west-1.compute.amazonaws.com dbname=d4piu8k00a3slu user=ijppypsnabbvel password=f472d00f7d1625c31cc6e29ca95a7d3a212257634da1604134a6feeca896a456")
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