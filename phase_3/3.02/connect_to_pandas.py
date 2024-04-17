import psycopg2
import pandas as pd

params = {
    "host": "first-aws-database.c1kgg6422jcl.us-east-1.rds.amazonaws.com",
    "dbname": "postgres",
    "user": "postgres",
    "password": "ds_2024_aws",
    "port": "5432"
}

# connect to your database using the dictionary above
conn = psycopg2.connect(**params)

# create a cursor
cursor = conn.cursor()

# lastly execute a SQL query on your cursor and view your results!
cursor.execute("SELECT * FROM covid_case")
rows = cursor.fetchall()

# Close out cursor (very important!)
cursor.close()

# NOTE: notice that your data is currently a list of tuples, while this isn't
# bad, we preferably would like to transform our data into a common object
# that we are used to interacting with...
# For example, a dataframe!
df = pd.DataFrame(rows, columns=["date", "rolling_average", "region", "state", "name", "fipscode"])
print(df.head())

# CHALLENGE: How do we save this dataframe as a csv file???
...
