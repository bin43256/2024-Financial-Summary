import os
import pandas as pd
from extract_transform import extractAndTransformData 
import psycopg2

print('script started')
# environment variables
DB_NAME = 'postgres_db'
DB_USER = 'Bin'
DB_PASSWORD = 'secret'
DB_HOST = "postgres"
DB_PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
    )
print("Connected to the database!")

def load_to_db(cleaned_csv, target_table):
    print("Loading data into the target_table:" + target_table)
    cur = conn.cursor()
    with open(cleaned_csv, 'r') as f:
        next(f) 
        cur.copy_from(f, target_table, sep=',', null='')
        conn.commit()
        cur.close()
    return print('sucessfully load into table: ' + target_table)


file_path = '/app/data/'
if os.path.isdir(file_path):
    print(f"{file_path} exists and is a directory.")
    print(os.listdir(file_path))
    extractAndTransformData(file_path)
else:
    print(f"{file_path} does not exist or is not a directory.")

load_to_db('./data/bank.csv','bank')
load_to_db('./data/dates.csv','dates')
load_to_db('./data/payment_method.csv','payment_method')
load_to_db('./processed_data/transactions.csv','transactions')

conn.close()
