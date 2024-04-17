import psycopg2

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

with conn.cursor() as cursor:
    # read in your sql commands (remember this from file I/O?)
    with open('commands.sql', 'r') as schema:
        # read --> reads in entire file
        queries = schema.read()
        # we are starting a transaction (or continuing)
        cursor.execute(queries)

        rows = cursor.fetchall()
        print(rows)

        # CHALLENGE: Can you express these rows as a pandas dataframe?
        ...
