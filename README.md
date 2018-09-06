# Upload-dirs-to-S3-recursively
Upload the entire directory to AWS S3 to one of your buckets

* Now the script can upload multiple inputs (dirs and files)

The script is uploading one or more dirs to S3.

    [alex@server1 ~]$ mkdir test_to_upload
    [alex@server1 ~] cd test_to_upload
    [alex@server1 test_to_upload] touch file_upload{1..10}.py
    [alex@server1 test_to_upload] ls -1
    file_upload10.py
    file_upload1.py
    file_upload2.py
    file_upload3.py
    file_upload4.py
    file_upload5.py
    file_upload6.py
    file_upload7.py
    file_upload8.py
    file_upload9.py
    [alex@server1 test_to_upload] cd ..
    [alex@server1 ~] upload_to_s3.py test_to_upload
    
    test-2018
    test-my-server1
    test-my-server2

    Please select bucket name to upload to: test-my-server2
    ('Uploading  ', 'test_to_upload/file_upload1.py')
    ('Uploading  ', 'test_to_upload/file_upload2.py')
    ('Uploading  ', 'test_to_upload/file_upload3.py')
    ('Uploading  ', 'test_to_upload/file_upload4.py')
    ('Uploading  ', 'test_to_upload/file_upload5.py')
    ('Uploading  ', 'test_to_upload/file_upload6.py')
    ('Uploading  ', 'test_to_upload/file_upload7.py')
    ('Uploading  ', 'test_to_upload/file_upload8.py')
    ('Uploading  ', 'test_to_upload/file_upload9.py')
    ('Uploading  ', 'test_to_upload/file_upload10.py')
    
    
    
  
