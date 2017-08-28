#!/usr/bin/env python
for number in range(1, 11):
	if number % 2 > 0:
		print number

for number in range(1, 10):
	if number == 5:
		print "I have counted to %s" % number
		break

for number in range(1, 10):
    if number == 5:
       print "I have counted to %s" % number
       break
else:
    print "I have counted from 1 to 10"

for number in range(1, 10):
    if number == 5:
       print "I have counted to %s" % number
else:
    print "I have counted from 1 to 10"

notes = "And a 1 and a 2 and a 3"
for x in notes:
	if x.isdigit():
		print x
