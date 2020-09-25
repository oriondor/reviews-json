import pandas as pd
prod = pd.read_csv('Products.csv')
rev = pd.read_csv('Reviews.csv')
prod.columns = [c.lower() for c in prod.columns] #postgres doesn't like capitals or spaces
rev.columns = [c.lower() for c in rev.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgres://ijppypsnabbvel:f472d00f7d1625c31cc6e29ca95a7d3a212257634da1604134a6feeca896a456@ec2-52-213-173-172.eu-west-1.compute.amazonaws.com:5432/d4piu8k00a3slu')

prod.to_sql("products", engine)
rev.to_sql("reviews", engine)