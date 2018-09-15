#xmlTest.py

import xml.dom.minidom

filename = "xmlTest.xml"
###1.DOM(Document Object Model)
print "1.DOM"
dom = xml.dom.minidom.parse(filename)
root = dom.documentElement

emplist = root.getElementsByTagName("emp")
num = 1
for node in emplist:
    print "*** emp node %d ***" % num
    print node, node.toxml(), node.nodeName, node.getAttribute("id")

    print "*** empno node ***"
    empnolist = node.getElementsByTagName("empno")
    print empnolist[0].toxml(), empnolist[0].nodeName, empnolist[0].firstChild.data

    print "*** ename node ***"
    enamelist = node.getElementsByTagName("ename")
    print enamelist[0].toxml(), enamelist[0].nodeName, enamelist[0].firstChild.data

    print "*** job node ***"
    joblist = node.getElementsByTagName("job")
    print joblist[0].toxml(), joblist[0].nodeName, joblist[0].firstChild.data

    print 
    num = num + 1
