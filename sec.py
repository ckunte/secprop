#!/usr/bin/env python
# encoding: utf-8
'''
sec.py

Usage: $ python sec.py


Copyright (c) 2011 by C. Kunte. 
<http://github.com/ckunte/secprop>

secprop comes with ABSOLUTELY NO WARRANTY. This is free 
software under MIT license.

<http://opensource.org/licenses/mit-license.php>

'''

from allsec import *

def main():
	print 
	print "Section Properties ver 1.0"
	print 
	print "1 - Tube.        4 - I (Equal)."
	print "2 - Hollow box.  5 - T."
	print "3 - Channel."
	
	# User input (via keyboard)
	sectype = input("Select section type: ")
	pass
	
	if sectype == 1 :
		tube()
	
	elif sectype == 2 :
		hbox()
		
	elif sectype == 3 :
		channel()
	
	elif sectype == 4 : 
		ieq()
	
	elif sectype == 5 :
		tee()
	
	else:
		print "No available option was selected."
		return


if __name__ == '__main__':
	main()

