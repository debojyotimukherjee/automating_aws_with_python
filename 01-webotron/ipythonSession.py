# coding: utf-8
import boto3
session = boto3.Session(profile_name = 'pythonAuto')
s3 = session.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket)
#
# for bucket in s3.buckets.all():
#     print(bucket)
#
# for bucket in s3.buckets.all():
#     print(bucket)
#
# newBucket = s3.create_bucket(Bucket = 'aws-python-dmukherjee-boto3')
# for bucket in s3.buckets.all():
#     print(bucket)
#
# newBucket = s3.create_bucket(Bucket = 'aws-python-dmukherjee-boto3-us-east-2',CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
# for bucket in s3.buckets.all():
#     print(bucket)
#
# bucketPolicy = s3.get_bucket_policy(Bucket = 'ws-python-dmukherjee')
# bucketPolicy = s3.get_bucket_policy(Bucket='bucket_name')
# bucketPolicy = s3.BucketPolicy('bucket_name')
# bucketPolicy = s3.BucketPolicy('aws-python-dmukherjee')
# bucketPolicy
