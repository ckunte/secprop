#!/usr/bin/env python
# encoding: utf-8
'''
allsec.py

Copyright (c) 2011 by C. Kunte.
<http://github.com/ckunte/secprop>

secprop comes with ABSOLUTELY NO WARRANTY. 
This is free software under MIT license.

<http://opensource.org/licenses/mit-license.php>

'''

from math import *

# Geometric section properties

# Tube section.
def tube():
	# User input (keyboard)
	D, t = input("Enter D, t: ")
	
	# Stop if any input is < or = to zero.
	while D <= 0 or t <= 0 :
		print "Pl. check input, and try again."
		print "Example: 508, 20"
		break
	
	# Continue calculation if input is > zero.
	else:
		# Calculate geometric section properties of a tube:
		A = pi * (D**2 - (D - 2 * t)**2) / 4
		# Alternatively:
		#	A = pi * (D - t) * t
		y = D / 2
		I = pi * (D**4 - (D - 2 * t)**4) / 64
		r = sqrt(I / A)
		J = pi * ((D - t)**3) * t / 4
		# Alternatively (Polar moment of inertia or torsion constant):
		# J = 2 * I
		S = I / y
		Z = (D**3 - (D - 2 * t)**3) / 6
		SF = Z / S
		
		# Print results (rounded-off at 2 decimals) 
		print "Area,                    A: ", round(A, 2)
		print "Moment of inertia,       I: ", round(I, 2)
		print "Radius of gyration,      r: ", round(r, 2)
		print "Polar moment of inertia, J: ", round(J, 2)
		print "Elastic section modulus, S: ", round(S, 2)
		print "Plastic section modulus, Z: ", round(Z, 2)
		print "Shape factor,          S/Z: ", round(SF, 2)
		print
		print "References:" 
		print "1. Pg 62, Structural Engineer's Pocket Book, Fiona Cobb,"
		print "   2nd Edition."
		print "2. Pg 67, Roark's Formulas for Stress & Strain, WC Young,"
		print "   6th Edition."
		print "3. Pg 35, Structural Engineering Formulas, Ilya Mikhelson."
		print 
	pass


# Hollow rectangular box section.
def hbox():
	# User input (keyboard)
	B, D, t = input("Enter B, D, t: ")
	
	# Stop if any input is < or = to zero.
	while B <= 0 or D <= 0 or t <= 0 :
		print "Pl. check input, and try again."
		print "Example: 230, 400, 16"
		break
	
	# Continue calculation if input > zero.
	else:
		# Calculate geometric section properties:
		b = B - 2 * t
		d = D - 2 * t
		#
		Ax = (B * D) - (b * d)
		#
		Iy = ((B * D**3) - (b * d**3)) / 12
		Iz = ((D * B**3) - (d * b**3)) / 12
		K = t * (B - t) * (D - t)**2
		#
		ry = sqrt(Iy / Ax)
		rz = sqrt(Iz / Ax)
		#
		Sy = Iy / (D / 2)
		Sz = Iz / (B / 2)
		#
		Zy = ((B * D**2) - (b * d**2)) / 4
		Zz = ((D * B**2) - (d * b**2)) / 4
		#
		sfy = Zy / Sy
		sfz = Zz / Sz
		#
		# Print results (rounded-off at 2 decimals) 
		print "Area,                    Ax: ", round(Ax, 2)
		print "Moment of inertia,       Iy: ", round(Iy, 2)
		print "Moment of inertia,       Iz: ", round(Iz, 2)
		print "Polar moment of inertia,  K: ", round(K, 2)
		print "Radius of gyration,      ry: ", round(ry, 2)
		print "Radius of gyration,      rz: ", round(rz, 2)
		print "Elastic section modulus, Sy: ", round(Sy, 2)
		print "Elastic section modulus, Sz: ", round(Sz, 2)
		print "Plastic section modulus, Zy: ", round(Zy, 2)
		print "Plastic section modulus, Zz: ", round(Zz, 2)
		print "Shape factor,           SFy: ", round(sfy, 2)
		print "Shape factor,           SFz: ", round(sfz, 2)
		print
		print "References:" 
		print "1. Pg 61, Structural Engineer's Pocket Book, Fiona Cobb,"
		print "   2nd Edition."
		print "2. Pg 62, Roark's Formulas for Stress & Strain, WC Young,"
		print "   6th Edition."
		print 
	pass	


# Channel section.
def channel():
	# User input (keyboard)
	B, D, tf, tw = input("Enter B, D, tf, tw: ")
	
	# Stop if any input is < or = to zero.
	while B <= 0 or D <= 0 or tf <= 0 or tw <= 0 :
		print "Pl. check input, and try again."
		print "Example: 230, 400, 16, 12"
		break
	
	# Continue calculation if input > zero.
	else:
		# Calculate geometric section properties:
		d = (D - 2 * tf)
		Ax = (B * D) - d * (B - tw)
		Cy = D / 2
		Cz = (2 * (B**2) * tf + d * (tw**2)) / (2 * B * D - 2 * d * (B - tw))
		Iy = ((B * D**3) - (B - tw) * (D - 2 * tf)**3) / 12
		Iz = ((2 * tf * (B**3) - (D - 2 * tf) * (tw**3)) / 12) \
		     + (2 * B * tf * ((B / 2) - Cz)**2) \
		     + (tw * (D - 2 * tf) * (Cz - 0.5 * tw)**2)
		K = Iy + Iz 
		ry = sqrt(Iy / Ax)
		rz = sqrt(Iz / Ax)
		Sy = Iy / Cy
		Sz = Iz / Cz
		Zy = (D**2 * tw / 4) + tf * (B - tw) * (D - tf)
		
		if (2* tf * (B - tw)) <= (D * tw) :
			Zz = (tf * (B - tw)**2 / 2) - (D**2 * tw**2 / (tf * 8)) \
			     + (D * tw * B / 2)
			# Neutral axis 2 is located at the following distance 
			# from the right:
			NA_from_right = ((D * tw / (2 * tf)) + (B - tw)) / 2
			
		if (2* tf * (B - tw)) > (D * tw) :
			Zz = (tw**2 * D / 4) + tf * (B - tw) * (B - tf * (B - tw) / D)
			# Neutral axis 2 is located at the following distance
			# from the left:
			NA_from_left = tf * (B - tw) + tw / 2
			
		SFy = fabs(Zy * D * 0.5 / Iy)
		SFz = fabs(Zz * (B - Cy) / Iz)
		
		# Print results (rounded-off at 2 decimals) 
		print "Area,                    Ax: ", round(Ax, 2)
		print "Moment of inertia,       Iy: ", round(Iy, 2)
		print "Moment of inertia,       Iz: ", round(Iz, 2)
		print "Polar moment of inertia,  K: ", round(K, 2)
		print "Radius of gyration,      ry: ", round(ry, 2)
		print "Radius of gyration,      rz: ", round(rz, 2)
		print "Elastic section modulus, Sy: ", round(Sy, 2)
		print "Elastic section modulus, Sz: ", round(Sz, 2)
		print "Plastic section modulus, Zy: ", round(Zy, 2)
		print "Plastic section modulus, Zz: ", round(Zz, 2)
		print "Shape factor,           SFy: ", round(SFy, 2)
		print "Shape factor,           SFz: ", round(SFz, 2)
		print
		print "References:" 
		print "1. Pg 61, Structural Engineer's Pocket Book, Fiona Cobb,"
		print "   2nd Edition."
		print 
	pass


# I (Equal)
def ieq():
	# User input (keyboard)
	B, D, tf, tw = input("Enter B, D, tf, tw: ")
	
	# Stop if any input is < or = to zero.
	while B <= 0 or D <= 0 or tf <= 0 or tw <=0 :
		print "Pl. check input, and try again."
		print "Example: 230, 400, 16, 12"
		break
	
	# Continue calculation if input > zero.
	else:
		# Calculate geometric section properties:
		d = (D - 2 * tf)
		b = (B - tw)
		Ax = (B * D) - (b * d)
		Iy = (B * D**3 - b * d**3) / 12
		Iz = (D * B**3 - d * b**3) / 12
		K = (B * tf**3 * 2 + D * tw**3) / 3
		ry = sqrt(Iy / Ax)
		rz = sqrt(Iz / Ax)
		Sy = Iy / (D / 2)
		Sz = Iz / (B / 2)
		Zy = (tw * d**2 / 4) + B * tf * (d + tf)
		Zz = (tf * B**2 / 2) + (d * tw**2 / 4)
		SFy = Zy * D * 0.5 / Iy
		SFz = Zz * B * 0.5 / Iz
		
		# Print results (rounded-off at 2 decimals) 
		print "Area,                    Ax: ", round(Ax, 2)
		print "Moment of inertia,       Iy: ", round(Iy, 2)
		print "Moment of inertia,       Iz: ", round(Iz, 2)
		print "Polar moment of inertia,  K: ", round(K, 2)
		print "Radius of gyration,      ry: ", round(ry, 2)
		print "Radius of gyration,      rz: ", round(rz, 2)
		print "Elastic section modulus, Sy: ", round(Sy, 2)
		print "Elastic section modulus, Sz: ", round(Sz, 2)
		print "Plastic section modulus, Zy: ", round(Zy, 2)
		print "Plastic section modulus, Zz: ", round(Zz, 2)
		print "Shape factor,           SFy: ", round(SFy, 2)
		print "Shape factor,           SFz: ", round(SFz, 2)
		print
		print "References:" 
		print "1. Pg 64, Roark's Formulas for Stress & Strain, WC Young,"
		print "   6th Edition."
		print 
	pass


# Tee section.
def tee():
	# User input (keyboard)
	B, D, tf, tw = input("Enter B, D, tf, tw: ")
	
	# Stop if any input is < or = to zero.
	while B <= 0 or D <= 0 or tf <= 0 or tw <= 0 :
		print "Pl. check input, and try again."
		print "Example: 230, 400, 16, 12"
		break
	
	# Continue calculation if input > zero.
	else:
		# Calculate geometric section properties:
		d = D - tf
		b = B - tw
		Cy = (B * tf**2 + tw * d * (tf * 2 + d)) / (B * tf * 2 + d * tw) 
		Cz = B / 2
		Ax = B * tf + d * tw
		Iy = (tw * Cy**3 + B * (D - Cy)**3 - b * (D - Cy - tf)**3) / 3
		Iz = (tf**3 * B + tw**3 * D) / 3 
		K = (tf * B**3 + d * tw**3) / 3
		ry = sqrt(Iy / Ax)
		rz = sqrt(Iz / Ax)
		Sy = Iy / Cy
		Sz = Iz / Cz
		'''		
		if (tw * d) <= (B * tf) :
			Zy = (tw * d**2 / 4) - (b**2 * tf**2 / (4 * tw)) \
			     + (b * tf * B / 2) 
			# Neutral axis 1 is located at the following distance 
			# from the bottom:
			NA_from_bott = ((B * tf / tw) + d) / 2
		
		if (tw * d) > (B * tf) :
			Zy = (B * tf**2 / 4) + (tw * d * (B - (tw * d / 2 * B))) / 2
			# Neutral axis 1 is located at the following distance
			# from the top:
			NA_from_top = ((tw * d / B) + tf) / 2 
		
		Zz = (B**2 * tf + tw**2 * d) / 4
		SFy = Zy * (B - Cy) / Iy
		SFz = Zz * B / (2 * Iz)
		'''	
		# Print results (rounded-off at 2 decimals)
		print "Area,                    Ax: ", round(Ax, 2)
		print "Moment of inertia,       Iy: ", round(Iy, 2)
		print "Moment of inertia,       Iz: ", round(Iz, 2)
		print "Polar moment of inertia,  J: ", round(K, 2)
		print "Radius of gyration,      ry: ", round(ry, 2)
		print "Radius of gyration,      rz: ", round(rz, 2)
		print "Elastic section modulus, Sy: ", round(Sy, 2)
		print "Elastic section modulus, Sz: ", round(Sz, 2)
		print "N.A distance (from top), Cy: ", round(Cy, 2)
		# print "Plastic section modulus, Zy: ", round(Zy, 2)
		# print "Plastic section modulus, Zz: ", round(Zz, 2)
		# print "Shape factor,           SFy: ", round(SFy, 2)
		# print "Shape factor,           SFz: ", round(SFz, 2)
		print
		print "References:" 
		print "1. Pg 63, Structural Engineer's Pocket Book, Fiona Cobb,"
		print "   2nd Edition."
		print "2. Pg 63, Roark's Formulas for Stress & Strain, WC Young,"
		print "   6th Edition."
		print
	pass


def donotrun():
	print
	print "-----------------------------------------" 
	print "Please do not execute this file directly."
	print "Usage: "
	print
	print "  python sec.py"
	print "-----------------------------------------" 
	print 


if __name__ == '__main__':
	donotrun()
