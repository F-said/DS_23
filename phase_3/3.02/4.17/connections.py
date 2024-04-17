import psycopg2

# NOTE: usually we want to keep this a secret. NEVER push this info to GitHub.
# Think... how can you "ignore" files in GitHub?
params = {
    "host": "first-aws-database.c1kgg6422jcl.us-east-1.rds.amazonaws.com",
    "dbname": "postgres",
    "user": "postgres",
    "password": "ds_2024_aws",
    "port": "5432"
}

# connect to your database using the dictionary above
# the ** operator unpacks all your settings into their appropriate params
# without the ** operator, we would have to manually set these params via
# psycopg2.connect(host="localhost", dbname="flights", user="postgres", password="password", port="...")
conn = psycopg2.connect(**params)

# create a cursor
# think of a cursor like an object that stores and executes queries
# we prepare it by calling conn.cursor() in Python
# for our purpose, a cursor is an object that allows us to execute queries 
# learn more about cursors here: https://www.geeksforgeeks.org/what-is-cursor-in-sql/
cursor = conn.cursor()

# lastly execute a SQL query on your cursor and view your results!
cursor.execute("SELECT * FROM covid_case LIMIT 10")
rows = cursor.fetchall()

# Amazing, no?
print(rows)

# Close out cursor (very important!)
cursor.close()

# CHALLENGE: How do we print out the first row of data from "rows"?
...
