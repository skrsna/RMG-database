#!/usr/bin/env python
# encoding: utf-8

name = "Isodesmic-Reference-Set"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "C2H2O_331",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07261,-0.00723578,8.21302e-05,-1.59282e-07,1.01047e-10,31214.6,5.64598], Tmin=(10,'K'), Tmax=(506.732,'K')),
            NASAPolynomial(coeffs=[3.09441,0.0117381,-7.34316e-06,2.25141e-09,-2.65993e-13,31169.3,8.27482], Tmin=(506.732,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (259.527,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 157-18-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 1,
    label = "CHNO_312",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98701,0.000735576,2.34314e-05,-4.03232e-08,2.15511e-11,-15651.3,4.99506], Tmin=(10,'K'), Tmax=(581.315,'K')),
            NASAPolynomial(coeffs=[3.14389,0.00936828,-6.14966e-06,1.9794e-09,-2.447e-13,-15601.1,8.19379], Tmin=(581.315,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.138,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 75-13-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 2,
    label = "C3H9N_269",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87509,0.00840485,7.29458e-05,-1.07025e-07,4.90047e-11,-5313.81,4.08298], Tmin=(10,'K'), Tmax=(569.717,'K')),
            NASAPolynomial(coeffs=[-1.35075,0.0450957,-2.36569e-05,6.01715e-09,-5.99737e-13,-4718.36,26.3545], Tmin=(569.717,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 75-50-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 3,
    label = "N2O_316",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p2 c0 {1,S}
3 N u0 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53196,-0.00313257,3.95541e-05,-7.14678e-08,4.16031e-11,64118.7,5.24681], Tmin=(10,'K'), Tmax=(550.917,'K')),
            NASAPolynomial(coeffs=[2.86194,0.00750449,-5.12415e-06,1.61585e-09,-1.91843e-13,64104.9,7.28483], Tmin=(550.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (533.109,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 227934-46-5*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 4,
    label = "CHCl2F_111",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93764,0.00380379,5.6033e-05,-1.23899e-07,7.93585e-11,-35799,10.2333], Tmin=(10,'K'), Tmax=(542.885,'K')),
            NASAPolynomial(coeffs=[4.36215,0.0142227,-1.01843e-05,3.38074e-09,-4.2061e-13,-36044.7,6.606], Tmin=(542.885,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-297.671,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-43-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 5,
    label = "C3H6O2_387",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67876,0.0338738,-8.27687e-05,2.19958e-07,-1.95559e-10,-51892.8,7.63583], Tmin=(10,'K'), Tmax=(426.778,'K')),
            NASAPolynomial(coeffs=[0.902785,0.0382378,-2.19994e-05,6.14413e-09,-6.67957e-13,-51458.7,20.975], Tmin=(426.778,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-431.47,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 79-20-9*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 6,
    label = "C2O_255",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,T}
2 O u1 p2 c0 {1,S}
3 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99232,0.000641705,2.07583e-05,-6.01238e-08,5.873e-11,44549.4,4.06931], Tmin=(10,'K'), Tmax=(259.216,'K')),
            NASAPolynomial(coeffs=[3.7267,0.0047404,-2.95943e-06,8.74594e-10,-9.95072e-14,44563.2,4.99213], Tmin=(259.216,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (370.407,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-b3lyp-gd3bj_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 12071-23-7*1 and used to tweak b3lyp-gd3bj_jun-cc-pvtz calculation
""",
)

entry(
    index = 7,
    label = "C2_86",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 C u0 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50719,-0.000421792,1.327e-06,1.58826e-09,-2.13987e-12,99292,4.16683], Tmin=(10,'K'), Tmax=(622.136,'K')),
            NASAPolynomial(coeffs=[2.87542,0.00211453,-1.10991e-06,2.58028e-10,-2.14493e-14,99400.2,7.15219], Tmin=(622.136,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (825.564,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12070-15-4*1 and used to tweak g4 calculation
""",
)

entry(
    index = 8,
    label = "C3H8O_315",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77373,0.0229867,-2.79724e-05,1.10644e-07,-1.08677e-10,-28158.6,6.48445], Tmin=(10,'K'), Tmax=(470.146,'K')),
            NASAPolynomial(coeffs=[-1.24501,0.0437908,-2.44913e-05,6.65033e-09,-7.04855e-13,-27444.7,29.4828], Tmin=(470.146,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-234.125,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 540-67-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 9,
    label = "C2H6O2_425",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79954,0.0201051,7.64488e-06,-1.74684e-08,6.37741e-12,-22041.8,7.38696], Tmin=(10,'K'), Tmax=(1048.79,'K')),
            NASAPolynomial(coeffs=[4.04804,0.0271404,-1.38348e-05,3.44285e-09,-3.37189e-13,-22533,4.08309], Tmin=(1048.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-183.269,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""Automated Thermochemistry Protocol Based on Explicitly Correlated Coupled-Cluster Theory-g4""",
    longDesc = 
u"""
H298 taken from Automated Thermochemistry Protocol Based on Explicitly Correlated Coupled-Cluster Theory  and used to tweak g4 calculation
""",
)

entry(
    index = 10,
    label = "C7H7_259",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14242,-0.0144988,0.000265499,-4.83852e-07,2.82512e-10,23277.9,9.81124], Tmin=(10,'K'), Tmax=(547.822,'K')),
            NASAPolynomial(coeffs=[-0.59819,0.0581298,-3.7454e-05,1.14931e-08,-1.3457e-12,23226.9,24.6228], Tmin=(547.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2154-56-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 11,
    label = "C5H12_198",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62771,0.0398558,-7.67853e-05,2.62881e-07,-2.54061e-10,-20164.5,6.94587], Tmin=(10,'K'), Tmax=(439.812,'K')),
            NASAPolynomial(coeffs=[-3.26534,0.0653517,-3.68852e-05,1.01137e-08,-1.08155e-12,-19198.4,38.6286], Tmin=(439.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-167.664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 109-66-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 12,
    label = "CF2_129",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0412,-0.0031357,2.85588e-05,-4.24484e-08,2.0024e-11,-24510.6,5.92936], Tmin=(10,'K'), Tmax=(692.351,'K')),
            NASAPolynomial(coeffs=[3.39404,0.00637104,-4.53401e-06,1.44937e-09,-1.71822e-13,-24559.2,7.81525], Tmin=(692.351,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-203.788,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2154-59-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 13,
    label = "H2N_115",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00645,-0.000320474,1.11883e-06,1.67624e-09,-1.44309e-12,21182.1,1.31655], Tmin=(10,'K'), Tmax=(794.107,'K')),
            NASAPolynomial(coeffs=[3.21764,0.00190988,1.982e-07,-3.14834e-10,5.38808e-14,21362.3,5.28627], Tmin=(794.107,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (176.12,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 13770-40-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 14,
    label = "C2H3ClN2_347",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C  u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H  u0 p0 c0 {5,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92574,0.0053541,0.00010379,-2.58732e-07,2.01129e-10,24311.8,8.82964], Tmin=(10,'K'), Tmax=(410.875,'K')),
            NASAPolynomial(coeffs=[2.86245,0.0271115,-1.72806e-05,5.27557e-09,-6.18303e-13,24302.9,11.842], Tmin=(410.875,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (202.14,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 4222-21-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 15,
    label = "CFO_39",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03011,-0.00211914,2.27358e-05,-3.45073e-08,1.67506e-11,-22421.2,6.8568], Tmin=(10,'K'), Tmax=(660.861,'K')),
            NASAPolynomial(coeffs=[3.41005,0.00556665,-3.6356e-06,1.10063e-09,-1.26202e-13,-22425.1,8.94164], Tmin=(660.861,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-186.418,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1871-24-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 16,
    label = "C2H_320",
    molecule = 
"""
multiplicity 2
1 C u0 p1 c0 {2,S} {3,S}
2 C u1 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49418,0.000417496,1.08261e-05,-2.69373e-08,2.18497e-11,67199.7,4.49197], Tmin=(10,'K'), Tmax=(402.125,'K')),
            NASAPolynomial(coeffs=[3.45551,0.00212636,-4.87769e-07,8.65505e-12,6.39061e-15,67192.2,4.51018], Tmin=(402.125,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (558.731,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 2122-48-7*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 17,
    label = "CHO2_152",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0463,-0.00445531,5.36329e-05,-9.85768e-08,5.89788e-11,-23413.3,6.89778], Tmin=(10,'K'), Tmax=(533.975,'K')),
            NASAPolynomial(coeffs=[3.19797,0.00932294,-5.92515e-06,1.8166e-09,-2.13398e-13,-23428.5,9.46725], Tmin=(533.975,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.673,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2564-86-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 18,
    label = "C3H2O_323",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94591,0.00360959,6.53998e-05,-1.5356e-07,1.09753e-10,14358.4,7.69363], Tmin=(10,'K'), Tmax=(464.514,'K')),
            NASAPolynomial(coeffs=[3.61951,0.0167553,-1.04241e-05,3.15936e-09,-3.71258e-13,14277.2,7.81785], Tmin=(464.514,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (119.373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 624-67-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 19,
    label = "O_40",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,29230.3,4.09089], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,29230.3,4.09089], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (243.035,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 17778-80-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 20,
    label = "CClF3_247",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91926,0.00475499,6.44412e-05,-1.40299e-07,8.63885e-11,-87101.2,8.88392], Tmin=(10,'K'), Tmax=(575.889,'K')),
            NASAPolynomial(coeffs=[4.9825,0.0158222,-1.24469e-05,4.34697e-09,-5.56867e-13,-87529.6,1.68458], Tmin=(575.889,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-724.233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-72-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 21,
    label = "CF_134",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p1 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51654,-0.000954125,5.5245e-06,-5.75088e-09,1.90336e-12,28633.3,4.9716], Tmin=(10,'K'), Tmax=(967.377,'K')),
            NASAPolynomial(coeffs=[3.05971,0.00222476,-1.4048e-06,4.02854e-10,-4.31818e-14,28661.3,6.84842], Tmin=(967.377,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.075,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3889-75-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 22,
    label = "C7H14_329",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96442,0.00152888,0.000211438,-3.38419e-07,1.75803e-10,-16758,8.84702], Tmin=(10,'K'), Tmax=(497.609,'K')),
            NASAPolynomial(coeffs=[-6.91196,0.0889596,-5.21196e-05,1.46858e-08,-1.60139e-12,-15675.6,53.728], Tmin=(497.609,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-139.363,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 291-64-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 23,
    label = "C3H3_203",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12798,-0.0105464,9.63207e-05,-1.52278e-07,7.85974e-11,57068,6.2193], Tmin=(10,'K'), Tmax=(613.863,'K')),
            NASAPolynomial(coeffs=[1.71409,0.01953,-1.22308e-05,3.68532e-09,-4.25528e-13,57094,14.4851], Tmin=(613.863,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (474.493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 28933-84-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 24,
    label = "C2HF4_409",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {1,S}
5 F u0 p3 c0 {1,S}
6 F u0 p3 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81426,0.0149197,6.79786e-05,-1.83682e-07,1.30541e-10,-86222.4,10.4726], Tmin=(10,'K'), Tmax=(509.468,'K')),
            NASAPolynomial(coeffs=[5.31278,0.0234476,-1.68786e-05,5.54262e-09,-6.78536e-13,-86638.4,1.66903], Tmin=(509.468,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-716.925,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 25,
    label = "CH3O_77",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07135,-0.00480556,3.82818e-05,-4.57256e-08,1.79279e-11,1320.38,4.30917], Tmin=(10,'K'), Tmax=(761.617,'K')),
            NASAPolynomial(coeffs=[1.27622,0.0142184,-7.74141e-06,2.04882e-09,-2.12191e-13,1620.15,16.2058], Tmin=(761.617,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (10.9937,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2143-68-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 26,
    label = "C4H2_50",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41192,0.0053924,6.8607e-05,-1.58616e-07,1.0444e-10,53733.5,6.08288], Tmin=(10,'K'), Tmax=(543.134,'K')),
            NASAPolynomial(coeffs=[4.87316,0.014118,-9.30954e-06,3.08122e-09,-3.94694e-13,53287.3,-2.72085], Tmin=(543.134,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (446.735,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 460-12-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 27,
    label = "C3H4O_339",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87972,0.00979777,3.5996e-05,-6.91517e-08,3.93e-11,-9512.34,7.15535], Tmin=(10,'K'), Tmax=(460.777,'K')),
            NASAPolynomial(coeffs=[2.08795,0.0253522,-1.46397e-05,4.10997e-09,-4.49237e-13,-9347.22,14.4112], Tmin=(460.777,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.1073,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 6004-44-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 28,
    label = "CH3Br_51",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0601,-0.00457022,4.25727e-05,-5.82708e-08,2.65902e-11,-5650.83,6.3771], Tmin=(10,'K'), Tmax=(638.296,'K')),
            NASAPolynomial(coeffs=[1.74537,0.0132773,-7.22257e-06,1.94027e-09,-2.05148e-13,-5423.41,15.9718], Tmin=(638.296,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.9769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-83-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 29,
    label = "C6H4_257",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {6,S} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14605,-0.01371,0.000191316,-3.36218e-07,1.90214e-10,53477.2,8.75653], Tmin=(10,'K'), Tmax=(564.63,'K')),
            NASAPolynomial(coeffs=[0.459218,0.040289,-2.62051e-05,8.06464e-09,-9.44388e-13,53449.1,20.5005], Tmin=(564.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (444.618,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 462-80-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 30,
    label = "Br2O_95",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93115,0.00483066,3.17626e-05,-1.07253e-07,9.11128e-11,10962.7,10.4915], Tmin=(10,'K'), Tmax=(453.353,'K')),
            NASAPolynomial(coeffs=[5.3949,0.0036487,-3.14718e-06,1.16955e-09,-1.5651e-13,10709.4,3.25788], Tmin=(453.353,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.1418,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 21308-80-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 31,
    label = "C2H2F3_418",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88698,0.0071619,9.59298e-05,-2.27005e-07,1.5477e-10,-65445.5,8.6571], Tmin=(10,'K'), Tmax=(514.155,'K')),
            NASAPolynomial(coeffs=[4.91269,0.0223003,-1.56803e-05,5.16268e-09,-6.3977e-13,-65856.5,1.41937], Tmin=(514.155,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-544.176,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 32,
    label = "C5H5_370",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22469,-0.0188655,0.000187744,-3.03364e-07,1.5906e-10,29875.5,8.74855], Tmin=(10,'K'), Tmax=(608.064,'K')),
            NASAPolynomial(coeffs=[-0.067003,0.0382647,-2.44752e-05,7.46596e-09,-8.68668e-13,29863.1,22.9254], Tmin=(608.064,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (248.399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2143-53-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 33,
    label = "C4H8_15",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1618,-0.0117238,0.000139765,-1.8992e-07,8.34629e-11,1728.63,6.18817], Tmin=(10,'K'), Tmax=(695.755,'K')),
            NASAPolynomial(coeffs=[-3.22986,0.0485564,-2.85374e-05,8.08485e-09,-8.85665e-13,2326.74,36.0739], Tmin=(695.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (14.3957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 287-23-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 34,
    label = "C3H_216",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98439,0.00439609,5.46415e-06,-8.68823e-09,3.18357e-12,84555.5,6.27382], Tmin=(10,'K'), Tmax=(1009.12,'K')),
            NASAPolynomial(coeffs=[4.29816,0.00682878,-3.61665e-06,9.21153e-10,-9.14569e-14,84305,3.82975], Tmin=(1009.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (703.047,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 119178-99-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 35,
    label = "C2H3O2_139",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74071,0.0285377,-0.000113784,2.95677e-07,-2.59103e-10,-21106.9,8.43898], Tmin=(10,'K'), Tmax=(402.604,'K')),
            NASAPolynomial(coeffs=[2.41517,0.0215311,-1.25085e-05,3.50046e-09,-3.79777e-13,-20836.7,15.6587], Tmin=(402.604,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.503,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 16481-04-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 36,
    label = "C2HCl5_291",
    molecule = 
"""
1 Cl u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {7,S}
4 Cl u0 p3 c0 {7,S}
5 Cl u0 p3 c0 {7,S}
6 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54015,0.0381175,8.54953e-05,-4.28989e-07,4.35944e-10,-21767.6,12.8095], Tmin=(10,'K'), Tmax=(398.472,'K')),
            NASAPolynomial(coeffs=[9.00857,0.0245842,-1.92565e-05,6.75549e-09,-8.70017e-13,-22531.7,-12.6611], Tmin=(398.472,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-180.976,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 76-01-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 37,
    label = "F2_117",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51838,-0.0012781,9.26111e-06,-1.24015e-08,5.29179e-12,-1051.46,4.31697], Tmin=(10,'K'), Tmax=(762.687,'K')),
            NASAPolynomial(coeffs=[3.22478,0.00225055,-1.59026e-06,5.02709e-10,-5.87856e-14,-1064.52,5.27468], Tmin=(762.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.73878,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7782-41-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 38,
    label = "FO_200",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51789,-0.00117846,8.00925e-06,-9.99864e-09,3.97816e-12,12288.2,5.42219], Tmin=(10,'K'), Tmax=(812.861,'K')),
            NASAPolynomial(coeffs=[3.17258,0.00226207,-1.55296e-06,4.79164e-10,-5.48735e-14,12286.8,6.6627], Tmin=(812.861,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.174,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12061-70-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 39,
    label = "HO3_33",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96254,0.00234468,3.42733e-05,-7.81874e-08,5.20558e-11,1336.33,7.38776], Tmin=(10,'K'), Tmax=(521.322,'K')),
            NASAPolynomial(coeffs=[4.21276,0.00831181,-5.58911e-06,1.80875e-09,-2.22938e-13,1203.07,5.31569], Tmin=(521.322,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (11.0995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12500-78-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 40,
    label = "C3H2_300",
    molecule = 
"""
multiplicity 1
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98173,0.00123765,4.42149e-05,-9.47497e-08,6.56553e-11,93611.6,5.23167], Tmin=(10,'K'), Tmax=(427.589,'K')),
            NASAPolynomial(coeffs=[2.99998,0.0132798,-8.05571e-06,2.37921e-09,-2.73119e-13,93669.5,8.82844], Tmin=(427.589,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (778.33,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 202744-75-0*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 41,
    label = "ClF_64",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 F  u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51957,-0.00179492,1.75286e-05,-3.18445e-08,1.83076e-11,-7770.55,6.13602], Tmin=(10,'K'), Tmax=(584.302,'K')),
            NASAPolynomial(coeffs=[3.48107,0.0020691,-1.63377e-06,5.6472e-10,-7.10791e-14,-7827.51,5.77518], Tmin=(584.302,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-64.6097,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7790-89-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 42,
    label = "CClO_72",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 C  u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96894,0.002107,2.21756e-05,-6.15909e-08,4.777e-11,-3840.92,7.99916], Tmin=(10,'K'), Tmax=(466.594,'K')),
            NASAPolynomial(coeffs=[4.43052,0.00400296,-2.73552e-06,8.86098e-10,-1.09523e-13,-3947.71,5.44143], Tmin=(466.594,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.9399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2602-42-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 43,
    label = "HO2_3",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02889,-0.0017506,1.08382e-05,-1.12721e-08,3.83496e-12,271.662,4.68924], Tmin=(10,'K'), Tmax=(897.121,'K')),
            NASAPolynomial(coeffs=[3.04293,0.0043564,-2.23341e-06,5.67426e-10,-5.67515e-14,379.719,8.95518], Tmin=(897.121,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (2.26642,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3170-83-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 44,
    label = "C2H5Br_34",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97135,0.00166156,6.18327e-05,-1.03507e-07,5.63585e-11,-9245.55,8.35396], Tmin=(10,'K'), Tmax=(473.344,'K')),
            NASAPolynomial(coeffs=[1.12297,0.0257374,-1.44796e-05,3.9975e-09,-4.33683e-13,-8975.96,19.9647], Tmin=(473.344,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-76.8859,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-96-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 45,
    label = "N2O4_344",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p3 c-1 {5,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 N u0 p0 c+1 {1,S} {2,S} {3,D}
6 N u0 p1 c0 {1,S} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72278,0.0301308,-5.32037e-05,7.21923e-08,-4.52686e-11,2760.01,10.5955], Tmin=(10,'K'), Tmax=(374.973,'K')),
            NASAPolynomial(coeffs=[4.60454,0.0207247,-1.55766e-05,5.29447e-09,-6.66637e-13,2693.88,7.2065], Tmin=(374.973,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.9693,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 15969-55-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 46,
    label = "C3H2O_395",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96149,0.0040167,0.000107698,-4.92648e-07,7.8401e-10,13977.4,6.57149], Tmin=(10,'K'), Tmax=(157.907,'K')),
            NASAPolynomial(coeffs=[3.47385,0.0163693,-9.64282e-06,2.74872e-09,-3.04187e-13,13992.8,8.02402], Tmin=(157.907,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 61244-93-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 47,
    label = "CH2F2_53",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0695,-0.00462327,4.15888e-05,-5.10561e-08,2.02105e-11,-55481.4,6.40486], Tmin=(10,'K'), Tmax=(778.507,'K')),
            NASAPolynomial(coeffs=[1.34801,0.0155303,-9.13124e-06,2.55842e-09,-2.75967e-13,-55244.6,17.6522], Tmin=(778.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-461.283,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-10-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 48,
    label = "ClHO3_177",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 O  u0 p2 c0 {1,S} {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88849,0.00739176,6.9671e-05,-1.93547e-07,1.46306e-10,3298.77,9.46472], Tmin=(10,'K'), Tmax=(487.353,'K')),
            NASAPolynomial(coeffs=[5.96568,0.0115847,-8.61314e-06,2.97499e-09,-3.82454e-13,2844.05,-1.65156], Tmin=(487.353,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 928652-99-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 49,
    label = "FH_202",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49714,0.000153872,-7.75105e-07,1.12876e-09,-4.00137e-13,-33845.3,0.92447], Tmin=(10,'K'), Tmax=(1065.55,'K')),
            NASAPolynomial(coeffs=[3.53379,-0.000473194,7.96714e-07,-2.85788e-10,3.28969e-14,-33825.3,0.875745], Tmin=(1065.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-281.407,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7664-39-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 50,
    label = "FO2_49",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98128,0.00106957,1.84169e-05,-3.64541e-08,2.09777e-11,1684.47,7.38473], Tmin=(10,'K'), Tmax=(596.13,'K')),
            NASAPolynomial(coeffs=[3.96917,0.0056131,-4.24377e-06,1.44459e-09,-1.81883e-13,1606.63,6.77185], Tmin=(596.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.9974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 15499-23-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 51,
    label = "C2F2_384",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 F u0 p3 c0 {1,S}
3 F u0 p3 c0 {1,S}
4 C u0 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00213,-0.00165095,6.73679e-05,-1.5054e-07,1.03791e-10,14242,7.56796], Tmin=(10,'K'), Tmax=(489.118,'K')),
            NASAPolynomial(coeffs=[3.95417,0.0108266,-7.96021e-06,2.64862e-09,-3.27184e-13,14102.1,6.28724], Tmin=(489.118,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.404,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 41895-33-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 52,
    label = "C2H2O_373",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10094,-0.00708116,5.40246e-05,-7.04153e-08,2.98409e-11,23913.6,6.21349], Tmin=(10,'K'), Tmax=(738.516,'K')),
            NASAPolynomial(coeffs=[1.54957,0.0154231,-9.32463e-06,2.69531e-09,-2.98973e-13,24053.5,16.1454], Tmin=(738.516,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.847,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 50983-85-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 53,
    label = "CHClF_416",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98281,0.000953962,2.74264e-05,-4.72954e-08,2.48139e-11,-9540.43,8.44098], Tmin=(10,'K'), Tmax=(604.669,'K')),
            NASAPolynomial(coeffs=[3.02033,0.0112887,-8.05394e-06,2.67488e-09,-3.33076e-13,-9496.57,12.0004], Tmin=(604.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.3318,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 54,
    label = "F_66",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,8799.92,3.94355], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,8799.92,3.94355], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.1667,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 14762-94-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 55,
    label = "C4H9_376",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61506,0.0391645,-9.64569e-05,2.46339e-07,-2.05866e-10,3697.79,4.41845], Tmin=(10,'K'), Tmax=(457.808,'K')),
            NASAPolynomial(coeffs=[-0.444623,0.0460843,-2.55835e-05,6.90967e-09,-7.29308e-13,4368.69,24.0999], Tmin=(457.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.7399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1605-73-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 56,
    label = "HN_37",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49648,0.000242666,-1.49771e-06,2.69076e-09,-1.21481e-12,42108.2,1.82705], Tmin=(10,'K'), Tmax=(866.175,'K')),
            NASAPolynomial(coeffs=[3.30253,0.000102203,5.39834e-07,-2.58482e-10,3.50118e-14,42180.7,2.95924], Tmin=(866.175,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (350.107,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 13774-92-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 57,
    label = "C2H2F2_185",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10255,-0.0102379,0.000125258,-2.37169e-07,1.45117e-10,-43644.6,7.78202], Tmin=(10,'K'), Tmax=(528.913,'K')),
            NASAPolynomial(coeffs=[2.57833,0.0199536,-1.3297e-05,4.19009e-09,-5.00552e-13,-43744.4,11.6968], Tmin=(528.913,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-362.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-38-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 58,
    label = "C8H8_225",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {9,S}
5  C u0 p0 c0 {2,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u0 p0 c0 {3,D} {6,S} {13,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91189,0.00523416,0.000185614,-3.35573e-07,1.90656e-10,15375.3,11.5394], Tmin=(10,'K'), Tmax=(531.966,'K')),
            NASAPolynomial(coeffs=[-2.57333,0.0707704,-4.64732e-05,1.45497e-08,-1.73875e-12,15827.9,36.503], Tmin=(531.966,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.803,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 100-42-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 59,
    label = "HNO2_394",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07366,-0.00495545,3.61841e-05,-4.52865e-08,1.829e-11,31313.2,5.74627], Tmin=(10,'K'), Tmax=(782.274,'K')),
            NASAPolynomial(coeffs=[2.24023,0.0109371,-6.78723e-06,1.98501e-09,-2.20891e-13,31400.7,12.8666], Tmin=(782.274,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (260.369,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 67394-35-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 60,
    label = "CH2_172",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00384,-0.000193176,3.21038e-06,-2.19456e-09,4.45663e-13,45888.6,0.613965], Tmin=(10,'K'), Tmax=(894.78,'K')),
            NASAPolynomial(coeffs=[3.25815,0.0026203,-6.34356e-07,2.0501e-11,8.24935e-15,46042.9,4.24489], Tmin=(894.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (381.541,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2465-56-7*1 and used to tweak g4 calculation
""",
)

entry(
    index = 61,
    label = "CHO2_9",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0778,-0.00579699,4.74285e-05,-6.7586e-08,3.10683e-11,24456.7,6.3518], Tmin=(10,'K'), Tmax=(695.542,'K')),
            NASAPolynomial(coeffs=[2.57679,0.0112183,-7.34542e-06,2.24242e-09,-2.5864e-13,24462.7,11.5907], Tmin=(695.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.354,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 120595-16-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 62,
    label = "C4H6O4_67",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {13,S}
2  O u0 p2 c0 {8,S} {14,S}
3  O u0 p2 c0 {7,D}
4  O u0 p2 c0 {8,D}
5  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {3,D} {5,S}
8  C u0 p0 c0 {2,S} {4,D} {6,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61006,0.0427247,-2.91373e-06,-2.39916e-08,1.15272e-11,-101260,12.7983], Tmin=(10,'K'), Tmax=(953.295,'K')),
            NASAPolynomial(coeffs=[7.72023,0.040319,-2.24797e-05,6.02174e-09,-6.26346e-13,-102718,-10.3712], Tmin=(953.295,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-841.918,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 110-15-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 63,
    label = "HNO_304",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01469,-0.00081302,2.54228e-06,3.14308e-09,-3.64334e-12,11677.1,3.73606], Tmin=(10,'K'), Tmax=(682.176,'K')),
            NASAPolynomial(coeffs=[2.5719,0.00437644,-1.67726e-06,2.38891e-10,-3.52186e-15,11950.1,10.7026], Tmin=(682.176,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (97.0952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 14332-28-6*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 64,
    label = "HNO_372",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01647,-0.00103118,4.45811e-06,2.04491e-09,-4.76956e-12,24680.7,3.72367], Tmin=(10,'K'), Tmax=(570.903,'K')),
            NASAPolynomial(coeffs=[2.8051,0.00445365,-2.06387e-06,4.48637e-10,-3.64752e-14,24868,9.31733], Tmin=(570.903,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (205.212,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 35337-59-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 65,
    label = "C4H8_30",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06724,-0.00556562,0.000131779,-2.00838e-07,9.91655e-11,1168.66,7.20619], Tmin=(10,'K'), Tmax=(604.365,'K')),
            NASAPolynomial(coeffs=[-1.94437,0.0463548,-2.71962e-05,7.74176e-09,-8.55195e-13,1673.72,31.3483], Tmin=(604.365,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.71404,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 594-11-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 66,
    label = "C8H10_217",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {6,S} {14,S}
5  C u0 p0 c0 {3,S} {8,D} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {8,S} {16,S}
8  C u0 p0 c0 {5,D} {7,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93337,0.00429575,0.000219206,-4.19242e-07,2.61383e-10,981.642,11.059], Tmin=(10,'K'), Tmax=(412.37,'K')),
            NASAPolynomial(coeffs=[-3.69683,0.0782586,-4.96513e-05,1.51164e-08,-1.7682e-12,1611.36,41.1164], Tmin=(412.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.1481,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 100-41-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 67,
    label = "CF2O_46",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06766,-0.00622841,6.91781e-05,-1.22323e-07,6.91125e-11,-74279.9,7.68732], Tmin=(10,'K'), Tmax=(578.83,'K')),
            NASAPolynomial(coeffs=[3.20722,0.0116973,-8.31977e-06,2.69079e-09,-3.24498e-13,-74380.9,9.63444], Tmin=(578.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-617.604,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 353-50-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 68,
    label = "C5H12_243",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80981,0.0134177,0.000148249,-3.06564e-07,2.05853e-10,-22676.8,2.58799], Tmin=(10,'K'), Tmax=(380.645,'K')),
            NASAPolynomial(coeffs=[-0.52859,0.0590084,-3.14123e-05,8.1026e-09,-8.17445e-13,-22346.5,19.3278], Tmin=(380.645,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.599,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 463-82-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 69,
    label = "C2F2_232",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37115,0.00991965,6.47499e-05,-2.53757e-07,2.51172e-10,-950.844,6.86752], Tmin=(10,'K'), Tmax=(388.799,'K')),
            NASAPolynomial(coeffs=[5.58915,0.00758024,-5.23531e-06,1.72305e-09,-2.16222e-13,-1278.1,-3.72834], Tmin=(388.799,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.89744,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 689-99-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 70,
    label = "C2H4O_36",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97569,0.00127485,4.37313e-05,-6.4387e-08,3.05587e-11,-21432.8,5.96385], Tmin=(10,'K'), Tmax=(545.176,'K')),
            NASAPolynomial(coeffs=[1.25146,0.0212635,-1.12674e-05,2.87044e-09,-2.84492e-13,-21135.8,17.454], Tmin=(545.176,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-07-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 71,
    label = "CH2BrF_31",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01514,-0.00138282,4.5385e-05,-7.57192e-08,4.05717e-11,-26951.1,9.3695], Tmin=(10,'K'), Tmax=(572.471,'K')),
            NASAPolynomial(coeffs=[2.49749,0.0142359,-8.67845e-06,2.54095e-09,-2.86772e-13,-26859.5,15.1271], Tmin=(572.471,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-224.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 373-52-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 72,
    label = "C6H5Br_241",
    molecule = 
"""
1  Br u0 p3 c0 {2,S}
2  C  u0 p0 c0 {1,S} {3,D} {7,S}
3  C  u0 p0 c0 {2,D} {4,S} {8,S}
4  C  u0 p0 c0 {3,S} {5,D} {9,S}
5  C  u0 p0 c0 {4,D} {6,S} {10,S}
6  C  u0 p0 c0 {5,S} {7,D} {11,S}
7  C  u0 p0 c0 {2,S} {6,D} {12,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91752,0.00476511,0.00013734,-2.47902e-07,1.37808e-10,10413.9,11.2705], Tmin=(10,'K'), Tmax=(566.386,'K')),
            NASAPolynomial(coeffs=[-0.194222,0.0518288,-3.50397e-05,1.11871e-08,-1.35445e-12,10590.6,26.2175], Tmin=(566.386,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.5507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 108-86-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 73,
    label = "C2H4Br2_156",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 Br u0 p3 c0 {2,S}
4 Br u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91383,0.00742795,0.000123652,-4.12903e-07,4.33631e-10,-6342.54,11.1249], Tmin=(10,'K'), Tmax=(306.693,'K')),
            NASAPolynomial(coeffs=[3.39171,0.0250602,-1.55175e-05,4.67314e-09,-5.44739e-13,-6361.41,12.197], Tmin=(306.693,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-52.7171,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 557-91-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 74,
    label = "C3H_283",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 C u1 p1 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44655,0.00383739,4.01296e-05,-1.20799e-07,1.02455e-10,85516,6.44901], Tmin=(10,'K'), Tmax=(425.7,'K')),
            NASAPolynomial(coeffs=[4.13707,0.00688707,-4.22464e-06,1.29416e-09,-1.55372e-13,85370.8,2.69227], Tmin=(425.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (711.019,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 53590-28-6*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 75,
    label = "C2F4_104",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,D}
6 C u0 p0 c0 {3,S} {4,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86405,0.00926915,9.29342e-05,-2.55475e-07,1.95867e-10,-83108.1,9.05975], Tmin=(10,'K'), Tmax=(468.153,'K')),
            NASAPolynomial(coeffs=[5.46985,0.0191373,-1.4263e-05,4.80436e-09,-6.00337e-13,-83516.9,-0.229281], Tmin=(468.153,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-691.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 116-14-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 76,
    label = "C7H7_218",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u1 p0 c0 {1,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  C u0 p0 c0 {1,D} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14242,-0.0144988,0.000265499,-4.83852e-07,2.82512e-10,23316.4,10.5044], Tmin=(10,'K'), Tmax=(547.822,'K')),
            NASAPolynomial(coeffs=[-0.59819,0.0581298,-3.7454e-05,1.14931e-08,-1.3457e-12,23265.4,25.3159], Tmin=(547.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2154-56-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 77,
    label = "HNO4_371",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p3 c-1 {5,S}
4 O u0 p2 c0 {5,D}
5 N u0 p0 c+1 {1,S} {3,S} {4,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91798,0.00547117,7.49765e-05,-1.82552e-07,1.3058e-10,-8147.77,9.40813], Tmin=(10,'K'), Tmax=(477.823,'K')),
            NASAPolynomial(coeffs=[4.0351,0.0190387,-1.32844e-05,4.30913e-09,-5.24879e-13,-8325.03,7.19178], Tmin=(477.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-67.7599,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 26404-66-0*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 78,
    label = "CBrClF2_191",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85898,0.00950447,8.10387e-05,-2.35227e-07,1.82532e-10,-55093.3,11.8165], Tmin=(10,'K'), Tmax=(478.391,'K')),
            NASAPolynomial(coeffs=[6.45095,0.0132875,-1.06392e-05,3.75964e-09,-4.85645e-13,-55632.5,-1.82155], Tmin=(478.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-458.096,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 353-59-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 79,
    label = "CBr3F_302",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73975,0.0208876,7.32384e-05,-3.44716e-07,3.57757e-10,-17968.2,12.912], Tmin=(10,'K'), Tmax=(386.07,'K')),
            NASAPolynomial(coeffs=[7.57437,0.0117039,-9.76043e-06,3.54405e-09,-4.66422e-13,-18492,-4.88649], Tmin=(386.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.382,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 353-54-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 80,
    label = "CH2Cl_127",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86518,0.0138948,-5.43045e-05,1.17033e-07,-8.73094e-11,12383.1,6.11963], Tmin=(10,'K'), Tmax=(450.56,'K')),
            NASAPolynomial(coeffs=[3.70579,0.00697806,-3.53911e-06,8.75569e-10,-8.48969e-14,12482.1,7.7], Tmin=(450.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 6806-86-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 81,
    label = "C3H7_88",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89269,0.0134197,2.22897e-05,-3.0062e-08,1.03096e-11,10242.2,6.37083], Tmin=(10,'K'), Tmax=(1007.32,'K')),
            NASAPolynomial(coeffs=[2.42344,0.028691,-1.45035e-05,3.58881e-09,-3.5012e-13,10059.4,11.0933], Tmin=(1007.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (85.1725,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2143-61-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 82,
    label = "CCl2_190",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96315,0.00218,2.45971e-05,-5.68397e-08,3.60132e-11,26343.5,8.03259], Tmin=(10,'K'), Tmax=(576.667,'K')),
            NASAPolynomial(coeffs=[4.79073,0.0048188,-4.06239e-06,1.48987e-09,-1.97777e-13,26108.8,3.28759], Tmin=(576.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1605-72-7*2 and used to tweak g4 calculation
""",
)

entry(
    index = 83,
    label = "C6H5F_223",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {2,S} {6,D} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14324,-0.0137404,0.000225507,-3.97373e-07,2.23792e-10,-15736.8,9.8972], Tmin=(10,'K'), Tmax=(569.791,'K')),
            NASAPolynomial(coeffs=[-0.0970643,0.0502039,-3.28013e-05,1.01214e-08,-1.18696e-12,-15808.4,23.1007], Tmin=(569.791,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 462-06-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 84,
    label = "C2H3F2_422",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 F u0 p3 c0 {2,S}
7 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96282,0.00244812,7.53666e-05,-1.58546e-07,1.0608e-10,-37556.9,7.51131], Tmin=(10,'K'), Tmax=(455.058,'K')),
            NASAPolynomial(coeffs=[2.31768,0.0233385,-1.46873e-05,4.43237e-09,-5.14311e-13,-37473.7,13.4215], Tmin=(455.058,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-312.272,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 85,
    label = "C2H5O_176",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96617,0.00229828,8.34901e-05,-1.78992e-07,1.24654e-10,-4889.31,7.05509], Tmin=(10,'K'), Tmax=(425.254,'K')),
            NASAPolynomial(coeffs=[2.15576,0.0246931,-1.44299e-05,4.18791e-09,-4.77667e-13,-4783.85,13.6708], Tmin=(425.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.6541,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 4422-54-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 86,
    label = "C2H2Cl4_279",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 C  u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {2,S}
6 Cl u0 p3 c0 {2,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61398,0.0336277,8.11177e-06,-1.05837e-07,9.85361e-11,-21277.9,12.5652], Tmin=(10,'K'), Tmax=(469.803,'K')),
            NASAPolynomial(coeffs=[6.54062,0.0252305,-1.78254e-05,5.82052e-09,-7.12275e-13,-21735.2,-1.2837], Tmin=(469.803,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-176.942,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 79-34-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 87,
    label = "N2O_303",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99101,0.000504706,1.44978e-05,-2.53932e-08,1.3551e-11,40787.3,5.23297], Tmin=(10,'K'), Tmax=(593.013,'K')),
            NASAPolynomial(coeffs=[3.50056,0.0058468,-4.15957e-06,1.36516e-09,-1.67979e-13,40809.7,7.04127], Tmin=(593.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (339.121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 227934-45-4*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 88,
    label = "CHBr3_226",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Br u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79369,0.0176551,3.53647e-05,-1.90554e-07,2.02761e-10,3887.19,12.782], Tmin=(10,'K'), Tmax=(381.082,'K')),
            NASAPolynomial(coeffs=[5.93144,0.0120687,-8.98032e-06,3.06822e-09,-3.89413e-13,3601.89,2.92541], Tmin=(381.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (32.3295,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-25-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 89,
    label = "C6H4_5",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,D} {7,S}
2  C u0 p0 c0 {1,S} {6,D} {8,S}
3  C u0 p0 c0 {4,D} {6,S} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u1 p0 c0 {1,D} {4,S}
6  C u1 p0 c0 {2,D} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.179,-0.0157765,0.000193274,-3.24815e-07,1.7551e-10,67777.4,9.19536], Tmin=(10,'K'), Tmax=(593.083,'K')),
            NASAPolynomial(coeffs=[0.186636,0.0412357,-2.70109e-05,8.3339e-09,-9.75886e-13,67721.8,21.9097], Tmin=(593.083,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (563.522,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3355-34-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 90,
    label = "CHBrF2_146",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95348,0.00280792,5.11833e-05,-1.06308e-07,6.56237e-11,-52552.9,10.5093], Tmin=(10,'K'), Tmax=(545.035,'K')),
            NASAPolynomial(coeffs=[3.67306,0.0150438,-1.05018e-05,3.40439e-09,-4.15083e-13,-52673.6,10.3051], Tmin=(545.035,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-436.967,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1511-62-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 91,
    label = "C5H8_128",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {2,S} {4,D} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12828,-0.00978698,0.00015541,-2.2329e-07,1.03093e-10,2446.75,8.62207], Tmin=(10,'K'), Tmax=(665.115,'K')),
            NASAPolynomial(coeffs=[-3.1857,0.0538418,-3.23873e-05,9.34763e-09,-1.0392e-12,2985.21,37.659], Tmin=(665.115,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.3531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 142-29-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 92,
    label = "CBr2F2_116",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82683,0.0125363,8.23574e-05,-2.77888e-07,2.41095e-10,-48149.5,12.0794], Tmin=(10,'K'), Tmax=(435.999,'K')),
            NASAPolynomial(coeffs=[6.67761,0.0129426,-1.04182e-05,3.69235e-09,-4.77691e-13,-48650.5,-2.20259], Tmin=(435.999,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-400.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-61-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 93,
    label = "C3H4_167",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98144,0.00125414,6.44955e-05,-1.30663e-07,8.79502e-11,20744.5,4.89563], Tmin=(10,'K'), Tmax=(379.414,'K')),
            NASAPolynomial(coeffs=[2.15142,0.0205488,-1.17913e-05,3.39107e-09,-3.86533e-13,20883.4,11.9507], Tmin=(379.414,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.479,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-99-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 94,
    label = "C4H8_174",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90749,0.00647551,9.11171e-05,-1.5712e-07,8.67654e-11,-4036.17,5.66935], Tmin=(10,'K'), Tmax=(467.498,'K')),
            NASAPolynomial(coeffs=[-0.269461,0.0422143,-2.35531e-05,6.40361e-09,-6.80604e-13,-3645.63,22.6447], Tmin=(467.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.5861,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 115-11-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 95,
    label = "C2HF_228",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46088,0.00241107,3.25333e-05,-7.45688e-08,4.92793e-11,11405.2,5.99676], Tmin=(10,'K'), Tmax=(535.784,'K')),
            NASAPolynomial(coeffs=[3.99989,0.00700001,-4.42729e-06,1.42421e-09,-1.79466e-13,11223.8,2.57907], Tmin=(535.784,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (94.8155,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2713-09-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 96,
    label = "HNO2_345",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05888,-0.00486503,4.69649e-05,-7.45234e-08,3.84528e-11,-10739.8,6.45335], Tmin=(10,'K'), Tmax=(615.585,'K')),
            NASAPolynomial(coeffs=[2.89527,0.00982643,-6.20879e-06,1.87926e-09,-2.1748e-13,-10731.7,10.4052], Tmin=(615.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.2949,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 7782-77-6*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 97,
    label = "C2H2O_240",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 O u0 p2 c0 {1,S} {5,S}
3 C u0 p0 c0 {1,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94869,0.00314102,4.51698e-05,-1.00739e-07,6.54582e-11,9614.48,5.20258], Tmin=(10,'K'), Tmax=(539.948,'K')),
            NASAPolynomial(coeffs=[4.52865,0.010263,-6.33591e-06,2.01896e-09,-2.53386e-13,9385.4,1.22069], Tmin=(539.948,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.9217,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 32038-79-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 98,
    label = "C2H5O2_426",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92536,0.0119594,2.59019e-05,-3.70831e-08,1.38274e-11,-5043.85,7.99771], Tmin=(10,'K'), Tmax=(929.737,'K')),
            NASAPolynomial(coeffs=[3.00802,0.0263315,-1.41053e-05,3.66475e-09,-3.72438e-13,-5323.87,9.9333], Tmin=(929.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.9128,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""Automated Thermochemistry Protocol Based on Explicitly Correlated Coupled-Cluster Theory-g4""",
    longDesc = 
u"""
H298 taken from Automated Thermochemistry Protocol Based on Explicitly Correlated Coupled-Cluster Theory  and used to tweak g4 calculation
""",
)

entry(
    index = 99,
    label = "C3H6O_301",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95588,0.00271961,0.000101057,-1.89422e-07,1.13295e-10,-22160.8,7.10363], Tmin=(10,'K'), Tmax=(499.187,'K')),
            NASAPolynomial(coeffs=[0.81512,0.0357853,-2.20367e-05,6.66769e-09,-7.84333e-13,-21945.6,19.0881], Tmin=(499.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-184.269,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 29456-04-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 100,
    label = "Cl2O_11",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95494,0.00277157,2.70036e-05,-6.83925e-08,4.65277e-11,7950.76,8.20118], Tmin=(10,'K'), Tmax=(546.312,'K')),
            NASAPolynomial(coeffs=[5.0637,0.00429904,-3.67417e-06,1.36213e-09,-1.82394e-13,7685.67,2.20499], Tmin=(546.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (66.0911,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7791-21-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 101,
    label = "C2Cl4_84",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {6,D}
6 C  u0 p0 c0 {3,S} {4,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70439,0.0233109,9.74499e-05,-4.13459e-07,4.108e-10,-5178.86,11.585], Tmin=(10,'K'), Tmax=(394.488,'K')),
            NASAPolynomial(coeffs=[7.92107,0.0165009,-1.3337e-05,4.75106e-09,-6.17509e-13,-5791.24,-8.38091], Tmin=(394.488,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.0472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 127-18-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 102,
    label = "N2_186",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50362,-0.000176566,1.12065e-07,1.39731e-09,-9.51439e-13,-1039.54,3.10326], Tmin=(10,'K'), Tmax=(807.109,'K')),
            NASAPolynomial(coeffs=[3.06755,0.000928663,2.04148e-08,-1.47916e-10,2.92707e-14,-934.752,5.32665], Tmin=(807.109,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.6419,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 15626-42-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 103,
    label = "C2HF_332",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 F u0 p3 c0 {1,S}
3 C u0 p1 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9715,0.00243035,2.17734e-05,-4.70162e-08,3.2027e-11,34675.8,6.33398], Tmin=(10,'K'), Tmax=(378.507,'K')),
            NASAPolynomial(coeffs=[3.30991,0.00942199,-5.93414e-06,1.7856e-09,-2.06188e-13,34725.9,8.88303], Tmin=(378.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (288.31,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 70302-00-0*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 104,
    label = "C2H3Br_90",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06068,-0.00628366,9.45114e-05,-1.81505e-07,1.14408e-10,7416.59,9.05043], Tmin=(10,'K'), Tmax=(495.466,'K')),
            NASAPolynomial(coeffs=[2.33165,0.0181479,-1.116e-05,3.34059e-09,-3.86268e-13,7459.37,14.8805], Tmin=(495.466,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.6586,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-60-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 105,
    label = "HO_148",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4968,0.000191524,-1.05694e-06,1.69321e-09,-6.72278e-13,3464.64,1.48207], Tmin=(10,'K'), Tmax=(966.629,'K')),
            NASAPolynomial(coeffs=[3.43201,-0.00024674,7.19308e-07,-2.87832e-10,3.56041e-14,3510.16,1.96316], Tmin=(966.629,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (28.8056,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3352-57-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 106,
    label = "C3H5O2_287",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u1 p0 c0 {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96658,0.00517873,0.000490089,-4.04636e-06,1.16962e-08,-28087.6,4.81102], Tmin=(10,'K'), Tmax=(102.126,'K')),
            NASAPolynomial(coeffs=[3.46774,0.0322915,-1.93855e-05,5.64262e-09,-6.36189e-13,-28081.4,5.88615], Tmin=(102.126,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-225.692,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2887-49-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 107,
    label = "CH4O2_6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04236,-0.00406752,8.21064e-05,-1.44378e-07,8.3622e-11,-48743.5,6.37564], Tmin=(10,'K'), Tmax=(517.708,'K')),
            NASAPolynomial(coeffs=[1.61369,0.0216657,-1.26429e-05,3.63244e-09,-4.071e-13,-48585.4,15.5918], Tmin=(517.708,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-405.281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 463-57-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 108,
    label = "ClHO2_92",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95609,0.00261318,3.53207e-05,-7.76047e-08,4.86272e-11,-1636.33,7.83371], Tmin=(10,'K'), Tmax=(566.522,'K')),
            NASAPolynomial(coeffs=[4.5902,0.00814335,-5.81863e-06,1.98757e-09,-2.55714e-13,-1868.77,3.71748], Tmin=(566.522,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-13.6222,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67952-07-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 109,
    label = "C4H8O_357",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63456,0.0388947,-9.01777e-05,2.53876e-07,-2.33916e-10,-31080.5,8.23872], Tmin=(10,'K'), Tmax=(421.758,'K')),
            NASAPolynomial(coeffs=[-0.0222892,0.0474205,-2.74746e-05,7.71805e-09,-8.43057e-13,-30539.4,25.4817], Tmin=(421.758,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-258.429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 78-93-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 110,
    label = "C2Cl2_330",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,D}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 C  u0 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79558,0.0179875,-1.92214e-05,-2.69241e-09,1.30515e-11,49330.6,9.78539], Tmin=(10,'K'), Tmax=(506.913,'K')),
            NASAPolynomial(coeffs=[5.82502,0.00770847,-5.7752e-06,1.94259e-09,-2.41595e-13,49051.2,0.646564], Tmin=(506.913,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (410.14,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 20394-25-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 111,
    label = "C3H5_162",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97296,0.00157187,6.32372e-05,-1.06055e-07,5.77231e-11,30507.1,6.26806], Tmin=(10,'K'), Tmax=(474.201,'K')),
            NASAPolynomial(coeffs=[1.02855,0.0264068,-1.53152e-05,4.37155e-09,-4.89528e-13,30786.4,18.2765], Tmin=(474.201,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (253.638,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 6067-68-1*2 and used to tweak g4 calculation
""",
)

entry(
    index = 112,
    label = "C6H10_349",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84727,0.0283045,3.71851e-05,-5.63335e-08,2.02604e-11,7447.87,9.91618], Tmin=(10,'K'), Tmax=(1004.5,'K')),
            NASAPolynomial(coeffs=[4.07907,0.0487876,-2.53674e-05,6.39628e-09,-6.31832e-13,6321.35,3.42125], Tmin=(1004.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.9865,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 592-42-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 113,
    label = "ClHO_193",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02913,-0.00248343,2.30292e-05,-3.83294e-08,2.09403e-11,-10465.7,5.498], Tmin=(10,'K'), Tmax=(584.654,'K')),
            NASAPolynomial(coeffs=[3.60189,0.00390929,-2.27405e-06,6.73938e-10,-7.81407e-14,-10475,6.82272], Tmin=(584.654,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.0169,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7790-92-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 114,
    label = "C2HF3_85",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92948,0.00430692,7.13505e-05,-1.53481e-07,9.72126e-11,-60391.5,9.51278], Tmin=(10,'K'), Tmax=(538.23,'K')),
            NASAPolynomial(coeffs=[3.90961,0.0196612,-1.38202e-05,4.50662e-09,-5.52253e-13,-60609.6,7.55016], Tmin=(538.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-502.148,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 359-11-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 115,
    label = "CHBr2F_153",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89833,0.00736524,6.35626e-05,-1.89698e-07,1.57122e-10,-23338.1,12.3696], Tmin=(10,'K'), Tmax=(433.781,'K')),
            NASAPolynomial(coeffs=[4.88556,0.0133948,-9.61668e-06,3.19314e-09,-3.96563e-13,-23566.2,6.79023], Tmin=(433.781,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1868-53-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 116,
    label = "C7H7_252",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {5,D} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u1 p0 c0 {5,S} {6,S} {8,S}
5  C u0 p0 c0 {2,D} {4,S} {10,S}
6  C u0 p0 c0 {3,D} {4,S} {11,S}
7  C u0 p0 c0 {1,D} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14242,-0.0144988,0.000265499,-4.83852e-07,2.82512e-10,23316.4,9.81124], Tmin=(10,'K'), Tmax=(547.822,'K')),
            NASAPolynomial(coeffs=[-0.59819,0.0581298,-3.7454e-05,1.14931e-08,-1.3457e-12,23265.4,24.6228], Tmin=(547.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2154-56-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 117,
    label = "C2F5_417",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u1 p0 c0 {4,S} {5,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73136,0.0237064,3.09072e-05,-1.07109e-07,7.27851e-11,-110357,10.614], Tmin=(10,'K'), Tmax=(581.082,'K')),
            NASAPolynomial(coeffs=[6.77498,0.0224032,-1.64482e-05,5.41129e-09,-6.5966e-13,-111043,-5.2717], Tmin=(581.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-917.606,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

# entry(
#     index = 118,
#     label = "CHBrClF_22",
#     molecule = 
# """
# 1 Br u0 p3 c0 {4,S}
# 2 Cl u0 p3 c0 {4,S}
# 3 F  u0 p3 c0 {4,S}
# 4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
# 5 H  u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.9225,0.00508781,6.16155e-05,-1.5542e-07,1.11993e-10,-29551.6,inf], Tmin=(10,'K'), Tmax=(489.806,'K')),
#             NASAPolynomial(coeffs=[4.68986,0.0135944,-9.67796e-06,3.19523e-09,-3.95555e-13,-29804,inf], Tmin=(489.806,'K'), Tmax=(3000,'K')),
#         ],
#         Tmin = (10,'K'),
#         Tmax = (3000,'K'),
#         E0 = (-245.723,'kJ/mol'),
#         Cp0 = (33.2579,'J/(mol*K)'),
#         CpInf = (108.088,'J/(mol*K)'),
#     ),
#     shortDesc = u"""atct-g4""",
#     longDesc = 
# u"""
# H298 taken from atct 593-98-6*0 and used to tweak g4 calculation
# """,
# )

entry(
    index = 119,
    label = "C3H6O_121",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.913,0.0172422,1.29732e-05,-2.04491e-08,6.73294e-12,-28090,5.81656], Tmin=(10,'K'), Tmax=(1143.51,'K')),
            NASAPolynomial(coeffs=[5.09497,0.0245749,-1.16876e-05,2.69788e-09,-2.44859e-13,-29110,-3.32244], Tmin=(1143.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-233.526,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67-64-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 120,
    label = "C7H12_296",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98296,0.000465765,0.000206541,-3.45244e-07,1.88135e-10,-3532.99,10.656], Tmin=(10,'K'), Tmax=(473.469,'K')),
            NASAPolynomial(coeffs=[-5.54991,0.081002,-4.86058e-05,1.40155e-08,-1.56019e-12,-2630.29,49.5192], Tmin=(473.469,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.3934,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (457.296,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 628-92-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 121,
    label = "CHNO_374",
    molecule = 
"""
1 N u0 p0 c+1 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46893,0.00189916,2.98061e-05,-6.48822e-08,4.16489e-11,19108.7,5.80891], Tmin=(10,'K'), Tmax=(538.77,'K')),
            NASAPolynomial(coeffs=[3.67255,0.00730618,-4.51046e-06,1.41613e-09,-1.74953e-13,18986.3,4.02056], Tmin=(538.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (158.868,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 51060-05-0*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 122,
    label = "CBr2O_206",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89185,0.00771813,5.60166e-05,-1.86994e-07,1.61653e-10,-15405.3,11.4818], Tmin=(10,'K'), Tmax=(438.843,'K')),
            NASAPolynomial(coeffs=[5.93564,0.00743002,-5.68891e-06,1.98156e-09,-2.55946e-13,-15761.3,1.29284], Tmin=(438.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.094,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-95-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 123,
    label = "C3H3_89",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11607,-0.00985615,9.42006e-05,-1.52737e-07,8.12947e-11,61562.2,6.94084], Tmin=(10,'K'), Tmax=(589.355,'K')),
            NASAPolynomial(coeffs=[1.6996,0.0191685,-1.18011e-05,3.51494e-09,-4.03066e-13,61627.8,15.4613], Tmin=(589.355,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (511.857,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 19528-44-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 124,
    label = "C7H7_318",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {1,S} {6,D} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9048,0.00566342,0.000164171,-3.06435e-07,1.77667e-10,31117.1,11.2566], Tmin=(10,'K'), Tmax=(540.134,'K')),
            NASAPolynomial(coeffs=[-0.531808,0.0585261,-3.8195e-05,1.19145e-08,-1.42108e-12,31304.5,27.2264], Tmin=(540.134,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (258.685,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3551-27-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 125,
    label = "C2H3O_188",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13191,-0.00958909,7.61556e-05,-1.03496e-07,4.58411e-11,18465.9,7.13683], Tmin=(10,'K'), Tmax=(706.218,'K')),
            NASAPolynomial(coeffs=[0.920838,0.020339,-1.23485e-05,3.59162e-09,-4.01203e-13,18626.7,19.4386], Tmin=(706.218,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 31586-84-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 126,
    label = "C3H2_275",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,D}
2 C u1 p0 c0 {1,D} {4,S}
3 C u1 p0 c0 {1,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47279,0.00192978,2.92461e-05,-8.00543e-08,6.58042e-11,64466.3,6.25753], Tmin=(10,'K'), Tmax=(423.379,'K')),
            NASAPolynomial(coeffs=[3.70526,0.00528056,-2.27863e-06,5.32247e-10,-5.47378e-14,64396.9,4.74864], Tmin=(423.379,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (536.002,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67152-18-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 127,
    label = "FNO_311",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02874,-0.00307456,3.66874e-05,-7.17273e-08,4.54911e-11,-11873.2,6.55129], Tmin=(10,'K'), Tmax=(507.791,'K')),
            NASAPolynomial(coeffs=[3.57903,0.00555815,-3.84968e-06,1.23369e-09,-1.48616e-13,-11893.2,7.76994], Tmin=(507.791,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-98.7232,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 7789-25-5*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 128,
    label = "CO2_124",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53657,-0.00353816,3.90447e-05,-7.01716e-08,4.12669e-11,-48446.3,5.39237], Tmin=(10,'K'), Tmax=(535.859,'K')),
            NASAPolynomial(coeffs=[2.76503,0.00715735,-4.71233e-06,1.45771e-09,-1.71219e-13,-48434.4,7.97198], Tmin=(535.859,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-402.808,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 124-38-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 129,
    label = "C2F6_68",
    molecule = 
"""
1 F u0 p3 c0 {7,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {8,S}
6 F u0 p3 c0 {8,S}
7 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7256,0.0223273,8.30893e-05,-2.3804e-07,1.70565e-10,-163995,9.33803], Tmin=(10,'K'), Tmax=(519.533,'K')),
            NASAPolynomial(coeffs=[6.80705,0.0285776,-2.15007e-05,7.22451e-09,-8.96134e-13,-164720,-7.40361], Tmin=(519.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1363.58,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 76-16-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 130,
    label = "CHBr2Cl_16",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84846,0.011711,6.21012e-05,-2.25167e-07,2.07771e-10,-1892.42,13.0305], Tmin=(10,'K'), Tmax=(408.564,'K')),
            NASAPolynomial(coeffs=[5.67782,0.0124756,-9.26825e-06,3.1637e-09,-4.01093e-13,-2197.77,3.93495], Tmin=(408.564,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.7328,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 124-48-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 131,
    label = "CHBrCl2_109",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8863,0.00796819,6.97293e-05,-2.07913e-07,1.68992e-10,-7737.99,12.0907], Tmin=(10,'K'), Tmax=(450.559,'K')),
            NASAPolynomial(coeffs=[5.52646,0.0125401,-9.18914e-06,3.10769e-09,-3.91816e-13,-8079.99,3.33035], Tmin=(450.559,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-64.3486,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-27-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 132,
    label = "C4H8_69",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83092,0.0146413,4.04023e-05,-5.67015e-08,2.19748e-11,-3408.13,5.45794], Tmin=(10,'K'), Tmax=(824.735,'K')),
            NASAPolynomial(coeffs=[0.0511465,0.041063,-2.23657e-05,5.9295e-09,-6.15568e-13,-3059.79,21.2969], Tmin=(824.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-28.3471,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 624-64-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 133,
    label = "CClN_308",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 N  u0 p1 c0 {3,T}
3 C  u0 p0 c0 {1,S} {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48107,0.00117414,1.72123e-05,-3.89126e-08,2.56522e-11,15137.1,7.10641], Tmin=(10,'K'), Tmax=(528.432,'K')),
            NASAPolynomial(coeffs=[3.63864,0.00408032,-2.67223e-06,8.52422e-10,-1.05046e-13,15063.2,5.90524], Tmin=(528.432,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.851,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 506-77-4*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 134,
    label = "C5H12_154",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71911,0.0260443,4.58171e-05,-6.50026e-08,2.37092e-11,-20978.8,6.55305], Tmin=(10,'K'), Tmax=(922.897,'K')),
            NASAPolynomial(coeffs=[-0.330796,0.0584893,-3.11205e-05,8.05853e-09,-8.18316e-13,-20865.4,22.3306], Tmin=(922.897,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-174.433,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 78-78-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 135,
    label = "C3H6_263",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96607,0.00206579,7.71004e-05,-1.38052e-07,8.1067e-11,34795,4.02606], Tmin=(10,'K'), Tmax=(436.901,'K')),
            NASAPolynomial(coeffs=[0.994748,0.0292694,-1.62968e-05,4.46305e-09,-4.81515e-13,35054.6,15.9006], Tmin=(436.901,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-mn15_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 40852-89-9*0 and used to tweak mn15_jun-cc-pvtz calculation
""",
)

entry(
    index = 136,
    label = "N_327",
    molecule = 
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,58176.4,4.17908], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,58176.4,4.17908], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (483.706,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 17778-87-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 137,
    label = "C4_338",
    molecule = 
"""
multiplicity 1
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 C u1 p0 c0 {1,D} {2,S}
4 C u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97281,0.00152649,3.39309e-05,-6.24657e-08,3.41681e-11,125451,5.48983], Tmin=(10,'K'), Tmax=(603.581,'K')),
            NASAPolynomial(coeffs=[3.31107,0.0124136,-9.283e-06,3.11135e-09,-3.85501e-13,125412,7.36715], Tmin=(603.581,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (1043.04,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12184-80-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 138,
    label = "CBrF3_219",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90289,0.00606441,7.01784e-05,-1.70303e-07,1.15396e-10,-80100.8,10.013], Tmin=(10,'K'), Tmax=(530.215,'K')),
            NASAPolynomial(coeffs=[5.39999,0.0148708,-1.16009e-05,4.02234e-09,-5.12228e-13,-80542.1,1.07585], Tmin=(530.215,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-666.026,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-63-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 139,
    label = "C2H3F3_420",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93064,0.00418297,9.11269e-05,-1.82024e-07,1.1044e-10,-92532,7.1485], Tmin=(10,'K'), Tmax=(539.526,'K')),
            NASAPolynomial(coeffs=[2.6558,0.0287298,-1.90866e-05,6.01988e-09,-7.23181e-13,-92614.1,10.4761], Tmin=(539.526,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-769.38,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 140,
    label = "O3_235",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p1 c+1 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04383,-0.0031318,2.56915e-05,-3.55092e-08,1.56098e-11,15816.7,6.33699], Tmin=(10,'K'), Tmax=(737.906,'K')),
            NASAPolynomial(coeffs=[3.2384,0.00648107,-4.51503e-06,1.41704e-09,-1.65304e-13,15792.7,9.01], Tmin=(737.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (131.515,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 10028-15-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 141,
    label = "Br2_17",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Br u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46735,0.00240462,1.27566e-05,-5.20328e-08,4.95597e-11,2540.73,8.84074], Tmin=(10,'K'), Tmax=(419.965,'K')),
            NASAPolynomial(coeffs=[4.22286,0.000681229,-6.34083e-07,2.52343e-10,-3.5824e-14,2429.01,5.27678], Tmin=(419.965,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.1245,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7726-95-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 142,
    label = "C5H10_74",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08136,-0.00607981,0.000150701,-2.09212e-07,9.31088e-11,-11111.4,9.45425], Tmin=(10,'K'), Tmax=(668.052,'K')),
            NASAPolynomial(coeffs=[-5.13247,0.0634036,-3.74549e-05,1.06289e-08,-1.16415e-12,-10199.8,47.7981], Tmin=(668.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.3785,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 287-92-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 143,
    label = "C2H5BrO_20",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90833,0.00765075,7.50697e-05,-1.64688e-07,1.15478e-10,-28422.2,10.7095], Tmin=(10,'K'), Tmax=(366.229,'K')),
            NASAPolynomial(coeffs=[1.82027,0.0304574,-1.83441e-05,5.36311e-09,-6.0736e-13,-28269.3,18.6857], Tmin=(366.229,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 540-51-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 144,
    label = "CHCl3_210",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9075,0.00601753,6.55765e-05,-1.69817e-07,1.22814e-10,-14051.3,9.95462], Tmin=(10,'K'), Tmax=(498.659,'K')),
            NASAPolynomial(coeffs=[5.3136,0.0128364,-9.37475e-06,3.1681e-09,-3.99892e-13,-14416.5,1.89324], Tmin=(498.659,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116.851,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67-66-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 145,
    label = "C3H2_149",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10371,-0.00769602,6.19183e-05,-8.67136e-08,3.95197e-11,58393.3,5.28739], Tmin=(10,'K'), Tmax=(691.536,'K')),
            NASAPolynomial(coeffs=[1.82991,0.0153428,-9.49961e-06,2.80963e-09,-3.18014e-13,58471.3,13.7092], Tmin=(691.536,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (485.522,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 16165-40-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 146,
    label = "C2HO_258",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97049,0.00177464,3.0158e-05,-6.31601e-08,3.92208e-11,20015.4,5.56497], Tmin=(10,'K'), Tmax=(550.4,'K')),
            NASAPolynomial(coeffs=[4.01778,0.00809053,-5.20382e-06,1.65453e-09,-2.03993e-13,19909.3,4.44872], Tmin=(550.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.406,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 51095-15-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 147,
    label = "C4H6_110",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {1,S} {3,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17928,-0.0135397,0.000137363,-1.95567e-07,9.04299e-11,17724.7,7.19773], Tmin=(10,'K'), Tmax=(671.115,'K')),
            NASAPolynomial(coeffs=[-1.51917,0.0395003,-2.38223e-05,6.90306e-09,-7.70432e-13,18059.9,29.2163], Tmin=(671.115,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.39,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 822-35-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 148,
    label = "C3H2O_360",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10516,-0.00979203,0.000111825,-1.98855e-07,1.14638e-10,17794.7,7.0465], Tmin=(10,'K'), Tmax=(555.793,'K')),
            NASAPolynomial(coeffs=[2.21694,0.0201648,-1.31971e-05,4.09299e-09,-4.82646e-13,17751.8,12.7727], Tmin=(555.793,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.945,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2961-80-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 149,
    label = "C3H3_250",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94032,0.00374182,5.95507e-05,-1.33429e-07,8.87796e-11,40622.9,6.20561], Tmin=(10,'K'), Tmax=(516.948,'K')),
            NASAPolynomial(coeffs=[4.23312,0.0143513,-8.59299e-06,2.62929e-09,-3.18758e-13,40420.6,3.32227], Tmin=(516.948,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (337.74,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2932-78-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 150,
    label = "C2H2O2_8",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88949,0.00954036,9.59244e-06,-1.70781e-08,6.75549e-12,-27191,7.36204], Tmin=(10,'K'), Tmax=(894.835,'K')),
            NASAPolynomial(coeffs=[3.35564,0.0163592,-9.26807e-06,2.50887e-09,-2.63264e-13,-27273,8.88666], Tmin=(894.835,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-226.086,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-22-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 151,
    label = "C2H5FO_158",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {3,S} {9,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96793,0.00195743,8.29935e-05,-1.4903e-07,8.71385e-11,-52617.7,8.83931], Tmin=(10,'K'), Tmax=(440.535,'K')),
            NASAPolynomial(coeffs=[0.668423,0.0319302,-1.91092e-05,5.55403e-09,-6.26751e-13,-52327.2,22.0512], Tmin=(440.535,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-437.501,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 371-62-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 152,
    label = "C4H6_238",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68418,0.0317029,-7.64244e-05,1.754e-07,-1.38786e-10,15494.7,5.80123], Tmin=(10,'K'), Tmax=(464.485,'K')),
            NASAPolynomial(coeffs=[1.47771,0.0320958,-1.75989e-05,4.71629e-09,-4.95412e-13,15900.4,16.915], Tmin=(464.485,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (128.825,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 503-17-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 153,
    label = "C2H2O_114",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97985,0.00119204,3.67749e-05,-6.71185e-08,3.84045e-11,-7277.44,4.89137], Tmin=(10,'K'), Tmax=(542.553,'K')),
            NASAPolynomial(coeffs=[2.9193,0.013238,-8.215e-06,2.52286e-09,-3.01891e-13,-7224.57,8.78609], Tmin=(542.553,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.5161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 463-51-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 154,
    label = "C6H6O_230",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {13,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {7,D} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {10,S}
7  C u0 p0 c0 {4,D} {6,S} {11,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12906,-0.0132766,0.000246926,-4.52411e-07,2.65004e-10,-13268.3,9.84621], Tmin=(10,'K'), Tmax=(548.14,'K')),
            NASAPolynomial(coeffs=[-0.0253804,0.0533109,-3.45494e-05,1.06478e-08,-1.25053e-12,-13357.8,22.4208], Tmin=(548.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.348,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 108-95-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 155,
    label = "CH2BrCl_140",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97095,0.00171544,4.14498e-05,-7.89722e-08,4.60594e-11,-6626.72,10.2809], Tmin=(10,'K'), Tmax=(554.336,'K')),
            NASAPolynomial(coeffs=[3.17793,0.0139115,-9.06991e-06,2.8525e-09,-3.44e-13,-6638.27,12.7417], Tmin=(554.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.1093,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-97-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 156,
    label = "H2O4_209",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90181,0.00614727,7.52371e-05,-1.80448e-07,1.2265e-10,-7165.4,8.43414], Tmin=(10,'K'), Tmax=(525.911,'K')),
            NASAPolynomial(coeffs=[5.37499,0.0156516,-1.09375e-05,3.66621e-09,-4.64636e-13,-7606.74,-0.44919], Tmin=(525.911,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-59.6066,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 29683-94-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 157,
    label = "CBrN_262",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 N  u0 p1 c0 {3,T}
3 C  u0 p0 c0 {1,S} {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47214,0.00181371,2.00166e-05,-5.23766e-08,3.83587e-11,20454.5,8.27852], Tmin=(10,'K'), Tmax=(495.894,'K')),
            NASAPolynomial(coeffs=[3.9724,0.00347602,-2.24566e-06,7.21241e-10,-9.04436e-14,20334.8,5.5096], Tmin=(495.894,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (170.062,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 506-68-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 158,
    label = "CH3ClO_4",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O  u0 p2 c0 {1,S} {6,S}
3 Cl u0 p3 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98403,0.000963587,4.70817e-05,-8.24271e-08,4.66535e-11,-30694.8,7.95712], Tmin=(10,'K'), Tmax=(458.236,'K')),
            NASAPolynomial(coeffs=[1.92667,0.0189642,-1.19781e-05,3.69447e-09,-4.40004e-13,-30506.7,16.2724], Tmin=(458.236,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-255.217,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 15454-33-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 159,
    label = "O2_135",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50748,-0.000447752,1.48307e-06,1.62059e-09,-2.35465e-12,-1040.52,4.7231], Tmin=(10,'K'), Tmax=(603.114,'K')),
            NASAPolynomial(coeffs=[2.87464,0.00218925,-1.19516e-06,2.91929e-10,-2.60079e-14,-935.808,7.69142], Tmin=(603.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.64859,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7782-44-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 160,
    label = "CCl3F_214",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83873,0.0108552,8.66126e-05,-2.59255e-07,2.03535e-10,-36805.3,10.3453], Tmin=(10,'K'), Tmax=(479.636,'K')),
            NASAPolynomial(coeffs=[7.22186,0.0122055,-1.00691e-05,3.63956e-09,-4.78428e-13,-37469.9,-7.03571], Tmin=(479.636,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-306.045,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-69-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 161,
    label = "C2H5_82",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9201,0.00825552,-2.80328e-06,2.91707e-08,-3.15874e-11,12878.8,4.09998], Tmin=(10,'K'), Tmax=(503.24,'K')),
            NASAPolynomial(coeffs=[1.27725,0.0200181,-1.03106e-05,2.61459e-09,-2.61712e-13,13261.8,16.1983], Tmin=(503.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (107.082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2025-56-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 162,
    label = "C2H5ClO_13",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97025,0.00212609,0.000106482,-2.35025e-07,1.72401e-10,-33894.3,9.70698], Tmin=(10,'K'), Tmax=(347.755,'K')),
            NASAPolynomial(coeffs=[1.44111,0.0312221,-1.9041e-05,5.65096e-09,-6.49982e-13,-33718.4,19.2368], Tmin=(347.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-281.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-07-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 163,
    label = "C2Cl2_366",
    molecule = 
"""
1 C  u0 p0 c0 {2,T} {3,S}
2 C  u0 p0 c0 {1,T} {4,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38839,0.00831843,5.58541e-05,-2.05413e-07,1.92149e-10,26508.4,8.53311], Tmin=(10,'K'), Tmax=(409.885,'K')),
            NASAPolynomial(coeffs=[5.41842,0.00670674,-4.84859e-06,1.64306e-09,-2.09769e-13,26189.1,-1.31497], Tmin=(409.885,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.405,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7572-29-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 164,
    label = "BrO2_58",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97162,0.00170919,2.20182e-05,-4.9831e-08,3.18047e-11,11751.3,9.53138], Tmin=(10,'K'), Tmax=(557.675,'K')),
            NASAPolynomial(coeffs=[4.36883,0.00511918,-3.9888e-06,1.38418e-09,-1.76553e-13,11609.7,6.97443], Tmin=(557.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (97.6957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m06hf-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 67177-47-3*0 and used to tweak m06hf-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 165,
    label = "C2H4O2_187",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97703,0.00159227,8.72689e-05,-1.82594e-07,1.26282e-10,-53777.6,7.8479], Tmin=(10,'K'), Tmax=(369.942,'K')),
            NASAPolynomial(coeffs=[1.60564,0.027246,-1.68023e-05,5.04729e-09,-5.8734e-13,-53602.3,16.9291], Tmin=(369.942,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-447.131,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 64-19-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 166,
    label = "C2Cl5_400",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {7,S}
5 Cl u0 p3 c0 {7,S}
6 C  u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C  u1 p0 c0 {4,S} {5,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46984,0.0450793,4.60214e-05,-3.66342e-07,4.01768e-10,98.6395,13.3545], Tmin=(10,'K'), Tmax=(397.616,'K')),
            NASAPolynomial(coeffs=[10.256,0.0191825,-1.61316e-05,5.87748e-09,-7.74078e-13,-775.971,-17.3382], Tmin=(397.616,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (0.830405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7094-17-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 167,
    label = "C4H6_47",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {3,T} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96557,0.00252504,0.000120869,-2.78534e-07,2.15293e-10,18033.8,7.1128], Tmin=(10,'K'), Tmax=(328.891,'K')),
            NASAPolynomial(coeffs=[1.43926,0.0332503,-1.92616e-05,5.51326e-09,-6.205e-13,18200,16.4915], Tmin=(328.891,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.947,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-00-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 168,
    label = "C3H8O_106",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86069,0.0151061,3.7938e-05,-5.22278e-08,1.94043e-11,-32762.7,7.47166], Tmin=(10,'K'), Tmax=(898.52,'K')),
            NASAPolynomial(coeffs=[1.09096,0.038827,-2.06777e-05,5.37164e-09,-5.47506e-13,-32724.8,17.9789], Tmin=(898.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-272.395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 71-23-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 169,
    label = "C8H18_168",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17528,0.0911875,-0.000282224,8.18001e-07,-7.58104e-10,-28806.3,10.7333], Tmin=(10,'K'), Tmax=(410.687,'K')),
            NASAPolynomial(coeffs=[-5.87697,0.104927,-6.05699e-05,1.69157e-08,-1.83571e-12,-27435.1,53.9909], Tmin=(410.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-239.54,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (631.9,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 111-65-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 170,
    label = "N2O_325",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 N u0 p2 c-1 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53515,-0.00365836,4.24438e-05,-8.09269e-08,5.0616e-11,8800.95,5.99617], Tmin=(10,'K'), Tmax=(504.517,'K')),
            NASAPolynomial(coeffs=[2.82656,0.00707742,-4.69102e-06,1.46307e-09,-1.73193e-13,8807.32,8.28445], Tmin=(504.517,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.1722,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 10024-97-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 171,
    label = "HN3_319",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 N u0 p0 c+1 {1,D} {3,D}
3 N u0 p2 c-1 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04332,-0.00431703,5.07067e-05,-9.64693e-08,6.13638e-11,33767.4,5.39285], Tmin=(10,'K'), Tmax=(480.467,'K')),
            NASAPolynomial(coeffs=[3.0073,0.00897802,-5.37932e-06,1.58175e-09,-1.80729e-13,33813.1,9.0707], Tmin=(480.467,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (280.756,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 7782-79-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 172,
    label = "C3H3_340",
    molecule = 
"""
multiplicity 4
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u2 p0 c0 {1,S} {5,S}
3 C u1 p0 c0 {1,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97235,0.00155264,4.97558e-05,-8.50745e-08,4.49098e-11,77113,7.19711], Tmin=(10,'K'), Tmax=(588.702,'K')),
            NASAPolynomial(coeffs=[2.0678,0.0205369,-1.40145e-05,4.57945e-09,-5.68314e-13,77232.6,14.4869], Tmin=(588.702,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (641.141,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 84654-90-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 173,
    label = "C2HCl_173",
    molecule = 
"""
1 C  u0 p0 c0 {2,T} {4,S}
2 C  u0 p0 c0 {1,T} {3,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42863,0.00453192,4.71828e-05,-1.21664e-07,8.64314e-11,26101.2,6.97056], Tmin=(10,'K'), Tmax=(517.402,'K')),
            NASAPolynomial(coeffs=[4.96379,0.00763437,-5.21303e-06,1.76987e-09,-2.30652e-13,25742,-1.36059], Tmin=(517.402,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.998,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-63-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 174,
    label = "C3H5O_254",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91861,0.00668587,8.49314e-05,-1.9375e-07,1.43275e-10,-5725.02,7.7571], Tmin=(10,'K'), Tmax=(346.029,'K')),
            NASAPolynomial(coeffs=[1.85577,0.0305319,-1.84394e-05,5.40728e-09,-6.1416e-13,-5582.26,15.5199], Tmin=(346.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-47.6037,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3122-07-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 175,
    label = "C2O_424",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 C u2 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46644,0.00225497,2.76622e-05,-7.18314e-08,5.36103e-11,44602.7,6.91662], Tmin=(10,'K'), Tmax=(471.24,'K')),
            NASAPolynomial(coeffs=[3.76599,0.00597498,-4.11379e-06,1.32439e-09,-1.61572e-13,44504.9,4.959], Tmin=(471.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (370.842,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12071-23-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 176,
    label = "C3H2_229",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p1 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94748,0.00420878,3.05993e-05,-8.46964e-08,7.67664e-11,65316.2,4.96809], Tmin=(10,'K'), Tmax=(279.608,'K')),
            NASAPolynomial(coeffs=[3.47754,0.0109316,-5.46622e-06,1.29357e-09,-1.17272e-13,65342.5,6.63643], Tmin=(279.608,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (543.061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 60731-10-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 177,
    label = "C2H4O_197",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09979,-0.00898036,0.000105141,-1.79953e-07,1.01545e-10,-16253.7,6.77168], Tmin=(10,'K'), Tmax=(548.154,'K')),
            NASAPolynomial(coeffs=[1.44195,0.0223636,-1.33285e-05,3.89801e-09,-4.42726e-13,-16141.9,16.3588], Tmin=(548.154,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-135.145,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 557-75-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 178,
    label = "C3H5_59",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92764,0.00521549,4.46739e-05,-7.30774e-08,3.74679e-11,28709.9,6.34169], Tmin=(10,'K'), Tmax=(506.752,'K')),
            NASAPolynomial(coeffs=[1.43171,0.0249169,-1.36427e-05,3.64204e-09,-3.80728e-13,28962.9,16.6865], Tmin=(506.752,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.69,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 15552-77-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 179,
    label = "C3H6_166",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02213,-0.00187623,7.72068e-05,-1.15997e-07,5.73098e-11,803.641,5.87137], Tmin=(10,'K'), Tmax=(522.043,'K')),
            NASAPolynomial(coeffs=[-0.272062,0.0310265,-1.7333e-05,4.73242e-09,-5.05821e-13,1252,23.7971], Tmin=(522.043,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.67944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 115-07-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 180,
    label = "C2H3F_126",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09187,-0.00748087,7.66916e-05,-1.17778e-07,5.93346e-11,-18489.8,6.78187], Tmin=(10,'K'), Tmax=(612.647,'K')),
            NASAPolynomial(coeffs=[1.4808,0.0190345,-1.14087e-05,3.31446e-09,-3.7235e-13,-18347.5,16.6494], Tmin=(612.647,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.73,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-02-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 181,
    label = "C2H4F_421",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 F u0 p3 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93886,0.00530281,3.91916e-05,-6.92317e-08,3.7964e-11,-8824.97,7.15681], Tmin=(10,'K'), Tmax=(474.603,'K')),
            NASAPolynomial(coeffs=[1.99256,0.0217064,-1.26528e-05,3.59354e-09,-3.97307e-13,-8640.23,15.096], Tmin=(474.603,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.3821,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 182,
    label = "C5H6_299",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14054,-0.0129229,0.000120257,1.79103e-08,-2.88424e-10,14461,8.26489], Tmin=(10,'K'), Tmax=(305.152,'K')),
            NASAPolynomial(coeffs=[-3.12007,0.0502979,-3.3442e-05,1.05492e-08,-1.26328e-12,15052.8,37.1128], Tmin=(305.152,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.24,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 542-92-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 183,
    label = "C2HF4_415",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 F u0 p3 c0 {2,S}
7 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79645,0.0202469,1.21107e-05,-4.33974e-08,2.44756e-11,-83162.7,10.9175], Tmin=(10,'K'), Tmax=(712.047,'K')),
            NASAPolynomial(coeffs=[5.88935,0.0204354,-1.34509e-05,4.09591e-09,-4.7147e-13,-83763.6,-0.595183], Tmin=(712.047,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-691.471,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 184,
    label = "CH3_199",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9864,0.000742432,9.38779e-06,-1.24352e-08,5.60878e-12,16331.5,0.227518], Tmin=(10,'K'), Tmax=(551.783,'K')),
            NASAPolynomial(coeffs=[3.47068,0.00448096,-7.75116e-07,-1.56487e-10,4.56766e-14,16388.5,2.40894], Tmin=(551.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (135.782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2229-07-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 185,
    label = "CHF3_163",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06652,-0.00577264,7.307e-05,-1.20796e-07,6.37901e-11,-85086.9,7.48385], Tmin=(10,'K'), Tmax=(609.325,'K')),
            NASAPolynomial(coeffs=[2.51063,0.0164098,-1.10009e-05,3.42257e-09,-4.01729e-13,-85119.5,12.3961], Tmin=(609.325,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-707.456,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-46-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 186,
    label = "CHO3_365",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9405,0.00468827,3.33339e-05,-6.83226e-08,4.07133e-11,-14258.1,8.66912], Tmin=(10,'K'), Tmax=(553.74,'K')),
            NASAPolynomial(coeffs=[3.42503,0.0144514,-9.47346e-06,2.91145e-09,-3.39831e-13,-14293.6,10.0152], Tmin=(553.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-118.56,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 56240-83-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 187,
    label = "C5H8_119",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95403,0.0031618,0.000156046,-3.268e-07,2.26708e-10,6932.71,8.36906], Tmin=(10,'K'), Tmax=(368.18,'K')),
            NASAPolynomial(coeffs=[-0.231998,0.0486339,-2.91876e-05,8.56146e-09,-9.78183e-13,7240.99,24.3821], Tmin=(368.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.6409,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 78-79-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 188,
    label = "C2H4Cl2_141",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93435,0.00448058,9.61314e-05,-2.23992e-07,1.62515e-10,-17862.4,9.15803], Tmin=(10,'K'), Tmax=(442.797,'K')),
            NASAPolynomial(coeffs=[2.87926,0.0257866,-1.59319e-05,4.78309e-09,-5.56187e-13,-17884.4,12.0853], Tmin=(442.797,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-148.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-34-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 189,
    label = "C4H6O_388",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {7,S} {8,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92514,0.00448013,0.000118496,-2.25578e-07,1.33102e-10,-10294.4,9.21568], Tmin=(10,'K'), Tmax=(538.833,'K')),
            NASAPolynomial(coeffs=[1.30977,0.0400103,-2.52736e-05,7.80338e-09,-9.31065e-13,-10246.5,18.0453], Tmin=(538.833,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.6211,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 59120-04-6*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 190,
    label = "Cl_21",
    molecule = 
"""
multiplicity 2
1 Cl u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,13844.3,4.85871], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,13844.3,4.85871], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.108,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 22537-15-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 191,
    label = "CCl2F2_93",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88226,0.00745491,7.60097e-05,-1.95196e-07,1.3698e-10,-61390.8,10.0839], Tmin=(10,'K'), Tmax=(521.793,'K')),
            NASAPolynomial(coeffs=[6.16918,0.0138391,-1.10928e-05,3.92842e-09,-5.08688e-13,-61955,-2.58135], Tmin=(521.793,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-510.466,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-71-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 192,
    label = "C6H5_273",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u1 p0 c0 {4,D} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.133,-0.0124541,0.000124157,2.43278e-08,-3.25805e-10,38849.8,10.3573], Tmin=(10,'K'), Tmax=(296.178,'K')),
            NASAPolynomial(coeffs=[-3.01472,0.0515158,-3.49046e-05,1.11492e-08,-1.34684e-12,39416,38.5547], Tmin=(296.178,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (323.028,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 2396-01-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 193,
    label = "C7H8_237",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {2,S} {7,D} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {13,S}
7  C u0 p0 c0 {4,D} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94354,0.0034172,0.000164167,-2.90322e-07,1.65467e-10,3734.37,10.183], Tmin=(10,'K'), Tmax=(455.283,'K')),
            NASAPolynomial(coeffs=[-3.16716,0.066034,-4.26079e-05,1.31506e-08,-1.5544e-12,4380.35,38.8767], Tmin=(455.283,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (31.0277,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 108-88-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 194,
    label = "C2H3F2_423",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 F u0 p3 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 F u0 p3 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90522,0.010685,2.00913e-05,-3.48911e-08,1.51986e-11,-31574.1,9.39991], Tmin=(10,'K'), Tmax=(802.983,'K')),
            NASAPolynomial(coeffs=[3.56712,0.0199956,-1.15474e-05,3.20437e-09,-3.44495e-13,-31765.6,9.4259], Tmin=(802.983,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-262.519,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 195,
    label = "CH2O3_45",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10702,-0.0106235,0.00012775,-2.43706e-07,1.49802e-10,-75081.6,7.62019], Tmin=(10,'K'), Tmax=(531.262,'K')),
            NASAPolynomial(coeffs=[2.88469,0.018812,-1.24856e-05,3.95701e-09,-4.75996e-13,-75237.3,10.0569], Tmin=(531.262,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-624.277,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 463-79-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 196,
    label = "C3H5_351",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p1 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94178,0.00486275,4.42913e-05,-6.88003e-08,3.32538e-11,56406.2,6.47519], Tmin=(10,'K'), Tmax=(540.931,'K')),
            NASAPolynomial(coeffs=[1.05664,0.0261974,-1.48698e-05,4.11253e-09,-4.44078e-13,56718.3,18.6215], Tmin=(540.931,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (468.979,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 85056-54-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 197,
    label = "H2_7",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49863,8.07443e-05,-2.55893e-07,2.03931e-11,2.94253e-13,-1005.73,-4.28109], Tmin=(10,'K'), Tmax=(614.458,'K')),
            NASAPolynomial(coeffs=[3.68771,-0.000782251,9.52742e-07,-3.16543e-10,3.48955e-14,-1035.91,-5.15773], Tmin=(614.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.36262,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 13983-20-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 198,
    label = "C3H_249",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02381,-0.00224774,3.98352e-05,-6.86356e-08,3.7968e-11,84661.4,5.68377], Tmin=(10,'K'), Tmax=(571.355,'K')),
            NASAPolynomial(coeffs=[3.07708,0.00984581,-6.26343e-06,1.8958e-09,-2.19303e-13,84680.4,8.94056], Tmin=(571.355,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (703.911,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-mn15_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 119178-99-3*0 and used to tweak mn15_jun-cc-pvtz calculation
""",
)

entry(
    index = 199,
    label = "C7H8_393",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {5,S} {7,D} {12,S}
7  C u0 p0 c0 {4,S} {6,D} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09694,-0.00945123,0.000226077,-3.8572e-07,2.10849e-10,19937,9.78945], Tmin=(10,'K'), Tmax=(572.359,'K')),
            NASAPolynomial(coeffs=[-2.11442,0.0628929,-3.93496e-05,1.17671e-08,-1.34942e-12,20174.1,32.1495], Tmin=(572.359,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.744,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 544-25-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 200,
    label = "C7H5FO_234",
    molecule = 
"""
1  F u0 p3 c0 {9,S}
2  O u0 p2 c0 {9,D}
3  C u0 p0 c0 {4,D} {5,S} {9,S}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {8,D} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {11,S}
7  C u0 p0 c0 {6,D} {8,S} {12,S}
8  C u0 p0 c0 {5,D} {7,S} {13,S}
9  C u0 p0 c0 {1,S} {2,D} {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87454,0.00749292,0.00018026,-3.4972e-07,2.07282e-10,-39120.3,11.9673], Tmin=(10,'K'), Tmax=(544.195,'K')),
            NASAPolynomial(coeffs=[0.386428,0.0603762,-4.06016e-05,1.28433e-08,-1.53998e-12,-39144.1,22.9665], Tmin=(544.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-325.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 455-32-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 201,
    label = "CBr2Cl2_10",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70322,0.0237788,8.45321e-05,-4.16029e-07,4.41965e-10,-1703.24,12.9803], Tmin=(10,'K'), Tmax=(381.76,'K')),
            NASAPolynomial(coeffs=[8.56295,0.010204,-8.86312e-06,3.30664e-09,-4.4346e-13,-2346.42,-9.3495], Tmin=(381.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-14.1416,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 594-18-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 202,
    label = "ClO_98",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51952,-0.00167237,1.52604e-05,-2.59484e-08,1.39934e-11,11169,6.56484], Tmin=(10,'K'), Tmax=(618.638,'K')),
            NASAPolynomial(coeffs=[3.42326,0.00212387,-1.63981e-06,5.56935e-10,-6.91185e-14,11120.2,6.49214], Tmin=(618.638,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (92.8639,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 14989-30-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 203,
    label = "BrO_2",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49391,0.000322384,6.23466e-06,-1.11064e-08,5.68788e-12,13774.4,7.74972], Tmin=(10,'K'), Tmax=(668.02,'K')),
            NASAPolynomial(coeffs=[3.42252,0.00236679,-1.98675e-06,7.21801e-10,-9.47609e-14,13747.8,7.79525], Tmin=(668.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.524,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 15656-19-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 204,
    label = "CCl_147",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 C  u1 p1 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51949,-0.00164997,1.48692e-05,-2.49718e-08,1.33058e-11,51154.9,6.33641], Tmin=(10,'K'), Tmax=(625.301,'K')),
            NASAPolynomial(coeffs=[3.41251,0.00213326,-1.64e-06,5.55112e-10,-6.87037e-14,51107.7,6.31785], Tmin=(625.301,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (425.325,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3889-76-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 205,
    label = "CHNO_293",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98426,0.000915275,2.41231e-05,-4.4177e-08,2.5007e-11,-3158.66,5.26043], Tmin=(10,'K'), Tmax=(564.823,'K')),
            NASAPolynomial(coeffs=[3.42354,0.00843568,-5.27509e-06,1.64785e-09,-2.00338e-13,-3151.94,7.14408], Tmin=(564.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.2692,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 420-05-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 206,
    label = "C2H3Cl3_221",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83144,0.0119811,0.000124934,-3.64376e-07,3.0019e-10,-19627.2,9.18519], Tmin=(10,'K'), Tmax=(434.68,'K')),
            NASAPolynomial(coeffs=[5.70859,0.0237311,-1.57682e-05,5.02732e-09,-6.12891e-13,-20064.6,-1.46102], Tmin=(434.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.199,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 71-55-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 207,
    label = "C4H6O_288",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80623,0.0168097,4.51691e-05,-8.23933e-08,4.11415e-11,-15504.2,8.50103], Tmin=(10,'K'), Tmax=(641.793,'K')),
            NASAPolynomial(coeffs=[1.65412,0.0379285,-2.22e-05,6.29483e-09,-6.92939e-13,-15386.7,16.6929], Tmin=(641.793,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.933,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 78-94-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 208,
    label = "CH4_73",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04161,-0.00248931,1.13758e-05,3.68147e-09,-9.41086e-12,-10160.5,-0.418503], Tmin=(10,'K'), Tmax=(616.574,'K')),
            NASAPolynomial(coeffs=[0.65634,0.0117858,-4.65258e-06,7.92677e-10,-4.12516e-14,-9596.9,15.4613], Tmin=(616.574,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-84.4637,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-82-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 209,
    label = "CH2O3_204",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96598,0.00199593,5.47769e-05,-1.01409e-07,5.79046e-11,-36275.9,7.98166], Tmin=(10,'K'), Tmax=(554.727,'K')),
            NASAPolynomial(coeffs=[2.54678,0.0196393,-1.2968e-05,4.08625e-09,-4.91346e-13,-36232.5,12.9645], Tmin=(554.727,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-301.629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-32-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 210,
    label = "F2O2_23",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93539,0.00384593,4.65724e-05,-1.0599e-07,6.70933e-11,2216.48,8.53063], Tmin=(10,'K'), Tmax=(569.497,'K')),
            NASAPolynomial(coeffs=[5.11012,0.0101204,-8.21235e-06,2.92833e-09,-3.80589e-13,1847.13,1.45656], Tmin=(569.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.4039,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7783-44-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 211,
    label = "CH2O_87",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03237,-0.0019765,9.323e-06,2.70349e-09,-8.07859e-12,-14333.9,3.47377], Tmin=(10,'K'), Tmax=(594.116,'K')),
            NASAPolynomial(coeffs=[1.39918,0.00964292,-4.58929e-06,1.00722e-09,-8.19307e-14,-13913.2,15.7137], Tmin=(594.116,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.168,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 50-00-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 212,
    label = "CH3N_367",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08138,-0.00477454,2.99362e-05,-2.97959e-08,9.65706e-12,9410.73,4.36621], Tmin=(10,'K'), Tmax=(937.133,'K')),
            NASAPolynomial(coeffs=[0.89482,0.0135091,-6.8237e-06,1.68634e-09,-1.63821e-13,9802.37,18.4357], Tmin=(937.133,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (78.267,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 2053-29-4*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 213,
    label = "CHO3_297",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 C u1 p0 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89266,0.00871188,5.62297e-05,-2.01978e-07,1.96785e-10,-10974,8.60717], Tmin=(10,'K'), Tmax=(372.251,'K')),
            NASAPolynomial(coeffs=[4.68722,0.0124767,-8.51486e-06,2.75594e-09,-3.37934e-13,-11118.4,4.41414], Tmin=(372.251,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-91.2342,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 153751-35-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 214,
    label = "C4H10O_278",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62823,0.0404713,-9.93058e-05,3.0755e-07,-2.89828e-10,-32551.2,7.13482], Tmin=(10,'K'), Tmax=(426.052,'K')),
            NASAPolynomial(coeffs=[-1.82873,0.0565554,-3.21852e-05,8.88764e-09,-9.56022e-13,-31767.2,32.5495], Tmin=(426.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-270.657,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 60-29-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 215,
    label = "C2HCl_272",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,D} {4,S}
2 Cl u0 p3 c0 {1,S}
3 C  u0 p1 c0 {1,D}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89758,0.0108618,-2.62053e-05,6.48755e-08,-6.24792e-11,50181.9,7.78878], Tmin=(10,'K'), Tmax=(353.988,'K')),
            NASAPolynomial(coeffs=[3.75751,0.00928758,-6.1573e-06,1.92539e-09,-2.2872e-13,50211.6,8.59845], Tmin=(353.988,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (417.235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 70277-82-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 216,
    label = "C2H4_19",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10206,-0.00694421,5.20886e-05,-6.26284e-08,2.48467e-11,5035.69,3.22962], Tmin=(10,'K'), Tmax=(753.837,'K')),
            NASAPolynomial(coeffs=[0.505419,0.0181264,-9.70899e-06,2.55723e-09,-2.64773e-13,5407.86,18.4368], Tmin=(753.837,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.8904,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-85-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 217,
    label = "C2H3Cl3_25",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77115,0.0197671,4.20273e-05,-1.38896e-07,1.11093e-10,-19987,12.1028], Tmin=(10,'K'), Tmax=(447.662,'K')),
            NASAPolynomial(coeffs=[4.27984,0.0263836,-1.75434e-05,5.51523e-09,-6.58624e-13,-20144.4,8.80836], Tmin=(447.662,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-166.194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 79-00-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 218,
    label = "C2H4Cl2_144",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87522,0.0140533,1.64233e-05,-2.97986e-08,1.23383e-11,-17567.5,9.57173], Tmin=(10,'K'), Tmax=(867.676,'K')),
            NASAPolynomial(coeffs=[3.75991,0.0227475,-1.27182e-05,3.43402e-09,-3.60827e-13,-17854.7,8.341], Tmin=(867.676,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-146.058,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-06-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 219,
    label = "F2O_159",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03432,-0.00340025,4.3115e-05,-8.13071e-08,4.80713e-11,1660.02,6.37943], Tmin=(10,'K'), Tmax=(568.912,'K')),
            NASAPolynomial(coeffs=[3.94418,0.00596247,-4.58565e-06,1.5591e-09,-1.94324e-13,1529.01,5.52198], Tmin=(568.912,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.7959,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7783-41-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 220,
    label = "NO_326",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50516,-0.000269817,5.12594e-07,1.49909e-09,-1.30355e-12,9920.14,4.72694], Tmin=(10,'K'), Tmax=(735.277,'K')),
            NASAPolynomial(coeffs=[2.93891,0.00151926,-5.02735e-07,3.10251e-11,7.76387e-15,10038.3,7.52202], Tmin=(735.277,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.4829,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 10102-43-9*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 221,
    label = "C3H6O_401",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96246,0.00225211,8.98878e-05,-1.57742e-07,9.01908e-11,-14578,7.23536], Tmin=(10,'K'), Tmax=(450.292,'K')),
            NASAPolynomial(coeffs=[0.230773,0.0354076,-2.05807e-05,5.84046e-09,-6.47485e-13,-14242,22.2605], Tmin=(450.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.225,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-25-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 222,
    label = "C3H6_248",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20647,-0.0151723,0.000123093,-1.67614e-07,7.48685e-11,5107.45,4.96408], Tmin=(10,'K'), Tmax=(690.983,'K')),
            NASAPolynomial(coeffs=[-1.31929,0.0337229,-1.97526e-05,5.61653e-09,-6.18665e-13,5467.47,26.6594], Tmin=(690.983,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.4944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-19-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 223,
    label = "CHO2_83",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98668,0.000793433,2.90304e-05,-5.26899e-08,2.99643e-11,-16685.8,6.76374], Tmin=(10,'K'), Tmax=(528.129,'K')),
            NASAPolynomial(coeffs=[2.92957,0.0112547,-7.65422e-06,2.41899e-09,-2.88763e-13,-16608.3,10.8647], Tmin=(528.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-138.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 16499-21-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 224,
    label = "C2H3N_295",
    molecule = 
"""
1 N u0 p1 c0 {3,T}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,T} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9893,0.000491441,3.74397e-05,-5.73813e-08,2.87271e-11,7466.09,5.03814], Tmin=(10,'K'), Tmax=(514.54,'K')),
            NASAPolynomial(coeffs=[1.96002,0.0162669,-8.54934e-06,2.2047e-09,-2.23981e-13,7674.92,13.4798], Tmin=(514.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (62.0688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 75-05-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 225,
    label = "CHClF2_99",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96415,0.00203803,4.61088e-05,-8.54404e-08,4.74837e-11,-59563.8,9.29535], Tmin=(10,'K'), Tmax=(591.357,'K')),
            NASAPolynomial(coeffs=[3.09666,0.0163561,-1.16444e-05,3.83207e-09,-4.72548e-13,-59608.9,11.7754], Tmin=(591.357,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-495.257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-45-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 226,
    label = "C2H6O_43",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96225,0.00194492,5.51404e-05,-7.72721e-08,3.48645e-11,-23735.6,4.60469], Tmin=(10,'K'), Tmax=(573.13,'K')),
            NASAPolynomial(coeffs=[0.166295,0.0284362,-1.41888e-05,3.36728e-09,-3.08531e-13,-23300.5,20.8052], Tmin=(573.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-197.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 115-10-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 227,
    label = "C2H2O_305",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u2 p0 c0 {2,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05029,-0.00531011,7.59653e-05,-1.45151e-07,9.10295e-11,29680.4,7.47095], Tmin=(10,'K'), Tmax=(496.647,'K')),
            NASAPolynomial(coeffs=[2.59698,0.0146604,-9.31462e-06,2.83277e-09,-3.30105e-13,29722.8,12.4389], Tmin=(496.647,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (246.772,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 39920-84-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 228,
    label = "CHF2_406",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05496,-0.00411968,4.01388e-05,-5.75052e-08,2.64733e-11,-30558.9,6.89415], Tmin=(10,'K'), Tmax=(689.187,'K')),
            NASAPolynomial(coeffs=[2.6252,0.0108481,-6.95445e-06,2.09115e-09,-2.38727e-13,-30520.2,12.1106], Tmin=(689.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-254.075,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 229,
    label = "CH3ClO_1",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O  u0 p2 c0 {1,S} {6,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96452,0.00240231,4.19623e-05,-7.80237e-08,4.70005e-11,-9115.69,6.95382], Tmin=(10,'K'), Tmax=(426.498,'K')),
            NASAPolynomial(coeffs=[2.40002,0.0170752,-9.64234e-06,2.64012e-09,-2.81909e-13,-8982.24,13.1684], Tmin=(426.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-75.8034,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-78-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 230,
    label = "CH4O2_180",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89319,0.00859746,1.90998e-05,-3.1923e-08,1.48052e-11,-17044.5,5.9734], Tmin=(10,'K'), Tmax=(577.545,'K')),
            NASAPolynomial(coeffs=[2.21033,0.0202527,-1.11709e-05,3.01868e-09,-3.19851e-13,-16850.1,13.1684], Tmin=(577.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-141.73,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3031-73-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 231,
    label = "N2O3_362",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 N u0 p1 c0 {1,S} {2,D}
5 N u0 p1 c0 {1,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85712,0.0114394,7.1258e-05,-2.74295e-07,2.74989e-10,8721.58,8.22141], Tmin=(10,'K'), Tmax=(372.787,'K')),
            NASAPolynomial(coeffs=[5.44059,0.0129627,-9.36641e-06,3.10979e-09,-3.86598e-13,8474.88,0.419141], Tmin=(372.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.5282,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 122413-35-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 232,
    label = "CH_192",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49629,0.000304807,-2.13315e-06,4.34855e-09,-2.24693e-12,70656.2,1.35182], Tmin=(10,'K'), Tmax=(769.263,'K')),
            NASAPolynomial(coeffs=[3.17093,0.000537345,2.58829e-07,-1.90338e-10,2.95425e-14,70749.4,3.11676], Tmin=(769.263,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (587.468,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3315-37-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 233,
    label = "C2H2Cl2_56",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {5,S} {6,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93246,0.00400659,6.56492e-05,-1.36711e-07,8.34463e-11,-1344.97,9.1914], Tmin=(10,'K'), Tmax=(563.649,'K')),
            NASAPolynomial(coeffs=[4.14439,0.0179123,-1.23657e-05,4.06631e-09,-5.07109e-13,-1613.64,6.11905], Tmin=(563.649,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.2091,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-35-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 234,
    label = "CHCl_183",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p1 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02743,-0.00218355,1.92821e-05,-2.85074e-08,1.39449e-11,37328.4,5.33556], Tmin=(10,'K'), Tmax=(623.072,'K')),
            NASAPolynomial(coeffs=[3.28251,0.00479783,-2.81934e-06,8.05021e-10,-8.92003e-14,37378.5,8.2344], Tmin=(623.072,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (310.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2108-20-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 235,
    label = "C4H9_205",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80284,0.0208321,2.98841e-05,-4.47508e-08,1.65231e-11,7409.26,7.53124], Tmin=(10,'K'), Tmax=(935.305,'K')),
            NASAPolynomial(coeffs=[1.87185,0.0410025,-2.15684e-05,5.54064e-09,-5.59216e-13,7249.43,13.9326], Tmin=(935.305,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.6114,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2492-36-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 236,
    label = "C3H5_108",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11814,-0.0110964,0.000134303,-2.39257e-07,1.40968e-10,18729.3,6.74355], Tmin=(10,'K'), Tmax=(523.348,'K')),
            NASAPolynomial(coeffs=[0.983819,0.0271553,-1.63073e-05,4.79213e-09,-5.46303e-13,18861.5,17.9649], Tmin=(523.348,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1981-80-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 237,
    label = "C7H8_350",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  C u0 p0 c0 {1,S} {7,D} {14,S}
7  C u0 p0 c0 {2,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.35065,-0.0295533,0.000310022,-5.01579e-07,2.62723e-10,26747.1,8.81212], Tmin=(10,'K'), Tmax=(608.147,'K')),
            NASAPolynomial(coeffs=[-2.94072,0.0658437,-4.2284e-05,1.28966e-08,-1.49874e-12,26756.7,33.15], Tmin=(608.147,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (222.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 121-46-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 238,
    label = "HNO3_310",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08296,-0.00750285,8.50848e-05,-1.48013e-07,8.27763e-11,-17523,8.16765], Tmin=(10,'K'), Tmax=(579.24,'K')),
            NASAPolynomial(coeffs=[2.76893,0.0154654,-1.03742e-05,3.26483e-09,-3.88143e-13,-17603.8,11.7775], Tmin=(579.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-145.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 7697-37-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 239,
    label = "CH4O_122",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02527,-0.00163243,3.21271e-05,-3.72138e-08,1.3958e-11,-25512.3,3.94416], Tmin=(10,'K'), Tmax=(653.048,'K')),
            NASAPolynomial(coeffs=[0.771836,0.0172633,-8.90472e-06,2.25399e-09,-2.24749e-13,-25065.4,18.4223], Tmin=(653.048,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-212.115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67-56-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 240,
    label = "CH5N_369",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03127,-0.00211002,4.13045e-05,-4.97941e-08,1.96608e-11,-3995.37,4.08087], Tmin=(10,'K'), Tmax=(657.441,'K')),
            NASAPolynomial(coeffs=[0.310237,0.0205291,-1.03475e-05,2.58183e-09,-2.55437e-13,-3506.09,20.4722], Tmin=(657.441,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.2125,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 74-89-5*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 241,
    label = "C2H6_137",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05992,-0.00389241,5.41919e-05,-6.33814e-08,2.41449e-11,-11500.7,2.44474], Tmin=(10,'K'), Tmax=(739.346,'K')),
            NASAPolynomial(coeffs=[-1.0236,0.0266365,-1.38853e-05,3.53967e-09,-3.55505e-13,-10831.7,24.8753], Tmin=(739.346,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.6077,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-84-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 242,
    label = "C4_364",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,T}
4 C u1 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17847,0.021789,-3.59294e-05,2.99921e-08,-9.59816e-12,126130,7.70866], Tmin=(10,'K'), Tmax=(910.866,'K')),
            NASAPolynomial(coeffs=[5.30466,0.00764605,-4.72457e-06,1.36057e-09,-1.49973e-13,125942,-1.25606], Tmin=(910.866,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (1048.64,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 78015-07-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 243,
    label = "CH3F_138",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05261,-0.00347518,1.80145e-05,2.15763e-09,-1.57027e-11,-29530.9,3.91631], Tmin=(10,'K'), Tmax=(527.943,'K')),
            NASAPolynomial(coeffs=[0.485443,0.0145091,-7.39059e-06,1.79508e-09,-1.6802e-13,-29028.2,20.0407], Tmin=(527.943,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.521,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-53-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 244,
    label = "H3N_392",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01845,-0.001085,6.80874e-06,-1.47928e-09,-1.98734e-12,-6684.78,0.271482], Tmin=(10,'K'), Tmax=(656.887,'K')),
            NASAPolynomial(coeffs=[2.4587,0.00547028,-1.4409e-06,7.38047e-11,1.69229e-14,-6416.37,7.62414], Tmin=(656.887,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.5736,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 7664-41-7*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 245,
    label = "C2H3O_179",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98784,0.0068595,9.88354e-06,-1.26627e-08,3.98216e-12,-2756.16,6.11514], Tmin=(10,'K'), Tmax=(1151.44,'K')),
            NASAPolynomial(coeffs=[4.29763,0.0123032,-5.70162e-06,1.27863e-09,-1.12498e-13,-3259.7,2.70009], Tmin=(1151.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-22.8965,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3170-69-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 246,
    label = "C4H9_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77275,0.0170085,6.73316e-05,-1.33099e-07,7.95031e-11,6555.53,6.60205], Tmin=(10,'K'), Tmax=(434.464,'K')),
            NASAPolynomial(coeffs=[0.91752,0.0432961,-2.34277e-05,6.1681e-09,-6.35142e-13,6803.63,17.9966], Tmin=(434.464,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.4557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 4630-45-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 247,
    label = "C2H6O2_178",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91564,0.00685818,7.62799e-05,-1.44422e-07,8.71124e-11,-48736.9,7.905], Tmin=(10,'K'), Tmax=(427.759,'K')),
            NASAPolynomial(coeffs=[0.977906,0.0343293,-2.00523e-05,5.71383e-09,-6.33731e-13,-48485.6,19.5832], Tmin=(427.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-405.234,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-21-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 248,
    label = "C4H9_207",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65676,0.0366547,-9.11402e-05,2.58029e-07,-2.31464e-10,5634.38,7.5003], Tmin=(10,'K'), Tmax=(435.99,'K')),
            NASAPolynomial(coeffs=[-0.556377,0.0465248,-2.60697e-05,7.1087e-09,-7.56905e-13,6275.32,27.4661], Tmin=(435.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.8392,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2348-55-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 249,
    label = "C3H4_60",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0627,-0.00630628,9.97985e-05,-1.8715e-07,1.17353e-10,21337.7,4.88022], Tmin=(10,'K'), Tmax=(472.72,'K')),
            NASAPolynomial(coeffs=[1.53862,0.0221538,-1.3045e-05,3.77294e-09,-4.25248e-13,21497,14.3269], Tmin=(472.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (177.408,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 463-49-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 250,
    label = "ClH_131",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49633,0.000282714,-1.8939e-06,3.69571e-09,-1.82356e-12,-12130,2.49162], Tmin=(10,'K'), Tmax=(801.508,'K')),
            NASAPolynomial(coeffs=[3.214,0.000384043,3.63713e-07,-2.17638e-10,3.19706e-14,-12042.8,4.05325], Tmin=(801.508,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-100.855,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7647-01-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 251,
    label = "CH2Br2_96",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96169,0.00238238,4.58985e-05,-9.74151e-08,6.25213e-11,-1071.54,10.7763], Tmin=(10,'K'), Tmax=(518.034,'K')),
            NASAPolynomial(coeffs=[3.63155,0.0130294,-8.37839e-06,2.61009e-09,-3.12739e-13,-1145.99,11.1032], Tmin=(518.034,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.92124,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-95-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 252,
    label = "CF3_171",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05551,-0.00554954,7.48407e-05,-1.39943e-07,8.24031e-11,-57658.1,7.44846], Tmin=(10,'K'), Tmax=(565.068,'K')),
            NASAPolynomial(coeffs=[3.59379,0.011834,-8.77407e-06,2.91194e-09,-3.5725e-13,-57831.3,7.41842], Tmin=(565.068,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-479.407,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2264-21-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 253,
    label = "BrHO_101",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02861,-0.00271188,2.88171e-05,-5.43334e-08,3.33132e-11,-8723.78,6.76747], Tmin=(10,'K'), Tmax=(533.199,'K')),
            NASAPolynomial(coeffs=[3.78691,0.00371022,-2.21543e-06,6.78328e-10,-8.10246e-14,-8763.52,7.16716], Tmin=(533.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.5359,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 13517-11-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 254,
    label = "C6H5O_244",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {2,S} {6,D} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10947,-0.0109129,0.00021442,-3.79993e-07,2.1396e-10,4729.49,10.5372], Tmin=(10,'K'), Tmax=(571.716,'K')),
            NASAPolynomial(coeffs=[0.165404,0.0499879,-3.27492e-05,1.01237e-08,-1.18854e-12,4636.15,22.5995], Tmin=(571.716,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.2974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2122-46-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 255,
    label = "ClO2_268",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96577,0.00224336,2.37469e-05,-6.21612e-08,4.52697e-11,10976.8,8.45086], Tmin=(10,'K'), Tmax=(494.699,'K')),
            NASAPolynomial(coeffs=[4.45106,0.00480012,-3.65589e-06,1.24871e-09,-1.57515e-13,10849.5,5.64968], Tmin=(494.699,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.2584,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-mn15_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 17376-09-9*0 and used to tweak mn15_jun-cc-pvtz calculation
""",
)

entry(
    index = 256,
    label = "C2H3F2_407",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93735,0.00414159,8.12195e-05,-1.84339e-07,1.2821e-10,-35773.9,8.84517], Tmin=(10,'K'), Tmax=(469.848,'K')),
            NASAPolynomial(coeffs=[3.1803,0.0223276,-1.4323e-05,4.41066e-09,-5.20807e-13,-35832.3,10.5465], Tmin=(469.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-297.452,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 257,
    label = "C2HBr_18",
    molecule = 
"""
1 C  u0 p0 c0 {2,T} {4,S}
2 C  u0 p0 c0 {1,T} {3,S}
3 Br u0 p3 c0 {2,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42215,0.00504752,4.92787e-05,-1.33374e-07,9.84192e-11,31625,8.17775], Tmin=(10,'K'), Tmax=(502.069,'K')),
            NASAPolynomial(coeffs=[5.13283,0.00730913,-4.95378e-06,1.67769e-09,-2.18685e-13,31252.9,-0.891187], Tmin=(502.069,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (262.926,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-61-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 258,
    label = "CHN_356",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53745,-0.00366976,3.69586e-05,-7.2782e-08,4.84816e-11,14451.9,4.01391], Tmin=(10,'K'), Tmax=(462.476,'K')),
            NASAPolynomial(coeffs=[2.92739,0.00509167,-2.76144e-06,7.68692e-10,-8.54132e-14,14471.1,6.08373], Tmin=(462.476,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.159,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 74-90-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 259,
    label = "CBrCl3_239",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75358,0.0185105,9.50744e-05,-3.80051e-07,3.62118e-10,-7235.86,11.7822], Tmin=(10,'K'), Tmax=(412.863,'K')),
            NASAPolynomial(coeffs=[8.37657,0.0104335,-8.96377e-06,3.32394e-09,-4.44325e-13,-7930.48,-10.2207], Tmin=(412.863,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.1609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-62-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 260,
    label = "C2H4Br2_102",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 Br u0 p3 c0 {1,S}
4 Br u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85003,0.0200283,-4.37298e-06,-4.57649e-09,2.09221e-12,-6632.5,11.4744], Tmin=(10,'K'), Tmax=(1204.89,'K')),
            NASAPolynomial(coeffs=[6.94575,0.0162697,-7.80895e-06,1.8148e-09,-1.6557e-13,-7851.67,-6.00119], Tmin=(1204.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.1378,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 106-93-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 261,
    label = "C2H2_292",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4736,0.00151353,2.87159e-05,-5.49752e-08,3.15299e-11,26191.3,3.12579], Tmin=(10,'K'), Tmax=(590.332,'K')),
            NASAPolynomial(coeffs=[3.37962,0.00852223,-5.28338e-06,1.70446e-09,-2.16508e-13,26091.3,2.5893], Tmin=(590.332,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.755,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-86-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 262,
    label = "CF4_103",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94891,0.00281243,5.38852e-05,-1.00063e-07,5.40986e-11,-113870,6.55069], Tmin=(10,'K'), Tmax=(628.318,'K')),
            NASAPolynomial(coeffs=[3.46542,0.0187006,-1.46269e-05,5.07882e-09,-6.46965e-13,-114062,6.64635], Tmin=(628.318,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-946.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-73-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 263,
    label = "CCl3_270",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88506,0.00783864,5.92676e-05,-1.83565e-07,1.47579e-10,6859.79,9.87716], Tmin=(10,'K'), Tmax=(471.121,'K')),
            NASAPolynomial(coeffs=[6.29658,0.00794781,-6.61688e-06,2.40493e-09,-3.17238e-13,6404.13,-2.3664], Tmin=(471.121,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.0179,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3170-80-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 264,
    label = "C2Br2_242",
    molecule = 
"""
1 C  u0 p0 c0 {2,T} {3,S}
2 C  u0 p0 c0 {1,T} {4,S}
3 Br u0 p3 c0 {1,S}
4 Br u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8518,0.0119261,6.08208e-05,-2.81102e-07,3.05034e-10,36852.4,7.24116], Tmin=(10,'K'), Tmax=(365.708,'K')),
            NASAPolynomial(coeffs=[6.41076,0.00586275,-4.24071e-06,1.44247e-09,-1.85042e-13,36518.6,-4.53484], Tmin=(365.708,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (306.424,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 624-61-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 265,
    label = "H_281",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,25921.4,-0.461279], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,25921.4,-0.461279], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (215.523,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 16873-17-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 266,
    label = "C7H8O_335",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  C u0 p0 c0 {3,S} {8,D} {16,S}
6  C u0 p0 c0 {4,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {8,S} {14,S}
8  C u0 p0 c0 {5,D} {7,S} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94383,0.00363638,0.000194814,-3.72805e-07,2.32224e-10,-11163.5,9.75957], Tmin=(10,'K'), Tmax=(414.074,'K')),
            NASAPolynomial(coeffs=[-2.88355,0.0697047,-4.49389e-05,1.3873e-08,-1.64081e-12,-10599.1,36.666], Tmin=(414.074,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.8288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 100-66-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 267,
    label = "CHClO_54",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,D} {4,S}
2 Cl u0 p3 c0 {1,S}
3 O  u0 p2 c0 {1,D}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03368,-0.00376018,5.30188e-05,-1.03553e-07,6.68066e-11,-23363.9,7.7584], Tmin=(10,'K'), Tmax=(477.506,'K')),
            NASAPolynomial(coeffs=[3.00091,0.0100271,-6.42478e-06,1.96299e-09,-2.29422e-13,-23323.8,11.3644], Tmin=(477.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2565-30-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 268,
    label = "C_24",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,85476.5,3.65985], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,85476.5,3.65985], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (710.692,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7440-44-0*500 and used to tweak g4 calculation
""",
)

entry(
    index = 269,
    label = "N2O2_294",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,D} {4,S}
4 N u0 p1 c0 {2,D} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74458,0.0177269,-3.05279e-05,2.71264e-08,-9.22632e-12,18899.3,4.47161], Tmin=(10,'K'), Tmax=(863.366,'K')),
            NASAPolynomial(coeffs=[5.33221,0.00634728,-3.76555e-06,1.06267e-09,-1.15931e-13,18775.2,-2.08595], Tmin=(863.366,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.09,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 16824-89-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 270,
    label = "C8H18_142",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3347,0.0522941,7.48145e-05,-1.48683e-07,7.5739e-11,-30623,6.01523], Tmin=(10,'K'), Tmax=(529.309,'K')),
            NASAPolynomial(coeffs=[-2.7367,0.0981755,-5.52066e-05,1.50779e-08,-1.60676e-12,-29980.3,31.4438], Tmin=(529.309,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-254.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (631.9,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 540-84-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 271,
    label = "C2H2F2_324",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98362,0.00101317,5.4777e-05,-9.88671e-08,5.72886e-11,-38795.6,7.62026], Tmin=(10,'K'), Tmax=(448.034,'K')),
            NASAPolynomial(coeffs=[1.65957,0.0217791,-1.48037e-05,4.75277e-09,-5.78104e-13,-38587.5,16.9646], Tmin=(448.034,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-322.57,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1630-77-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 272,
    label = "CBr3Cl_246",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36427,0.0449489,-8.64939e-05,7.54621e-08,-2.45831e-11,4158.17,13.8176], Tmin=(10,'K'), Tmax=(876.544,'K')),
            NASAPolynomial(coeffs=[9.99388,0.00581926,-4.34318e-06,1.42875e-09,-1.73011e-13,3336.93,-15.3478], Tmin=(876.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.4567,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 594-15-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 273,
    label = "C4H6O2_157",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55185,0.0449755,-8.41683e-05,1.77272e-07,-1.46961e-10,-41920,8.1819], Tmin=(10,'K'), Tmax=(423.269,'K')),
            NASAPolynomial(coeffs=[2.35723,0.0423626,-2.56401e-05,7.48792e-09,-8.45359e-13,-41694.4,14.3893], Tmin=(423.269,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-348.555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 431-03-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 274,
    label = "CHClO_112",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p1 c0 {1,S} {3,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97761,0.00124162,2.81429e-05,-5.0495e-08,2.71014e-11,-30.794,7.54953], Tmin=(10,'K'), Tmax=(615.08,'K')),
            NASAPolynomial(coeffs=[3.42319,0.0103246,-7.36585e-06,2.47005e-09,-3.10989e-13,-66.2037,9.11259], Tmin=(615.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-0.266425,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 147723-60-2*2 and used to tweak g4 calculation
""",
)

entry(
    index = 275,
    label = "C6H5Cl_222",
    molecule = 
"""
1  Cl u0 p3 c0 {2,S}
2  C  u0 p0 c0 {1,S} {3,D} {7,S}
3  C  u0 p0 c0 {2,D} {4,S} {8,S}
4  C  u0 p0 c0 {3,S} {5,D} {9,S}
5  C  u0 p0 c0 {4,D} {6,S} {10,S}
6  C  u0 p0 c0 {5,S} {7,D} {11,S}
7  C  u0 p0 c0 {2,S} {6,D} {12,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92745,0.00414772,0.000133844,-2.34435e-07,1.27008e-10,4144.29,10.0366], Tmin=(10,'K'), Tmax=(570.685,'K')),
            NASAPolynomial(coeffs=[-0.976458,0.0538016,-3.68337e-05,1.18709e-08,-1.44694e-12,4455.16,28.7642], Tmin=(570.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.4251,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 108-90-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 276,
    label = "ClNO_353",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97246,0.00183611,2.11296e-05,-5.57596e-08,4.16937e-11,4959.17,7.61554], Tmin=(10,'K'), Tmax=(477.798,'K')),
            NASAPolynomial(coeffs=[4.32649,0.00417338,-2.85047e-06,9.20632e-10,-1.13305e-13,4864.83,5.53579], Tmin=(477.798,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.2279,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 2696-92-6*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 277,
    label = "C2H6O_169",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96561,0.00190765,6.46986e-05,-1.01576e-07,5.17019e-11,-29921.6,6.22097], Tmin=(10,'K'), Tmax=(506.972,'K')),
            NASAPolynomial(coeffs=[0.518684,0.0290985,-1.57363e-05,4.17466e-09,-4.36146e-13,-29572,20.5096], Tmin=(506.972,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-248.8,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 64-17-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 278,
    label = "CH2O2_81",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10145,-0.00697205,5.25855e-05,-6.69052e-08,2.76131e-11,-1045.92,5.82953], Tmin=(10,'K'), Tmax=(758.003,'K')),
            NASAPolynomial(coeffs=[1.40873,0.0158441,-9.59649e-06,2.76339e-09,-3.04889e-13,-884.957,16.4433], Tmin=(758.003,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.67596,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 157-26-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 279,
    label = "C2H5F_100",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02275,-0.000160901,5.06434e-05,-6.34055e-08,2.47725e-11,-34249.9,6.04846], Tmin=(10,'K'), Tmax=(790.044,'K')),
            NASAPolynomial(coeffs=[0.27316,0.0264917,-1.45195e-05,3.86687e-09,-4.02732e-13,-33896.7,21.7398], Tmin=(790.044,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-284.754,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 353-36-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 280,
    label = "C3H8_12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97109,0.00136321,7.62846e-05,-1.07548e-07,4.89605e-11,-14357.6,4.59474], Tmin=(10,'K'), Tmax=(568.991,'K')),
            NASAPolynomial(coeffs=[-1.21244,0.037804,-1.97836e-05,5.01293e-09,-4.96775e-13,-13767.7,26.6793], Tmin=(568.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.393,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-98-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 281,
    label = "C2H2F4_408",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {1,S}
5 F u0 p3 c0 {2,S}
6 F u0 p3 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82974,0.0179251,2.39112e-05,-5.36365e-08,2.67023e-11,-107998,10.0916], Tmin=(10,'K'), Tmax=(744.91,'K')),
            NASAPolynomial(coeffs=[4.90211,0.0248569,-1.56012e-05,4.59533e-09,-5.16288e-13,-108510,2.87056], Tmin=(744.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-897.953,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 282,
    label = "C2H3F3_410",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90663,0.011919,2.92766e-05,-4.82301e-08,2.06087e-11,-82252.6,9.75951], Tmin=(10,'K'), Tmax=(819.152,'K')),
            NASAPolynomial(coeffs=[3.59898,0.0246137,-1.44645e-05,4.04851e-09,-4.36995e-13,-82577.7,8.89032], Tmin=(819.152,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-683.875,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 283,
    label = "CH3Cl_52",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07027,-0.00487183,3.90088e-05,-4.79846e-08,1.94933e-11,-11189.8,5.09984], Tmin=(10,'K'), Tmax=(731.041,'K')),
            NASAPolynomial(coeffs=[1.44256,0.0136057,-7.31658e-06,1.93272e-09,-2.00668e-13,-10915.1,16.2045], Tmin=(731.041,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.0234,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 74-87-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 284,
    label = "C2HF5_412",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76393,0.0215677,3.91919e-05,-1.05839e-07,6.48388e-11,-136327,10.4267], Tmin=(10,'K'), Tmax=(612.963,'K')),
            NASAPolynomial(coeffs=[5.79792,0.026705,-1.84328e-05,5.83424e-09,-6.92848e-13,-136923,-1.21183], Tmin=(612.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1133.53,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 285,
    label = "BrH_182",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49627,0.000335913,-2.49609e-06,5.40075e-09,-2.96952e-12,-5353.39,3.90951], Tmin=(10,'K'), Tmax=(727.155,'K')),
            NASAPolynomial(coeffs=[3.11763,0.000746544,1.06363e-07,-1.47789e-10,2.54112e-14,-5254.11,5.91957], Tmin=(727.155,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.5103,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 10035-10-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 286,
    label = "C6H14_189",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46997,0.0586056,-0.00015974,4.89889e-07,-4.61206e-10,-23053.3,8.18301], Tmin=(10,'K'), Tmax=(419.843,'K')),
            NASAPolynomial(coeffs=[-4.05347,0.0783309,-4.45976e-05,1.23156e-08,-1.32441e-12,-21963.6,43.4029], Tmin=(419.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-191.693,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 110-54-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 287,
    label = "C3H6O2_321",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {5,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9283,0.00477694,0.000131538,-2.8548e-07,1.96495e-10,-38527.1,8.39025], Tmin=(10,'K'), Tmax=(450.934,'K')),
            NASAPolynomial(coeffs=[1.58913,0.0384299,-2.33285e-05,6.93315e-09,-8.00882e-13,-38447.3,16.3578], Tmin=(450.934,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-320.343,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 4453-91-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 288,
    label = "CHCl2_42",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95707,0.00256024,3.60535e-05,-7.85752e-08,4.91189e-11,9363.45,8.8156], Tmin=(10,'K'), Tmax=(563.536,'K')),
            NASAPolynomial(coeffs=[4.45875,0.00872822,-6.26033e-06,2.11757e-09,-2.69306e-13,9152.42,5.31238], Tmin=(563.536,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.8357,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3474-12-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 289,
    label = "C6H12_307",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03847,-0.0033239,0.000184941,-2.78442e-07,1.35706e-10,-17011.2,8.11179], Tmin=(10,'K'), Tmax=(576.678,'K')),
            NASAPolynomial(coeffs=[-6.35352,0.0770376,-4.56243e-05,1.29996e-08,-1.43194e-12,-15950.3,51.3329], Tmin=(576.678,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-141.446,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 110-82-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 290,
    label = "C2N2_317",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 N u0 p1 c0 {1,T}
4 N u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45272,0.00315546,3.8217e-05,-1.00191e-07,7.51803e-11,35971.7,6.38484], Tmin=(10,'K'), Tmax=(474.679,'K')),
            NASAPolynomial(coeffs=[4.06018,0.00737582,-4.63178e-06,1.43719e-09,-1.74427e-13,35808.8,2.79856], Tmin=(474.679,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (299.077,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 460-19-5*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 291,
    label = "CH2O2_194",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07352,-0.00563249,5.32066e-05,-7.64509e-08,3.59311e-11,-46806.7,6.5751], Tmin=(10,'K'), Tmax=(656.88,'K')),
            NASAPolynomial(coeffs=[1.92743,0.0144309,-8.58197e-06,2.46958e-09,-2.74749e-13,-46675.7,14.8781], Tmin=(656.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-389.166,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 64-18-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 292,
    label = "F2O3_211",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u0 p2 c0 {1,S} {3,S}
5 O u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85005,0.0104412,7.78053e-05,-2.34512e-07,1.87269e-10,10958.2,9.35014], Tmin=(10,'K'), Tmax=(464.359,'K')),
            NASAPolynomial(coeffs=[6.15045,0.0143839,-1.16765e-05,4.13647e-09,-5.32616e-13,10488.4,-2.74145], Tmin=(464.359,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.0921,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 16829-28-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 293,
    label = "C4H8O_348",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83152,0.0162276,5.78653e-05,-9.00108e-08,3.93691e-11,-18546.8,8.41458], Tmin=(10,'K'), Tmax=(740.667,'K')),
            NASAPolynomial(coeffs=[0.602183,0.0456138,-2.58409e-05,7.10824e-09,-7.61968e-13,-18396.1,20.8128], Tmin=(740.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 109-92-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 294,
    label = "CHFO_208",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05454,-0.00381435,3.27768e-05,-4.25471e-08,1.79e-11,-47225.4,6.56862], Tmin=(10,'K'), Tmax=(736.141,'K')),
            NASAPolynomial(coeffs=[2.3049,0.0105357,-6.33159e-06,1.80718e-09,-1.9814e-13,-47099,13.5824], Tmin=(736.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-392.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 1493-02-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 295,
    label = "H2O2_120",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99389,0.000388605,2.08779e-05,-3.83532e-08,2.32968e-11,-17621.2,4.53827], Tmin=(10,'K'), Tmax=(422.556,'K')),
            NASAPolynomial(coeffs=[3.24868,0.00744818,-4.20106e-06,1.24347e-09,-1.47551e-13,-17558.2,7.49097], Tmin=(422.556,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-146.512,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7722-84-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 296,
    label = "CH3O2_28",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97763,0.00129211,4.05515e-05,-6.75921e-08,3.66201e-11,27.4525,6.95791], Tmin=(10,'K'), Tmax=(475.102,'K')),
            NASAPolynomial(coeffs=[2.09874,0.017111,-9.39239e-06,2.48978e-09,-2.57367e-13,205.984,14.6241], Tmin=(475.102,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (0.216895,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2143-58-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 297,
    label = "CBrCl2F_14",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80865,0.0136762,8.95443e-05,-3.05743e-07,2.64737e-10,-30919.1,12.4026], Tmin=(10,'K'), Tmax=(441.826,'K')),
            NASAPolynomial(coeffs=[7.45181,0.0118126,-9.77836e-06,3.53766e-09,-4.6488e-13,-31544.8,-5.63498], Tmin=(441.826,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-257.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 353-58-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 298,
    label = "FHO_164",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02864,-0.00195562,1.38225e-05,-1.69813e-08,6.87949e-12,-11703.9,4.36071], Tmin=(10,'K'), Tmax=(756.574,'K')),
            NASAPolynomial(coeffs=[3.23673,0.00419182,-2.25282e-06,6.08938e-10,-6.48346e-14,-11640.2,7.58944], Tmin=(756.574,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.3062,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 14034-79-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 299,
    label = "C3H5_155",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17133,-0.0135436,0.000122018,-1.82317e-07,8.92829e-11,33562.6,6.60874], Tmin=(10,'K'), Tmax=(636.337,'K')),
            NASAPolynomial(coeffs=[0.0797977,0.0288995,-1.74527e-05,5.10322e-09,-5.75735e-13,33744.7,21.838], Tmin=(636.337,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (279.066,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2417-82-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 300,
    label = "C3H5O_215",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91861,0.00668587,8.49314e-05,-1.9375e-07,1.43275e-10,-5733.44,8.45025], Tmin=(10,'K'), Tmax=(346.029,'K')),
            NASAPolynomial(coeffs=[1.85577,0.0305319,-1.84394e-05,5.40728e-09,-6.1416e-13,-5590.68,16.2131], Tmin=(346.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-47.6737,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3122-07-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 301,
    label = "C2HO_236",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46935,0.00186211,3.0352e-05,-6.5004e-08,4.1157e-11,20143.8,6.49227], Tmin=(10,'K'), Tmax=(542.811,'K')),
            NASAPolynomial(coeffs=[3.59146,0.00780066,-4.95565e-06,1.56879e-09,-1.93342e-13,20029.8,5.04981], Tmin=(542.811,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (167.474,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 51095-15-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 302,
    label = "CH2Cl2_201",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98027,0.00114086,3.83781e-05,-6.75388e-08,3.70495e-11,-12768.8,8.3477], Tmin=(10,'K'), Tmax=(558.928,'K')),
            NASAPolynomial(coeffs=[2.58912,0.0151449,-1.00688e-05,3.20505e-09,-3.8917e-13,-12676.5,13.6842], Tmin=(558.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.174,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-09-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 303,
    label = "C7H16_175",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28052,0.0797048,-0.000253584,7.31278e-07,-6.71885e-10,-25959.1,9.32129], Tmin=(10,'K'), Tmax=(413.65,'K')),
            NASAPolynomial(coeffs=[-4.86174,0.0913121,-5.22513e-05,1.44774e-08,-1.56028e-12,-24711.2,48.3574], Tmin=(413.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-215.863,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (557.07,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 142-82-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 304,
    label = "C2HBr_382",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,D} {4,S}
2 Br u0 p3 c0 {1,S}
3 C  u0 p1 c0 {1,D}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95258,0.0032298,3.85525e-05,-1.02557e-07,7.84008e-11,53829.2,8.83403], Tmin=(10,'K'), Tmax=(461.778,'K')),
            NASAPolynomial(coeffs=[4.41071,0.00799379,-5.2881e-06,1.68623e-09,-2.05669e-13,53693.8,5.96969], Tmin=(461.778,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (447.555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 161957-27-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 305,
    label = "HNO2_378",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05963,-0.00363399,2.56519e-05,-2.79948e-08,9.83209e-12,-6528.13,6.32464], Tmin=(10,'K'), Tmax=(883.166,'K')),
            NASAPolynomial(coeffs=[1.89433,0.0106139,-6.08973e-06,1.6592e-09,-1.7383e-13,-6318.85,15.5214], Tmin=(883.166,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.2617,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 90266-90-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 306,
    label = "CClF2_403",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95079,0.00285264,4.13421e-05,-8.6859e-08,5.19481e-11,-34705,9.25042], Tmin=(10,'K'), Tmax=(588.262,'K')),
            NASAPolynomial(coeffs=[4.46152,0.0109008,-8.55666e-06,2.98275e-09,-3.81482e-13,-34964.4,5.3631], Tmin=(588.262,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-288.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 307,
    label = "CH3NO2_342",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0909,-0.00689831,7.35427e-05,-1.03845e-07,4.79136e-11,-10368.5,7.11455], Tmin=(10,'K'), Tmax=(658.002,'K')),
            NASAPolynomial(coeffs=[0.60586,0.0227596,-1.33802e-05,3.79101e-09,-4.15906e-13,-10093.2,21.0755], Tmin=(658.002,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.199,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 75-52-5*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 308,
    label = "C2H2Cl4_398",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
6 Cl u0 p3 c0 {2,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6898,0.0251047,0.000102499,-3.9986e-07,3.83726e-10,-20924.1,11.8306], Tmin=(10,'K'), Tmax=(395.374,'K')),
            NASAPolynomial(coeffs=[6.77811,0.0254361,-1.85529e-05,6.24831e-09,-7.84914e-13,-21415.1,-3.32406], Tmin=(395.374,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-173.963,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 630-20-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 309,
    label = "Cl2_27",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48687,0.00076201,8.40368e-06,-1.91499e-08,1.18609e-11,-1114.87,6.49204], Tmin=(10,'K'), Tmax=(594.632,'K')),
            NASAPolynomial(coeffs=[3.82659,0.00155672,-1.37039e-06,5.18774e-10,-7.05036e-14,-1209.73,4.57183], Tmin=(594.632,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.27499,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7782-50-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 310,
    label = "C2H2Cl2_213",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {3,S} {5,S}
2 C  u0 p0 c0 {1,D} {4,S} {6,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94123,0.00349411,6.3534e-05,-1.29494e-07,7.83866e-11,-1895.32,9.53612], Tmin=(10,'K'), Tmax=(558.358,'K')),
            NASAPolynomial(coeffs=[3.68752,0.0185905,-1.26947e-05,4.11429e-09,-5.05794e-13,-2073.98,8.75869], Tmin=(558.358,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.7815,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 540-59-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 311,
    label = "CH2ClO_161",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {5,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96668,0.00190167,4.08293e-05,-7.63218e-08,4.28974e-11,-8808.91,8.41452], Tmin=(10,'K'), Tmax=(590.003,'K')),
            NASAPolynomial(coeffs=[3.40539,0.0136427,-9.19611e-06,3.00071e-09,-3.73278e-13,-8880.8,9.65574], Tmin=(590.003,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.2561,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 147139-06-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 312,
    label = "C3H5O2_274",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82693,0.0154018,7.18635e-05,-1.95037e-07,1.62742e-10,-28441.7,8.30615], Tmin=(10,'K'), Tmax=(307.82,'K')),
            NASAPolynomial(coeffs=[2.35946,0.034471,-2.10607e-05,6.21532e-09,-7.08317e-13,-28351.3,13.6568], Tmin=(307.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.48,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 54668-31-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 313,
    label = "BrCl_195",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47954,0.00130928,1.0413e-05,-2.98483e-08,2.20765e-11,597.706,8.40259], Tmin=(10,'K'), Tmax=(517.008,'K')),
            NASAPolynomial(coeffs=[4.04506,0.00108603,-9.85669e-07,3.83365e-10,-5.332e-14,483.74,5.5107], Tmin=(517.008,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.96411,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 13863-41-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 314,
    label = "C2H2F4_413",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 F u0 p3 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84756,0.0141298,5.17126e-05,-1.1109e-07,6.35084e-11,-111453,9.52576], Tmin=(10,'K'), Tmax=(614.496,'K')),
            NASAPolynomial(coeffs=[4.23373,0.0271298,-1.78901e-05,5.50662e-09,-6.42179e-13,-111793,5.46751], Tmin=(614.496,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-926.696,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 315,
    label = "Cl2O2_78",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8786,0.00839001,6.01079e-05,-1.91818e-07,1.57474e-10,14039.7,10.453], Tmin=(10,'K'), Tmax=(463.177,'K')),
            NASAPolynomial(coeffs=[6.36186,0.00798594,-6.72579e-06,2.45711e-09,-3.24656e-13,13584,-2.0525], Tmin=(463.177,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12292-23-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 316,
    label = "C2H5O_62",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93622,0.00464756,5.78695e-05,-1.1138e-07,6.91234e-11,-8400.69,6.66949], Tmin=(10,'K'), Tmax=(413.913,'K')),
            NASAPolynomial(coeffs=[1.89556,0.0243682,-1.35971e-05,3.72678e-09,-4.00255e-13,-8231.76,14.7144], Tmin=(413.913,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.8624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2348-46-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 317,
    label = "CBr2ClF_41",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76847,0.017678,8.62865e-05,-3.48425e-07,3.35757e-10,-24679,13.2787], Tmin=(10,'K'), Tmax=(406.354,'K')),
            NASAPolynomial(coeffs=[7.65661,0.0115328,-9.62571e-06,3.49886e-09,-4.60985e-13,-25260.2,-5.24179], Tmin=(406.354,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-205.188,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 353-55-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 318,
    label = "C2H4F_414",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 F u0 p3 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97193,0.00172276,5.57309e-05,-1.01153e-07,6.01572e-11,-10487.9,6.81928], Tmin=(10,'K'), Tmax=(431.16,'K')),
            NASAPolynomial(coeffs=[1.88137,0.0211175,-1.17431e-05,3.1768e-09,-3.36267e-13,-10307.7,15.1463], Tmin=(431.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.2137,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 319,
    label = "C3H7_143",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77149,0.0245727,-6.39547e-05,1.85609e-07,-1.6461e-10,8699.89,5.12721], Tmin=(10,'K'), Tmax=(446.727,'K')),
            NASAPolynomial(coeffs=[0.281201,0.0333812,-1.81718e-05,4.82376e-09,-5.01403e-13,9235.68,21.6599], Tmin=(446.727,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.3322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2025-55-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 320,
    label = "H2O_107",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0047,-0.000234947,7.23287e-07,1.59163e-09,-1.22898e-12,-30277.9,-0.0974083], Tmin=(10,'K'), Tmax=(783.278,'K')),
            NASAPolynomial(coeffs=[3.51049,0.00103974,6.74289e-07,-4.0262e-10,5.73404e-14,-30162.2,2.41074], Tmin=(783.278,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-251.743,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 7732-18-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 321,
    label = "C3H8O_133",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89765,0.00711322,0.000103856,-2.05997e-07,1.33002e-10,-34952.7,6.39446], Tmin=(10,'K'), Tmax=(396.54,'K')),
            NASAPolynomial(coeffs=[0.593679,0.0404413,-2.22158e-05,5.95583e-09,-6.25299e-13,-34690.7,19.2781], Tmin=(396.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-290.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67-63-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 322,
    label = "C2H3O2_29",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94655,0.00505632,0.000120378,-4.49956e-07,5.50903e-10,-21065.7,7.97722], Tmin=(10,'K'), Tmax=(250.674,'K')),
            NASAPolynomial(coeffs=[3.3283,0.0211402,-1.30765e-05,3.92851e-09,-4.56769e-13,-21054.2,9.7148], Tmin=(250.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.138,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 3122-12-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 323,
    label = "C4H10_113",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84463,0.0109791,8.09983e-05,-1.26334e-07,6.11396e-11,-18319.6,4.28917], Tmin=(10,'K'), Tmax=(538.97,'K')),
            NASAPolynomial(coeffs=[-1.37562,0.0497213,-2.68238e-05,7.0333e-09,-7.22118e-13,-17756.9,26.2473], Tmin=(538.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-152.357,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-28-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 324,
    label = "C4H10_170",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9032,0.0156417,4.51359e-05,-5.54442e-08,1.85806e-11,-17281.9,5.56281], Tmin=(10,'K'), Tmax=(1012.37,'K')),
            NASAPolynomial(coeffs=[0.815353,0.0446397,-2.2718e-05,5.62836e-09,-5.48242e-13,-17517.5,16.2465], Tmin=(1012.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.656,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 106-97-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 325,
    label = "O2_284",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50685,-0.000393636,1.16281e-06,1.56496e-09,-1.94016e-12,10311.7,3.59324], Tmin=(10,'K'), Tmax=(642.779,'K')),
            NASAPolynomial(coeffs=[2.87884,0.00202656,-1.01275e-06,2.20064e-10,-1.64065e-14,10423.1,6.58461], Tmin=(642.779,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (85.7388,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 12185-07-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 326,
    label = "C2H4F2_150",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96966,0.00171885,6.4435e-05,-1.05184e-07,5.52545e-11,-55522.2,8.41513], Tmin=(10,'K'), Tmax=(492.957,'K')),
            NASAPolynomial(coeffs=[0.6741,0.0284576,-1.692e-05,4.82871e-09,-5.32952e-13,-55197.3,21.9836], Tmin=(492.957,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-461.653,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 624-72-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 327,
    label = "C8H6_354",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {3,D} {5,S} {12,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8804,0.00698184,0.000169787,-3.19191e-07,1.83008e-10,35729.5,10.3136], Tmin=(10,'K'), Tmax=(564.067,'K')),
            NASAPolynomial(coeffs=[0.393647,0.0586421,-3.92169e-05,1.24825e-08,-1.51242e-12,35694.4,21.3405], Tmin=(564.067,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (297.022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 536-74-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 328,
    label = "CCl2O_130",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93289,0.00415779,4.62396e-05,-1.12959e-07,7.63841e-11,-27934.2,9.29154], Tmin=(10,'K'), Tmax=(537.137,'K')),
            NASAPolynomial(coeffs=[5.20599,0.00893308,-6.90673e-06,2.41442e-09,-3.11877e-13,-28276.6,2.02643], Tmin=(537.137,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.28,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-44-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 329,
    label = "C3_313",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 C u0 p1 c0 {1,D}
3 C u0 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88514,0.0106406,-4.07153e-05,7.65227e-08,-5.02237e-11,97661.5,2.19172], Tmin=(10,'K'), Tmax=(502.626,'K')),
            NASAPolynomial(coeffs=[3.9221,0.00405011,-2.25696e-06,5.89878e-10,-5.93377e-14,97737.3,2.83001], Tmin=(502.626,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (812.002,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 12075-35-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 330,
    label = "C2H2O4_61",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {6,S} {8,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 C u0 p0 c0 {2,S} {4,D} {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90167,0.00609675,0.000102085,-2.22734e-07,1.44006e-10,-89953.6,9.58617], Tmin=(10,'K'), Tmax=(525.194,'K')),
            NASAPolynomial(coeffs=[3.79426,0.0276785,-1.88571e-05,6.06358e-09,-7.38239e-13,-90228.7,7.30898], Tmin=(525.194,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-747.948,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 144-62-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 331,
    label = "C3O2_91",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,D} {5,D}
4 C u0 p0 c0 {1,D} {3,D}
5 C u0 p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88222,0.0099638,2.16098e-05,-6.40157e-08,4.55885e-11,-12846.4,7.57117], Tmin=(10,'K'), Tmax=(509.68,'K')),
            NASAPolynomial(coeffs=[4.32692,0.0134273,-9.04764e-06,2.85219e-09,-3.4009e-13,-12982.1,4.83945], Tmin=(509.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.826,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 504-64-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 332,
    label = "C3H4_94",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14812,-0.0113958,9.78159e-05,-1.41349e-07,6.69712e-11,32764.6,5.7085], Tmin=(10,'K'), Tmax=(655.919,'K')),
            NASAPolynomial(coeffs=[0.522451,0.0242192,-1.45138e-05,4.21072e-09,-4.71694e-13,32949.7,19.4568], Tmin=(655.919,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (272.434,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2781-85-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 333,
    label = "CCl4_220",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79104,0.0148036,9.54102e-05,-3.29156e-07,2.84438e-10,-13617.5,9.51612], Tmin=(10,'K'), Tmax=(446.679,'K')),
            NASAPolynomial(coeffs=[8.17782,0.0107311,-9.15642e-06,3.38575e-09,-4.52249e-13,-14360.6,-12.0442], Tmin=(446.679,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-113.239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 56-23-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 334,
    label = "C2N2_368",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 C u0 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94031,0.00488523,4.26699e-05,-1.45841e-07,1.42821e-10,99457.5,6.61827], Tmin=(10,'K'), Tmax=(355.72,'K')),
            NASAPolynomial(coeffs=[4.15304,0.00953128,-6.60015e-06,2.11906e-09,-2.56716e-13,99397.8,5.18594], Tmin=(355.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (826.944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 204253-88-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 335,
    label = "C2H4O2_79",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95937,0.0104969,1.66635e-05,-2.18299e-08,7.08908e-12,-45020,7.02192], Tmin=(10,'K'), Tmax=(1109.14,'K')),
            NASAPolynomial(coeffs=[4.17469,0.0198811,-9.76895e-06,2.31729e-09,-2.15391e-13,-45692.7,3.14344], Tmin=(1109.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-374.291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-31-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 336,
    label = "H4N2_386",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.057,-0.00445017,4.97255e-05,-7.11012e-08,3.42413e-11,10389.8,4.24397], Tmin=(10,'K'), Tmax=(585.924,'K')),
            NASAPolynomial(coeffs=[1.52648,0.0154366,-7.87083e-06,2.03861e-09,-2.11214e-13,10641.5,14.717], Tmin=(585.924,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.3902,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 302-01-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 337,
    label = "H3NO_385",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03182,-0.00243167,3.30571e-05,-4.65703e-08,2.1977e-11,-6547.5,4.78664], Tmin=(10,'K'), Tmax=(591.753,'K')),
            NASAPolynomial(coeffs=[2.21479,0.0113659,-5.75836e-06,1.48613e-09,-1.53601e-13,-6358.98,12.3753], Tmin=(591.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.436,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 7803-49-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 338,
    label = "N2O5_343",
    molecule = 
"""
1 O u0 p2 c0 {6,S} {7,S}
2 O u0 p3 c-1 {6,S}
3 O u0 p3 c-1 {7,S}
4 O u0 p2 c0 {6,D}
5 O u0 p2 c0 {7,D}
6 N u0 p0 c+1 {1,S} {2,S} {4,D}
7 N u0 p0 c+1 {1,S} {3,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85385,0.0265333,-1.58219e-05,1.0236e-09,1.34593e-12,-402.416,11.2471], Tmin=(10,'K'), Tmax=(1127.14,'K')),
            NASAPolynomial(coeffs=[10.2156,0.0117702,-6.57364e-06,1.70391e-09,-1.69115e-13,-2332.88,-22.408], Tmin=(1127.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.30745,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 10102-03-1*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 339,
    label = "C4H6_80",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96487,0.00206041,8.9144e-05,-1.51294e-07,8.30009e-11,11530.9,7.31034], Tmin=(10,'K'), Tmax=(470.858,'K')),
            NASAPolynomial(coeffs=[-0.175694,0.0371868,-2.26033e-05,6.70595e-09,-7.72998e-13,11921.3,24.1732], Tmin=(470.858,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.8569,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 106-99-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 340,
    label = "C2H4O_132",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1569,-0.0108647,8.22186e-05,-1.04447e-07,4.32871e-11,-7621.15,5.91143], Tmin=(10,'K'), Tmax=(747.065,'K')),
            NASAPolynomial(coeffs=[-0.24913,0.0250654,-1.46989e-05,4.14926e-09,-4.52254e-13,-7307.15,23.5787], Tmin=(747.065,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.3354,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-21-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 341,
    label = "CHO3_264",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96918,0.00168968,4.29804e-05,-7.4804e-08,3.90706e-11,-45407.2,8.41243], Tmin=(10,'K'), Tmax=(621.724,'K')),
            NASAPolynomial(coeffs=[2.71648,0.0172538,-1.2676e-05,4.29017e-09,-5.40462e-13,-45396.5,12.6942], Tmin=(621.724,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-377.552,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 38330-85-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 342,
    label = "Br_97",
    molecule = 
"""
multiplicity 2
1 Br u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,12707.6,6.07964], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,12707.6,6.07964], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (105.657,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 10097-32-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 343,
    label = "C3H6O_35",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98981,0.0131058,2.35999e-05,-3.01697e-08,9.78421e-12,-24388.6,7.15611], Tmin=(10,'K'), Tmax=(1103.73,'K')),
            NASAPolynomial(coeffs=[4.26698,0.0258648,-1.24448e-05,2.89982e-09,-2.65248e-13,-25288.2,1.99382], Tmin=(1103.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.73,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 123-38-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 344,
    label = "C3H3_71",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94036,0.00373843,5.95442e-05,-1.3337e-07,8.8716e-11,40617,5.51291], Tmin=(10,'K'), Tmax=(517.042,'K')),
            NASAPolynomial(coeffs=[4.2311,0.0143581,-8.59898e-06,2.63142e-09,-3.19029e-13,40414.9,2.6386], Tmin=(517.042,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (337.691,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2932-78-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 345,
    label = "C3H4O_266",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97197,0.00172712,7.29656e-05,-1.32866e-07,7.88746e-11,-9544.9,8.14436], Tmin=(10,'K'), Tmax=(433.314,'K')),
            NASAPolynomial(coeffs=[1.17156,0.0275765,-1.65107e-05,4.78629e-09,-5.38491e-13,-9302.2,19.3129], Tmin=(433.314,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.3713,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 107-02-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 346,
    label = "C2Cl6_227",
    molecule = 
"""
1 Cl u0 p3 c0 {7,S}
2 Cl u0 p3 c0 {7,S}
3 Cl u0 p3 c0 {7,S}
4 Cl u0 p3 c0 {8,S}
5 Cl u0 p3 c0 {8,S}
6 Cl u0 p3 c0 {8,S}
7 C  u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44498,0.0444584,0.000146678,-7.05825e-07,7.32586e-10,-21216,11.4678], Tmin=(10,'K'), Tmax=(388.99,'K')),
            NASAPolynomial(coeffs=[11.8654,0.0226928,-1.93536e-05,7.12425e-09,-9.45622e-13,-22361.5,-27.5091], Tmin=(388.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-176.372,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 67-72-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 347,
    label = "C2HCl3_145",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {5,D} {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84338,0.0112268,9.2427e-05,-2.84151e-07,2.37328e-10,-3778.47,11.8198], Tmin=(10,'K'), Tmax=(438.247,'K')),
            NASAPolynomial(coeffs=[5.88886,0.0172457,-1.26764e-05,4.27974e-09,-5.38021e-13,-4194.84,0.934016], Tmin=(438.247,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.4261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 79-01-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 348,
    label = "C2H3O_181",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0683,-0.00648803,8.46575e-05,-1.49131e-07,8.69218e-11,480.005,7.29798], Tmin=(10,'K'), Tmax=(521.688,'K')),
            NASAPolynomial(coeffs=[1.8162,0.0188585,-1.14497e-05,3.36847e-09,-3.83114e-13,605.05,15.644], Tmin=(521.688,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.98683,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 6912-06-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 349,
    label = "CHO_48",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01463,-0.000868486,4.70369e-06,2.81271e-10,-2.87058e-12,3825.15,4.15731], Tmin=(10,'K'), Tmax=(623.103,'K')),
            NASAPolynomial(coeffs=[2.68378,0.00485379,-2.28031e-06,4.87451e-10,-3.80178e-14,4045.77,10.3878], Tmin=(623.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (31.8096,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2597-44-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 350,
    label = "CBr4_224",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 Br u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55007,0.0413244,-6.66637e-06,-2.76541e-07,4.06341e-10,9932.32,12.4922], Tmin=(10,'K'), Tmax=(341.805,'K')),
            NASAPolynomial(coeffs=[9.03791,0.00940142,-8.31636e-06,3.13662e-09,-4.23561e-13,9368.49,-10.8521], Tmin=(341.805,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.6149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 558-13-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 351,
    label = "C2H5O_75",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91928,0.00895798,2.20621e-05,-2.93549e-08,1.04934e-11,-3141.01,6.65772], Tmin=(10,'K'), Tmax=(940.569,'K')),
            NASAPolynomial(coeffs=[2.25161,0.0232731,-1.22863e-05,3.15556e-09,-3.17897e-13,-3146.8,12.9026], Tmin=(940.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.1084,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2154-50-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 352,
    label = "C2H3_118",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07297,-0.00594472,5.36048e-05,-8.06356e-08,4.06161e-11,34430.9,4.92904], Tmin=(10,'K'), Tmax=(591.105,'K')),
            NASAPolynomial(coeffs=[1.95224,0.0132533,-7.4126e-06,2.05398e-09,-2.23489e-13,34596.9,13.3291], Tmin=(591.105,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (286.278,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2669-89-8*0 and used to tweak g4 calculation
""",
)

entry(
    index = 353,
    label = "CH2O2_346",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p1 c+1 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07501,-0.00636449,6.69272e-05,-1.08187e-07,5.70556e-11,11278.5,5.83342], Tmin=(10,'K'), Tmax=(595.631,'K')),
            NASAPolynomial(coeffs=[2.29676,0.0147152,-9.17069e-06,2.74272e-09,-3.14764e-13,11328.2,12.1304], Tmin=(595.631,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.7743,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 56077-92-0*0 and used to tweak g4 calculation
""",
)

entry(
    index = 354,
    label = "C2H2_151",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99374,0.000547555,3.44085e-05,-1.02595e-07,1.06564e-10,48205.6,3.13141], Tmin=(10,'K'), Tmax=(242.411,'K')),
            NASAPolynomial(coeffs=[3.62607,0.00661682,-3.16166e-06,7.68553e-10,-7.68408e-14,48223.4,4.38404], Tmin=(242.411,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (400.807,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2143-69-3*0 and used to tweak g4 calculation
""",
)

entry(
    index = 355,
    label = "C2H4_38",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u2 p0 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98422,0.000789378,3.2695e-05,-4.65535e-08,2.1459e-11,41191.8,4.9828], Tmin=(10,'K'), Tmax=(560.677,'K')),
            NASAPolynomial(coeffs=[1.84431,0.0160558,-8.14736e-06,2.00899e-09,-1.9429e-13,41431.8,14.0685], Tmin=(560.677,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (342.479,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 4218-50-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 356,
    label = "CHF_55",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01851,-0.0011767,5.53482e-06,1.84561e-09,-5.60759e-12,16684.6,4.04236], Tmin=(10,'K'), Tmax=(556.082,'K')),
            NASAPolynomial(coeffs=[2.62639,0.00538053,-2.82899e-06,6.94526e-10,-6.46918e-14,16892.8,10.4221], Tmin=(556.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.729,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 13453-52-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 357,
    label = "H2O3_70",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95626,0.0025465,4.35236e-05,-8.74864e-08,5.18123e-11,-12428.1,6.03357], Tmin=(10,'K'), Tmax=(579.327,'K')),
            NASAPolynomial(coeffs=[4.04355,0.0122349,-8.20759e-06,2.70696e-09,-3.4149e-13,-12610.9,4.16962], Tmin=(579.327,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-103.351,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 14699-99-1*0 and used to tweak g4 calculation
""",
)

entry(
    index = 358,
    label = "C2H3ClO_57",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {4,D}
3 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C  u0 p0 c0 {1,S} {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94764,0.00410824,9.20057e-05,-2.54823e-07,2.2592e-10,-30830.8,8.33583], Tmin=(10,'K'), Tmax=(350.608,'K')),
            NASAPolynomial(coeffs=[3.05749,0.0214813,-1.32004e-05,3.93725e-09,-4.55064e-13,-30812.7,11.0647], Tmin=(350.608,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-36-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 359,
    label = "CH2O_136",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05926,-0.00354413,2.22747e-05,-2.3011e-08,7.73129e-12,11890.6,4.19267], Tmin=(10,'K'), Tmax=(912.571,'K')),
            NASAPolynomial(coeffs=[1.9594,0.00933136,-4.92348e-06,1.26679e-09,-1.27345e-13,12121,13.2936], Tmin=(912.571,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.88,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 19710-56-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 360,
    label = "HNO3_389",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92093,0.00556975,6.0011e-05,-1.68743e-07,1.35243e-10,-3075.96,7.92843], Tmin=(10,'K'), Tmax=(442.123,'K')),
            NASAPolynomial(coeffs=[4.6447,0.0123753,-8.38407e-06,2.70334e-09,-3.30857e-13,-3270.48,3.55135], Tmin=(442.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-25.5813,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 14691-52-2*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 361,
    label = "CH3O_125",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04544,-0.00430255,5.67278e-05,-1.04626e-07,6.53281e-11,-3370.74,4.63246], Tmin=(10,'K'), Tmax=(471.266,'K')),
            NASAPolynomial(coeffs=[2.60701,0.0117118,-6.35621e-06,1.74855e-09,-1.91134e-13,-3277.42,10.0416], Tmin=(471.266,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-28.0268,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 2597-43-5*0 and used to tweak g4 calculation
""",
)

entry(
    index = 362,
    label = "CCl2F_411",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92186,0.00489228,5.05502e-05,-1.27783e-07,8.82588e-11,-12966.7,10.1532], Tmin=(10,'K'), Tmax=(530.424,'K')),
            NASAPolynomial(coeffs=[5.49822,0.00919927,-7.42645e-06,2.64507e-09,-3.44062e-13,-13361.7,1.40029], Tmin=(530.424,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-107.835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 363,
    label = "CH2F_404",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03345,-0.00266443,2.81896e-05,-4.05508e-08,1.95706e-11,-4916.65,4.51046], Tmin=(10,'K'), Tmax=(587.628,'K')),
            NASAPolynomial(coeffs=[2.5976,0.0086642,-4.697e-06,1.26165e-09,-1.33625e-13,-4774.75,10.4458], Tmin=(587.628,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.8769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 364,
    label = "C4H8_165",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95132,0.00282321,0.000104077,-1.74422e-07,9.49977e-11,-1914.48,7.61399], Tmin=(10,'K'), Tmax=(473.367,'K')),
            NASAPolynomial(coeffs=[-0.848903,0.0433993,-2.4544e-05,6.78276e-09,-7.3456e-13,-1460.19,27.1806], Tmin=(473.367,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.9419,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 106-98-9*0 and used to tweak g4 calculation
""",
)

entry(
    index = 365,
    label = "C2H3Cl_44",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07706,-0.00721557,9.05844e-05,-1.60498e-07,9.32817e-11,1188.85,7.86541], Tmin=(10,'K'), Tmax=(537.056,'K')),
            NASAPolynomial(coeffs=[2.06966,0.0185075,-1.13464e-05,3.37892e-09,-3.88422e-13,1249.12,14.8558], Tmin=(537.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.87916,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-01-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 366,
    label = "CFN_358",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 N u0 p1 c0 {3,T}
3 C u0 p0 c0 {1,S} {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47941,0.00121208,2.15265e-05,-4.36029e-08,2.61034e-11,-109.994,6.00956], Tmin=(10,'K'), Tmax=(567.978,'K')),
            NASAPolynomial(coeffs=[3.43741,0.00624857,-4.29461e-06,1.40024e-09,-1.73433e-13,-181.692,5.51525], Tmin=(567.978,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-0.922812,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 1495-50-7*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 367,
    label = "HN3_306",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06047,-0.00460551,4.12095e-05,-5.95331e-08,2.79118e-11,53771.8,5.47239], Tmin=(10,'K'), Tmax=(671.42,'K')),
            NASAPolynomial(coeffs=[2.60656,0.0104056,-6.51124e-06,1.93422e-09,-2.19541e-13,53823.9,10.8417], Tmin=(671.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (447.09,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 157-29-9*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 368,
    label = "C2H3O_253",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06828,-0.00648706,8.46644e-05,-1.49163e-07,8.69525e-11,455.901,6.60484], Tmin=(10,'K'), Tmax=(521.603,'K')),
            NASAPolynomial(coeffs=[1.81647,0.0188583,-1.14496e-05,3.3685e-09,-3.83122e-13,580.937,14.9497], Tmin=(521.603,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.78642,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 6912-06-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 369,
    label = "C2H4F2_196",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97288,0.00163521,7.24654e-05,-1.27905e-07,7.31101e-11,-62161.6,7.43444], Tmin=(10,'K'), Tmax=(451.834,'K')),
            NASAPolynomial(coeffs=[0.90349,0.0288149,-1.77887e-05,5.29551e-09,-6.08836e-13,-61884.3,19.8032], Tmin=(451.834,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-516.852,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-37-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 370,
    label = "C2Br2_271",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,D}
2 Br u0 p3 c0 {1,S}
3 Br u0 p3 c0 {1,S}
4 C  u0 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63763,0.0242996,-4.29209e-05,3.54307e-08,-1.09675e-11,58142.7,11.7871], Tmin=(10,'K'), Tmax=(940.334,'K')),
            NASAPolynomial(coeffs=[6.75898,0.0053267,-3.57084e-06,1.09188e-09,-1.25701e-13,57807.5,-1.74068], Tmin=(940.334,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (483.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 261771-36-2*0 and used to tweak g4 calculation
""",
)

entry(
    index = 371,
    label = "H3NO_379",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 O u0 p3 c-1 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07654,-0.0044601,2.8069e-05,-2.74923e-08,8.781e-12,5990.01,3.67599], Tmin=(10,'K'), Tmax=(945.754,'K')),
            NASAPolynomial(coeffs=[0.939818,0.0130429,-6.41048e-06,1.54884e-09,-1.47707e-13,6393.86,17.6323], Tmin=(945.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (49.8241,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 38544-48-8*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 372,
    label = "C2H7N_355",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
4  H u0 p0 c0 {2,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96407,0.00180871,6.25434e-05,-8.68189e-08,3.88563e-11,-3837.33,5.17337], Tmin=(10,'K'), Tmax=(578.312,'K')),
            NASAPolynomial(coeffs=[-0.423575,0.0321567,-1.61721e-05,3.92297e-09,-3.70797e-13,-3329.85,23.9383], Tmin=(578.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-m062x-gd3_jun-cc-pvtz""",
    longDesc = 
u"""
H298 taken from atct 124-40-3*0 and used to tweak m062x-gd3_jun-cc-pvtz calculation
""",
)

entry(
    index = 373,
    label = "CClF_419",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98034,0.00109405,1.88967e-05,-3.63431e-08,2.01631e-11,2394.01,7.66223], Tmin=(10,'K'), Tmax=(621.372,'K')),
            NASAPolynomial(coeffs=[3.97648,0.00600089,-4.73374e-06,1.65416e-09,-2.11756e-13,2300.25,6.92061], Tmin=(621.372,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (19.896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""diet-HEAT-F12-network-g4""",
    longDesc = 
u"""
H298 taken from diet-HEAT-F12-network  and used to tweak g4 calculation
""",
)

entry(
    index = 374,
    label = "C7H6O_212",
    molecule = 
"""
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {4,D} {6,S} {12,S}
8  C u0 p0 c0 {1,D} {2,S} {14,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91829,0.00485469,0.000164193,-2.99382e-07,1.70864e-10,-6793.38,10.684], Tmin=(10,'K'), Tmax=(534.239,'K')),
            NASAPolynomial(coeffs=[-1.56147,0.0619132,-4.10197e-05,1.2864e-08,-1.53512e-12,-6436.63,31.5443], Tmin=(534.239,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.5155,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 100-52-7*0 and used to tweak g4 calculation
""",
)

entry(
    index = 375,
    label = "C3H3_123",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 C u1 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10128,-0.00465758,3.35486e-05,-3.46245e-08,1.15184e-11,62013.5,5.5704], Tmin=(10,'K'), Tmax=(939.132,'K')),
            NASAPolynomial(coeffs=[1.28903,0.0139985,-6.91566e-06,1.6719e-09,-1.59483e-13,62247.2,17.3933], Tmin=(939.132,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (515.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (116.403,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 89342-91-6*0 and used to tweak g4 calculation
""",
)

entry(
    index = 376,
    label = "CH2ClF_32",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03925,-0.00319802,4.84959e-05,-7.42041e-08,3.66823e-11,-33040.1,8.19895], Tmin=(10,'K'), Tmax=(623.339,'K')),
            NASAPolynomial(coeffs=[2.18195,0.0146961,-8.94458e-06,2.60874e-09,-2.92905e-13,-32924.7,15.3502], Tmin=(623.339,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 593-70-4*0 and used to tweak g4 calculation
""",
)

entry(
    index = 377,
    label = "C2H5Cl_63",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99746,0.000135079,6.36011e-05,-9.97389e-08,5.09912e-11,-14993.6,7.16404], Tmin=(10,'K'), Tmax=(505.093,'K')),
            NASAPolynomial(coeffs=[0.649025,0.0266524,-1.51487e-05,4.20214e-09,-4.55277e-13,-14655.3,21.0313], Tmin=(505.093,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.668,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = u"""atct-g4""",
    longDesc = 
u"""
H298 taken from atct 75-00-3*0 and used to tweak g4 calculation
""",
)

