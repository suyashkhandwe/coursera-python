"""Module for demo of GEO Coding API"""

import urllib.request, urllib.parse, urllib.error
import http, json, ssl

params = dict()
params['q'] = 'Ann Arbor, MI'
url = 'https://py4e-data.dr-chuck.net/opengeo?' + urllib.parse.urlencode(params)

# Ignore Cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url).read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js or 'features' not in js:
    print('Download failed')
    quit()

if len(js['features']) == 0:
    print('Not found')
    quit()

lat = js['features'][0]['properties']['lat']
lon = js['features'][0]['properties']['lon']
print('lat:', lat, 'lon:', lon)