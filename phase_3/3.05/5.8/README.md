# S3 Set-Up

This guide takes heavily from the following resources. If you would like a more guided experience, read through each numbered section. Otherwise, consult these articles/docs to figure out s3 programmatic connections:
* https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html
* https://felipeagq99.medium.com/connect-to-a-aws-s3-bucket-with-boto3-of-python-6f22441c5390
* https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey

## 1 PIP Installations

First, we need to ensure that we've installed all necessary packages and cli configuration tools. After activating your conda environment in your terminal install the `awscli` and `boto3` packages.

```
conda activate phase1
pip install awscli
pip install boto3
```

We will use these packages to programmatically interact with our AWS resources. 

## 2 AWS Configure

Next, we should create an access key from our individual IAM accounts. Consult [this page](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_add-key.html#:~:text=Use%20your%20AWS%20account's%20email,section%2C%20choose%20Create%20access%20key.) to figure out how to create your ID and key. Write this information down in some secure location, as you will not be able to view it again!

After generating this key-pair, execute the command below in your conda environment:

```
aws configure
```

And input all pertinent information. It will ask you for your key id, key, region, and output format. For your id and key you will use the information that you've written down. For your region, you will use the region that your bucket is in, and for your output format you will use `text`.

## 3 boto3

Now that you have all of this set up, you should be able to interact with your s3 bucket programmatically! Read and run the files listed in this folder to figure out which commands you can use! 

Run to view buckets:
```
python view_buckets.py
```

Run to push, view, and delete from buckets:
```
python push_view_delete.py
```

Run to read from buckets and save onto your local machine:
```
python read_buckets.py
```

Feel free to re-use this code in your own s3 bucket integration. Remember, you should only be creating jupyter notebooks for your `EDA` and machine learning. Database interactions such as this should go in `.py` files.