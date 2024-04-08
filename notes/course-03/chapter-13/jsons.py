"""Module for demo of JSONs and schema"""

import json
data = '''
{
    "name": "My name - 1",
    "phone": {
        "type": "intl",
        "number": "+1 111 111 1111"
    },
    "email": {
        "hide": "yes"
    }
}
'''
# JSON is a nested dictionary of dictionaries in python

jsonData = json.loads(data)
print('Name:', jsonData["name"])
print('Email Status:', jsonData["email"]["hide"])

dataWithCollection = '''
[
    {
        "name": "My name - 1",
        "phone": {
            "type": "intl",
            "number": "+1 111 111 1111"
        },
        "email": {
            "hide": "yes"
        }
    },
    {
        "name": "My name - 2",
        "phone": {
            "type": "intl",
            "number": "+1 222 222 2222"
        },
        "email": {
            "hide": "yes"
        }
    }
]
'''
# Read about e-framework

jsonDataOfCollection = json.loads(dataWithCollection)
print('Count:', len(jsonDataOfCollection))
for it in jsonDataOfCollection:
    print('Name:', it["name"])
    print('Email Status:', it["email"]["hide"])

quizData = '''[ "Glenn", "Sally", "Jen" ]'''
quizJson = json.loads(quizData)
print(len(quizJson))
print(quizJson)