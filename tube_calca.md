### Tube: Geometric properties

	D = 508mm
	t = 20mm

Area:

	Ax = (pi / 4) * (D^2 - (D - 2t)^2) => 30661.94mm^2

Area can also be calculated as follows:

	A = pi * (D - t) * t => 30661.94mm^2

Moment of inertia (about the tube's centroidal axis):

	Iy = (pi / 64) * (D^4 - (D - 2t)^4) => 914277855.11mm^4

Radius of gyration:

	r = sqrt(Iy / Ax) => 172.68mm

Polar moment of inertia (also known as torsion constant):

	J = (pi / 4) * ((D - t)^3) * t => 1825489515.79mm^4

(Torsion constant can also be approximated to 2.Iy, although this results in a slightly higher value of J.)

Distance of tube centroid from the extreme outer fibre:

	y = D / 2 => 254mm

Section modulus (Elastic):

	S = Iy / y => 3599519.11mm^3

Section modulus (Plastic):

	Z = (D^3 - (D - 2t)^3) / 6 => 4765546.67mm^3

Shape factor of tube:

	SF = Z / S => 1.32

Summary of results:

    D  => 508mm
    t  => 20mm
    
    Ax => 30661.94mm^2
    y  => 254mm
    r  => 172.68mm

    Iy => 914277855.11mm^4
    J  => 1825489515.79mm^4

    S  => 3599519.11mm^3
    Z  => 4765546.67mm^3
    SF => 1.32