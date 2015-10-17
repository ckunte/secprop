# secprop

[![Build Status](https://travis-ci.org/ckunte/secprop.svg?branch=master)](https://travis-ci.org/ckunte/secprop)

`secprop` is a simple python script set for calculating geometric section properties of tubes and prismatic sections, viz., hollow box, channel, I (Equal), and T sections.

### Axes, Conventions:

             y
             |
         +--+|+--+
         +--+|+--+
            |||
    z -------+-------- z
            |||
         +--+|+--+
         +--+|+--+
             |
             y
          
   (Typical Cross section)


Legend: All symbols used in the calculations are standard symbols.

- Ax -- Cross-sectional area.
- D -- Diameter (Outer), or Depth.
- B -- Breadth.
- t -- Wall thickness.
- Cy, Cz -- Distances to centroid in y and z directions respectively.
- Iy -- Moment of inertia (Second moment of area) about y -- y axis.
- Iz -- Moment of inertia (Second moment of area) about z -- z axis.
- J, K -- Polar moment of inertia (torsional constant).
- ry, rz -- Radii of gyration  about y -- y and z -- z axes respectively.
- Sy, Sz -- Elastic section moduli about y -- y and z -- z axes respectively.
- Zy, Zz -- Plastic section moduli about y -- y and z -- z axes respectively.
- SFy, SFz -- Shape factors about  y -- y and z -- z axes respectively.

Note: All moments of inertia are with respect to the section's geometric centroid.

## Download

Clone the repository on your computer. The following downloads `moorprop` folder:

	git clone https://github.com/ckunte/secprop.git

## Run

	python secprop.py

