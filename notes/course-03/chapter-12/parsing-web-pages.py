"""Module for demo of Parsing Web Pages"""
# This uses beautifulsoup4-4.12.3
import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page2.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

print(re.findall('href="(.+)"', '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'))