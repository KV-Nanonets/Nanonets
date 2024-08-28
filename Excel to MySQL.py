import pandas as pd
import mysql.connector

df = pd.read_excel('employee_data.xlsx')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='yourdatabase'
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id VARCHAR(10),
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);
""")

# Insert DataFrame to MySQL
for i, row in df.iterrows():
    sql = "INSERT INTO employees (employee_id, name, department, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))

conn.commit()
cursor.close()
conn.close()