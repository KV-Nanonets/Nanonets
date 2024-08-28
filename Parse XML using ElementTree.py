import xml.etree.ElementTree as ET
tree = ET.parse('travel_pckgs.xml')

#calling the root element
root = tree.getroot()
print("Root is",root)

for x in root[0]:
  print(x.tag, x.attrib)
  
for x in root.iter('description'):
  print(x.text)

#Loop through XML  
for tour in root:
  print(tour.attrib)
  
#Findall  
for package in root.findall('package'):
  price = int(package.find('price').text)
  refund = package.find('payment/refund').text.strip("'")
  if price < 4000 and refund == 'yes':
      print(package.attrib['id'])
  
#Modify XML  
for price in root.iter('price'):
    new_price = int(price.text)*2
    price.text = str(new_price)
    price.set('updated', 'yes')
    tree.write('christmas_packages.xml')