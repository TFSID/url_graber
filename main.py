import os
import xml.etree.ElementTree as ET
import re
import icecream as ic

tree = ET.parse('sample.xml')
root = tree.getroot()

with open('sample.xml','r') as file:
    xml_data = file.read()
    url_pattern = r'xmlUrl=\"(https?:\/\/(w?w?w?\.)?([a-zA-Z]\S*\.)?([a-zA-Z]*\.)?(com)?([a-zA-Z]\.)?([a-z].[a-z]?)(\/\S*))\"'
    data_url = re.findall(url_pattern,xml_data)
    result = []
    for match in data_url:
        try:
            result.append(data_url)
        except:
            continue
    with open('parsed.txt','w') as file:
        for r1 in result:
            for r in r1:
                file.write(f'{r[0]}\n')
            