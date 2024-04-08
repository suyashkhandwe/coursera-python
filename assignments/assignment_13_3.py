"""Module for assignment 13.3"""

# Calling a JSON API

# In this assignment you will write a Python program somewhat similar 
# to http://www.py4e.com/code3/opengeo.py. The program will 
# prompt for a location, 
# contact a web service 
# and retrieve JSON for the web service 
# and parse that data, 
# and retrieve the first plus_code from the JSON. 
# 
# An Open Location Code is a textual identifier that is another 
# form of address based on the location of the address.
# 
# API End Points
# To complete this assignment, you should use this API endpoint 
# that has a static subset of the Open Street Map Data.
# http://py4e-data.dr-chuck.net/opengeo?
# This API also has no rate limit so you can test as often as you like. 
# If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to provide the address that you are 
# requesting as the q= parameter that is properly URL encoded 
# using the urllib.parse.urlencode() 
# function as shown in http://www.py4e.com/code3/opengeo.py
#
# Test Data / Sample Execution
# You can test to see if your program is working with a location of 
# "South Federal University" which will have a plus_code of "6FV8QPRJ+VQ".
# $ python solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 1466 characters
# Plus code 6FV8QPRJ+VQ
# Turn In
#
# Please run your program to find the plus_code for this location:
# universidad complutense de madrid
# 
# Make sure to enter the name and case exactly as above and 
# enter the plus_code and your Python code below. 
# Hint: The first five characters of the plus_code are "8CGRC ..."
# 
# Make sure to retreive the data from the URL specified above 
# and not the normal Google API. 
# Your program should work with the Google API - 
# but the plus_code may not match for this assignment.

import urllib.request, urllib.parse, urllib.error
import json, ssl

# Ignore Cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

API_PATH = 'http://py4e-data.dr-chuck.net/opengeo?'

location = input('Enter location: ')
queryParameters = dict()
queryParameters['q'] = location
url = API_PATH + urllib.parse.urlencode(queryParameters)
print('Retrieving:', url)

response = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(response), 'characters')

try:
    payload = json.loads(response)
except:
    payload = None

if not payload or 'features' not in payload:
    print('Failed to download from url=', url)
    quit()

if len(payload['features']) < 1:
    print('Location not found:', location)
    quit()

if 'properties' not in payload['features'][0]:
    print('No properties found for location:', location)
    quit()

print('Plus code', payload['features'][0]['properties']['plus_code'])
