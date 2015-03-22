### I-Section (equal): Geometric Properties

    B = 220mm
    D = 400mm
    tf = 12mm
    tw = 9mm
    
Depth of web:

    d = D - 2tf => 376mm

Flange width excluding the web thickness:

    b = B - tw => 211mm

Area of cross-section:

    Ax = (B * D - b * d) => 8664mm^2

Moment of inertia about major axis:

    Iy = (B * D^3 - b * d^3) / 12 => 238649472mm^4

Moment of inertia about minor axis:

    Iz = (D * B^3 - d * b^3) / 12 => 60590162mm^4

Polar moment of inertia:

    K = (2 * B * tf^3 + D * tw^3) / 3 => 350640mm^4

Radius of gyration (major axis):

    ry = sqrt(Iy / Ax) => 165.97mm

Radius of gyration (minor axis):

    rz = sqrt(Iz / Ax) => 83.63mm

Section modulus (elastic):

    Sy = Iy / (D / 2) => 1193247.36mm^3
    Sz = Iz / (B / 2) => 550819.65mm^3

Section modulus (plastic):

    Zy = (tw * d^2 / 4) + B * tf * (d + tf) => 1342416mm^3
    Zz = (tf * B^2 / 2) + (d * tw^2 / 4) => 298014mm^3
    
Shape factors (ratio of plastic to elastic section modulus):

    SFy = Zy / Sy => 1.13
    SFz = Zz / Sz => 0.54

Summary of results:

    B   => 220mm
    D   => 400mm
    tf  => 12mm
    tw  => 9mm
    
    Ax  => 8664mm^2
    ry  => 165.97mm
    rz  => 83.63mm
    
    Iy  => 238649472mm^4
    Iz  => 60590162mm^4
    K   => 350640mm^4
    
    Sy  => 1193247.36mm^3
    Sz  => 550819.65mm^3
    Zy  => 1342416mm^3
    Zz  => 298014mm^3
    SFy => 1.13
    SFz => 0.54
