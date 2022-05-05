#!/usr/bin/python3
"""Votes 4096 times for my id in a specified url
"""
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level1.php"

for i in range(4096):
    session = requests.Session()
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    key = soup.find_all("input")[2]["value"]

    data = {'id': '3673', 'holdthedoor': 'submit', 'key': key}
    session.post(url, data)

    print("Vote:", i + 1)
