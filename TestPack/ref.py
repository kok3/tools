# -*- coding: cp936 -*-
import os,sys
imagedir = 'E:\\Test\\testin'
outplistdir = 'E:\\Test\\testout'
comend = 'texturepacker'

print "imagedir = %s \noutdir = "%imagedir,outplistdir
herolist = os.listdir(imagedir)
print "heave %d hero convert"%len(herolist)
for n in range(len(herolist)):
  herodirtmp = imagedir + os.sep + herolist[n]
  herotmplist = os.listdir(herodirtmp)
  cmdtmp = comend
  print "hero %s heave image = %d"%(str(herolist[n]),len(herotmplist))
  allImage = ""
  for im in range(len(herotmplist)):
    allImage = allImage + " " + herodirtmp + os.sep + herotmplist[im]
    print allImage
  cmdtmp = cmdtmp + " " + allImage +\
          " --format cocos2d" +\
          " --data " + outplistdir + os.sep + herolist[n] + ".plist"\
          " --sheet " + outplistdir + os.sep + herolist[n] + ".pvr.ccz"\
          " --texture-format pvr2ccz" \
          " --opt RGBA4444" \
          " --allow-free-size" 
  os.system(cmdtmp)

import os
import re

rootdir = '../meishu/res_etc'
comend = 'texturepacker'
tga2pkm = 'F:\\JpegCompress.exe'

herolist = os.listdir(imagedir)
for n in range(len(herolist)):
  fulldirpath = rootdir + os.sep + herolist[n]
  for fileName in os.listdir(fulldirpath):
    if re.match('[^.]+.png', fileName) is None:
      continue
    inputimageName = fulldirpath +  os.sep + fileName
    outputimageName = inputimageName
    outputimageName = outputimageName.replace('.png', '.tga')
    cmdtmp = comend
    cmdtmp = cmdtmp + " " + inputimageName + \
      " --format cocos2d" +\
      " --data " + outplistdir + os.sep + herolist[n] + ".plist"\
      " --sheet " + outplistdir + os.sep + herolist[n] + ".pvr.ccz"\
      " --texture-format pvr2ccz" \
      " --opt RGBA4444" \
      " --allow-free-size" 
    os.system(cmdtmp)
    print ('@@@@outputimageName:%s' % outputimageName)
os.remove(rootdir + "/tmp.plist")

if raw_input("\r\n Press Any Key To Quit"):
  pass
