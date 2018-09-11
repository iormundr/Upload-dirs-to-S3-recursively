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
                        try:
                                with open(full_path, 'rb') as data:
                                        bucket_to_upload.put_object(Key=PATH + "/" + full_path[len(PATH)+1:], Body=data)
                                        print("Uploading  ", os.path.join(root,file))
                        except IOError:
                                print("Did not upload, check permission on file: ",file)


def verify_file_exist_for_upload(PATH):
        bool_list = []
        for i in range(len(PATH)):
                if os.path.isdir(PATH[i]):
                        bool_list.append(False)
                        pass
                elif os.path.isfile(PATH[i]):
                        bool_list.append(True)
                else:
                        print
                        print("Specified input is neither file nor directory, check your input\n")
                        exit()
        return bool_list

def upload_single_files(my_bucket,PATH,isFile):
        print
        print("Printing standalone files\n")
        for bool_value in range(len(PATH)):
                if isFile[bool_value]:
                        s3.Bucket(my_bucket).put_object(Key=PATH[bool_value],Body=PATH[bool_value])
                        print("Uploading  ", PATH[bool_value])


if __name__ == "__main__":
        s3 = boto3.resource('s3')
        if len(sys.argv) < 2:
                print("Need input file/dir to upload")
                exit()
        elif len(sys.argv) >= 2:
                PATH = sys.argv[1:]
                return_code = verify_file_exist_for_upload(PATH)
        print
        bucket_list = fetch_buckets_from_s3()
        print
        my_bucket = raw_input("Please select bucket name to upload to: ")
        print
        if my_bucket not in bucket_list:
                print("Bucket name was not entered correctly")
                exit()
        for i in range(len(PATH)):
                upload_recursively_to_s3(my_bucket,PATH[i])
        upload_single_files(my_bucket,PATH,return_code)
