#!/usr/bin/python3
"""Votes 1024 times for my id in the specified url
"""
import requests

url = "http://158.69.76.135/level0.php"
data = {'id': '3673', 'holdthedoor': 'submit'}

for i in range(1024):
    requests.post(url, data)
    print("Vote", i + 1)
