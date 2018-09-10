#xmlTest.py

import xml.dom.minidom

filename = "xmlTest.xml"
###1.DOM(Document Object Model)

dom = xml.dom.minidom.parse(filename)
root = dom.documentElement

emplist = root.getElementsByTagName("emp")
num = 1
for node in emplist:
    print node.getAttribute("type1"), node.getAttribute("type2")

    print 
    num = num + 1
