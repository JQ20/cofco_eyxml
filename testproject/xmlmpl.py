# 导入第三方库
import xml.etree.ElementTree as ET


file_xml = r'xmlt1.xml'

tree = ET.parse(file_xml)  # 类ElementTree
root = tree.getroot()  # 类Element
# print(root)  # 这时得到的root是一个指向Element的对象
# print(root.attrib)

# for neighbor in root.iter('voucher'):
# 	print(neighbor.attrib)

# year = root.find('voucher').find('voucher_head').find('year').text

# print(year)

details = root.find('voucher').find('voucher_head').find('details')

items = details.findall('item')
test = root.find('12321')
print(test)
for item in items:
    explanation = item.find('explanation').text
    # print(explanation)

# print(ET.tostring(item))


# print(ET.tostring(root))
# tree = ET.parse('test.xml')
# root = tree.getroot()

# a = root.find('a')
# b = ET.SubElement(a, 'b')
# c = ET.SubElement(b, 'c')
# c.text = 'text3'

# print ET.tostring(root)