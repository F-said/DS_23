import boto3
import pandas as pd
from io import StringIO


# create s3 client
s3 = boto3.client('s3')

# specify the bucket & folder you'd like to interact with
# will be using the cyber data as an example
name = 'western-shield'
folder = 'batch/'

# view all objects within this folder
response = s3.list_objects_v2(Bucket=name, Prefix=folder)

print("\n Multiple object retrieval \n")
####
# NOTE: The below code is for when you have multiple objects

# Example code: concatenate all files together
concat_list = []

# Interacting with multiple objects
# loop through all objects, handle them as a dataframe
for file in response['Contents']:
    fname = file['Key']

    # if this is a csv file...
    if fname.endswith('.csv'):
        # get csv object
        object = s3.get_object(Bucket=name, Key=fname)

        # transform into dataframe
        df = pd.read_csv(object['Body'])

        # print out first 5 rows of each object
        # print(df.head())
        concat_list.append(df)

# concatenate all files together
hpot_data = pd.concat(concat_list)

# verify columns
print(hpot_data.columns)
# verify shape
print(hpot_data.shape)
####

print("\n Single object retrieval \n")
####
# NOTE: Alternatively, we can also load one object at a time
name = "tkh-nyc-energy"
file = "energy_clean.csv"
single_object = s3.get_object(Bucket=name, Key=file)
single_df = pd.read_csv(single_object['Body'])
print(single_df.head())
####

# Lastly, after we are done performing our transformations, we load this data back into our bucket

# create an empty buffer to prepare our data push
buffer = StringIO()

# load our dataframe into this placeholder
single_df.to_csv(buffer, index=False)

# push this buffer to our s3 data store
s3.put_object(
    Bucket='ds24aws',
    Key='transformed_file.csv',
    Body=buffer.getvalue()
)
