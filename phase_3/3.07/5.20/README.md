# ETL 

Congratulations on making it to Sprint 2!

Now that we have data inside of our **S3 buckets**, let's create maintainable scripts that will allow us to transform our raw data into a restructured dataset that we can easily use for analytics.

As mentioned in the slides, we will give you the option of using:

* pandas (easy)
* pyspark (challenging)
* step functions (challenging)

As part of the capstone, we will be asking you to choose which technology stack you would like to use. As a group, please decide which tool you would prefer for your etl pipeline.

Please be sure to create your ETL in a **python** file as opposed to a jupyter notebook. Remember, jupyter is great for visualization and EDA, but not suited for code like this. 

**REMEMBER! Before coding, please activate your phase1 conda environment**. Docs & relevant template code listed in each respective file:

## Pandas

Within the file labeled `pandas_etl.py`, you will find a small script that downloads and manipulates data from an s3 bucket using the `get_object` method:

```python
# create s3 client
s3 = boto3.client('s3')

# specify the bucket & folder you'd like to interact with
# will be using the cyber data as an example
name = 'western-shield'
folder = 'batch/'

# view all objects within this folder
response = s3.list_objects_v2(Bucket=name, Prefix=folder)
```

After completing our brief manipulation, we then push the data back into our bucket using the `put_object` method

```python
buffer = StringIO()

single_df.to_csv(buffer, index=False)

s3.put_object(
    Bucket='ds24aws',
    Key='transformed_file.csv',
    Body=buffer.getvalue()
)
```

Feel free to use this script as a starter for your own ETL code as well. Notice that after the initial data load, this is just pandas code which you all have been working with for the past few months:

```python
hpot_data = pd.concat(concat_list)
```

## PySpark

To learn about and use PySpark, read up on the following guides:

* [Getting Started with PySpark](https://www.datacamp.com/tutorial/pyspark-tutorial-getting-started-with-pyspark)
* [Using PySpark with AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html)

## Step Functions

Lastly, we also have the option of using step functions to transform our S3 dataset:

* [Getting started with AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html)

