#!/usr/bin/python3
"""Votes 1024 times for my id in a specified url making a request with headers
"""
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level2.php"
windows_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/74.0.3729.169 Safari/537.36"

for i in range(1024):
    session = requests.Session()
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    key = soup.find_all("input")[2]["value"]

    headers = {'user-agent': windows_user, 'referer': url}
    data = {'id': '3673', 'holdthedoor': 'submit', 'key': key}
    # Fakes a browser visit using the user-agent header
    session.post(url, data=data, headers=headers)

    print("Vote:", i + 1)
