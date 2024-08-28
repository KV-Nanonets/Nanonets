from lxml import etree

# Parse the XML file
tree = etree.parse('travel_pckgs.xml')

# Calling the root element
root = tree.getroot()
print("Root is", root)

for x in root[0]:
    print(x.tag, x.attrib)
    
descriptions = root.xpath('//description')
for desc in descriptions:
    print(desc.text)
    
#iterating through Child elements    
for tour in root:
    print(tour.attrib)