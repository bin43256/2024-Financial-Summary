import psycopg2

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
extractAndTransformData(file_path)
cur = conn.cursor()
csv_file_path = './data/banks.csv'  
table_name = 'banks'

with open(csv_file_path, 'r') as f:
     next(f)
     cur.copy_from(f, table_name, sep=',', null='')
     conn.commit()
cur.close()
conn.close()
print("Data inserted successfully!")