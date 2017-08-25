#!/usr/bin/env python
import platform
import random

print platform.linux_distribution()

print "function 'platform.linux_distribution()' with function join()"

sys_info = ' '.join(platform.linux_distribution())
print sys_info

if "CentOS" in sys_info:
	print "CentOS"
elif "Ubuntu" in sys_info:
	print "Debian OS"
else:
	print "Unknow OS"

#print "Indentations have matters, if they there are not present in if statement, python will return error code"
#if "CentOS" in sys_info:
#print "Red Hat"

test_score = random.randint(0,100)
if test_score >=90:
	print "A"
elif test_score >=80:
	print "B"
elif test_score >=70:
	print "C"
elif test_score >=60:
	print "D"
else:
	print "F"
print test_score
