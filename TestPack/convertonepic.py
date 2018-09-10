# -*- coding: cp936 -*-
import os,sys
imagedir = 'E:\\Test\\testonepic'
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
          " --sheet " + outplistdir + os.sep + herolist[n] + ".jpg"\
          " --algorithm Basic" \
          " --no-trim" \
          " --texture-format jpg" \
          " --opt RGB888" \
          " --size-constraints AnySize" \
          " --shape-padding 0" \
          " --padding 0" \
          " --allow-free-size"
  os.system(cmdtmp)