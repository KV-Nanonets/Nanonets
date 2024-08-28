import xml.dom.minidom

# parse the XML file
xml_doc = xml.dom.minidom.parse('travel_pckgs.xml')

# get the root element
root = xml_doc.documentElement
print('Root is',root)

# get all the package elements
packages = xml_doc.getElementsByTagName('package')

# loop through the packages and extract the data
for package in packages:
  package_id = package.getAttribute('id')
  
  description =   package.getElementsByTagName('description')[0].childNodes[0].data
  
  price = package.getElementsByTagName('price')[0].childNodes[0].data
  
  duration = package.getElementsByTagName('duration')[0].childNodes[0].data
  
  print('Package ID:', package_id)
  print('Description:', description)
  print('Price:', price)
  

# get the first package element
paris_package = xml_doc.getElementsByTagName('package')[0]

# get the first child of the package element
first_child = paris_package.firstChild

print(first_child)

child_elements=paris_package.childNodes
print(child_elements)