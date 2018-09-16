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
print ('@@@@pack.type:%s' % pack[0].getAttribute("type"))
print ('@@@@pack.type2:%s' % pack[0].getAttribute("type2"))
print ('@@@@pack.alphaRate:%s' % pack[0].getAttribute("alphaRate"))
print ('@@@@pack.rgbRate:%s' % pack[0].getAttribute("rgbRate"))

commtype = pack[0].getAttribute("type")
commtype2 = pack[0].getAttribute("type2")

itemlist = pack[0].getElementsByTagName("item")
num = 1
for node in itemlist:
    print ('@@@@name:%s' % node.getAttribute("name"))
    print ('@@@@type:%s' % node.getAttribute("type"))
    print ('@@@@type2:%s' % node.getAttribute("type2"))
    print ('@@@@alphaRate:%s' % node.getAttribute("alphaRate"))
    print ('@@@@rgbRate:%s' % node.getAttribute("rgbRate"))

print ('====================================================')
root_dir = pack[0].getAttribute("src")
out_dir = pack[0].getAttribute("dest")
comend = cmdPath
tga2pkm = 'F:\\JpegCompress.exe'

layer1_dir_list = os.listdir(root_dir)
for i in range(len(layer1_dir_list)):
	layer1_dir = root_dir + os.sep + layer1_dir_list[i]
	if os.path.isdir(layer1_dir):
		print ('===========layer1_dir:%s' % layer1_dir)
		layer2_dir_list = os.listdir(layer1_dir)
		for j in range(len(layer2_dir_list)):
			layer2_dir = layer1_dir + os.sep + layer2_dir_list[j]
			if os.path.isdir(layer2_dir):
				print ('=====layer2_dir:%s' % layer2_dir)
				cmdtmp = comend
				allImage = ""

				localtype = commtype
				localtype2 = commtype2
				for node in itemlist:
					plistname = node.getAttribute("name")
					if plistname == layer2_dir_list[j] :
						type1 = node.getAttribute("type")
						type2 = node.getAttribute("type2")
						localtype = type1
						localtype2 = type2
				    	print ('@@@@special plistname:%s' % plistname)
				    	print ('@@@@special type:%s' % localtype)
				    	print ('@@@@special type2:%s' % localtype2)

				for fileName in os.listdir(layer2_dir):
				    if re.match('[^.]+.png', fileName) is None:
				      continue
				    allImage = allImage + " " + layer2_dir + os.sep + fileName
				cmdtmp = cmdtmp + " " + allImage +\
		          " --format cocos2d" +\
		          " --data " + out_dir + os.sep + layer1_dir_list[i] + os.sep + layer2_dir_list[j] + ".plist"\
		          " --sheet " + out_dir + os.sep + layer1_dir_list[i] + os.sep + layer2_dir_list[j] + ".pvr"\
		          " --texture-format" + " " + localtype + " " \
		          " --opt " + " " + localtype2 + " " \
		          " --allow-free-size"
		        print("cmd start========================================") 
		        # print ('@@@@cmd:%s' % cmdtmp)
		        print("cmd end========================================") 
		        os.system(cmdtmp)

# os.remove(rootdir + "/tmp.plist")

if raw_input("\r\n Pack Completed! Press Any Key To Exit!"):
  pass

