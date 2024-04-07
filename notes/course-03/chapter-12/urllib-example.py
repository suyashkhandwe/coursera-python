"""Module for demo of urllib"""
import urllib.request, urllib.parse, urllib.error
handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in handle:
    print(line.decode().strip())
