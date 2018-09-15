#xmlTest.py

import xml.dom.minidom
import os
import re
import sys

filename = "IOSConfig.xml"

dom = xml.dom.minidom.parse(filename)

texturepacker = dom.documentElement

cmdPath = texturepacker.getAttribute("cmdPath")
pack = texturepacker.getElementsByTagName("pack")
print ('@@@@pack.name:%s' % pack[0].getAttribute("name"))
print ('@@@@pack.type:%s' % pack[0].getAttribute("type"))
print ('@@@@pack.type2:%s' % pack[0].getAttribute("type2"))
print ('@@@@pack.alphaRate:%s' % pack[0].getAttribute("alphaRate"))
print ('@@@@pack.rgbRate:%s' % pack[0].getAttribute("rgbRate"))

itemlist = pack[0].getElementsByTagName("item")
num = 1
for node in itemlist:
    print ('@@@@name:%s' % node.getAttribute("name"))
    print ('@@@@type:%s' % node.getAttribute("type"))
    print ('@@@@type2:%s' % node.getAttribute("type2"))
    print ('@@@@alphaRate:%s' % node.getAttribute("alphaRate"))
    print ('@@@@rgbRate:%s' % node.getAttribute("rgbRate"))

if raw_input("\r\n Press Any Key To Quit"):
  pass

