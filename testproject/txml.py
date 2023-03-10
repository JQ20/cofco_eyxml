import xml.etree.ElementTree as ET

tree = ET.parse('txml.xml')
root = tree.getroot()

a = root.find('country')
b = ET.SubElement(a, 'b')
b.text = 'text3'

print(ET.tostring(a))

tree=ET.ElementTree(root) 
tree.write("result.xml")