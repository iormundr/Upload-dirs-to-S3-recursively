#!/usr/bin/env python

import boto3
import sys
import os

def fetch_buckets_from_s3():
        bucket_list = []
        for bucket in s3.buckets.all():
                bucket_list.append(bucket.name)
                print(bucket.name)
        return bucket_list


def upload_recursively_to_s3(my_bucket,PATH):
        bucket_to_upload = s3.Bucket(my_bucket)
        for root,dirs,files in os.walk(PATH):
                for file in files:
                        full_path = os.path.join(root,file)
                        with open(full_path, 'rb') as data:
                                bucket_to_upload.put_object(Key=PATH + "/" + full_path[len(PATH)+1:], Body=data)
                                print("Uploading  ", os.path.join(root,file))

def verify_file_exist_for_upload(PATH):
        for i in range(len(PATH)):
                if not os.path.exists(PATH[i]):
                        print("File or directiry does not exist in the specified")
                        exit()

if __name__ == "__main__":
        s3 = boto3.resource('s3')
        if len(sys.argv) < 2:
                print("Need input file/dir to upload")
                exit()
        elif len(sys.argv) >= 2:
                PATH = sys.argv[1:]
                verify_file_exist_for_upload(PATH)
        print("")
        bucket_list = fetch_buckets_from_s3()
        print("")
        my_bucket = raw_input("Please select bucket name to upload to: ")
        print("")
        if my_bucket not in bucket_list:
                print("Bucket name was not entered correctly")
                exit()
        for i in range(len(PATH)):
                upload_recursively_to_s3(my_bucket,PATH[i])
