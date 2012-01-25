#!/usr/bin/python
# This is pretty cheap right now, I hope to make it a bit nicer.

import sys
import re

#fd = open("/tmp/regex_run.log","w")
#print >>fd, 'dammit'
#fd.flush()


reg_line = "null"
regex = ""
while (reg_line.strip() != ''):
   #print >>fd, "loop head"
   reg_line = sys.stdin.readline()
   #print >>fd, "reg recv: '%s' --" % reg_line
   #fd.flush()
   #print >>fd, "post flush"
   regex += reg_line
   #print >>fd, "loop tail"
   
sys.stdout.write('next')

sys.stdout.flush()


#print >>fd, "next sent to stdout"
str_to_match = ""
str_line = "null"
while (str_line.strip() != ''):
 #  print >>fd, 'loop head'
   str_line = sys.stdin.readline()
  # print >>fd, "str recv: '%s' --" % str_line
   #fd.flush()
   str_to_match += str_line
   #print >>fd, 'loop tail'

# Set up regular expression:
my_re = re.compile(r"""%s""" % regex,re.VERBOSE)
reg_match = my_re.search(str_to_match)
if(reg_match):
   sys.stdout.write("Match!<br />")
   gd = reg_match.groupdict()
   gl = reg_match.groups()
   if (len(gd) > 0):
      print "Group dictionary:<br />%s" % (
            "<br />".join(["%s => %s" % (k,v) for (k,v) in gd.items()])
            )
   elif (len(gl) > 0):
      sys.stdout.write("Group tuple: <br />%s<br />" % "<br />".join(gl))
   else:
      sys.stdout.write("No groups!")
else:
   sys.stdout.write("No match!")
      
sys.stdout.flush()
fd.close()
