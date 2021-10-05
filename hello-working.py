#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys
import requests
import json

from requests.sessions import session
import boto3
from  botocore.exceptions import ClientError

print('Hello, World.')
def get_region_name():
    identity_doc = requests.get("http://169.254.169.254/latest/dynamic/instance-idenitity/document").json()
    return identity_doc['region']

client = boto3.client('ec2')
response = client
region_name = get_region_name()
print('region is ' | region_name)
