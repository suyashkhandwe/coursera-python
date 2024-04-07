"""Module for demo of XMLs and XML schema"""

# Schema languages for XMLS
# - DFD - Document Type Definition
# - SGML - Standard Generalized Markup Language (ISO 8879:1986)
# - XML Schema - XSD (W3C Schema)
# -- xs:schema
# -- xs:element
# -- xs:attribute
# -- xs:restrictions
# --- constraints: type, minOccurs, maxOccurs
# -- xs:sequence
# -- xs:complexType

import xml.etree.cElementTree as ET
person = '''
<person>
    <name>My Name</name>
    <phone type="intl">+1 000 000 0000</phone>
    <email hide="yes"/>
</person>
'''
personTree = ET.fromstring(person)
print('Name:', personTree.find('name').text)
print('Attr:', personTree.find('email').get('hide'))

persons = '''
<people>
    <persons>
        <person id="1">
            <name>My Name 1</name>
            <phone type="intl">+1 000 000 0000</phone>
            <email hide="yes"/>
        </person>
        <person id="2">
            <name>My Name 2</name>
            <phone type="intl">+1 111 111 1111</phone>
            <email hide="yes"/>
        </person>
    </persons>
</people>
'''
personsTree = ET.fromstring(persons)
allPersons = personsTree.findall('persons/person')
print('Person Count:', len(allPersons))
for p in allPersons:
    print('Name:', personTree.find('name').text)
    print('Attr:', personTree.find('email').get('hide'))
