#!/usr/bin/env python
# encoding: utf-8

name = "CHOF_G4_library"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "F[CH]COF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77128,0.0232243,-3.7685e-06,-1.17437e-08,6.29369e-12,-14586.9,10.7794], Tmin=(10,'K'), Tmax=(903.557,'K')),
            NASAPolynomial(coeffs=[5.96217,0.0208513,-1.1991e-05,3.29645e-09,-3.50455e-13,-15281.9,-1.22306], Tmin=(903.557,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 1,
    label = "OC#CF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88872,0.00845003,6.82767e-05,-2.41296e-07,2.28464e-10,-2959.12,6.86217], Tmin=(10,'K'), Tmax=(394.091,'K')),
            NASAPolynomial(coeffs=[5.551,0.00979359,-6.17005e-06,1.92996e-09,-2.34963e-13,-3231.59,-1.40416], Tmin=(394.091,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.5975,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.029 kJ/mol
""",
    rank = 5,
)

entry(
    index = 2,
    label = "CC(F)[C]DO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86257,0.0128705,9.89406e-05,-3.56821e-07,4.20264e-10,-28617.6,10.283], Tmin=(10,'K'), Tmax=(215.028,'K')),
            NASAPolynomial(coeffs=[2.96293,0.029606,-1.7805e-05,5.13972e-09,-5.72543e-13,-28578.9,13.2404], Tmin=(215.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-237.928,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 3,
    label = "CC(O)(F)OF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {10,S}
4  F u0 p3 c0 {2,S}
5  O u0 p2 c0 {2,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82446,0.0126991,0.000144456,-3.90644e-07,3.10016e-10,-69166.6,10.4811], Tmin=(10,'K'), Tmax=(431.375,'K')),
            NASAPolynomial(coeffs=[4.16047,0.0353213,-2.3704e-05,7.5517e-09,-9.13102e-13,-69435.1,6.36684], Tmin=(431.375,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-575.093,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 4,
    label = "CC(F)O[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  F u0 p3 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79829,0.0294358,-1.36595e-07,-1.55098e-08,6.45216e-12,-58805,11.7588], Tmin=(10,'K'), Tmax=(1083.37,'K')),
            NASAPolynomial(coeffs=[7.66407,0.0273743,-1.41904e-05,3.54311e-09,-3.45519e-13,-60359.3,-10.5084], Tmin=(1083.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-488.901,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 5,
    label = "FCC#CC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,T}
4  C u0 p0 c0 {3,T} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53079,0.0499616,-0.000142123,3.49047e-07,-3.26455e-10,-49678.3,12.8891], Tmin=(10,'K'), Tmax=(355.522,'K')),
            NASAPolynomial(coeffs=[3.2609,0.0376113,-2.50961e-05,7.86482e-09,-9.34894e-13,-49561.9,15.2796], Tmin=(355.522,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-413.056,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.479 kJ/mol
""",
    rank = 5,
)

entry(
    index = 6,
    label = "FCDC[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80686,0.0151136,0.000100311,-3.06546e-07,2.61323e-10,-50419.7,10.6554], Tmin=(10,'K'), Tmax=(412.309,'K')),
            NASAPolynomial(coeffs=[4.60447,0.0276804,-1.92768e-05,6.25825e-09,-7.64801e-13,-50658.1,5.4211], Tmin=(412.309,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-419.214,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.026 kJ/mol
""",
    rank = 5,
)

entry(
    index = 7,
    label = "CC(O)(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {9,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9072,0.00579253,0.000109485,-2.3442e-07,1.51458e-10,-89524.2,8.26046], Tmin=(10,'K'), Tmax=(515.561,'K')),
            NASAPolynomial(coeffs=[3.18586,0.0308485,-2.00303e-05,6.26436e-09,-7.51165e-13,-89708.4,8.75452], Tmin=(515.561,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-744.375,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 8,
    label = "CDC1[C]DC1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91712,0.00500017,8.4413e-05,-1.78165e-07,1.10896e-10,51121,8.90151], Tmin=(10,'K'), Tmax=(547.937,'K')),
            NASAPolynomial(coeffs=[3.90593,0.0234112,-1.61653e-05,5.25684e-09,-6.46481e-13,50847,6.43793], Tmin=(547.937,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (425.013,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.354 kJ/mol
""",
    rank = 5,
)

entry(
    index = 9,
    label = "FOC1OC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89848,0.00658547,0.00010881,-2.47629e-07,1.68345e-10,-40037.6,10.7733], Tmin=(10,'K'), Tmax=(492.029,'K')),
            NASAPolynomial(coeffs=[3.34208,0.0301274,-2.09404e-05,6.73296e-09,-8.12815e-13,-40213.1,10.7236], Tmin=(492.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-332.916,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 10,
    label = "CD[C]CCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86803,0.0232933,1.00522e-05,-2.17901e-08,7.79564e-12,3120.96,10.1662], Tmin=(10,'K'), Tmax=(1103.36,'K')),
            NASAPolynomial(coeffs=[6.16011,0.0279593,-1.3931e-05,3.35905e-09,-3.17608e-13,1825.34,-4.69638], Tmin=(1103.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.9852,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.199 kJ/mol
""",
    rank = 5,
)

entry(
    index = 11,
    label = "OD[C]CDCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92491,0.00745903,0.000103979,-3.81613e-07,4.66361e-10,-13867.6,9.74537], Tmin=(10,'K'), Tmax=(207.034,'K')),
            NASAPolynomial(coeffs=[3.06695,0.0240353,-1.61183e-05,5.10844e-09,-6.14941e-13,-13832,12.5334], Tmin=(207.034,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.28,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.398 kJ/mol
""",
    rank = 5,
)

entry(
    index = 12,
    label = "FCDC1CDC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.886,0.00723517,0.000109215,-2.50856e-07,1.69131e-10,4517.4,10.4424], Tmin=(10,'K'), Tmax=(509.577,'K')),
            NASAPolynomial(coeffs=[4.24608,0.0275936,-1.89606e-05,6.11909e-09,-7.46553e-13,4179.69,5.99433], Tmin=(509.577,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.5281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.296 kJ/mol
""",
    rank = 5,
)

entry(
    index = 13,
    label = "FOC1CC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89804,0.00641189,0.00012961,-2.75915e-07,1.78415e-10,-22316.5,10.9081], Tmin=(10,'K'), Tmax=(507.528,'K')),
            NASAPolynomial(coeffs=[2.48326,0.0382242,-2.54777e-05,8.01568e-09,-9.57076e-13,-22439,14.1525], Tmin=(507.528,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-185.58,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 14,
    label = "COC(F)DCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84364,0.015311,0.000129833,-4.9901e-07,6.28482e-10,-58218.2,9.41744], Tmin=(10,'K'), Tmax=(200.969,'K')),
            NASAPolynomial(coeffs=[2.81714,0.035742,-2.26603e-05,6.85015e-09,-7.93435e-13,-58177,12.7226], Tmin=(200.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-484.025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.383 kJ/mol
""",
    rank = 5,
)

entry(
    index = 15,
    label = "C#CC[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86267,0.0113789,0.000113154,-3.35823e-07,3.01941e-10,20205.5,10.3086], Tmin=(10,'K'), Tmax=(363.615,'K')),
            NASAPolynomial(coeffs=[3.29565,0.0306082,-1.97651e-05,6.13933e-09,-7.30584e-13,20160.9,11.2895], Tmin=(363.615,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.799 kJ/mol
""",
    rank = 5,
)

entry(
    index = 16,
    label = "O[C]1CDC1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90789,0.00562694,8.69032e-05,-1.90086e-07,1.21499e-10,14399.8,9.89108], Tmin=(10,'K'), Tmax=(540.054,'K')),
            NASAPolynomial(coeffs=[4.3277,0.0225323,-1.56423e-05,5.12481e-09,-6.33934e-13,14062.6,5.42216], Tmin=(540.054,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (119.695,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 17,
    label = "[CH2]CDC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90954,0.00561901,9.85123e-05,-2.13222e-07,1.37737e-10,-28990.6,9.36891], Tmin=(10,'K'), Tmax=(522.151,'K')),
            NASAPolynomial(coeffs=[3.61262,0.0270314,-1.79776e-05,5.70326e-09,-6.89937e-13,-29220.5,8.11022], Tmin=(522.151,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-241.07,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.936 kJ/mol
""",
    rank = 5,
)

entry(
    index = 18,
    label = "FCD[C]C(F)CF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u1 p0 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50795,0.0531568,-0.000160562,4.24523e-07,-4.12326e-10,-39757.4,13.0028], Tmin=(10,'K'), Tmax=(354.16,'K')),
            NASAPolynomial(coeffs=[2.56078,0.0429104,-2.84587e-05,8.87381e-09,-1.05052e-12,-39559,18.4436], Tmin=(354.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-330.573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 19,
    label = "CC[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82493,0.0188896,2.28767e-05,-4.19243e-08,1.76677e-11,-40695.5,8.70345], Tmin=(10,'K'), Tmax=(848.356,'K')),
            NASAPolynomial(coeffs=[3.56408,0.030906,-1.74416e-05,4.74645e-09,-5.02095e-13,-41039.4,7.6313], Tmin=(848.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-338.358,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.766 kJ/mol
""",
    rank = 5,
)

entry(
    index = 20,
    label = "C#CC([O])(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8481,0.00977804,0.000109036,-2.77012e-07,1.96897e-10,-19134,10.9565], Tmin=(10,'K'), Tmax=(506.423,'K')),
            NASAPolynomial(coeffs=[6.15083,0.0217991,-1.60487e-05,5.44314e-09,-6.88081e-13,-19754.6,-2.41078], Tmin=(506.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-159.128,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 21,
    label = "FCDCOCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.935,0.0248145,2.34914e-06,-1.46739e-08,5.53834e-12,-60538.2,10.7935], Tmin=(10,'K'), Tmax=(1171.29,'K')),
            NASAPolynomial(coeffs=[9.10893,0.0207875,-9.96459e-06,2.27862e-09,-2.0245e-13,-62686,-18.9805], Tmin=(1171.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-503.284,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.383 kJ/mol
""",
    rank = 5,
)

entry(
    index = 22,
    label = "FC1(F)[CH]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92999,0.00395221,8.79684e-05,-1.61853e-07,8.92407e-11,-13920.7,9.43976], Tmin=(10,'K'), Tmax=(598.588,'K')),
            NASAPolynomial(coeffs=[2.38422,0.0310321,-2.18658e-05,7.2219e-09,-8.9773e-13,-14035.7,13.5973], Tmin=(598.588,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.775,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 23,
    label = "CC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7802,0.019532,4.23391e-05,-1.11958e-07,8.16368e-11,-37458.4,10.6377], Tmin=(10,'K'), Tmax=(359.012,'K')),
            NASAPolynomial(coeffs=[2.41209,0.0347752,-2.1349e-05,6.3083e-09,-7.18699e-13,-37360.2,15.8365], Tmin=(359.012,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-311.459,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 24,
    label = "ODC(F)C(F)(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74779,0.0221766,3.22619e-05,-1.05624e-07,7.10662e-11,-125087,10.7021], Tmin=(10,'K'), Tmax=(578.609,'K')),
            NASAPolynomial(coeffs=[6.37303,0.022456,-1.62357e-05,5.29783e-09,-6.42752e-13,-125700,-3.19245], Tmin=(578.609,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1040.08,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.331 kJ/mol
""",
    rank = 5,
)

entry(
    index = 25,
    label = "FCDC(F)OF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79296,0.016688,6.26097e-05,-1.85666e-07,1.40579e-10,-45431.1,10.7693], Tmin=(10,'K'), Tmax=(483.329,'K')),
            NASAPolynomial(coeffs=[5.34224,0.0230193,-1.64799e-05,5.41169e-09,-6.63799e-13,-45804.5,2.10704], Tmin=(483.329,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-377.761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 26,
    label = "FC[C]1CDC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {3,S} {4,D} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93474,0.0043517,0.00011027,-2.40813e-07,1.65256e-10,29857.4,9.90277], Tmin=(10,'K'), Tmax=(454.648,'K')),
            NASAPolynomial(coeffs=[1.97614,0.032877,-2.11022e-05,6.45929e-09,-7.56089e-13,29918.8,16.5244], Tmin=(454.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (248.239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 27,
    label = "CC1C[C]1F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94641,0.00342075,0.000125466,-2.47507e-07,1.56202e-10,6007.69,9.08849], Tmin=(10,'K'), Tmax=(471.224,'K')),
            NASAPolynomial(coeffs=[0.459714,0.0420595,-2.63109e-05,7.94003e-09,-9.23899e-13,6235.9,22.2211], Tmin=(471.224,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (49.9383,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.705 kJ/mol
""",
    rank = 5,
)

entry(
    index = 28,
    label = "FCCOC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54227,0.0513048,-0.000178933,5.40981e-07,-5.53441e-10,-105935,12.6623], Tmin=(10,'K'), Tmax=(356.186,'K')),
            NASAPolynomial(coeffs=[0.881219,0.0487596,-3.16462e-05,9.6949e-09,-1.1316e-12,-105540,25.641], Tmin=(356.186,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-880.816,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.921 kJ/mol
""",
    rank = 5,
)

entry(
    index = 29,
    label = "CDCC[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83799,0.0223114,1.6635e-05,-3.16338e-08,1.21125e-11,-1040.2,10.4264], Tmin=(10,'K'), Tmax=(980.599,'K')),
            NASAPolynomial(coeffs=[4.7441,0.0313711,-1.67359e-05,4.3192e-09,-4.35554e-13,-1831.2,2.94559], Tmin=(980.599,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.62139,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.94 kJ/mol
""",
    rank = 5,
)

entry(
    index = 30,
    label = "FC1[CH]OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 O u0 p2 c0 {2,S} {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94902,0.00287767,7.30964e-05,-1.31468e-07,7.15466e-11,-4893.6,9.66935], Tmin=(10,'K'), Tmax=(593.159,'K')),
            NASAPolynomial(coeffs=[2.03621,0.0276484,-1.95659e-05,6.41908e-09,-7.89981e-13,-4875.53,16.1381], Tmin=(593.159,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.7109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 31,
    label = "OCDC(F)CF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67712,0.0288182,1.9115e-06,-2.69762e-08,1.47761e-11,-63371.4,10.8189], Tmin=(10,'K'), Tmax=(761.964,'K')),
            NASAPolynomial(coeffs=[4.98659,0.0304482,-1.80388e-05,5.12663e-09,-5.62721e-13,-63817.9,3.23748], Tmin=(761.964,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-526.931,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 32,
    label = "CC(O)F",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 O u0 p2 c0 {2,S} {9,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97329,0.00181956,9.8764e-05,-2.01859e-07,1.3609e-10,-58879.4,8.47206], Tmin=(10,'K'), Tmax=(379.873,'K')),
            NASAPolynomial(coeffs=[1.13064,0.0317665,-1.95438e-05,5.8671e-09,-6.83132e-13,-58663.6,19.4334], Tmin=(379.873,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-489.551,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 33,
    label = "C#CCOF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8906,0.0076795,0.000108379,-2.80498e-07,2.16589e-10,18735.9,9.72786], Tmin=(10,'K'), Tmax=(438.434,'K')),
            NASAPolynomial(coeffs=[3.88115,0.0260516,-1.70369e-05,5.3331e-09,-6.37841e-13,18561,7.7614], Tmin=(438.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.771,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 34,
    label = "[CH2]CC#CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84721,0.0165204,0.000185867,-1.00483e-06,1.62181e-09,28849.2,9.7634], Tmin=(10,'K'), Tmax=(213.061,'K')),
            NASAPolynomial(coeffs=[4.10547,0.0285763,-1.80204e-05,5.51798e-09,-6.51736e-13,28799.8,8.01636], Tmin=(213.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (239.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.85 kJ/mol
""",
    rank = 5,
)

entry(
    index = 35,
    label = "FC[C]1CDC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,D} {9,S}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77533,0.0227085,1.60592e-05,-4.4086e-08,2.20866e-11,9177.86,11.7005], Tmin=(10,'K'), Tmax=(764.945,'K')),
            NASAPolynomial(coeffs=[5.10368,0.0276267,-1.68499e-05,4.87097e-09,-5.40171e-13,8627.52,3.37908], Tmin=(764.945,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (76.2975,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 36,
    label = "OCOC(F)F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81105,0.0201291,3.12191e-05,-6.20972e-08,2.92698e-11,-101825,10.6974], Tmin=(10,'K'), Tmax=(761.346,'K')),
            NASAPolynomial(coeffs=[4.08745,0.0322248,-1.93039e-05,5.51567e-09,-6.06811e-13,-102260,6.86064], Tmin=(761.346,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-846.628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 37,
    label = "FCC(F)OF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78957,0.0256154,2.58295e-07,-1.78168e-08,8.40139e-12,-63510.6,10.7161], Tmin=(10,'K'), Tmax=(946.252,'K')),
            NASAPolynomial(coeffs=[6.71694,0.0237784,-1.35341e-05,3.66907e-09,-3.84487e-13,-64536.4,-5.73787], Tmin=(946.252,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-528.041,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 38,
    label = "ODCCOF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85882,0.019647,2.03292e-06,-1.38255e-08,5.82526e-12,-24208.5,9.71265], Tmin=(10,'K'), Tmax=(1020.66,'K')),
            NASAPolynomial(coeffs=[6.12588,0.0194681,-1.04986e-05,2.71673e-09,-2.73576e-13,-25124.7,-3.49237], Tmin=(1020.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-201.259,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 39,
    label = "CDC[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95711,0.00249477,7.71091e-05,-1.38306e-07,7.71344e-11,-4616.75,8.69993], Tmin=(10,'K'), Tmax=(557.563,'K')),
            NASAPolynomial(coeffs=[1.5167,0.0291213,-1.90559e-05,6.00904e-09,-7.25881e-13,-4486.35,17.7768], Tmin=(557.563,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.4041,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.013 kJ/mol
""",
    rank = 5,
)

entry(
    index = 40,
    label = "C[CH]OC(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {11,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81688,0.0319654,-8.73544e-06,-5.82085e-09,2.90687e-12,-61900.9,10.3196], Tmin=(10,'K'), Tmax=(1239,'K')),
            NASAPolynomial(coeffs=[10.316,0.0221436,-1.03554e-05,2.32058e-09,-2.02753e-13,-64368,-25.8843], Tmin=(1239,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-514.645,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.363 kJ/mol
""",
    rank = 5,
)

entry(
    index = 41,
    label = "FCDC(F)COF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  O u0 p2 c0 {5,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67797,0.0359617,-1.72437e-05,-2.75272e-09,3.32182e-12,-47470,11.8297], Tmin=(10,'K'), Tmax=(1022.82,'K')),
            NASAPolynomial(coeffs=[8.97532,0.024381,-1.36584e-05,3.64321e-09,-3.75977e-13,-49031.5,-16.1825], Tmin=(1022.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-394.682,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 42,
    label = "OC(F)D[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81906,0.0149653,4.82143e-05,-1.74042e-07,1.54624e-10,-27598.4,10.3907], Tmin=(10,'K'), Tmax=(418.305,'K')),
            NASAPolynomial(coeffs=[5.02945,0.0176391,-1.2466e-05,4.09417e-09,-5.04518e-13,-27824.4,4.11616], Tmin=(418.305,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-229.469,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 43,
    label = "FC1(F)CC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0991,-0.0100262,0.000167648,-3.0804e-07,1.8114e-10,-42567.5,8.66782], Tmin=(10,'K'), Tmax=(547.766,'K')),
            NASAPolynomial(coeffs=[1.47548,0.0342486,-2.23724e-05,6.93389e-09,-8.17592e-13,-42656.8,16.3066], Tmin=(547.766,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-353.945,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 44,
    label = "[CH2]C(F)CO",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
7  O u0 p2 c0 {6,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90221,0.00950739,0.000185878,-6.55962e-07,7.82883e-10,-32952.7,10.3221], Tmin=(10,'K'), Tmax=(211.644,'K')),
            NASAPolynomial(coeffs=[2.32945,0.0392313,-2.47808e-05,7.58262e-09,-8.93434e-13,-32886.1,15.4675], Tmin=(211.644,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-273.955,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 45,
    label = "F[C]1CDCC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9427,0.00335575,9.57322e-05,-1.75807e-07,9.97692e-11,14179.7,9.76288], Tmin=(10,'K'), Tmax=(554.639,'K')),
            NASAPolynomial(coeffs=[1.27097,0.0349799,-2.32101e-05,7.32551e-09,-8.80744e-13,14286,19.3643], Tmin=(554.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (117.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 46,
    label = "FOC1CO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9457,0.00317073,8.53204e-05,-1.57911e-07,8.97168e-11,-15468.8,9.55393], Tmin=(10,'K'), Tmax=(559.618,'K')),
            NASAPolynomial(coeffs=[1.74187,0.0308485,-2.08319e-05,6.62633e-09,-7.98746e-13,-15408.9,17.2384], Tmin=(559.618,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.638,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.92 kJ/mol
""",
    rank = 5,
)

entry(
    index = 47,
    label = "[O]CDCCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97122,0.0018237,9.05724e-05,-1.69884e-07,1.03512e-10,-26407.9,10.1988], Tmin=(10,'K'), Tmax=(423.226,'K')),
            NASAPolynomial(coeffs=[0.636188,0.0333685,-2.13163e-05,6.50097e-09,-7.60038e-13,-26125.8,23.4182], Tmin=(423.226,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-219.575,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.942 kJ/mol
""",
    rank = 5,
)

entry(
    index = 48,
    label = "O[C](F)COF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65203,0.0311619,-7.35084e-06,-2.07583e-08,1.4197e-11,-38541.7,12.0233], Tmin=(10,'K'), Tmax=(726.906,'K')),
            NASAPolynomial(coeffs=[6.16966,0.0264336,-1.64247e-05,4.83412e-09,-5.44562e-13,-39148.9,-0.978143], Tmin=(726.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-320.491,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.824 kJ/mol
""",
    rank = 5,
)

entry(
    index = 49,
    label = "CC(F)D[C]CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,D} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58845,0.043209,-0.000102162,2.53388e-07,-2.33005e-10,-19772.3,10.6459], Tmin=(10,'K'), Tmax=(386.769,'K')),
            NASAPolynomial(coeffs=[2.22667,0.0403412,-2.52977e-05,7.57996e-09,-8.71902e-13,-19540.2,17.5611], Tmin=(386.769,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-164.407,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 50,
    label = "OC1(F)CO1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93525,0.00370355,8.56947e-05,-1.58782e-07,8.88378e-11,-57963.9,8.92798], Tmin=(10,'K'), Tmax=(584.865,'K')),
            NASAPolynomial(coeffs=[2.29865,0.030037,-2.06728e-05,6.72453e-09,-8.27227e-13,-58031.4,13.732], Tmin=(584.865,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-481.968,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 51,
    label = "CDC(CF)OF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {2,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74817,0.0258046,1.19266e-05,-3.68544e-08,1.7645e-11,-26480.4,10.9271], Tmin=(10,'K'), Tmax=(817.127,'K')),
            NASAPolynomial(coeffs=[5.2241,0.0303113,-1.7882e-05,5.03578e-09,-5.46955e-13,-27113.2,1.70808], Tmin=(817.127,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.177,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 52,
    label = "C[C](O)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {8,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94062,0.00411366,9.50233e-05,-2.218e-07,1.6287e-10,-36057.9,8.14086], Tmin=(10,'K'), Tmax=(430.095,'K')),
            NASAPolynomial(coeffs=[2.68946,0.025843,-1.5961e-05,4.79389e-09,-5.56959e-13,-36043.6,12.0361], Tmin=(430.095,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-299.806,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.469 kJ/mol
""",
    rank = 5,
)

entry(
    index = 53,
    label = "F[CH]CCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90888,0.0205511,1.19062e-05,-2.35926e-08,8.58567e-12,-35856.1,10.4775], Tmin=(10,'K'), Tmax=(1071.42,'K')),
            NASAPolynomial(coeffs=[6.14343,0.0252286,-1.28705e-05,3.16601e-09,-3.04508e-13,-37082.2,-3.94458], Tmin=(1071.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-298.078,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.292 kJ/mol
""",
    rank = 5,
)

entry(
    index = 54,
    label = "CD[C]COF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74831,0.0226925,9.614e-06,-3.32893e-08,1.72012e-11,25052,10.4871], Tmin=(10,'K'), Tmax=(742.284,'K')),
            NASAPolynomial(coeffs=[4.36419,0.0274477,-1.6311e-05,4.64853e-09,-5.1155e-13,24738.1,6.20105], Tmin=(742.284,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (208.27,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 55,
    label = "O[CH]C(F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90549,0.00637315,0.000103151,-2.45021e-07,1.75471e-10,-57966.3,10.6389], Tmin=(10,'K'), Tmax=(464.454,'K')),
            NASAPolynomial(coeffs=[3.37151,0.027472,-1.82785e-05,5.76605e-09,-6.90634e-13,-58094.7,10.8896], Tmin=(464.454,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-481.974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.289 kJ/mol
""",
    rank = 5,
)

entry(
    index = 56,
    label = "OC(F)C(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82934,0.0147801,6.31563e-05,-1.37579e-07,8.23834e-11,-105914,10.7785], Tmin=(10,'K'), Tmax=(572.569,'K')),
            NASAPolynomial(coeffs=[3.62731,0.0314397,-2.04351e-05,6.26194e-09,-7.30102e-13,-106140,9.45788], Tmin=(572.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-880.647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 57,
    label = "FCC[C](F)CF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47457,0.0567128,-0.000166124,4.45345e-07,-4.24613e-10,-63611.9,12.7172], Tmin=(10,'K'), Tmax=(373.085,'K')),
            NASAPolynomial(coeffs=[1.48097,0.0507516,-3.22539e-05,9.74618e-09,-1.12716e-12,-63272.9,22.9192], Tmin=(373.085,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-528.916,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 58,
    label = "[O]CCDC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78355,0.0216205,2.43657e-05,-5.91636e-08,3.049e-11,-38495.8,11.6712], Tmin=(10,'K'), Tmax=(723.1,'K')),
            NASAPolynomial(coeffs=[4.91702,0.0286699,-1.78876e-05,5.2659e-09,-5.92558e-13,-39007.9,4.16249], Tmin=(723.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-320.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.554 kJ/mol
""",
    rank = 5,
)

entry(
    index = 59,
    label = "OC1CC1F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93749,0.00364692,0.000105748,-1.92523e-07,1.08478e-10,-35807,9.18381], Tmin=(10,'K'), Tmax=(557.677,'K')),
            NASAPolynomial(coeffs=[0.901994,0.03896,-2.56552e-05,8.10026e-09,-9.76902e-13,-35679,20.1678], Tmin=(557.677,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-297.742,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 60,
    label = "C[CH]C#CF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58544,0.0401691,-8.80582e-05,1.54699e-07,-1.08025e-10,22903.9,9.50749], Tmin=(10,'K'), Tmax=(452.057,'K')),
            NASAPolynomial(coeffs=[3.9679,0.0277012,-1.65463e-05,4.78671e-09,-5.36798e-13,22962.2,8.99257], Tmin=(452.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (190.421,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 61,
    label = "C[C]DCDCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61494,0.0381247,-8.45387e-05,1.61406e-07,-1.21369e-10,13834.5,11.3501], Tmin=(10,'K'), Tmax=(432.787,'K')),
            NASAPolynomial(coeffs=[3.57638,0.0285996,-1.72772e-05,5.03974e-09,-5.68584e-13,13930.4,12.573], Tmin=(432.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.017,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.769 kJ/mol
""",
    rank = 5,
)

entry(
    index = 62,
    label = "F[C]DCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96273,0.00227507,4.82866e-05,-9.84684e-08,6.08565e-11,-6639.51,9.13556], Tmin=(10,'K'), Tmax=(530.029,'K')),
            NASAPolynomial(coeffs=[3.31952,0.0150351,-1.01986e-05,3.23554e-09,-3.88038e-13,-6682.38,10.7828], Tmin=(530.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.2169,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.199 kJ/mol
""",
    rank = 5,
)

entry(
    index = 63,
    label = "FC1(F)[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {2,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94595,0.00297557,6.37801e-05,-1.1534e-07,6.16373e-11,-33701.3,9.35233], Tmin=(10,'K'), Tmax=(624.072,'K')),
            NASAPolynomial(coeffs=[2.84669,0.0234255,-1.75906e-05,6.00156e-09,-7.58566e-13,-33825.1,12.046], Tmin=(624.072,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-280.234,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.363 kJ/mol
""",
    rank = 5,
)

entry(
    index = 64,
    label = "CO[C]DC(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61615,0.0397511,-9.04591e-05,1.97606e-07,-1.73508e-10,-28971.9,10.4911], Tmin=(10,'K'), Tmax=(372.712,'K')),
            NASAPolynomial(coeffs=[3.51613,0.0316116,-2.06234e-05,6.37077e-09,-7.50137e-13,-28900.5,11.7333], Tmin=(372.712,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.256 kJ/mol
""",
    rank = 5,
)

entry(
    index = 65,
    label = "C#CC(C)F",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {6,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90746,0.00642796,0.000130514,-3.14201e-07,2.35021e-10,-4218.6,9.49885], Tmin=(10,'K'), Tmax=(432.195,'K')),
            NASAPolynomial(coeffs=[2.71745,0.0337197,-2.07023e-05,6.19764e-09,-7.20001e-13,-4267.77,12.4828], Tmin=(432.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.0815,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 66,
    label = "FCD[C]C(F)OF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 O u0 p2 c0 {4,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91488,0.0140944,0.000749975,-8.25348e-06,2.83674e-08,-22499,1.1601], Tmin=(10,'K'), Tmax=(100.189,'K')),
            NASAPolynomial(coeffs=[4.18148,0.0346414,-2.46239e-05,8.04964e-09,-9.84869e-13,-22520,-0.29397], Tmin=(100.189,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-162.843,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 67,
    label = "FOCDCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69352,0.032575,-3.09472e-06,-2.20829e-08,1.19023e-11,-52893.2,11.6886], Tmin=(10,'K'), Tmax=(867.349,'K')),
            NASAPolynomial(coeffs=[7.25308,0.028368,-1.69328e-05,4.78203e-09,-5.18711e-13,-53969.9,-7.62493], Tmin=(867.349,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-439.781,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 68,
    label = "FCOCDC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78641,0.0326611,-1.18046e-05,-5.2007e-09,3.33996e-12,-83578,11.822], Tmin=(10,'K'), Tmax=(1129.58,'K')),
            NASAPolynomial(coeffs=[9.87137,0.0217077,-1.13279e-05,2.8211e-09,-2.73108e-13,-85628.6,-21.2677], Tmin=(1129.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-694.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.738 kJ/mol
""",
    rank = 5,
)

entry(
    index = 69,
    label = "[O]C1DCDC1F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94088,0.00354961,5.68041e-05,-1.20963e-07,7.50861e-11,20396.6,9.62063], Tmin=(10,'K'), Tmax=(553.889,'K')),
            NASAPolynomial(coeffs=[4.07532,0.0156607,-1.14216e-05,3.79508e-09,-4.69956e-13,20181.1,7.24], Tmin=(553.889,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.565,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.616 kJ/mol
""",
    rank = 5,
)

entry(
    index = 70,
    label = "F[C]DC(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90297,0.00678624,6.59753e-05,-1.82412e-07,1.41932e-10,-28613,10.2903], Tmin=(10,'K'), Tmax=(455.705,'K')),
            NASAPolynomial(coeffs=[4.71392,0.0149224,-1.10172e-05,3.67877e-09,-4.5619e-13,-28845.3,5.2774], Tmin=(455.705,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-237.913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.083 kJ/mol
""",
    rank = 5,
)

entry(
    index = 71,
    label = "FC1[CH]OC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96114,0.00232228,9.38649e-05,-1.68176e-07,9.51937e-11,-14154.8,9.88065], Tmin=(10,'K'), Tmax=(520.778,'K')),
            NASAPolynomial(coeffs=[0.321262,0.0368674,-2.46107e-05,7.78016e-09,-9.34901e-13,-13865.1,24.2085], Tmin=(520.778,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-117.705,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.903 kJ/mol
""",
    rank = 5,
)

entry(
    index = 72,
    label = "FCDC(F)CF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77712,0.0231743,9.13857e-06,-3.03264e-08,1.43622e-11,-65009.6,10.7085], Tmin=(10,'K'), Tmax=(838.243,'K')),
            NASAPolynomial(coeffs=[5.31305,0.0264153,-1.55761e-05,4.373e-09,-4.73196e-13,-65638.4,1.35446], Tmin=(838.243,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-540.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 73,
    label = "C[C]1CC1F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88166,0.0151778,4.63628e-05,-7.30372e-08,3.11185e-11,5268.8,9.0383], Tmin=(10,'K'), Tmax=(799.411,'K')),
            NASAPolynomial(coeffs=[2.48993,0.0366162,-2.10239e-05,5.80969e-09,-6.2263e-13,5028.8,12.5482], Tmin=(799.411,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (43.8205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.96 kJ/mol
""",
    rank = 5,
)

entry(
    index = 74,
    label = "CC[CH]CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60745,0.042679,-0.00011855,3.3699e-07,-3.14065e-10,-15978.2,10.1606], Tmin=(10,'K'), Tmax=(407.359,'K')),
            NASAPolynomial(coeffs=[-0.0291982,0.0482911,-2.83888e-05,8.062e-09,-8.87802e-13,-15432.2,27.5045], Tmin=(407.359,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.864,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.126 kJ/mol
""",
    rank = 5,
)

entry(
    index = 75,
    label = "FCC(F)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88193,0.0247651,1.0673e-05,-2.45553e-08,9.08087e-12,-82087.1,10.4465], Tmin=(10,'K'), Tmax=(1081.74,'K')),
            NASAPolynomial(coeffs=[7.0284,0.0279634,-1.43304e-05,3.53012e-09,-3.39467e-13,-83635.7,-8.99198], Tmin=(1081.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-682.46,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 76,
    label = "OC[C](F)CF",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7276,0.0310844,-3.14474e-06,-1.42102e-08,6.54341e-12,-55778.2,11.4788], Tmin=(10,'K'), Tmax=(1019.97,'K')),
            NASAPolynomial(coeffs=[6.92896,0.0290457,-1.56119e-05,4.04681e-09,-4.09079e-13,-56978.3,-6.71066], Tmin=(1019.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-463.756,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 77,
    label = "ODCCCF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98419,0.0184404,1.33981e-05,-2.20048e-08,7.30928e-12,-46341.6,9.23467], Tmin=(10,'K'), Tmax=(1165.75,'K')),
            NASAPolynomial(coeffs=[7.03385,0.0224949,-1.05005e-05,2.34595e-09,-2.04006e-13,-48039.2,-10.1772], Tmin=(1165.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-385.249,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.178 kJ/mol
""",
    rank = 5,
)

entry(
    index = 78,
    label = "FCDCC[C](F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79333,0.0339846,-6.97886e-06,-1.14978e-08,5.55706e-12,-51207.5,12.0861], Tmin=(10,'K'), Tmax=(1096.78,'K')),
            NASAPolynomial(coeffs=[9.72543,0.0255258,-1.34298e-05,3.37627e-09,-3.29951e-13,-53301.2,-20.6936], Tmin=(1096.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-425.718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.993 kJ/mol
""",
    rank = 5,
)

entry(
    index = 79,
    label = "F[CH]OCCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58432,0.0464323,-0.000166057,4.83963e-07,-4.76476e-10,-53475,12.0557], Tmin=(10,'K'), Tmax=(367.782,'K')),
            NASAPolynomial(coeffs=[1.15503,0.0425909,-2.69648e-05,8.10607e-09,-9.32572e-13,-53091.6,24.1282], Tmin=(367.782,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-444.636,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 80,
    label = "C#CCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {6,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84876,0.0132672,6.84284e-05,-1.58225e-07,1.12294e-10,-4289.64,9.58812], Tmin=(10,'K'), Tmax=(363.987,'K')),
            NASAPolynomial(coeffs=[1.86507,0.0350668,-2.14083e-05,6.31687e-09,-7.20023e-13,-4145.23,17.1535], Tmin=(363.987,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.6736,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.468 kJ/mol
""",
    rank = 5,
)

entry(
    index = 81,
    label = "OCDC(F)OF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80961,0.0142881,0.000110159,-3.27296e-07,2.717e-10,-48002.8,10.7772], Tmin=(10,'K'), Tmax=(427.131,'K')),
            NASAPolynomial(coeffs=[5.02858,0.0269585,-1.89214e-05,6.19206e-09,-7.61431e-13,-48326.7,3.36138], Tmin=(427.131,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-399.125,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.762 kJ/mol
""",
    rank = 5,
)

entry(
    index = 82,
    label = "FOC1CC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94502,0.00320947,0.000104929,-1.87761e-07,1.04727e-10,-1264.01,9.54979], Tmin=(10,'K'), Tmax=(551.514,'K')),
            NASAPolynomial(coeffs=[0.381214,0.0403339,-2.67129e-05,8.44228e-09,-1.01723e-12,-1042.42,23.0674], Tmin=(551.514,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.5328,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 83,
    label = "FCDC(OF)OF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 O u0 p2 c0 {3,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59577,0.0354189,-8.65514e-06,-4.47396e-08,3.76294e-11,-26549.2,11.8374], Tmin=(10,'K'), Tmax=(594.411,'K')),
            NASAPolynomial(coeffs=[7.3956,0.0242808,-1.69678e-05,5.4304e-09,-6.50844e-13,-27255.9,-6.6626], Tmin=(594.411,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.795,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.053 kJ/mol
""",
    rank = 5,
)

entry(
    index = 84,
    label = "F[C]1CDCO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92933,0.00409135,7.90398e-05,-1.5425e-07,8.93661e-11,2210.56,9.40535], Tmin=(10,'K'), Tmax=(580.23,'K')),
            NASAPolynomial(coeffs=[3.29982,0.024943,-1.7552e-05,5.77702e-09,-7.15449e-13,2005.66,9.7045], Tmin=(580.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.3496,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.357 kJ/mol
""",
    rank = 5,
)

entry(
    index = 85,
    label = "[CH2]C(F)OO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 O u0 p2 c0 {4,S} {7,S}
7 O u0 p2 c0 {6,S} {9,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80887,0.0156377,0.000115694,-3.75619e-07,3.48319e-10,-24033.9,10.5468], Tmin=(10,'K'), Tmax=(374.42,'K')),
            NASAPolynomial(coeffs=[4.34876,0.0296343,-1.95601e-05,6.18763e-09,-7.46672e-13,-24212.9,6.62244], Tmin=(374.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-199.814,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.258 kJ/mol
""",
    rank = 5,
)

entry(
    index = 86,
    label = "O[C](F)CCF",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77141,0.0199312,5.58179e-05,-1.18129e-07,6.67459e-11,-61087.3,11.5174], Tmin=(10,'K'), Tmax=(596.336,'K')),
            NASAPolynomial(coeffs=[2.83182,0.0389858,-2.41876e-05,7.1712e-09,-8.16543e-13,-61202,13.6635], Tmin=(596.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-507.942,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 87,
    label = "CCC[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85115,0.0306611,7.32796e-06,-2.20032e-08,7.95281e-12,-43823.6,9.48497], Tmin=(10,'K'), Tmax=(1146.89,'K')),
            NASAPolynomial(coeffs=[8.19688,0.031793,-1.54559e-05,3.62378e-09,-3.32659e-13,-45891.7,-16.7466], Tmin=(1146.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-364.32,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.182 kJ/mol
""",
    rank = 5,
)

entry(
    index = 88,
    label = "F[CH]CCCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8863,0.0299687,9.25502e-06,-2.36982e-08,8.4334e-12,-39345.3,11.468], Tmin=(10,'K'), Tmax=(1151.55,'K')),
            NASAPolynomial(coeffs=[8.52018,0.031259,-1.50734e-05,3.49768e-09,-3.17295e-13,-41565.3,-16.547], Tmin=(1151.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-327.074,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.842 kJ/mol
""",
    rank = 5,
)

entry(
    index = 89,
    label = "FC1(F)CO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09076,-0.0093034,0.000141795,-2.65499e-07,1.58434e-10,-60230.2,9.31533], Tmin=(10,'K'), Tmax=(546.014,'K')),
            NASAPolynomial(coeffs=[2.38221,0.025984,-1.7701e-05,5.61942e-09,-6.72378e-13,-60383.1,13.4159], Tmin=(546.014,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-500.8,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.987 kJ/mol
""",
    rank = 5,
)

entry(
    index = 90,
    label = "FCDC(F)CCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77263,0.0344417,-3.28576e-06,-1.47984e-08,6.43354e-12,-69573.5,11.6164], Tmin=(10,'K'), Tmax=(1099.89,'K')),
            NASAPolynomial(coeffs=[8.89664,0.0295157,-1.52631e-05,3.79289e-09,-3.67769e-13,-71529.9,-17.3613], Tmin=(1099.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-578.429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 91,
    label = "OC1(F)CC1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93782,0.00353139,0.000103462,-1.82014e-07,9.85335e-11,-40384.5,8.67076], Tmin=(10,'K'), Tmax=(581.801,'K')),
            NASAPolynomial(coeffs=[0.598786,0.0403663,-2.72865e-05,8.80722e-09,-1.08037e-12,-40230.8,20.9525], Tmin=(581.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-335.804,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 92,
    label = "[CH2]C(C)DCF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,D} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89925,0.00877643,0.00013932,-3.76705e-07,3.36116e-10,-8902.9,8.7717], Tmin=(10,'K'), Tmax=(285.053,'K')),
            NASAPolynomial(coeffs=[1.67424,0.0399987,-2.49766e-05,7.54125e-09,-8.7749e-13,-8776.05,16.7135], Tmin=(285.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-74.0097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 93,
    label = "FC1DC[CH]C1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90254,0.00600006,0.00011531,-2.42111e-07,1.52798e-10,-8506.27,11.0421], Tmin=(10,'K'), Tmax=(526.65,'K')),
            NASAPolynomial(coeffs=[2.9312,0.0339822,-2.30747e-05,7.35336e-09,-8.86362e-13,-8689.7,12.3925], Tmin=(526.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-70.7575,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 94,
    label = "C[C]1OC1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89096,0.0121597,4.29699e-05,-7.29131e-08,3.38726e-11,-14329.2,8.94223], Tmin=(10,'K'), Tmax=(729.893,'K')),
            NASAPolynomial(coeffs=[2.89003,0.029661,-1.76908e-05,5.04758e-09,-5.55478e-13,-14503.2,11.2634], Tmin=(729.893,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.569 kJ/mol
""",
    rank = 5,
)

entry(
    index = 95,
    label = "FC1C(F)C1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9123,0.00564253,0.000116778,-2.52742e-07,1.67257e-10,-57503.6,9.58767], Tmin=(10,'K'), Tmax=(489.714,'K')),
            NASAPolynomial(coeffs=[2.3723,0.0348231,-2.34537e-05,7.38738e-09,-8.79267e-13,-57551.8,13.8853], Tmin=(489.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-478.133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 96,
    label = "CDC(F)OCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82955,0.0172779,4.54556e-05,-8.60804e-08,4.25935e-11,-64929.9,10.6987], Tmin=(10,'K'), Tmax=(700.603,'K')),
            NASAPolynomial(coeffs=[3.42734,0.0338793,-2.07155e-05,6.02919e-09,-6.73981e-13,-65224.6,9.99047], Tmin=(700.603,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-539.872,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.383 kJ/mol
""",
    rank = 5,
)

entry(
    index = 97,
    label = "CD[C]CDCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90012,0.00709122,0.000120722,-3.02808e-07,2.32927e-10,13612.7,10.2951], Tmin=(10,'K'), Tmax=(425.5,'K')),
            NASAPolynomial(coeffs=[3.08036,0.0308703,-1.97666e-05,6.08097e-09,-7.17691e-13,13536.9,11.8398], Tmin=(425.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.178,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.919 kJ/mol
""",
    rank = 5,
)

entry(
    index = 98,
    label = "OOCDCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84558,0.0127782,8.79689e-05,-2.67872e-07,2.35878e-10,-26330.7,9.59761], Tmin=(10,'K'), Tmax=(384.928,'K')),
            NASAPolynomial(coeffs=[3.83347,0.0263633,-1.74191e-05,5.48992e-09,-6.59264e-13,-26429.5,8.34926], Tmin=(384.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-218.919,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.178 kJ/mol
""",
    rank = 5,
)

entry(
    index = 99,
    label = "OOC(F)DCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76029,0.0195212,7.89584e-05,-2.60815e-07,2.23178e-10,-50490.4,10.6917], Tmin=(10,'K'), Tmax=(425.167,'K')),
            NASAPolynomial(coeffs=[5.20063,0.0265677,-1.85701e-05,6.05537e-09,-7.42563e-13,-50799.1,2.78544], Tmin=(425.167,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-419.808,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 100,
    label = "FC1CD[C]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u1 p0 c0 {3,D} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07786,-0.00785483,0.000130693,-2.39149e-07,1.38677e-10,10877.3,9.67963], Tmin=(10,'K'), Tmax=(563.21,'K')),
            NASAPolynomial(coeffs=[2.41788,0.0258813,-1.76081e-05,5.58069e-09,-6.66413e-13,10716.2,13.6449], Tmin=(563.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (90.4217,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.254 kJ/mol
""",
    rank = 5,
)

entry(
    index = 101,
    label = "OC[C](F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8103,0.0171093,2.36231e-05,-5.68497e-08,3.1219e-11,-54526.6,9.90919], Tmin=(10,'K'), Tmax=(653.413,'K')),
            NASAPolynomial(coeffs=[4.03059,0.0249517,-1.54793e-05,4.57292e-09,-5.18111e-13,-54751.6,7.4388], Tmin=(653.413,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-453.383,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.819 kJ/mol
""",
    rank = 5,
)

entry(
    index = 102,
    label = "ODCCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01561,0.00948174,1.47974e-05,-2.05388e-08,6.93945e-12,-41680.2,8.22618], Tmin=(10,'K'), Tmax=(1087.51,'K')),
            NASAPolynomial(coeffs=[5.06269,0.0157386,-7.77482e-06,1.84532e-09,-1.71022e-13,-42505.6,0.338584], Tmin=(1087.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-346.502,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.071 kJ/mol
""",
    rank = 5,
)

entry(
    index = 103,
    label = "F[C]DCDCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85197,0.0122938,7.39879e-05,-2.7129e-07,2.69659e-10,5758.69,10.0852], Tmin=(10,'K'), Tmax=(362.467,'K')),
            NASAPolynomial(coeffs=[4.72944,0.0178967,-1.24574e-05,4.0528e-09,-4.97064e-13,5594.66,5.3572], Tmin=(362.467,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (47.8949,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.907 kJ/mol
""",
    rank = 5,
)

entry(
    index = 104,
    label = "FCC#C[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78689,0.0276934,0.000314844,-2.75811e-06,6.6856e-09,-29112.9,10.8698], Tmin=(10,'K'), Tmax=(151.09,'K')),
            NASAPolynomial(coeffs=[4.70163,0.0325931,-2.28669e-05,7.48127e-09,-9.21289e-13,-29173.8,7.0856], Tmin=(151.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.059,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.999 kJ/mol
""",
    rank = 5,
)

entry(
    index = 105,
    label = "[O]C1CDC1F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90632,0.00577798,8.84872e-05,-1.96214e-07,1.27236e-10,13855.9,9.82414], Tmin=(10,'K'), Tmax=(532.195,'K')),
            NASAPolynomial(coeffs=[4.33582,0.02263,-1.5607e-05,5.07903e-09,-6.25534e-13,13525.8,5.35131], Tmin=(532.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.173,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.958 kJ/mol
""",
    rank = 5,
)

entry(
    index = 106,
    label = "[C]#COC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93574,0.0103904,0.000500879,-5.36136e-06,1.7981e-08,-3832.61,4.85303], Tmin=(10,'K'), Tmax=(102.187,'K')),
            NASAPolynomial(coeffs=[4.09076,0.0250272,-1.78946e-05,5.8832e-09,-7.23557e-13,-3846.59,3.92982], Tmin=(102.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-17.1685,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.741 kJ/mol
""",
    rank = 5,
)

entry(
    index = 107,
    label = "C[CH]CCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59568,0.0440629,-0.000128692,3.62027e-07,-3.34735e-10,-16860.4,9.78073], Tmin=(10,'K'), Tmax=(407.067,'K')),
            NASAPolynomial(coeffs=[-0.026329,0.0482372,-2.83051e-05,8.02233e-09,-8.81786e-13,-16305.2,27.1967], Tmin=(407.067,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.153 kJ/mol
""",
    rank = 5,
)

entry(
    index = 108,
    label = "FCC(F)DCOF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  O u0 p2 c0 {5,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6843,0.0380415,-2.47269e-05,6.09756e-09,-7.3529e-14,-48076.8,11.9338], Tmin=(10,'K'), Tmax=(1212.02,'K')),
            NASAPolynomial(coeffs=[11.1315,0.01991,-1.02652e-05,2.53123e-09,-2.4307e-13,-50355.5,-27.3798], Tmin=(1212.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-399.727,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 109,
    label = "CC1(F)CDC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {2,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93068,0.00411583,0.000109193,-2.06118e-07,1.2016e-10,920.727,7.84107], Tmin=(10,'K'), Tmax=(545.544,'K')),
            NASAPolynomial(coeffs=[1.40071,0.0376859,-2.4408e-05,7.61264e-09,-9.11094e-13,973.259,16.4651], Tmin=(545.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (7.62814,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.227 kJ/mol
""",
    rank = 5,
)

entry(
    index = 110,
    label = "CO[C](O)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {9,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76209,0.0261031,-1.03834e-05,-1.59407e-09,1.52075e-12,-51872.7,9.23913], Tmin=(10,'K'), Tmax=(1183.23,'K')),
            NASAPolynomial(coeffs=[7.47165,0.019588,-9.76249e-06,2.35976e-09,-2.23943e-13,-53172.3,-11.0638], Tmin=(1183.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-431.297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.638 kJ/mol
""",
    rank = 5,
)

entry(
    index = 111,
    label = "C#CC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89605,0.00666809,9.27662e-05,-2.20453e-07,1.52344e-10,5841.94,10.1575], Tmin=(10,'K'), Tmax=(503.278,'K')),
            NASAPolynomial(coeffs=[4.61212,0.0218953,-1.49644e-05,4.84031e-09,-5.93477e-13,5504.94,4.56258], Tmin=(503.278,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.5457,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.59 kJ/mol
""",
    rank = 5,
)

entry(
    index = 112,
    label = "[CH]DCC(C)F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,D}
2  H u0 p0 c0 {1,S}
3  C u0 p0 c0 {1,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86941,0.0113957,9.96446e-05,-2.30738e-07,1.69844e-10,3220.28,10.2768], Tmin=(10,'K'), Tmax=(348.861,'K')),
            NASAPolynomial(coeffs=[1.341,0.0403863,-2.50068e-05,7.46922e-09,-8.5998e-13,3396.7,19.8123], Tmin=(348.861,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.7737,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 113,
    label = "C[CH]C(F)DCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,D} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64526,0.0340795,-9.3594e-06,-9.92691e-09,5.69908e-12,-30457.1,11.3104], Tmin=(10,'K'), Tmax=(959.123,'K')),
            NASAPolynomial(coeffs=[6.58211,0.0303326,-1.67947e-05,4.48247e-09,-4.65562e-13,-31411.5,-4.77404], Tmin=(959.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-253.25,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.394 kJ/mol
""",
    rank = 5,
)

entry(
    index = 114,
    label = "FOC#CC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61038,0.0421954,-5.64018e-05,4.6869e-08,-1.74214e-11,-23421.3,12.443], Tmin=(10,'K'), Tmax=(608.574,'K')),
            NASAPolynomial(coeffs=[5.8936,0.0271884,-1.94127e-05,6.34891e-09,-7.75883e-13,-23699.2,2.56168], Tmin=(608.574,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.724,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 115,
    label = "OC1[C]DC1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92395,0.00454659,8.12222e-05,-1.67384e-07,1.02271e-10,18311,9.82025], Tmin=(10,'K'), Tmax=(554.058,'K')),
            NASAPolynomial(coeffs=[3.65708,0.0234961,-1.61654e-05,5.24954e-09,-6.44779e-13,18079.2,8.59229], Tmin=(554.058,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.217,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 116,
    label = "FC#CC[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58968,0.0366432,-2.45448e-05,1.87709e-09,3.36394e-12,-20784.1,12.2165], Tmin=(10,'K'), Tmax=(824.619,'K')),
            NASAPolynomial(coeffs=[7.56997,0.0243133,-1.48086e-05,4.26672e-09,-4.71344e-13,-21677.7,-7.65701], Tmin=(824.619,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-172.847,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.878 kJ/mol
""",
    rank = 5,
)

entry(
    index = 117,
    label = "ODC([CH]F)OF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 O u0 p2 c0 {2,S} {7,S}
7 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75227,0.02042,4.8872e-05,-1.75311e-07,1.46069e-10,-32156,11.3423], Tmin=(10,'K'), Tmax=(451.632,'K')),
            NASAPolynomial(coeffs=[5.41957,0.0228619,-1.63937e-05,5.39881e-09,-6.6433e-13,-32482.1,2.68087], Tmin=(451.632,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-267.376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.592 kJ/mol
""",
    rank = 5,
)

entry(
    index = 118,
    label = "OC(O)(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {7,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8902,0.00687446,9.29217e-05,-2.1622e-07,1.44851e-10,-108335,9.46048], Tmin=(10,'K'), Tmax=(523.698,'K')),
            NASAPolynomial(coeffs=[4.93106,0.0218083,-1.53974e-05,5.10905e-09,-6.36787e-13,-108758,2.11615], Tmin=(523.698,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-900.78,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.03 kJ/mol
""",
    rank = 5,
)

entry(
    index = 119,
    label = "CDCC(C)F",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85048,0.013046,7.19619e-05,-1.24183e-07,6.32231e-11,-26232.7,9.64043], Tmin=(10,'K'), Tmax=(611.334,'K')),
            NASAPolynomial(coeffs=[0.638786,0.0434364,-2.56113e-05,7.31007e-09,-8.09233e-13,-26015.2,22.1215], Tmin=(611.334,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-218.132,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 120,
    label = "FCC#COF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65677,0.0340714,-3.43736e-05,2.04065e-08,-5.42352e-12,625.405,11.0251], Tmin=(10,'K'), Tmax=(806.908,'K')),
            NASAPolynomial(coeffs=[5.72978,0.0237951,-1.52705e-05,4.62353e-09,-5.33591e-13,290.858,1.46872], Tmin=(806.908,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.17834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 121,
    label = "FCDCCF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88883,0.0149108,2.52031e-05,-4.18182e-08,1.70583e-11,-44097,9.59929], Tmin=(10,'K'), Tmax=(870.921,'K')),
            NASAPolynomial(coeffs=[3.72658,0.0270257,-1.52449e-05,4.13341e-09,-4.35076e-13,-44500,7.88406], Tmin=(870.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-366.625,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.405 kJ/mol
""",
    rank = 5,
)

entry(
    index = 122,
    label = "FC1DCC[CH]1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 C u1 p0 c0 {2,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10153,-0.0104378,0.000172616,-3.21389e-07,1.91802e-10,12954,9.78716], Tmin=(10,'K'), Tmax=(539.458,'K')),
            NASAPolynomial(coeffs=[1.49303,0.0343085,-2.24436e-05,6.9641e-09,-8.22082e-13,12865.8,17.3355], Tmin=(539.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (107.686,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.848 kJ/mol
""",
    rank = 5,
)

entry(
    index = 123,
    label = "F[C]1OC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94695,0.0030248,6.42639e-05,-1.21083e-07,6.79964e-11,-30990.5,9.80796], Tmin=(10,'K'), Tmax=(590.655,'K')),
            NASAPolynomial(coeffs=[2.97574,0.0221034,-1.59352e-05,5.27056e-09,-6.50919e-13,-31093.9,12.1361], Tmin=(590.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-257.693,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.674 kJ/mol
""",
    rank = 5,
)

entry(
    index = 124,
    label = "FCC1[C]DC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 C u1 p0 c0 {3,S} {5,D}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8083,0.0221727,1.19742e-05,-3.28117e-08,1.49881e-11,16608.3,11.3419], Tmin=(10,'K'), Tmax=(856.402,'K')),
            NASAPolynomial(coeffs=[5.43934,0.0261627,-1.53459e-05,4.28279e-09,-4.60766e-13,15903.2,1.24059], Tmin=(856.402,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.779 kJ/mol
""",
    rank = 5,
)

entry(
    index = 125,
    label = "CC(F)[C]DCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75858,0.0308725,-4.39182e-06,-1.13107e-08,5.07555e-12,-18604.7,11.7528], Tmin=(10,'K'), Tmax=(1096.42,'K')),
            NASAPolynomial(coeffs=[7.72171,0.0271682,-1.40365e-05,3.49944e-09,-3.41141e-13,-20120.2,-10.6796], Tmin=(1096.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.67,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 126,
    label = "FCOCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92575,0.0325362,-1.92691e-06,-1.30817e-08,5.07935e-12,-103263,11.3309], Tmin=(10,'K'), Tmax=(1236.14,'K')),
            NASAPolynomial(coeffs=[11.8918,0.0231347,-1.03897e-05,2.1991e-09,-1.78432e-13,-106484,-33.8499], Tmin=(1236.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-858.514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.066 kJ/mol
""",
    rank = 5,
)

entry(
    index = 127,
    label = "[CH2]CDCCF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83641,0.0174184,3.97251e-05,-6.66439e-08,2.91869e-11,-7696.17,9.79841], Tmin=(10,'K'), Tmax=(780.723,'K')),
            NASAPolynomial(coeffs=[2.58616,0.0364093,-2.09422e-05,5.80814e-09,-6.25061e-13,-7884.5,13.0643], Tmin=(780.723,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.99,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.695 kJ/mol
""",
    rank = 5,
)

entry(
    index = 128,
    label = "CC1(F)C[C]1F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {2,S} {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86837,0.00963391,0.000136047,-3.15838e-07,2.24478e-10,-16928.4,9.93081], Tmin=(10,'K'), Tmax=(452.669,'K')),
            NASAPolynomial(coeffs=[2.19901,0.0416102,-2.69902e-05,8.33637e-09,-9.83055e-13,-16953.7,14.7121], Tmin=(452.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.765,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 129,
    label = "COOCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88966,0.0207406,9.68553e-06,-2.03911e-08,7.29654e-12,-42984.6,8.36424], Tmin=(10,'K'), Tmax=(1101.72,'K')),
            NASAPolynomial(coeffs=[6.10925,0.0248346,-1.24344e-05,3.00607e-09,-2.84595e-13,-44211.2,-5.9062], Tmin=(1101.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-357.358,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.724 kJ/mol
""",
    rank = 5,
)

entry(
    index = 130,
    label = "CC1(F)CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95157,0.00293783,0.000106575,-1.97101e-07,1.15305e-10,-40745,8.03071], Tmin=(10,'K'), Tmax=(513.297,'K')),
            NASAPolynomial(coeffs=[0.449188,0.0391261,-2.51708e-05,7.77033e-09,-9.20216e-13,-40502.6,21.4505], Tmin=(513.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-338.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.176 kJ/mol
""",
    rank = 5,
)

entry(
    index = 131,
    label = "OD[C]C(O)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u0 p2 c0 {3,S} {7,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83796,0.0135756,5.70509e-05,-1.75141e-07,1.45882e-10,-44982.1,10.7446], Tmin=(10,'K'), Tmax=(418.301,'K')),
            NASAPolynomial(coeffs=[4.12395,0.0222437,-1.49222e-05,4.73357e-09,-5.69734e-13,-45105.7,8.42167], Tmin=(418.301,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-374.005,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 132,
    label = "FCCCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00116,0.0152944,3.17129e-05,-4.29146e-08,1.48752e-11,-59893.2,8.78439], Tmin=(10,'K'), Tmax=(1032.07,'K')),
            NASAPolynomial(coeffs=[4.47088,0.0306929,-1.56929e-05,3.87257e-09,-3.73799e-13,-60907.2,2.06057], Tmin=(1032.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-497.909,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.203 kJ/mol
""",
    rank = 5,
)

entry(
    index = 133,
    label = "OOCC(F)F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74818,0.0217647,4.31782e-05,-1.06037e-07,6.4557e-11,-69919.2,10.8176], Tmin=(10,'K'), Tmax=(572.037,'K')),
            NASAPolynomial(coeffs=[3.64885,0.0345118,-2.18517e-05,6.58301e-09,-7.58922e-13,-70105.1,9.5177], Tmin=(572.037,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-581.376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.687 kJ/mol
""",
    rank = 5,
)

entry(
    index = 134,
    label = "[CH2]C(C)F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87777,0.0100265,9.18917e-05,-2.32463e-07,1.90284e-10,-14322.2,8.29356], Tmin=(10,'K'), Tmax=(311.647,'K')),
            NASAPolynomial(coeffs=[2.07701,0.0331392,-1.93519e-05,5.50463e-09,-6.09201e-13,-14210,14.8817], Tmin=(311.647,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 135,
    label = "[CH2]C(DO)OF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p2 c0 {4,S} {7,S}
7 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8868,0.00744283,9.65339e-05,-2.39858e-07,1.72355e-10,-11541.8,9.42861], Tmin=(10,'K'), Tmax=(486.446,'K')),
            NASAPolynomial(coeffs=[4.7678,0.0219179,-1.5075e-05,4.88657e-09,-5.99065e-13,-11884.5,3.17183], Tmin=(486.446,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.9878,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 136,
    label = "[CH2]C(O)OF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5 O u0 p2 c0 {4,S} {9,S}
6 O u0 p2 c0 {4,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84396,0.0110746,0.000131317,-3.5984e-07,2.87099e-10,-14589.8,10.4179], Tmin=(10,'K'), Tmax=(435.537,'K')),
            NASAPolynomial(coeffs=[4.68277,0.0290774,-1.92186e-05,6.09796e-09,-7.37997e-13,-14906.7,4.26926], Tmin=(435.537,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.316,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.206 kJ/mol
""",
    rank = 5,
)

entry(
    index = 137,
    label = "OC1C[C]1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92113,0.00468014,0.00010215,-1.99832e-07,1.18492e-10,-8367.07,9.91689], Tmin=(10,'K'), Tmax=(553.65,'K')),
            NASAPolynomial(coeffs=[2.47006,0.0327942,-2.1785e-05,6.91823e-09,-8.37634e-13,-8476.6,13.6193], Tmin=(553.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.5987,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.686 kJ/mol
""",
    rank = 5,
)

entry(
    index = 138,
    label = "FC[CH]CF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6695,0.0371803,-0.000130698,3.91112e-07,-3.86112e-10,-34920.5,10.8123], Tmin=(10,'K'), Tmax=(374.394,'K')),
            NASAPolynomial(coeffs=[1.1214,0.0373761,-2.31971e-05,6.86902e-09,-7.81154e-13,-34540.2,23.1318], Tmin=(374.394,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-290.362,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.184 kJ/mol
""",
    rank = 5,
)

entry(
    index = 139,
    label = "CC(F)C(C)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6438,0.0301581,2.54735e-05,-5.26032e-08,2.30337e-11,-66805.1,9.52988], Tmin=(10,'K'), Tmax=(799.754,'K')),
            NASAPolynomial(coeffs=[2.16963,0.0478769,-2.71635e-05,7.44957e-09,-7.94833e-13,-66900.2,14.244], Tmin=(799.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-555.483,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.748 kJ/mol
""",
    rank = 5,
)

entry(
    index = 140,
    label = "C[CH]C(C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59256,0.0418947,-8.31504e-05,2.08161e-07,-1.84293e-10,-19121.3,9.87204], Tmin=(10,'K'), Tmax=(427.835,'K')),
            NASAPolynomial(coeffs=[0.845459,0.0467926,-2.74468e-05,7.80419e-09,-8.6188e-13,-18696,23.0161], Tmin=(427.835,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 141,
    label = "OCC(O)F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92998,0.00427192,0.000111198,-2.1781e-07,1.32309e-10,-77523.9,9.80276], Tmin=(10,'K'), Tmax=(522.797,'K')),
            NASAPolynomial(coeffs=[1.62247,0.0365404,-2.33145e-05,7.18556e-09,-8.51174e-13,-77482.3,17.5286], Tmin=(522.797,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-644.594,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.964 kJ/mol
""",
    rank = 5,
)

entry(
    index = 142,
    label = "ODCC[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84516,0.023606,-3.99572e-06,-6.97456e-09,3.03174e-12,-22334.9,10.2448], Tmin=(10,'K'), Tmax=(1185.4,'K')),
            NASAPolynomial(coeffs=[7.73922,0.0191341,-9.30567e-06,2.18044e-09,-2.00006e-13,-23867.1,-11.7729], Tmin=(1185.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-185.684,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.18 kJ/mol
""",
    rank = 5,
)

entry(
    index = 143,
    label = "FCC(CF)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50177,0.0550002,-0.000172339,5.00175e-07,-4.88314e-10,-85094.5,10.6177], Tmin=(10,'K'), Tmax=(378.187,'K')),
            NASAPolynomial(coeffs=[0.106961,0.0555798,-3.45226e-05,1.02378e-08,-1.16634e-12,-84585.1,27.0347], Tmin=(378.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-707.538,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.411 kJ/mol
""",
    rank = 5,
)

entry(
    index = 144,
    label = "[O]CC#CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88528,0.00868397,9.86023e-05,-2.92126e-07,2.5411e-10,16924.8,10.1177], Tmin=(10,'K'), Tmax=(395.164,'K')),
            NASAPolynomial(coeffs=[4.2064,0.0219602,-1.4526e-05,4.56396e-09,-5.4688e-13,16770.4,7.23402], Tmin=(395.164,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.726,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.253 kJ/mol
""",
    rank = 5,
)

entry(
    index = 145,
    label = "[CH2]CC(F)F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77573,0.0193471,3.73902e-05,-8.26462e-08,4.64867e-11,-40445.4,9.85852], Tmin=(10,'K'), Tmax=(595.417,'K')),
            NASAPolynomial(coeffs=[2.83482,0.0340454,-2.07425e-05,6.07253e-09,-6.85396e-13,-40481.9,12.663], Tmin=(595.417,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-336.311,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.759 kJ/mol
""",
    rank = 5,
)

entry(
    index = 146,
    label = "FC1CC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13568,-0.01118,0.000133646,-2.09255e-07,1.06209e-10,-17456.8,8.26145], Tmin=(10,'K'), Tmax=(617.155,'K')),
            NASAPolynomial(coeffs=[0.0201552,0.0339574,-2.09362e-05,6.20276e-09,-7.06155e-13,-17300.5,23.2815], Tmin=(617.155,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-145.143,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.878 kJ/mol
""",
    rank = 5,
)

entry(
    index = 147,
    label = "[O]COF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95718,0.00256936,6.12089e-05,-1.19671e-07,7.14503e-11,-6865.54,9.43001], Tmin=(10,'K'), Tmax=(540.511,'K')),
            NASAPolynomial(coeffs=[2.80301,0.0203402,-1.37212e-05,4.33929e-09,-5.19561e-13,-6875.6,13.0409], Tmin=(540.511,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-57.0995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.56 kJ/mol
""",
    rank = 5,
)

entry(
    index = 148,
    label = "F[C]1CC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93925,0.0035238,8.65405e-05,-1.61353e-07,9.15668e-11,-10658.5,9.98586], Tmin=(10,'K'), Tmax=(569.361,'K')),
            NASAPolynomial(coeffs=[2.05238,0.0305155,-2.07571e-05,6.65396e-09,-8.07864e-13,-10666.3,16.071], Tmin=(569.361,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.6457,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 149,
    label = "FC1D[C]OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u1 p0 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94365,0.00365362,5.24993e-05,-1.24589e-07,8.65079e-11,-36374.6,10.1082], Tmin=(10,'K'), Tmax=(494.941,'K')),
            NASAPolynomial(coeffs=[4.11264,0.0131624,-9.27537e-06,3.0108e-09,-3.66865e-13,-36524.6,8.06623], Tmin=(494.941,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-302.449,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 150,
    label = "FC1[C]DCC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07024,-0.00631007,0.000126133,-2.06517e-07,1.07427e-10,24146.9,9.81639], Tmin=(10,'K'), Tmax=(611.103,'K')),
            NASAPolynomial(coeffs=[0.656499,0.0351452,-2.25304e-05,6.83641e-09,-7.9015e-13,24207.3,21.6849], Tmin=(611.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (200.759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 151,
    label = "OC(F)OCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  F u0 p3 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8051,0.024542,9.60782e-06,-2.80859e-08,1.20597e-11,-102252,10.8664], Tmin=(10,'K'), Tmax=(928.583,'K')),
            NASAPolynomial(coeffs=[5.80333,0.0280975,-1.57838e-05,4.24983e-09,-4.43728e-13,-103147,-1.44951], Tmin=(928.583,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-850.15,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 152,
    label = "CC(F)CD[C]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u1 p0 c0 {4,D} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75873,0.0223986,7.4877e-05,-2.51581e-07,2.52109e-10,-19250.8,11.4887], Tmin=(10,'K'), Tmax=(255.848,'K')),
            NASAPolynomial(coeffs=[2.67494,0.0393429,-2.44649e-05,7.27597e-09,-8.31367e-13,-19195.3,15.24], Tmin=(255.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-160.054,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 153,
    label = "F[CH]C1OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {4,S} {6,S}
6 O u0 p2 c0 {4,S} {5,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81616,0.0170003,1.6089e-05,-4.59824e-08,2.59246e-11,-5051.32,10.0563], Tmin=(10,'K'), Tmax=(670.688,'K')),
            NASAPolynomial(coeffs=[4.75944,0.020739,-1.32164e-05,3.96532e-09,-4.53464e-13,-5388.46,4.31215], Tmin=(670.688,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-42.0205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.349 kJ/mol
""",
    rank = 5,
)

entry(
    index = 154,
    label = "CCOCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69266,0.0349351,-0.000109099,3.47546e-07,-3.40372e-10,-55306,8.88419], Tmin=(10,'K'), Tmax=(399.157,'K')),
            NASAPolynomial(coeffs=[-0.53983,0.0451519,-2.64969e-05,7.49886e-09,-8.22501e-13,-54711.6,28.6294], Tmin=(399.157,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-459.856,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.503 kJ/mol
""",
    rank = 5,
)

entry(
    index = 155,
    label = "FC(F)C1OO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
5 O u0 p2 c0 {4,S} {6,S}
6 O u0 p2 c0 {4,S} {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88854,0.0163586,2.63679e-05,-5.21557e-08,2.40025e-11,-52996.4,10.3696], Tmin=(10,'K'), Tmax=(804.443,'K')),
            NASAPolynomial(coeffs=[5.25731,0.0239956,-1.48035e-05,4.28299e-09,-4.7325e-13,-53684,1.15929], Tmin=(804.443,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-440.62,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 156,
    label = "CCC(F)CF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84546,0.0300373,1.43457e-05,-2.86176e-08,9.91427e-12,-64029.5,10.3587], Tmin=(10,'K'), Tmax=(1134.77,'K')),
            NASAPolynomial(coeffs=[7.17595,0.0362809,-1.7679e-05,4.16203e-09,-3.84096e-13,-65943.2,-11.2318], Tmin=(1134.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-532.322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.035 kJ/mol
""",
    rank = 5,
)

entry(
    index = 157,
    label = "[C]#CC(DC)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86137,0.0109969,7.11709e-05,-1.9992e-07,1.59526e-10,51245.8,10.1508], Tmin=(10,'K'), Tmax=(430.344,'K')),
            NASAPolynomial(coeffs=[4.01475,0.0226882,-1.53011e-05,4.86596e-09,-5.86349e-13,51111.2,8.12899], Tmin=(430.344,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (426.076,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.296 kJ/mol
""",
    rank = 5,
)

entry(
    index = 158,
    label = "C[C](F)CDO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {9,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87063,0.0111942,9.12758e-05,-2.72267e-07,2.62779e-10,-30033.5,9.10582], Tmin=(10,'K'), Tmax=(263.523,'K')),
            NASAPolynomial(coeffs=[2.60052,0.0304731,-1.8463e-05,5.35516e-09,-5.98896e-13,-29966.5,13.5395], Tmin=(263.523,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.712,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.694 kJ/mol
""",
    rank = 5,
)

entry(
    index = 159,
    label = "OCCOF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80687,0.0181505,3.17456e-05,-6.06847e-08,2.88529e-11,-35573.3,9.91656], Tmin=(10,'K'), Tmax=(724.976,'K')),
            NASAPolynomial(coeffs=[3.01876,0.0326326,-1.91855e-05,5.43073e-09,-5.94977e-13,-35725.3,11.6286], Tmin=(724.976,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-295.789,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.756 kJ/mol
""",
    rank = 5,
)

entry(
    index = 160,
    label = "O[CH]C#CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87011,0.00981112,9.32752e-05,-2.78008e-07,2.38367e-10,5753.75,10.0924], Tmin=(10,'K'), Tmax=(406.737,'K')),
            NASAPolynomial(coeffs=[4.47078,0.0214577,-1.44125e-05,4.60536e-09,-5.58973e-13,5559.69,5.94989], Tmin=(406.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (47.8415,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 161,
    label = "O[C]DCDCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76546,0.0218937,7.04115e-05,-3.77951e-07,4.70906e-10,3238.95,10.0773], Tmin=(10,'K'), Tmax=(309.936,'K')),
            NASAPolynomial(coeffs=[5.43631,0.0197565,-1.32639e-05,4.26606e-09,-5.22412e-13,3042.07,2.46838], Tmin=(309.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.9557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.018 kJ/mol
""",
    rank = 5,
)

entry(
    index = 162,
    label = "FC[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89225,0.0155689,9.68674e-06,-2.40175e-08,1.0511e-11,-57384.8,9.73801], Tmin=(10,'K'), Tmax=(896.812,'K')),
            NASAPolynomial(coeffs=[5.46313,0.0181196,-1.05649e-05,2.92012e-09,-3.10852e-13,-58050.9,0.187729], Tmin=(896.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-477.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.202 kJ/mol
""",
    rank = 5,
)

entry(
    index = 163,
    label = "C[C](F)C(C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67581,0.0370467,-8.69558e-06,-7.82547e-09,3.69646e-12,-43149,10.1222], Tmin=(10,'K'), Tmax=(1189.37,'K')),
            NASAPolynomial(coeffs=[8.60563,0.0314032,-1.53705e-05,3.64687e-09,-3.39968e-13,-45095.2,-17.7681], Tmin=(1189.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-358.761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 164,
    label = "F[C]DCDC(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81157,0.0146788,8.11017e-05,-2.82662e-07,2.57201e-10,-17811,11.4804], Tmin=(10,'K'), Tmax=(405.886,'K')),
            NASAPolynomial(coeffs=[5.58389,0.0188171,-1.40342e-05,4.7393e-09,-5.93746e-13,-18132.8,2.33578], Tmin=(405.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-148.086,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.584 kJ/mol
""",
    rank = 5,
)

entry(
    index = 165,
    label = "ODCOF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9684,0.00186269,4.55355e-05,-8.67806e-08,5.04047e-11,-27931.6,8.23694], Tmin=(10,'K'), Tmax=(555.027,'K')),
            NASAPolynomial(coeffs=[3.01328,0.0157137,-1.07285e-05,3.4188e-09,-4.11573e-13,-27932.9,11.3157], Tmin=(555.027,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.249,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 166,
    label = "FC1CD[C]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u1 p0 c0 {3,D} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07735,-0.00704865,0.000132756,-2.21272e-07,1.17398e-10,23510.1,9.78497], Tmin=(10,'K'), Tmax=(600.413,'K')),
            NASAPolynomial(coeffs=[0.781621,0.0350007,-2.2493e-05,6.84528e-09,-7.9354e-13,23543.7,20.9877], Tmin=(600.413,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (195.463,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 167,
    label = "FCCDCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82444,0.0323728,2.35686e-06,-2.01128e-08,8.12263e-12,-73917.7,11.3194], Tmin=(10,'K'), Tmax=(1089.3,'K')),
            NASAPolynomial(coeffs=[8.75857,0.0297607,-1.53991e-05,3.82229e-09,-3.69823e-13,-75912.6,-17.1298], Tmin=(1089.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-614.533,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.129 kJ/mol
""",
    rank = 5,
)

entry(
    index = 168,
    label = "O[C](F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95192,0.00276297,4.92656e-05,-9.7094e-08,5.61315e-11,-56249.1,8.32962], Tmin=(10,'K'), Tmax=(589.874,'K')),
            NASAPolynomial(coeffs=[3.82739,0.0150114,-1.08804e-05,3.65661e-09,-4.58991e-13,-56432.8,7.18293], Tmin=(589.874,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-467.702,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.931 kJ/mol
""",
    rank = 5,
)

entry(
    index = 169,
    label = "OOCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78463,0.019311,5.39668e-05,-2.36024e-07,2.47925e-10,5341.3,10.2593], Tmin=(10,'K'), Tmax=(354.498,'K')),
            NASAPolynomial(coeffs=[4.83154,0.0215222,-1.47297e-05,4.76158e-09,-5.8243e-13,5178.95,5.05141], Tmin=(354.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (44.4262,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.708 kJ/mol
""",
    rank = 5,
)

entry(
    index = 170,
    label = "C[CH]COF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  O u0 p2 c0 {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59366,0.0426674,-0.000109547,2.70477e-07,-2.40667e-10,3453.75,10.005], Tmin=(10,'K'), Tmax=(400.625,'K')),
            NASAPolynomial(coeffs=[1.99789,0.0391928,-2.38737e-05,6.9925e-09,-7.90194e-13,3737.35,18.1878], Tmin=(400.625,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (28.704,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 171,
    label = "ODC([CH]F)CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72596,0.0250146,7.34851e-06,-3.32647e-08,1.7646e-11,-49228.9,11.4785], Tmin=(10,'K'), Tmax=(755.427,'K')),
            NASAPolynomial(coeffs=[5.06547,0.0275334,-1.67379e-05,4.83413e-09,-5.36267e-13,-49705.5,3.5766], Tmin=(755.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-409.336,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.522 kJ/mol
""",
    rank = 5,
)

entry(
    index = 172,
    label = "C#COC(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8548,0.010222,0.000114316,-3.04882e-07,2.35617e-10,-40857.1,10.8214], Tmin=(10,'K'), Tmax=(448.37,'K')),
            NASAPolynomial(coeffs=[4.47894,0.0273515,-1.89233e-05,6.13093e-09,-7.4838e-13,-41141.2,5.7667], Tmin=(448.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-339.72,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.445 kJ/mol
""",
    rank = 5,
)

entry(
    index = 173,
    label = "[CH2]OC(C)F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  O u0 p2 c0 {1,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80903,0.0165585,8.2106e-05,-2.20093e-07,1.82808e-10,-34461.5,9.24928], Tmin=(10,'K'), Tmax=(308.843,'K')),
            NASAPolynomial(coeffs=[2.139,0.038188,-2.29449e-05,6.6691e-09,-7.50193e-13,-34358.4,15.344], Tmin=(308.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-286.536,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.98 kJ/mol
""",
    rank = 5,
)

entry(
    index = 174,
    label = "FCDCOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85978,0.0115119,5.32356e-05,-1.30349e-07,8.78424e-11,-21886.1,9.72359], Tmin=(10,'K'), Tmax=(512.191,'K')),
            NASAPolynomial(coeffs=[3.95736,0.0228197,-1.52281e-05,4.77144e-09,-5.66561e-13,-22054.4,7.7726], Tmin=(512.191,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.993,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 175,
    label = "FCC#CCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,T}
4  C u0 p0 c0 {3,T} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9403,0.0295778,-1.35004e-05,1.42755e-09,3.42799e-13,-24343.6,9.99899], Tmin=(10,'K'), Tmax=(1609.25,'K')),
            NASAPolynomial(coeffs=[17.8089,0.00453704,1.04909e-06,-9.57902e-10,1.47593e-13,-30028.5,-67.3018], Tmin=(1609.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.413,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.562 kJ/mol
""",
    rank = 5,
)

entry(
    index = 176,
    label = "FC1DC(F)[CH]1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {2,S} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93112,0.00418895,7.09874e-05,-1.51195e-07,9.49936e-11,16737.2,9.27177], Tmin=(10,'K'), Tmax=(541.083,'K')),
            NASAPolynomial(coeffs=[3.82834,0.0198954,-1.399e-05,4.55823e-09,-5.58081e-13,16529.5,7.68265], Tmin=(541.083,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.136,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.589 kJ/mol
""",
    rank = 5,
)

entry(
    index = 177,
    label = "OOCCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83713,0.0139724,5.58891e-05,-1.09354e-07,6.09367e-11,-43012.5,9.74497], Tmin=(10,'K'), Tmax=(574.559,'K')),
            NASAPolynomial(coeffs=[2.06949,0.0348929,-2.12178e-05,6.20929e-09,-7.01063e-13,-42951.5,16.0559], Tmin=(574.559,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-357.649,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.256 kJ/mol
""",
    rank = 5,
)

entry(
    index = 178,
    label = "OCC[CH]F",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76209,0.0233651,1.74923e-05,-3.73281e-08,1.59917e-11,-32086,10.6918], Tmin=(10,'K'), Tmax=(853.464,'K')),
            NASAPolynomial(coeffs=[3.67837,0.0339378,-1.89822e-05,5.13951e-09,-5.42019e-13,-32442.5,8.91033], Tmin=(853.464,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-266.785,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.377 kJ/mol
""",
    rank = 5,
)

entry(
    index = 179,
    label = "CC(F)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 O u1 p2 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81586,0.0183184,1.96531e-05,-4.09434e-08,1.87424e-11,-30827.8,10.4601], Tmin=(10,'K'), Tmax=(788.852,'K')),
            NASAPolynomial(coeffs=[3.84659,0.0276413,-1.60982e-05,4.50252e-09,-4.8743e-13,-31127.5,8.44984], Tmin=(788.852,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 180,
    label = "COC[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61402,0.0412446,-0.000102007,2.75178e-07,-2.65426e-10,-52334.3,9.84642], Tmin=(10,'K'), Tmax=(378.954,'K')),
            NASAPolynomial(coeffs=[1.79904,0.0412173,-2.59592e-05,7.7983e-09,-8.98411e-13,-52059,18.659], Tmin=(378.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-435.144,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.253 kJ/mol
""",
    rank = 5,
)

entry(
    index = 181,
    label = "CDC(C)[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88365,0.0131147,0.000246399,-1.19281e-06,1.97988e-09,-32805.5,9.48505], Tmin=(10,'K'), Tmax=(151.595,'K')),
            NASAPolynomial(coeffs=[2.83729,0.0407228,-2.67646e-05,8.41724e-09,-1.01099e-12,-32773.8,12.5592], Tmin=(151.595,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-272.513,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.188 kJ/mol
""",
    rank = 5,
)

entry(
    index = 182,
    label = "CDCOC(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86846,0.0236831,1.09891e-05,-2.76894e-08,1.11868e-11,-68919.1,11.8155], Tmin=(10,'K'), Tmax=(989.283,'K')),
            NASAPolynomial(coeffs=[6.63222,0.0265079,-1.4521e-05,3.80616e-09,-3.87214e-13,-70151,-4.95066], Tmin=(989.283,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-572.981,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.383 kJ/mol
""",
    rank = 5,
)

entry(
    index = 183,
    label = "F[C]DCCDCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78819,0.0224409,1.41048e-05,-3.87686e-08,1.87084e-11,-3578,11.2806], Tmin=(10,'K'), Tmax=(800.939,'K')),
            NASAPolynomial(coeffs=[5.21968,0.0269514,-1.61784e-05,4.61315e-09,-5.05681e-13,-4181.29,2.35764], Tmin=(800.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.7529,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 184,
    label = "ODC(F)OCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93203,0.0197898,3.9853e-06,-1.62309e-08,6.53518e-12,-97420.2,10.4007], Tmin=(10,'K'), Tmax=(1064.61,'K')),
            NASAPolynomial(coeffs=[7.54973,0.0177638,-9.45698e-06,2.39195e-09,-2.34448e-13,-98845.9,-10.3576], Tmin=(1064.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-809.945,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.851 kJ/mol
""",
    rank = 5,
)

entry(
    index = 185,
    label = "FCCOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90944,0.0170204,1.75203e-05,-3.10931e-08,1.20441e-11,-38054.5,9.71498], Tmin=(10,'K'), Tmax=(963.365,'K')),
            NASAPolynomial(coeffs=[5.0043,0.0247009,-1.34758e-05,3.53081e-09,-3.59845e-13,-38832.9,1.52911], Tmin=(963.365,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-316.366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 186,
    label = "O[C]1OC1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92363,0.0046119,8.26801e-05,-1.72299e-07,1.06647e-10,-30388.9,9.92542], Tmin=(10,'K'), Tmax=(545.289,'K')),
            NASAPolynomial(coeffs=[3.58137,0.023892,-1.64864e-05,5.34013e-09,-6.52677e-13,-30600.9,9.08298], Tmin=(545.289,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-252.696,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 187,
    label = "CC1(F)CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96027,0.00250109,0.000130176,-2.40149e-07,1.43836e-10,-23586.8,7.91504], Tmin=(10,'K'), Tmax=(429.896,'K')),
            NASAPolynomial(coeffs=[-1.02871,0.0488347,-3.11891e-05,9.62128e-09,-1.14183e-12,-23157,27.7815], Tmin=(429.896,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-196.122,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.327 kJ/mol
""",
    rank = 5,
)

entry(
    index = 188,
    label = "COC(O)(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  O u0 p2 c0 {3,S} {10,S}
5  F u0 p3 c0 {3,S}
6  F u0 p3 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69796,0.0262946,2.21053e-05,-6.91641e-08,4.19159e-11,-106035,9.72301], Tmin=(10,'K'), Tmax=(608.656,'K')),
            NASAPolynomial(coeffs=[4.25725,0.0331487,-2.0736e-05,6.18349e-09,-7.06872e-13,-106298,5.70021], Tmin=(608.656,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-881.66,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 189,
    label = "FOCC(F)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69027,0.0366592,-1.7758e-05,-2.8216e-09,3.41009e-12,-46101.4,11.7198], Tmin=(10,'K'), Tmax=(1032.79,'K')),
            NASAPolynomial(coeffs=[9.5476,0.0238062,-1.33711e-05,3.56474e-09,-3.67147e-13,-47835.6,-19.2662], Tmin=(1032.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-383.295,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.324 kJ/mol
""",
    rank = 5,
)

entry(
    index = 190,
    label = "FOOCDC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62945,0.0337342,-9.71846e-06,-2.99069e-08,2.29251e-11,-38923.6,12.1843], Tmin=(10,'K'), Tmax=(677.149,'K')),
            NASAPolynomial(coeffs=[7.63002,0.0233094,-1.58815e-05,4.9636e-09,-5.82794e-13,-39768.1,-7.79224], Tmin=(677.149,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-323.672,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 191,
    label = "FCC(CF)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52387,0.0510785,-0.000133151,3.55975e-07,-3.49276e-10,-63746.5,11.7603], Tmin=(10,'K'), Tmax=(362.085,'K')),
            NASAPolynomial(coeffs=[2.02181,0.0469955,-3.05802e-05,9.41347e-09,-1.10451e-12,-63502.2,19.3526], Tmin=(362.085,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-530.029,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 192,
    label = "[CH2]C(O)CF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  O u0 p2 c0 {4,S} {9,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87683,0.0117121,0.000156862,-5.28928e-07,5.94396e-10,-32324.8,10.3231], Tmin=(10,'K'), Tmax=(225.234,'K')),
            NASAPolynomial(coeffs=[2.34489,0.0389184,-2.43243e-05,7.36055e-09,-8.58542e-13,-32255.8,15.4303], Tmin=(225.234,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-268.742,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 193,
    label = "FOCOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85373,0.0160467,1.49614e-05,-3.72087e-08,1.84304e-11,-18831.7,9.11995], Tmin=(10,'K'), Tmax=(769.553,'K')),
            NASAPolynomial(coeffs=[5.06839,0.0198941,-1.23438e-05,3.6036e-09,-4.01955e-13,-19319.5,1.62326], Tmin=(769.553,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-156.578,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.133 kJ/mol
""",
    rank = 5,
)

entry(
    index = 194,
    label = "[CH2]C(DO)CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89564,0.00802462,9.27578e-05,-2.06557e-07,1.40493e-10,-26978.1,9.81957], Tmin=(10,'K'), Tmax=(467.342,'K')),
            NASAPolynomial(coeffs=[2.38078,0.0321643,-2.05866e-05,6.29065e-09,-7.35616e-13,-26958.5,14.67], Tmin=(467.342,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-224.322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.75 kJ/mol
""",
    rank = 5,
)

entry(
    index = 195,
    label = "O[C]1CC1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9272,0.00425559,9.92077e-05,-1.88198e-07,1.08543e-10,-11096.8,9.86934], Tmin=(10,'K'), Tmax=(564.542,'K')),
            NASAPolynomial(coeffs=[2.11993,0.0335452,-2.24147e-05,7.14844e-09,-8.68082e-13,-11155.4,15.2285], Tmin=(564.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.2941,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.822 kJ/mol
""",
    rank = 5,
)

entry(
    index = 196,
    label = "C[CH]CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7325,0.0293067,-8.15913e-05,2.39009e-07,-2.24449e-10,-13280.1,8.48045], Tmin=(10,'K'), Tmax=(410.006,'K')),
            NASAPolynomial(coeffs=[0.834166,0.0350873,-2.044e-05,5.75911e-09,-6.30002e-13,-12853.3,22.185], Tmin=(410.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.427,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.356 kJ/mol
""",
    rank = 5,
)

entry(
    index = 197,
    label = "FCC(F)OOF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71996,0.0379683,-2.41877e-05,5.60994e-09,3.70644e-14,-57932.9,11.7652], Tmin=(10,'K'), Tmax=(1242.84,'K')),
            NASAPolynomial(coeffs=[11.9378,0.0186073,-9.37496e-06,2.25283e-09,-2.10643e-13,-60523,-31.8701], Tmin=(1242.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-481.665,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 198,
    label = "C#CC(DC)F",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90578,0.00568492,9.54305e-05,-2.01477e-07,1.25686e-10,10273.7,9.07158], Tmin=(10,'K'), Tmax=(547.964,'K')),
            NASAPolynomial(coeffs=[4.02266,0.0258372,-1.72351e-05,5.55109e-09,-6.83873e-13,9945.55,5.70049], Tmin=(547.964,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (85.386,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.725 kJ/mol
""",
    rank = 5,
)

entry(
    index = 199,
    label = "FC1OC1(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91658,0.00488117,8.78034e-05,-1.76648e-07,1.04565e-10,-83851,10.1307], Tmin=(10,'K'), Tmax=(572.891,'K')),
            NASAPolynomial(coeffs=[3.54048,0.0266613,-1.93746e-05,6.43368e-09,-7.96256e-13,-84122.2,8.99236], Tmin=(572.891,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-697.211,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.538 kJ/mol
""",
    rank = 5,
)

entry(
    index = 200,
    label = "C#C[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9073,0.00621604,7.54636e-05,-1.97406e-07,1.48212e-10,19787.1,8.53809], Tmin=(10,'K'), Tmax=(471.968,'K')),
            NASAPolynomial(coeffs=[4.94468,0.015244,-9.86381e-06,3.11957e-09,-3.8064e-13,19490.7,2.20963], Tmin=(471.968,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (164.504,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.17 kJ/mol
""",
    rank = 5,
)

entry(
    index = 201,
    label = "CCOOF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77619,0.0246135,3.49033e-06,-1.80032e-08,7.55819e-12,-11970.6,8.88526], Tmin=(10,'K'), Tmax=(987.405,'K')),
            NASAPolynomial(coeffs=[5.43293,0.0272289,-1.46516e-05,3.81206e-09,-3.87283e-13,-12752.5,-1.38889], Tmin=(987.405,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-99.5231,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 202,
    label = "CC(F)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79241,0.0179312,5.14474e-05,-1.08398e-07,6.52215e-11,-30657,10.4569], Tmin=(10,'K'), Tmax=(437.416,'K')),
            NASAPolynomial(coeffs=[1.37516,0.0400357,-2.43532e-05,7.12896e-09,-8.05591e-13,-30445.5,20.12], Tmin=(437.416,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-254.915,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 203,
    label = "OO[C](F)CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68951,0.0367911,0.000181912,-1.63441e-06,3.40797e-09,-71440.9,12.2473], Tmin=(10,'K'), Tmax=(188.259,'K')),
            NASAPolynomial(coeffs=[5.5869,0.0292992,-1.99151e-05,6.40695e-09,-7.81785e-13,-71570.5,4.71723], Tmin=(188.259,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-593.628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 204,
    label = "OC(CF)OF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {2,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68099,0.0297617,-2.50078e-07,-2.36551e-08,1.27423e-11,-60777.4,10.9583], Tmin=(10,'K'), Tmax=(809.178,'K')),
            NASAPolynomial(coeffs=[5.61474,0.0296281,-1.7475e-05,4.93137e-09,-5.37142e-13,-61398.9,0.131824], Tmin=(809.178,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-505.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 205,
    label = "[O]OC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9172,0.0118609,1.81366e-05,-3.80792e-08,1.81208e-11,-51537.7,10.5851], Tmin=(10,'K'), Tmax=(788.222,'K')),
            NASAPolynomial(coeffs=[5.16865,0.0161371,-1.02243e-05,3.01247e-09,-3.37249e-13,-52065.1,2.75126], Tmin=(788.222,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-428.498,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.337 kJ/mol
""",
    rank = 5,
)

entry(
    index = 206,
    label = "CDCC(F)D[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {3,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79039,0.0175735,7.03148e-05,-1.96723e-07,1.51679e-10,-1083.14,11.1012], Tmin=(10,'K'), Tmax=(439.228,'K')),
            NASAPolynomial(coeffs=[3.58313,0.0319088,-2.11514e-05,6.62842e-09,-7.89534e-13,-1185.01,10.5638], Tmin=(439.228,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.01646,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 207,
    label = "OCCCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
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
            NASAPolynomial(coeffs=[3.87644,0.0145385,5.25185e-05,-7.87329e-08,3.28652e-11,-55867,9.70643], Tmin=(10,'K'), Tmax=(795.903,'K')),
            NASAPolynomial(coeffs=[1.38141,0.0408493,-2.30224e-05,6.28188e-09,-6.67385e-13,-55906,18.4338], Tmin=(795.903,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-464.495,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.378 kJ/mol
""",
    rank = 5,
)

entry(
    index = 208,
    label = "[O]CCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88895,0.01443,1.05626e-05,-1.87743e-08,6.74492e-12,-25091.4,9.14805], Tmin=(10,'K'), Tmax=(1048.5,'K')),
            NASAPolynomial(coeffs=[4.54696,0.0206289,-1.07653e-05,2.70887e-09,-2.66409e-13,-25708.1,3.65944], Tmin=(1048.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-208.607,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.378 kJ/mol
""",
    rank = 5,
)

entry(
    index = 209,
    label = "FC1CO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11086,-0.00889343,9.96436e-05,-1.52447e-07,7.52807e-11,-33617.8,8.16205], Tmin=(10,'K'), Tmax=(638.71,'K')),
            NASAPolynomial(coeffs=[0.995487,0.025498,-1.60719e-05,4.81077e-09,-5.50079e-13,-33523.4,19.4191], Tmin=(638.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-279.51,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.556 kJ/mol
""",
    rank = 5,
)

entry(
    index = 210,
    label = "CCDC(F)OF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66364,0.0296292,4.09236e-06,-3.45665e-08,2.00135e-11,-29954.8,9.67395], Tmin=(10,'K'), Tmax=(707.093,'K')),
            NASAPolynomial(coeffs=[4.95866,0.0314286,-1.9083e-05,5.53527e-09,-6.17878e-13,-30366.1,2.26195], Tmin=(707.093,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.096,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 211,
    label = "CDCDC[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72006,0.0250253,5.04193e-05,-1.95496e-07,1.78845e-10,-9910.68,10.5732], Tmin=(10,'K'), Tmax=(395.479,'K')),
            NASAPolynomial(coeffs=[4.40346,0.0309526,-2.07604e-05,6.585e-09,-7.92845e-13,-10065.1,6.64077], Tmin=(395.479,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-82.3992,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.618 kJ/mol
""",
    rank = 5,
)

entry(
    index = 212,
    label = "FC1[C]DCO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04687,-0.00472207,0.000106077,-1.84771e-07,1.01115e-10,13264.1,9.68248], Tmin=(10,'K'), Tmax=(594.194,'K')),
            NASAPolynomial(coeffs=[2.18978,0.0260028,-1.74891e-05,5.48066e-09,-6.47792e-13,13163.1,14.9681], Tmin=(594.194,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.27,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 213,
    label = "F[C]1OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06,-0.00594738,7.75738e-05,-1.45017e-07,8.53559e-11,-1266.95,8.07641], Tmin=(10,'K'), Tmax=(566.536,'K')),
            NASAPolynomial(coeffs=[3.64636,0.0118298,-8.82974e-06,2.945e-09,-3.62544e-13,-1458.5,7.73275], Tmin=(566.536,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.5447,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.84 kJ/mol
""",
    rank = 5,
)

entry(
    index = 214,
    label = "FC1D[C]OC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u1 p0 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95556,0.00254392,7.15872e-05,-1.28578e-07,7.06802e-11,20134.6,9.57596], Tmin=(10,'K'), Tmax=(575.887,'K')),
            NASAPolynomial(coeffs=[1.79222,0.0274557,-1.90489e-05,6.15297e-09,-7.48437e-13,20219.8,17.3957], Tmin=(575.887,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (167.389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.254 kJ/mol
""",
    rank = 5,
)

entry(
    index = 215,
    label = "[O]CCDCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8766,0.0156851,2.90849e-05,-5.14975e-08,2.25426e-11,-13358.6,10.6516], Tmin=(10,'K'), Tmax=(812.876,'K')),
            NASAPolynomial(coeffs=[3.94173,0.027817,-1.62803e-05,4.55337e-09,-4.91758e-13,-13780.6,7.82028], Tmin=(812.876,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-111.058,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.583 kJ/mol
""",
    rank = 5,
)

entry(
    index = 216,
    label = "CC(F)C(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73195,0.0240467,2.48331e-05,-5.34609e-08,2.50726e-11,-88137.3,10.8501], Tmin=(10,'K'), Tmax=(763.051,'K')),
            NASAPolynomial(coeffs=[3.44485,0.036611,-2.16062e-05,6.10668e-09,-6.66738e-13,-88415.5,10.0478], Tmin=(763.051,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-732.838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.13 kJ/mol
""",
    rank = 5,
)

entry(
    index = 217,
    label = "FCCC[C](F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8626,0.0353208,-6.2493e-07,-1.63254e-08,6.37899e-12,-66531.4,11.6953], Tmin=(10,'K'), Tmax=(1185.23,'K')),
            NASAPolynomial(coeffs=[10.8902,0.0286163,-1.36709e-05,3.12336e-09,-2.77828e-13,-69392.2,-28.4444], Tmin=(1185.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-553.109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.269 kJ/mol
""",
    rank = 5,
)

entry(
    index = 218,
    label = "OCD[C]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80413,0.0215219,4.86072e-06,-1.89899e-08,8.1484e-12,-12662.1,10.3649], Tmin=(10,'K'), Tmax=(945.642,'K')),
            NASAPolynomial(coeffs=[5.16654,0.0244011,-1.34146e-05,3.55809e-09,-3.67556e-13,-13306.2,1.82511], Tmin=(945.642,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 219,
    label = "C[CH]C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86813,0.0254031,-2.35136e-06,-8.95576e-09,3.54388e-12,-41309.7,9.78138], Tmin=(10,'K'), Tmax=(1223.58,'K')),
            NASAPolynomial(coeffs=[8.64917,0.0205102,-9.51528e-06,2.11886e-09,-1.84096e-13,-43283.4,-17.5334], Tmin=(1223.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-343.44,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.689 kJ/mol
""",
    rank = 5,
)

entry(
    index = 220,
    label = "F[C]1OCC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93042,0.00413092,0.000104798,-2.00095e-07,1.1701e-10,-38821.8,11.1744], Tmin=(10,'K'), Tmax=(547.266,'K')),
            NASAPolynomial(coeffs=[1.59686,0.0362545,-2.45483e-05,7.7796e-09,-9.32402e-13,-38792,18.9642], Tmin=(547.266,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-322.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.093 kJ/mol
""",
    rank = 5,
)

entry(
    index = 221,
    label = "CC([O])(O)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u1 p2 c0 {2,S}
4 O u0 p2 c0 {2,S} {9,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89563,0.00656475,0.000113366,-2.49873e-07,1.64645e-10,-55270.7,9.91679], Tmin=(10,'K'), Tmax=(512.296,'K')),
            NASAPolynomial(coeffs=[3.64003,0.0302989,-1.97777e-05,6.221e-09,-7.49914e-13,-55529.7,8.19483], Tmin=(512.296,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-459.577,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 222,
    label = "CCOF",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8921,0.0104958,3.70062e-05,-5.7306e-08,2.48135e-11,-16752.3,7.5376], Tmin=(10,'K'), Tmax=(754.745,'K')),
            NASAPolynomial(coeffs=[1.9151,0.0292339,-1.66517e-05,4.59127e-09,-4.92529e-13,-16689.2,14.9606], Tmin=(754.745,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-139.291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 223,
    label = "[CH2]CC(C)F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68327,0.0293328,1.34338e-05,-3.28348e-08,1.35545e-11,-18104.4,9.5857], Tmin=(10,'K'), Tmax=(903.669,'K')),
            NASAPolynomial(coeffs=[3.48804,0.0404261,-2.19594e-05,5.80224e-09,-5.99857e-13,-18486.8,8.19681], Tmin=(903.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-150.544,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 224,
    label = "FCDCC(F)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65969,0.0358338,-1.54526e-05,-6.01834e-09,4.94447e-12,-52062.5,11.7161], Tmin=(10,'K'), Tmax=(956.8,'K')),
            NASAPolynomial(coeffs=[8.32501,0.025915,-1.49294e-05,4.08727e-09,-4.31718e-13,-53394,-12.878], Tmin=(956.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-432.875,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 225,
    label = "[CH]DCOOF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86875,0.00877077,0.00010168,-2.63926e-07,1.95284e-10,35689.7,10.5311], Tmin=(10,'K'), Tmax=(478.047,'K')),
            NASAPolynomial(coeffs=[5.17162,0.0219981,-1.55355e-05,5.12215e-09,-6.34047e-13,35289.4,2.32344], Tmin=(478.047,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (296.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 226,
    label = "C#CCC(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {7,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82198,0.0145745,9.87456e-05,-2.54609e-07,1.93312e-10,-31303.5,10.7832], Tmin=(10,'K'), Tmax=(430.493,'K')),
            NASAPolynomial(coeffs=[2.9318,0.0362698,-2.36231e-05,7.32798e-09,-8.67531e-13,-31351.3,12.8828], Tmin=(430.493,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-260.28,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.827 kJ/mol
""",
    rank = 5,
)

entry(
    index = 227,
    label = "[O]C(O)(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {6,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91388,0.00503082,7.45771e-05,-1.5679e-07,9.45858e-11,-76685.3,9.76162], Tmin=(10,'K'), Tmax=(580.646,'K')),
            NASAPolynomial(coeffs=[4.70617,0.0195797,-1.46918e-05,5.04507e-09,-6.42534e-13,-77114.6,3.46575], Tmin=(580.646,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-637.633,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 228,
    label = "OCOF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95344,0.00295724,7.40363e-05,-1.53518e-07,9.9067e-11,-34379.5,8.74486], Tmin=(10,'K'), Tmax=(491.339,'K')),
            NASAPolynomial(coeffs=[2.62718,0.0228682,-1.45731e-05,4.46251e-09,-5.24202e-13,-34359.2,13.0813], Tmin=(491.339,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-285.86,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.366 kJ/mol
""",
    rank = 5,
)

entry(
    index = 229,
    label = "CC[C]DC(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u1 p0 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80843,0.0310345,-7.2335e-06,-6.80494e-09,3.15801e-12,-19432.6,10.6542], Tmin=(10,'K'), Tmax=(1226.28,'K')),
            NASAPolynomial(coeffs=[9.61651,0.0230527,-1.08808e-05,2.46861e-09,-2.18904e-13,-21681.4,-21.9123], Tmin=(1226.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-161.547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 230,
    label = "F[C]1OOC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91449,0.00517856,9.10536e-05,-1.91399e-07,1.18883e-10,-28600.5,11.2066], Tmin=(10,'K'), Tmax=(543.655,'K')),
            NASAPolynomial(coeffs=[3.50573,0.0266604,-1.91897e-05,6.29524e-09,-7.69538e-13,-28829.1,10.4185], Tmin=(543.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-237.829,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 231,
    label = "FC(F)[C]1CC1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91825,0.00538003,0.000141482,-3.02867e-07,2.03635e-10,-20899.8,11.4404], Tmin=(10,'K'), Tmax=(462.67,'K')),
            NASAPolynomial(coeffs=[1.20281,0.0432552,-2.79933e-05,8.5963e-09,-1.00699e-12,-20802.7,20.7825], Tmin=(462.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-173.786,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.369 kJ/mol
""",
    rank = 5,
)

entry(
    index = 232,
    label = "[O]OC(F)DCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,D} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79734,0.016396,5.59523e-05,-1.60958e-07,1.17656e-10,-29785.5,11.3726], Tmin=(10,'K'), Tmax=(498.054,'K')),
            NASAPolynomial(coeffs=[5.08837,0.0232363,-1.64771e-05,5.36582e-09,-6.53751e-13,-30127.5,3.90133], Tmin=(498.054,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-247.678,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 233,
    label = "OOF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97542,0.00135438,2.85958e-05,-5.16587e-08,2.76807e-11,-7170.06,6.74021], Tmin=(10,'K'), Tmax=(624.092,'K')),
            NASAPolynomial(coeffs=[3.54968,0.0102075,-7.40237e-06,2.51916e-09,-3.20767e-13,-7236.19,7.6379], Tmin=(624.092,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-59.6267,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 234,
    label = "FC[C]1CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97312,0.0129716,2.95068e-05,-4.39297e-08,1.67828e-11,-8825.26,10.0295], Tmin=(10,'K'), Tmax=(934.37,'K')),
            NASAPolynomial(coeffs=[4.32335,0.0258534,-1.426e-05,3.76994e-09,-3.87045e-13,-9518.48,5.00428], Tmin=(934.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.3261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.569 kJ/mol
""",
    rank = 5,
)

entry(
    index = 235,
    label = "CC(F)[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71912,0.0278802,3.50151e-06,-2.52873e-08,1.2375e-11,-63282.1,10.3965], Tmin=(10,'K'), Tmax=(853.613,'K')),
            NASAPolynomial(coeffs=[5.56598,0.0294028,-1.70573e-05,4.73566e-09,-5.08378e-13,-63968.1,-0.39297], Tmin=(853.613,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-526.167,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 236,
    label = "FCC1D[C]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74396,0.0274631,-7.2417e-05,1.9055e-07,-1.88094e-10,20327.9,10.7892], Tmin=(10,'K'), Tmax=(352.365,'K')),
            NASAPolynomial(coeffs=[3.19098,0.0239679,-1.59368e-05,4.98188e-09,-5.91148e-13,20427.5,13.7411], Tmin=(352.365,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.254 kJ/mol
""",
    rank = 5,
)

entry(
    index = 237,
    label = "CC[C](F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56661,0.0461193,-0.000110237,2.98252e-07,-2.81434e-10,-41271.5,10.8096], Tmin=(10,'K'), Tmax=(395.434,'K')),
            NASAPolynomial(coeffs=[0.894206,0.0490533,-2.99529e-05,8.78586e-09,-9.93781e-13,-40871.8,23.6053], Tmin=(395.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-343.165,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 238,
    label = "CDC(O)OF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {8,S}
4 O u0 p2 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8821,0.00750715,0.000106561,-2.49873e-07,1.70783e-10,-23855.9,9.54511], Tmin=(10,'K'), Tmax=(508.391,'K')),
            NASAPolynomial(coeffs=[4.68905,0.0252747,-1.70172e-05,5.48657e-09,-6.73281e-13,-24249.6,3.13279], Tmin=(508.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-198.382,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.447 kJ/mol
""",
    rank = 5,
)

entry(
    index = 239,
    label = "[CH]DCC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91823,0.00521639,9.89581e-05,-2.17031e-07,1.441e-10,-18522.9,10.5641], Tmin=(10,'K'), Tmax=(498.205,'K')),
            NASAPolynomial(coeffs=[3.12679,0.0278867,-1.84216e-05,5.77335e-09,-6.89027e-13,-18646.5,11.7987], Tmin=(498.205,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.029,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.914 kJ/mol
""",
    rank = 5,
)

entry(
    index = 240,
    label = "CC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 O u1 p2 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96587,0.00210502,8.05126e-05,-1.50989e-07,9.01474e-11,-32054.3,9.13571], Tmin=(10,'K'), Tmax=(496.629,'K')),
            NASAPolynomial(coeffs=[1.35045,0.0290279,-1.84957e-05,5.66667e-09,-6.67363e-13,-31866.7,19.1958], Tmin=(496.629,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-266.525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 241,
    label = "FCO[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91989,0.0230697,-4.02014e-06,-8.61239e-09,3.9567e-12,-78666.9,10.8887], Tmin=(10,'K'), Tmax=(1135.38,'K')),
            NASAPolynomial(coeffs=[9.13123,0.015355,-7.89171e-06,1.91888e-09,-1.80526e-13,-80536.4,-17.9363], Tmin=(1135.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-654.022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.238 kJ/mol
""",
    rank = 5,
)

entry(
    index = 242,
    label = "CDCC(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94857,0.0034528,0.000108311,-2.32184e-07,1.58943e-10,-48212,10.0109], Tmin=(10,'K'), Tmax=(440.257,'K')),
            NASAPolynomial(coeffs=[1.58627,0.0331768,-2.11079e-05,6.41197e-09,-7.46015e-13,-48084,18.5603], Tmin=(440.257,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-400.863,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.94 kJ/mol
""",
    rank = 5,
)

entry(
    index = 243,
    label = "ODCDCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95422,0.00289145,5.02547e-05,-1.11198e-07,7.35968e-11,-20647.9,7.96235], Tmin=(10,'K'), Tmax=(508.801,'K')),
            NASAPolynomial(coeffs=[3.80236,0.0135254,-8.92536e-06,2.8086e-09,-3.37698e-13,-20754.7,7.39162], Tmin=(508.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-171.69,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.696 kJ/mol
""",
    rank = 5,
)

entry(
    index = 244,
    label = "[C]#COCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70559,0.0314885,-0.000101029,2.51107e-07,-2.27796e-10,25492.9,10.4944], Tmin=(10,'K'), Tmax=(372.74,'K')),
            NASAPolynomial(coeffs=[3.31626,0.0228522,-1.47067e-05,4.48217e-09,-5.21555e-13,25610.9,13.1825], Tmin=(372.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (211.951,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.329 kJ/mol
""",
    rank = 5,
)

entry(
    index = 245,
    label = "[O]CC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86679,0.0129991,3.794e-05,-7.3235e-08,3.73384e-11,-52258.5,10.4929], Tmin=(10,'K'), Tmax=(678.68,'K')),
            NASAPolynomial(coeffs=[3.58678,0.0260777,-1.62246e-05,4.78223e-09,-5.39748e-13,-52483.7,9.79619], Tmin=(678.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-434.517,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.744 kJ/mol
""",
    rank = 5,
)

entry(
    index = 246,
    label = "[CH]DC(C)OF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84332,0.013372,0.000105677,-3.24394e-07,2.96862e-10,24612.1,9.22315], Tmin=(10,'K'), Tmax=(359.488,'K')),
            NASAPolynomial(coeffs=[3.3907,0.0309756,-2.02142e-05,6.31787e-09,-7.54666e-13,24563.4,9.81425], Tmin=(359.488,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (204.651,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 247,
    label = "CO[CH]CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61958,0.040371,-0.000112351,2.88046e-07,-2.5532e-10,-29137.3,9.55071], Tmin=(10,'K'), Tmax=(410.22,'K')),
            NASAPolynomial(coeffs=[1.42086,0.0388755,-2.302e-05,6.58083e-09,-7.2894e-13,-28763.9,20.5511], Tmin=(410.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-242.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.338 kJ/mol
""",
    rank = 5,
)

entry(
    index = 248,
    label = "F[CH]CDCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {7,S}
5 C u0 p0 c0 {4,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91222,0.0057628,0.000101844,-2.33696e-07,1.62071e-10,-26882.9,10.3654], Tmin=(10,'K'), Tmax=(478.888,'K')),
            NASAPolynomial(coeffs=[3.30251,0.0274562,-1.81026e-05,5.67018e-09,-6.7644e-13,-27014.8,10.8705], Tmin=(478.888,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-223.535,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.014 kJ/mol
""",
    rank = 5,
)

entry(
    index = 249,
    label = "C#CC([CH2])(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {9,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 F u0 p3 c0 {3,S}
8 F u0 p3 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7906,0.0144368,0.000147213,-4.15389e-07,3.27829e-10,-4900.32,10.6437], Tmin=(10,'K'), Tmax=(457.049,'K')),
            NASAPolynomial(coeffs=[6.55342,0.0276754,-1.90387e-05,6.23612e-09,-7.73981e-13,-5543.69,-4.79761], Tmin=(457.049,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.7691,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 250,
    label = "O[C]DCOF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30254,0.0654757,-0.000201655,3.14798e-07,-1.85403e-10,-43877.8,11.5196], Tmin=(10,'K'), Tmax=(484.288,'K')),
            NASAPolynomial(coeffs=[8.2308,0.0139198,-8.36085e-06,2.44656e-09,-2.77802e-13,-44227.9,-7.36936], Tmin=(484.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-364.847,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 251,
    label = "OD[C]OCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86912,0.0173554,-1.95088e-06,-6.83644e-09,2.93564e-12,-45971.3,10.1588], Tmin=(10,'K'), Tmax=(1130.65,'K')),
            NASAPolynomial(coeffs=[6.54879,0.0147501,-7.61503e-06,1.88115e-09,-1.81031e-13,-47016.6,-5.04139], Tmin=(1130.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-382.214,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 252,
    label = "OCO[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83723,0.0162057,2.8827e-05,-5.5157e-08,2.60713e-11,-49037.2,10.3553], Tmin=(10,'K'), Tmax=(740.203,'K')),
            NASAPolynomial(coeffs=[3.477,0.0284525,-1.68641e-05,4.79432e-09,-5.2636e-13,-49266,10.0787], Tmin=(740.203,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-407.728,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.767 kJ/mol
""",
    rank = 5,
)

entry(
    index = 253,
    label = "C[C](F)CCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84562,0.0330662,-2.40373e-07,-1.40245e-08,5.19965e-12,-42418,10.1026], Tmin=(10,'K'), Tmax=(1235.14,'K')),
            NASAPolynomial(coeffs=[10.146,0.0280023,-1.27199e-05,2.76637e-09,-2.34129e-13,-45144.5,-26.3605], Tmin=(1235.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-352.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 254,
    label = "CDC(C)OF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88099,0.0107409,0.000106232,-2.84596e-07,2.46079e-10,-6514.9,8.57166], Tmin=(10,'K'), Tmax=(295.234,'K')),
            NASAPolynomial(coeffs=[2.0053,0.036154,-2.28859e-05,6.9673e-09,-8.14773e-13,-6404.15,15.3324], Tmin=(295.234,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.1577,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 255,
    label = "CD[C]C#CF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8519,0.011801,0.000107197,-3.72912e-07,3.65272e-10,43734.2,9.36479], Tmin=(10,'K'), Tmax=(365.406,'K')),
            NASAPolynomial(coeffs=[5.02115,0.0200468,-1.30424e-05,4.07683e-09,-4.88882e-13,43508.3,2.97846], Tmin=(365.406,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (363.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.67 kJ/mol
""",
    rank = 5,
)

entry(
    index = 256,
    label = "FC[C]DCOF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83623,0.0314344,-2.01969e-05,5.89923e-09,-6.00608e-13,4157.72,11.3028], Tmin=(10,'K'), Tmax=(1567.58,'K')),
            NASAPolynomial(coeffs=[14.3233,0.0090851,-3.03161e-06,3.93995e-10,-8.87667e-15,327.93,-45.7342], Tmin=(1567.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.5694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 257,
    label = "FCD[C]OCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63713,0.0390226,-0.000109483,2.88684e-07,-2.81329e-10,-30813.1,11.8842], Tmin=(10,'K'), Tmax=(356.434,'K')),
            NASAPolynomial(coeffs=[2.81804,0.0332136,-2.19065e-05,6.80721e-09,-8.04078e-13,-30659.4,16.3276], Tmin=(356.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.202,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.256 kJ/mol
""",
    rank = 5,
)

entry(
    index = 258,
    label = "OCC[C](F)F",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72444,0.0290771,5.64465e-06,-2.63759e-08,1.19344e-11,-58954.5,11.0443], Tmin=(10,'K'), Tmax=(905.328,'K')),
            NASAPolynomial(coeffs=[5.61365,0.0320537,-1.80489e-05,4.88738e-09,-5.13817e-13,-59760.6,-0.445134], Tmin=(905.328,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-490.174,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.144 kJ/mol
""",
    rank = 5,
)

entry(
    index = 259,
    label = "OC1DCC1F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92919,0.00410574,8.75806e-05,-1.67453e-07,9.6287e-11,-14582.4,9.06742], Tmin=(10,'K'), Tmax=(575.412,'K')),
            NASAPolynomial(coeffs=[2.73989,0.0287993,-1.96116e-05,6.34951e-09,-7.79879e-13,-14717.4,11.7848], Tmin=(575.412,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.275,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.614 kJ/mol
""",
    rank = 5,
)

entry(
    index = 260,
    label = "CDCCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87663,0.0103147,7.74223e-05,-1.78106e-07,1.24386e-10,19240.4,9.89037], Tmin=(10,'K'), Tmax=(442.763,'K')),
            NASAPolynomial(coeffs=[2.31029,0.0317859,-2.01189e-05,6.10383e-09,-7.10564e-13,19307.3,15.3606], Tmin=(442.763,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (159.966,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 261,
    label = "CCD[C]C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u1 p0 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78769,0.0317271,-8.34028e-06,-6.18729e-09,3.05349e-12,-23073,10.1766], Tmin=(10,'K'), Tmax=(1213.29,'K')),
            NASAPolynomial(coeffs=[9.44977,0.0236038,-1.13323e-05,2.61904e-09,-2.36861e-13,-25223,-21.4324], Tmin=(1213.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-191.819,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.085 kJ/mol
""",
    rank = 5,
)

entry(
    index = 262,
    label = "[CH]DCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0746,-0.00741469,8.78749e-05,-1.66706e-07,1.03304e-10,12889.3,7.27794], Tmin=(10,'K'), Tmax=(515.063,'K')),
            NASAPolynomial(coeffs=[2.79473,0.0142004,-9.07657e-06,2.7931e-09,-3.2913e-13,12866.3,11.1], Tmin=(515.063,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (107.161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.17 kJ/mol
""",
    rank = 5,
)

entry(
    index = 263,
    label = "[C]#CCC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79973,0.026177,-2.91288e-06,-1.30307e-08,6.20758e-12,10064.2,11.2385], Tmin=(10,'K'), Tmax=(1005.75,'K')),
            NASAPolynomial(coeffs=[7.29297,0.0224138,-1.24085e-05,3.27801e-09,-3.35631e-13,8849.19,-8.18145], Tmin=(1005.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (83.7002,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.096 kJ/mol
""",
    rank = 5,
)

entry(
    index = 264,
    label = "[CH]DCOCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84171,0.0144641,4.07635e-05,-7.88077e-08,4.07546e-11,-9351.62,10.2729], Tmin=(10,'K'), Tmax=(652.992,'K')),
            NASAPolynomial(coeffs=[2.9745,0.0299616,-1.82328e-05,5.31073e-09,-5.95582e-13,-9455.52,12.4244], Tmin=(652.992,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.7737,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.673 kJ/mol
""",
    rank = 5,
)

entry(
    index = 265,
    label = "FCDCC(F)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82439,0.0330177,5.65336e-07,-1.82997e-08,7.48638e-12,-70346.9,11.5936], Tmin=(10,'K'), Tmax=(1103.12,'K')),
            NASAPolynomial(coeffs=[9.15071,0.0290558,-1.49222e-05,3.67579e-09,-3.52979e-13,-72456.1,-18.8592], Tmin=(1103.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-584.843,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 266,
    label = "FCC1DCC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87392,0.0200221,2.51664e-05,-4.64381e-08,1.93822e-11,-19594.1,10.6708], Tmin=(10,'K'), Tmax=(885.384,'K')),
            NASAPolynomial(coeffs=[5.03118,0.0298982,-1.71552e-05,4.697e-09,-4.97082e-13,-20391,1.88523], Tmin=(885.384,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-162.881,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 267,
    label = "FC1DCO[CH]1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u1 p0 c0 {2,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92531,0.00425777,7.96005e-05,-1.53678e-07,8.74347e-11,5857.19,9.16227], Tmin=(10,'K'), Tmax=(595.822,'K')),
            NASAPolynomial(coeffs=[3.48651,0.0251215,-1.80337e-05,6.03784e-09,-7.58052e-13,5591.43,8.38302], Tmin=(595.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.6666,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.046 kJ/mol
""",
    rank = 5,
)

entry(
    index = 268,
    label = "FCDC1CC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9161,0.00547799,0.000128092,-2.76321e-07,1.85111e-10,-22114,10.838], Tmin=(10,'K'), Tmax=(473.542,'K')),
            NASAPolynomial(coeffs=[1.80605,0.0386003,-2.52874e-05,7.83474e-09,-9.23427e-13,-22085.7,17.6293], Tmin=(473.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-183.884,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 269,
    label = "C[C](F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67396,0.0348599,-8.8849e-05,2.40192e-07,-2.26283e-10,-38720.7,9.68971], Tmin=(10,'K'), Tmax=(392.075,'K')),
            NASAPolynomial(coeffs=[1.77138,0.0358235,-2.1962e-05,6.45988e-09,-7.3212e-13,-38429.7,18.8953], Tmin=(392.075,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-321.953,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.765 kJ/mol
""",
    rank = 5,
)

entry(
    index = 270,
    label = "CCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  F u0 p3 c0 {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94958,0.00292302,9.16041e-05,-1.5348e-07,8.36508e-11,-37284.7,8.16508], Tmin=(10,'K'), Tmax=(472.114,'K')),
            NASAPolynomial(coeffs=[-0.233803,0.0383691,-2.10219e-05,5.5673e-09,-5.7543e-13,-36889.7,25.2075], Tmin=(472.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-310.028,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.532 kJ/mol
""",
    rank = 5,
)

entry(
    index = 271,
    label = "ODCD[C]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87939,0.017416,-6.22858e-07,-9.33607e-09,4.08678e-12,-6536.59,10.3453], Tmin=(10,'K'), Tmax=(1049.05,'K')),
            NASAPolynomial(coeffs=[6.25498,0.0155869,-8.34403e-06,2.13956e-09,-2.13427e-13,-7432.79,-3.12514], Tmin=(1049.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.3289,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.209 kJ/mol
""",
    rank = 5,
)

entry(
    index = 272,
    label = "FC1[CH]CDC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,D} {8,S}
6 C u0 p0 c0 {2,S} {5,D} {9,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07333,-0.00747742,0.000151082,-2.71361e-07,1.54768e-10,13493.7,9.7833], Tmin=(10,'K'), Tmax=(565.98,'K')),
            NASAPolynomial(coeffs=[1.5117,0.0343085,-2.24255e-05,6.9421e-09,-8.16854e-13,13404.3,17.3328], Tmin=(565.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (112.174,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.761 kJ/mol
""",
    rank = 5,
)

entry(
    index = 273,
    label = "FOC1[C]DC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {3,S} {5,D}
5 C u0 p0 c0 {3,S} {4,D} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90765,0.00570864,8.91222e-05,-1.97059e-07,1.27738e-10,53379.2,10.1957], Tmin=(10,'K'), Tmax=(529.954,'K')),
            NASAPolynomial(coeffs=[4.17032,0.0233309,-1.62465e-05,5.2968e-09,-6.50682e-13,53076,6.49784], Tmin=(529.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (443.789,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 274,
    label = "CC#C[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46023,0.0548226,-0.00016313,3.24077e-07,-2.47075e-10,-8758.42,12.0483], Tmin=(10,'K'), Tmax=(403.326,'K')),
            NASAPolynomial(coeffs=[4.79881,0.0286972,-1.81771e-05,5.48818e-09,-6.35062e-13,-8761.88,8.10154], Tmin=(403.326,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.8335,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.293 kJ/mol
""",
    rank = 5,
)

entry(
    index = 275,
    label = "COCDCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93446,0.0214927,5.41864e-06,-1.47664e-08,5.08206e-12,-34501.3,8.57532], Tmin=(10,'K'), Tmax=(1209.69,'K')),
            NASAPolynomial(coeffs=[7.8941,0.0209804,-9.54611e-06,2.07799e-09,-1.75831e-13,-36379.8,-15.0861], Tmin=(1209.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-286.818,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.117 kJ/mol
""",
    rank = 5,
)

entry(
    index = 276,
    label = "CC(O)[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81134,0.0193632,0.000130042,-5.05971e-07,6.33063e-10,-59986,10.1912], Tmin=(10,'K'), Tmax=(202.721,'K')),
            NASAPolynomial(coeffs=[2.74048,0.0404926,-2.62983e-05,8.16254e-09,-9.68367e-13,-59942.6,13.6485], Tmin=(202.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-498.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 277,
    label = "F[C]DCC#CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8203,0.0141266,9.88089e-05,-3.32713e-07,3.07069e-10,27205.7,11.4143], Tmin=(10,'K'), Tmax=(390.099,'K')),
            NASAPolynomial(coeffs=[5.14336,0.0222179,-1.55815e-05,5.09551e-09,-6.27057e-13,26937.7,4.16464], Tmin=(390.099,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (226.21,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 278,
    label = "OC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89683,0.00715871,0.000104898,-2.59997e-07,1.93478e-10,-55185,10.6796], Tmin=(10,'K'), Tmax=(449.238,'K')),
            NASAPolynomial(coeffs=[3.53166,0.0272006,-1.80843e-05,5.70504e-09,-6.83892e-13,-55321.6,10.2634], Tmin=(449.238,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-458.846,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 279,
    label = "FCDC1OC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90525,0.00621007,0.00010637,-2.42813e-07,1.668e-10,-37964.4,10.5796], Tmin=(10,'K'), Tmax=(483.079,'K')),
            NASAPolynomial(coeffs=[3.184,0.0295803,-2.02186e-05,6.43811e-09,-7.72937e-13,-38097.7,11.4333], Tmin=(483.079,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.674,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 280,
    label = "CDC[C]DCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86068,0.0116397,7.92726e-05,-1.93534e-07,1.41426e-10,15099.3,10.3098], Tmin=(10,'K'), Tmax=(433.057,'K')),
            NASAPolynomial(coeffs=[2.63757,0.0316579,-2.02712e-05,6.2089e-09,-7.28188e-13,15123.4,14.2429], Tmin=(433.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.536,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 281,
    label = "FCC1OC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {3,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93376,0.0043753,0.00012644,-2.68561e-07,1.80402e-10,-60420.9,11.0526], Tmin=(10,'K'), Tmax=(455.852,'K')),
            NASAPolynomial(coeffs=[1.2443,0.0392498,-2.5417e-05,7.78308e-09,-9.08877e-13,-60292.9,20.6299], Tmin=(455.852,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-502.379,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.427 kJ/mol
""",
    rank = 5,
)

entry(
    index = 282,
    label = "C[C]DCDC(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89758,0.0126606,0.000310069,-2.13431e-06,4.56357e-09,-9109.73,9.57253], Tmin=(10,'K'), Tmax=(159.298,'K')),
            NASAPolynomial(coeffs=[4.0659,0.0279404,-1.74893e-05,5.23618e-09,-6.02568e-13,-9139.84,8.29283], Tmin=(159.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-74.7668,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.192 kJ/mol
""",
    rank = 5,
)

entry(
    index = 283,
    label = "FCC1D[C]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89084,0.0160964,2.15744e-05,-3.72648e-08,1.50226e-11,34700.8,10.0203], Tmin=(10,'K'), Tmax=(900.453,'K')),
            NASAPolynomial(coeffs=[4.25044,0.0261661,-1.46354e-05,3.9331e-09,-4.10503e-13,34163,5.69672], Tmin=(900.453,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (288.543,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 284,
    label = "C[C]1CDC1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89898,0.0080125,0.000111084,-2.88577e-07,2.34401e-10,30305.7,8.98369], Tmin=(10,'K'), Tmax=(384.439,'K')),
            NASAPolynomial(coeffs=[2.55255,0.03188,-2.05066e-05,6.32056e-09,-7.46118e-13,30336.4,13.2448], Tmin=(384.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.938 kJ/mol
""",
    rank = 5,
)

entry(
    index = 285,
    label = "FC1COC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9493,0.00305706,0.000111843,-2.05716e-07,1.19171e-10,-62581.5,10.9728], Tmin=(10,'K'), Tmax=(517.492,'K')),
            NASAPolynomial(coeffs=[0.0922628,0.042076,-2.79409e-05,8.73767e-09,-1.03766e-12,-62305.5,25.849], Tmin=(517.492,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-520.35,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.486 kJ/mol
""",
    rank = 5,
)

entry(
    index = 286,
    label = "OCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04407,-0.00347044,5.55173e-05,-8.18901e-08,3.92327e-11,-52627,7.08531], Tmin=(10,'K'), Tmax=(629.909,'K')),
            NASAPolynomial(coeffs=[1.49817,0.0185451,-1.08359e-05,3.07546e-09,-3.38841e-13,-52422.3,17.2701], Tmin=(629.909,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-437.564,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 287,
    label = "C#CC[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77246,0.0189407,7.5134e-05,-2.2098e-07,1.75227e-10,-6190.75,10.9472], Tmin=(10,'K'), Tmax=(439.478,'K')),
            NASAPolynomial(coeffs=[4.15073,0.0312996,-2.09828e-05,6.63982e-09,-7.96917e-13,-6376.6,7.69708], Tmin=(439.478,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-51.4848,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.071 kJ/mol
""",
    rank = 5,
)

entry(
    index = 288,
    label = "FC[C]1CC1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96064,0.00255267,0.000123375,-2.39179e-07,1.51566e-10,6334.26,10.2771], Tmin=(10,'K'), Tmax=(405.561,'K')),
            NASAPolynomial(coeffs=[-0.156897,0.0431835,-2.69753e-05,8.09115e-09,-9.34023e-13,6668.08,26.4237], Tmin=(405.561,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.658,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.783 kJ/mol
""",
    rank = 5,
)

entry(
    index = 289,
    label = "ODCO[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88341,0.0162631,5.44553e-06,-1.7788e-08,7.71263e-12,-44018.6,10.099], Tmin=(10,'K'), Tmax=(940.314,'K')),
            NASAPolynomial(coeffs=[5.62119,0.0173628,-9.85523e-06,2.66431e-09,-2.78477e-13,-44720.8,-0.174152], Tmin=(940.314,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-365.972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.118 kJ/mol
""",
    rank = 5,
)

entry(
    index = 290,
    label = "[CH]DCDC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77089,0.0199152,5.37666e-05,-2.6679e-07,2.91697e-10,-2773.95,10.3414], Tmin=(10,'K'), Tmax=(359.41,'K')),
            NASAPolynomial(coeffs=[5.83118,0.0162829,-1.16124e-05,3.87044e-09,-4.84069e-13,-3046.69,0.775989], Tmin=(359.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-23.0458,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.39 kJ/mol
""",
    rank = 5,
)

entry(
    index = 291,
    label = "[O]C(O)CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 O u0 p2 c0 {2,S} {7,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77893,0.0198116,2.2968e-05,-5.54138e-08,2.95173e-11,-48472.6,10.4713], Tmin=(10,'K'), Tmax=(672.092,'K')),
            NASAPolynomial(coeffs=[3.82865,0.0287238,-1.74739e-05,5.08683e-09,-5.7002e-13,-48687.3,8.704], Tmin=(672.092,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-403.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 292,
    label = "CDC(F)C[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67201,0.0322593,1.04865e-05,-4.40893e-08,2.28822e-11,-51862.7,12.1908], Tmin=(10,'K'), Tmax=(778.092,'K')),
            NASAPolynomial(coeffs=[5.94791,0.0345793,-2.10137e-05,6.05715e-09,-6.70118e-13,-52641.3,-0.945228], Tmin=(778.092,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-431.231,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.051 kJ/mol
""",
    rank = 5,
)

entry(
    index = 293,
    label = "OC1O[C]1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92605,0.00436031,8.04485e-05,-1.61983e-07,9.67346e-11,-28907.4,9.74204], Tmin=(10,'K'), Tmax=(565.204,'K')),
            NASAPolynomial(coeffs=[3.50939,0.0241603,-1.68206e-05,5.49781e-09,-6.77467e-13,-29129.5,9.13332], Tmin=(565.204,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.38,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.493 kJ/mol
""",
    rank = 5,
)

entry(
    index = 294,
    label = "CDC(O)CF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {8,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92351,0.00484872,0.000117181,-2.43857e-07,1.57562e-10,-42831.5,9.83907], Tmin=(10,'K'), Tmax=(494.312,'K')),
            NASAPolynomial(coeffs=[2.01114,0.0355823,-2.23829e-05,6.81696e-09,-8.00465e-13,-42828.9,15.832], Tmin=(494.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-356.142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.256 kJ/mol
""",
    rank = 5,
)

entry(
    index = 295,
    label = "C#C[C]DCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84579,0.0115535,0.000105727,-3.38352e-07,3.0218e-10,37490.3,10.0747], Tmin=(10,'K'), Tmax=(403.824,'K')),
            NASAPolynomial(coeffs=[5.43818,0.0196566,-1.30597e-05,4.1648e-09,-5.07296e-13,37167,1.42582], Tmin=(403.824,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.716,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 296,
    label = "FC1DCCDC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {2,S} {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89456,0.00636602,0.000104145,-2.21704e-07,1.38546e-10,5072,9.23041], Tmin=(10,'K'), Tmax=(548.31,'K')),
            NASAPolynomial(coeffs=[4.06069,0.0284283,-1.98809e-05,6.50828e-09,-8.02991e-13,4703.92,5.33842], Tmin=(548.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.1324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.391 kJ/mol
""",
    rank = 5,
)

entry(
    index = 297,
    label = "FC1[CH]C1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92709,0.0042794,9.11231e-05,-1.77065e-07,1.0359e-10,-10005,9.28942], Tmin=(10,'K'), Tmax=(564.264,'K')),
            NASAPolynomial(coeffs=[2.69173,0.0296008,-2.02223e-05,6.51126e-09,-7.93566e-13,-10129.3,12.2058], Tmin=(564.264,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-83.2159,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.804 kJ/mol
""",
    rank = 5,
)

entry(
    index = 298,
    label = "[CH2]OC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83504,0.0139762,4.76828e-05,-1.11774e-07,7.08579e-11,-56489.3,9.7045], Tmin=(10,'K'), Tmax=(537.071,'K')),
            NASAPolynomial(coeffs=[3.54611,0.0266618,-1.7167e-05,5.24306e-09,-6.111e-13,-56610.2,9.50449], Tmin=(537.071,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-469.703,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.392 kJ/mol
""",
    rank = 5,
)

entry(
    index = 299,
    label = "[O]C#CCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8369,0.0168604,4.48723e-06,-1.85054e-08,8.77056e-12,-7290.14,9.97937], Tmin=(10,'K'), Tmax=(854.412,'K')),
            NASAPolynomial(coeffs=[4.9552,0.0186061,-1.08335e-05,3.01178e-09,-3.23433e-13,-7736.05,3.269], Tmin=(854.412,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.6161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.68 kJ/mol
""",
    rank = 5,
)

entry(
    index = 300,
    label = "[CH]DC(O)CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {7,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90503,0.00603322,0.000111326,-2.44618e-07,1.62326e-10,-11730.4,10.3478], Tmin=(10,'K'), Tmax=(502.19,'K')),
            NASAPolynomial(coeffs=[3.25942,0.0305415,-1.97232e-05,6.14119e-09,-7.33729e-13,-11909.7,10.5865], Tmin=(502.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.5577,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 301,
    label = "O[C]DCCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83408,0.0155937,6.14924e-05,-1.84012e-07,1.66243e-10,-13848.2,10.3131], Tmin=(10,'K'), Tmax=(284.453,'K')),
            NASAPolynomial(coeffs=[2.74114,0.0309626,-1.95516e-05,5.92813e-09,-6.9024e-13,-13786,14.2119], Tmin=(284.453,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.135,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 302,
    label = "ODCDCDCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84023,0.0163457,-3.94384e-06,-6.74532e-09,3.85679e-12,-11729.3,8.93733], Tmin=(10,'K'), Tmax=(912.732,'K')),
            NASAPolynomial(coeffs=[5.5534,0.0138257,-7.99984e-06,2.2046e-09,-2.34577e-13,-12249.8,-0.309499], Tmin=(912.732,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.5261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.011 kJ/mol
""",
    rank = 5,
)

entry(
    index = 303,
    label = "CC1(F)O[C]1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u1 p0 c0 {2,S} {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87609,0.00873419,0.000120806,-2.96166e-07,2.18279e-10,-38457.5,9.89757], Tmin=(10,'K'), Tmax=(449.978,'K')),
            NASAPolynomial(coeffs=[3.20102,0.0331995,-2.23004e-05,7.04418e-09,-8.4324e-13,-38583.7,10.5382], Tmin=(449.978,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-319.767,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.183 kJ/mol
""",
    rank = 5,
)

entry(
    index = 304,
    label = "C#CC(F)DCF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85196,0.00996881,0.000119285,-3.11497e-07,2.33339e-10,-9640.6,10.3876], Tmin=(10,'K'), Tmax=(470.645,'K')),
            NASAPolynomial(coeffs=[5.23671,0.0255402,-1.74799e-05,5.65893e-09,-6.94138e-13,-10073.8,1.53373], Tmin=(470.645,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-80.1809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 305,
    label = "OD[C]C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80061,0.0166968,3.95698e-05,-1.23352e-07,8.87016e-11,-74992.4,10.5663], Tmin=(10,'K'), Tmax=(528.357,'K')),
            NASAPolynomial(coeffs=[5.80804,0.0184638,-1.36089e-05,4.51705e-09,-5.55846e-13,-75441.3,-0.0784846], Tmin=(528.357,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-623.554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.336 kJ/mol
""",
    rank = 5,
)

entry(
    index = 306,
    label = "C#CCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89328,0.00696356,9.27645e-05,-2.27867e-07,1.62317e-10,41361.5,10.0458], Tmin=(10,'K'), Tmax=(490.831,'K')),
            NASAPolynomial(coeffs=[4.77852,0.0208113,-1.39205e-05,4.46099e-09,-5.45508e-13,41020.9,3.82057], Tmin=(490.831,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (343.875,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 307,
    label = "FCOOC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85741,0.0312466,-7.24759e-06,-9.59721e-09,4.69499e-12,-95763.9,11.2712], Tmin=(10,'K'), Tmax=(1131.69,'K')),
            NASAPolynomial(coeffs=[10.4391,0.020971,-1.08424e-05,2.66139e-09,-2.53259e-13,-98085.3,-24.9705], Tmin=(1131.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-796.169,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.111 kJ/mol
""",
    rank = 5,
)

entry(
    index = 308,
    label = "CC(F)DC[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {9,S}
5 O u1 p2 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87063,0.0111942,9.12758e-05,-2.72267e-07,2.62779e-10,-30208.8,9.10582], Tmin=(10,'K'), Tmax=(263.523,'K')),
            NASAPolynomial(coeffs=[2.60052,0.0304731,-1.8463e-05,5.35516e-09,-5.98896e-13,-30141.9,13.5395], Tmin=(263.523,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-251.17,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.758 kJ/mol
""",
    rank = 5,
)

entry(
    index = 309,
    label = "[CH2]CDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {7,S}
5 C u0 p0 c0 {4,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95711,0.00249477,7.71091e-05,-1.38306e-07,7.71344e-11,-4836.27,8.00678], Tmin=(10,'K'), Tmax=(557.563,'K')),
            NASAPolynomial(coeffs=[1.5167,0.0291213,-1.90559e-05,6.00904e-09,-7.25881e-13,-4705.88,17.0836], Tmin=(557.563,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.2293,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.797 kJ/mol
""",
    rank = 5,
)

entry(
    index = 310,
    label = "[O]C(F)CDO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {7,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82996,0.0141423,3.87574e-05,-1.04586e-07,7.30713e-11,-38645.1,10.4289], Tmin=(10,'K'), Tmax=(496.126,'K')),
            NASAPolynomial(coeffs=[3.86129,0.0229447,-1.52336e-05,4.75229e-09,-5.62525e-13,-38759.6,9.17663], Tmin=(496.126,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-321.332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 311,
    label = "C[C](F)C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61661,0.0403652,-8.96913e-05,2.21373e-07,-2.11549e-10,-64040.5,10.7222], Tmin=(10,'K'), Tmax=(365.924,'K')),
            NASAPolynomial(coeffs=[2.76771,0.0370022,-2.40814e-05,7.42317e-09,-8.72469e-13,-63893.7,15.1208], Tmin=(365.924,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-532.469,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.097 kJ/mol
""",
    rank = 5,
)

entry(
    index = 312,
    label = "[CH]DC(C)CF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,D}
2  H u0 p0 c0 {1,S}
3  C u0 p0 c0 {1,D} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77137,0.0204192,3.09102e-05,-5.89634e-08,2.75631e-11,3985.64,9.30011], Tmin=(10,'K'), Tmax=(726.82,'K')),
            NASAPolynomial(coeffs=[2.47545,0.0365976,-2.11485e-05,5.91148e-09,-6.41851e-13,3935.08,13.4949], Tmin=(726.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (33.117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 313,
    label = "FOC(F)OF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76711,0.0222263,1.00388e-05,-4.59478e-08,2.77423e-11,-42736.8,10.7333], Tmin=(10,'K'), Tmax=(683.214,'K')),
            NASAPolynomial(coeffs=[6.2091,0.02051,-1.38142e-05,4.27975e-09,-4.99167e-13,-43364.1,-2.26646], Tmin=(683.214,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-355.359,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 314,
    label = "CC(F)D[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93736,0.00623783,0.000164862,-6.64841e-07,8.88483e-10,-13057.5,8.99151], Tmin=(10,'K'), Tmax=(225.379,'K')),
            NASAPolynomial(coeffs=[3.14763,0.0269286,-1.72687e-05,5.30065e-09,-6.2449e-13,-13038.9,11.2487], Tmin=(225.379,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-108.543,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 315,
    label = "FCDCDCDCF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {4,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74023,0.0225086,1.71997e-05,-6.50374e-08,4.37081e-11,-4590.11,9.8471], Tmin=(10,'K'), Tmax=(567.87,'K')),
            NASAPolynomial(coeffs=[4.72406,0.0254232,-1.6503e-05,5.05689e-09,-5.89997e-13,-4860.58,4.25978], Tmin=(567.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.1972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.871 kJ/mol
""",
    rank = 5,
)

entry(
    index = 316,
    label = "FC[C]DCCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u1 p0 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54966,0.0493149,-0.000169184,4.5927e-07,-4.323e-10,-17679.7,11.8602], Tmin=(10,'K'), Tmax=(376.229,'K')),
            NASAPolynomial(coeffs=[1.66384,0.0413774,-2.5955e-05,7.75166e-09,-8.8767e-13,-17339.7,21.7471], Tmin=(376.229,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.015,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.636 kJ/mol
""",
    rank = 5,
)

entry(
    index = 317,
    label = "[O]COCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99412,0.0153583,2.03366e-05,-3.16903e-08,1.14638e-11,-47086.6,10.0542], Tmin=(10,'K'), Tmax=(1030.79,'K')),
            NASAPolynomial(coeffs=[5.8005,0.0229803,-1.20469e-05,3.02444e-09,-2.95535e-13,-48236.3,-2.48582], Tmin=(1030.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-391.434,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.929 kJ/mol
""",
    rank = 5,
)

entry(
    index = 318,
    label = "OC(F)CF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94212,0.00369334,0.000103556,-2.12188e-07,1.36533e-10,-79705,9.99966], Tmin=(10,'K'), Tmax=(483.189,'K')),
            NASAPolynomial(coeffs=[1.73051,0.0329117,-2.10179e-05,6.41888e-09,-7.50865e-13,-79618.6,17.7429], Tmin=(483.189,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-662.719,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 319,
    label = "O[CH]CDCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91077,0.00541468,0.000105848,-2.17448e-07,1.34567e-10,-26552.8,10.0343], Tmin=(10,'K'), Tmax=(538.062,'K')),
            NASAPolynomial(coeffs=[3.0628,0.0312267,-2.04945e-05,6.47591e-09,-7.83076e-13,-26744,10.9756], Tmin=(538.062,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.805,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.348 kJ/mol
""",
    rank = 5,
)

entry(
    index = 320,
    label = "CDC(C)CF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83133,0.0171033,4.48949e-05,-7.06221e-08,2.99366e-11,-25706.2,8.55158], Tmin=(10,'K'), Tmax=(786.725,'K')),
            NASAPolynomial(coeffs=[1.56576,0.0406439,-2.29095e-05,6.25807e-09,-6.65955e-13,-25721.8,16.5737], Tmin=(786.725,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-213.736,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.245 kJ/mol
""",
    rank = 5,
)

entry(
    index = 321,
    label = "C[C](F)COF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  O u0 p2 c0 {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58034,0.0431599,-7.97064e-05,1.76483e-07,-1.60052e-10,-21072.2,10.6627], Tmin=(10,'K'), Tmax=(381.937,'K')),
            NASAPolynomial(coeffs=[2.81638,0.0402943,-2.57754e-05,7.8548e-09,-9.15991e-13,-20934.6,14.6506], Tmin=(381.937,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.211,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 322,
    label = "CDC[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90954,0.00561901,9.85123e-05,-2.13222e-07,1.37737e-10,-28689.2,9.36891], Tmin=(10,'K'), Tmax=(522.151,'K')),
            NASAPolynomial(coeffs=[3.61262,0.0270314,-1.79776e-05,5.70326e-09,-6.89937e-13,-28919.1,8.11022], Tmin=(522.151,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-238.564,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.238 kJ/mol
""",
    rank = 5,
)

entry(
    index = 323,
    label = "CC(F)CCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83194,0.0280414,2.30326e-05,-3.98738e-08,1.44635e-11,-65458.5,10.5708], Tmin=(10,'K'), Tmax=(1031.93,'K')),
            NASAPolynomial(coeffs=[5.20503,0.0405083,-2.09475e-05,5.24464e-09,-5.14281e-13,-66689,-0.686069], Tmin=(1031.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-544.204,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.748 kJ/mol
""",
    rank = 5,
)

entry(
    index = 324,
    label = "CDC(F)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 O u1 p2 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91922,0.00486971,8.40944e-05,-1.7642e-07,1.09397e-10,-11554.1,10.2339], Tmin=(10,'K'), Tmax=(547.907,'K')),
            NASAPolynomial(coeffs=[3.77588,0.0237566,-1.64535e-05,5.35006e-09,-6.56681e-13,-11806.2,8.39548], Tmin=(547.907,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.0964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 325,
    label = "OCCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85206,0.0139836,7.78141e-05,-2.42211e-07,2.36399e-10,-10053.1,10.3094], Tmin=(10,'K'), Tmax=(261.673,'K')),
            NASAPolynomial(coeffs=[2.74043,0.0309762,-1.95934e-05,5.95398e-09,-6.94773e-13,-9994.93,14.1821], Tmin=(261.673,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-83.5759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 326,
    label = "OCDC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89887,0.00682815,9.26875e-05,-2.32315e-07,1.71024e-10,-59609.5,9.59641], Tmin=(10,'K'), Tmax=(466.779,'K')),
            NASAPolynomial(coeffs=[4.22283,0.022199,-1.50226e-05,4.80786e-09,-5.82977e-13,-59837.5,6.16265], Tmin=(466.779,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-495.638,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.298 kJ/mol
""",
    rank = 5,
)

entry(
    index = 327,
    label = "[C]#C",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49701,0.000330019,-2.83786e-06,7.20073e-09,-4.13372e-12,67588.6,4.58989], Tmin=(10,'K'), Tmax=(725.767,'K')),
            NASAPolynomial(coeffs=[2.86766,0.00133535,1.75325e-07,-2.43506e-10,4.13942e-14,67744.9,7.87133], Tmin=(725.767,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (561.965,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (45.7296,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.276 kJ/mol
""",
    rank = 5,
)

entry(
    index = 328,
    label = "[O]C(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07207,-0.00682615,8.90382e-05,-1.59038e-07,9.05369e-11,-51432.5,9.19567], Tmin=(10,'K'), Tmax=(572.526,'K')),
            NASAPolynomial(coeffs=[2.86151,0.0165903,-1.15034e-05,3.67099e-09,-4.39361e-13,-51539.1,12.2197], Tmin=(572.526,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-427.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.136 kJ/mol
""",
    rank = 5,
)

entry(
    index = 329,
    label = "F[C]DCCOF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71242,0.0292414,-9.30847e-06,-8.91337e-09,5.58333e-12,3712.25,11.6729], Tmin=(10,'K'), Tmax=(928.473,'K')),
            NASAPolynomial(coeffs=[6.92183,0.0236566,-1.36012e-05,3.7296e-09,-3.95201e-13,2761.03,-5.48551], Tmin=(928.473,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.8589,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 330,
    label = "FOC1D[C]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84797,0.011828,5.27777e-05,-1.79515e-07,1.55322e-10,40027.5,9.91038], Tmin=(10,'K'), Tmax=(428.882,'K')),
            NASAPolynomial(coeffs=[5.20193,0.0146476,-1.11108e-05,3.77603e-09,-4.73898e-13,39769.3,2.86827], Tmin=(428.882,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (332.802,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 331,
    label = "FCCDC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82954,0.0210453,1.52931e-05,-3.63231e-08,1.62605e-11,-68819.1,10.8505], Tmin=(10,'K'), Tmax=(857.896,'K')),
            NASAPolynomial(coeffs=[5.35616,0.0262655,-1.54068e-05,4.29759e-09,-4.61997e-13,-69535.1,1.07321], Tmin=(857.896,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-572.181,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.691 kJ/mol
""",
    rank = 5,
)

entry(
    index = 332,
    label = "CC1(F)[CH]C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92424,0.00453435,0.000122575,-2.32874e-07,1.37105e-10,5050.19,8.60906], Tmin=(10,'K'), Tmax=(537.87,'K')),
            NASAPolynomial(coeffs=[1.06284,0.0419834,-2.69553e-05,8.35365e-09,-9.95353e-13,5124.11,18.4649], Tmin=(537.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.9609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 333,
    label = "FCDC[CH]CF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78995,0.0263378,1.32014e-05,-3.33459e-08,1.40509e-11,-30712.1,11.3174], Tmin=(10,'K'), Tmax=(926.199,'K')),
            NASAPolynomial(coeffs=[5.60104,0.0320337,-1.79149e-05,4.80867e-09,-5.01023e-13,-31627.4,-0.411247], Tmin=(926.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-255.334,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.708 kJ/mol
""",
    rank = 5,
)

entry(
    index = 334,
    label = "[CH2]CCDCF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74759,0.0249902,1.28863e-05,-3.19716e-08,1.37334e-11,-886.562,10.0443], Tmin=(10,'K'), Tmax=(878.167,'K')),
            NASAPolynomial(coeffs=[4.15451,0.0332551,-1.85141e-05,4.98694e-09,-5.23301e-13,-1348.18,5.91266], Tmin=(878.167,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.37698,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.678 kJ/mol
""",
    rank = 5,
)

entry(
    index = 335,
    label = "FC1[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 O u0 p2 c0 {2,S} {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09535,-0.00831212,9.91376e-05,-1.65561e-07,8.86965e-11,-7353,8.7543], Tmin=(10,'K'), Tmax=(600.939,'K')),
            NASAPolynomial(coeffs=[2.13601,0.020827,-1.37765e-05,4.27775e-09,-5.02881e-13,-7408.17,14.7908], Tmin=(600.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.1412,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.238 kJ/mol
""",
    rank = 5,
)

entry(
    index = 336,
    label = "ODCC(F)(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80773,0.0170413,3.38212e-05,-9.06345e-08,5.67392e-11,-95073,9.61743], Tmin=(10,'K'), Tmax=(591.335,'K')),
            NASAPolynomial(coeffs=[5.09552,0.0223581,-1.52491e-05,4.80376e-09,-5.69622e-13,-95470.6,2.00737], Tmin=(591.335,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-790.513,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.007 kJ/mol
""",
    rank = 5,
)

entry(
    index = 337,
    label = "CCDC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63864,0.0319962,1.31647e-06,-2.74053e-08,1.47636e-11,-30650.2,10.2412], Tmin=(10,'K'), Tmax=(776.578,'K')),
            NASAPolynomial(coeffs=[4.93986,0.0341719,-2.00347e-05,5.64546e-09,-6.15514e-13,-31120,2.56892], Tmin=(776.578,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-254.874,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.752 kJ/mol
""",
    rank = 5,
)

entry(
    index = 338,
    label = "CDC(O)F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94462,0.00323891,6.98855e-05,-1.34443e-07,7.82086e-11,-41901.3,8.30759], Tmin=(10,'K'), Tmax=(567.032,'K')),
            NASAPolynomial(coeffs=[3.00035,0.0225997,-1.49255e-05,4.768e-09,-5.82844e-13,-41998.4,10.5272], Tmin=(567.032,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-348.41,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 339,
    label = "CDC([CH]F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7409,0.0226279,4.64643e-05,-1.04694e-07,5.9566e-11,-30288.3,12.3821], Tmin=(10,'K'), Tmax=(604.271,'K')),
            NASAPolynomial(coeffs=[3.22516,0.0385094,-2.39074e-05,7.08848e-09,-8.06949e-13,-30453.6,12.727], Tmin=(604.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-251.867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 340,
    label = "OC[C]DCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81924,0.0238672,-4.23893e-06,-7.37925e-09,3.34566e-12,-9921.57,10.6025], Tmin=(10,'K'), Tmax=(1131.6,'K')),
            NASAPolynomial(coeffs=[7.14241,0.0202505,-1.02219e-05,2.49477e-09,-2.38484e-13,-11194.2,-8.14071], Tmin=(1131.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-82.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 341,
    label = "CDCC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  F u0 p3 c0 {3,S}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6895,0.0285021,1.48016e-05,-4.56848e-08,2.3215e-11,-24508.2,11.5949], Tmin=(10,'K'), Tmax=(748.187,'K')),
            NASAPolynomial(coeffs=[4.49309,0.0352784,-2.09826e-05,5.98055e-09,-6.57919e-13,-24938.3,5.88004], Tmin=(748.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-203.8,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.852 kJ/mol
""",
    rank = 5,
)

entry(
    index = 342,
    label = "CDC(F)C[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 O u1 p2 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91589,0.00540145,0.000111611,-2.42756e-07,1.61651e-10,-14768.3,10.4493], Tmin=(10,'K'), Tmax=(489.888,'K')),
            NASAPolynomial(coeffs=[2.68541,0.0320307,-2.06989e-05,6.39401e-09,-7.56314e-13,-14846.7,13.4768], Tmin=(489.888,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-122.811,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.693 kJ/mol
""",
    rank = 5,
)

entry(
    index = 343,
    label = "FC[CH]OCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54148,0.0500809,-0.000171185,4.60127e-07,-4.31042e-10,-54953.7,12.191], Tmin=(10,'K'), Tmax=(376.204,'K')),
            NASAPolynomial(coeffs=[1.77944,0.041229,-2.58966e-05,7.74403e-09,-8.87748e-13,-54625.9,21.5638], Tmin=(376.204,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-456.929,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.363 kJ/mol
""",
    rank = 5,
)

entry(
    index = 344,
    label = "FC1DCCC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07685,-0.00705805,0.000118956,-1.11466e-07,-5.61638e-11,-6991.79,9.21664], Tmin=(10,'K'), Tmax=(316.195,'K')),
            NASAPolynomial(coeffs=[-1.37741,0.0429483,-2.81725e-05,8.77735e-09,-1.04116e-12,-6551.92,30.7516], Tmin=(316.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-58.129,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.057 kJ/mol
""",
    rank = 5,
)

entry(
    index = 345,
    label = "FC1CC1(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90949,0.00533494,0.000109699,-2.15872e-07,1.27452e-10,-62349.9,10.2596], Tmin=(10,'K'), Tmax=(561.735,'K')),
            NASAPolynomial(coeffs=[2.61941,0.0349843,-2.41162e-05,7.7892e-09,-9.49681e-13,-62527.8,12.8657], Tmin=(561.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-518.443,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 346,
    label = "O[CH]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95344,0.00296109,8.50049e-05,-1.72759e-07,1.10614e-10,-30737,9.39685], Tmin=(10,'K'), Tmax=(484.784,'K')),
            NASAPolynomial(coeffs=[2.11804,0.0269892,-1.68305e-05,5.0854e-09,-5.93061e-13,-30663.5,15.846], Tmin=(484.784,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-255.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.19 kJ/mol
""",
    rank = 5,
)

entry(
    index = 347,
    label = "[O]C(F)CO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {4,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91454,0.00544125,0.00011048,-2.3856e-07,1.57174e-10,-50158.9,10.4114], Tmin=(10,'K'), Tmax=(497.332,'K')),
            NASAPolynomial(coeffs=[2.76737,0.0317886,-2.06239e-05,6.40284e-09,-7.60337e-13,-50256.5,13.0159], Tmin=(497.332,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-417.067,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 348,
    label = "ODCC(O)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 O u0 p2 c0 {3,S} {8,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90547,0.00734564,7.5722e-05,-1.64103e-07,1.07343e-10,-65405,9.60014], Tmin=(10,'K'), Tmax=(491.575,'K')),
            NASAPolynomial(coeffs=[2.68429,0.0276243,-1.77136e-05,5.4102e-09,-6.31759e-13,-65409.9,13.3535], Tmin=(491.575,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-543.824,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 349,
    label = "FCC1CC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00591,-0.00113466,0.000128292,-2.07786e-07,1.07553e-10,-21072.2,9.72102], Tmin=(10,'K'), Tmax=(578.025,'K')),
            NASAPolynomial(coeffs=[-1.44669,0.0481244,-2.94491e-05,8.64383e-09,-9.75551e-13,-20634.4,31.3722], Tmin=(578.025,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.218,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.611 kJ/mol
""",
    rank = 5,
)

entry(
    index = 350,
    label = "CDC(F)CO",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92111,0.0051344,0.000120895,-2.6101e-07,1.75405e-10,-41466.7,9.79139], Tmin=(10,'K'), Tmax=(474.715,'K')),
            NASAPolynomial(coeffs=[2.12234,0.0353507,-2.21679e-05,6.72737e-09,-7.87091e-13,-41465.6,15.342], Tmin=(474.715,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-344.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 351,
    label = "C[C]DC(F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89734,0.0336589,-1.62811e-05,2.49831e-09,1.59226e-13,-19728.5,9.79179], Tmin=(10,'K'), Tmax=(1639.48,'K')),
            NASAPolynomial(coeffs=[19.4185,0.0052691,1.021e-06,-1.01083e-09,1.56577e-13,-26091.7,-76.6472], Tmin=(1639.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-164.052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 352,
    label = "CDCC[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80363,0.0265512,1.14726e-05,-3.03741e-08,1.25646e-11,-27959.6,10.8614], Tmin=(10,'K'), Tmax=(957.201,'K')),
            NASAPolynomial(coeffs=[5.99902,0.0311007,-1.71628e-05,4.54824e-09,-4.68377e-13,-29008.6,-2.91815], Tmin=(957.201,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.44,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.89 kJ/mol
""",
    rank = 5,
)

entry(
    index = 353,
    label = "OD[C]C#CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8529,0.0134147,4.48717e-05,-2.18942e-07,2.56613e-10,13327.4,9.20515], Tmin=(10,'K'), Tmax=(321.722,'K')),
            NASAPolynomial(coeffs=[4.71225,0.0139603,-1.00311e-05,3.3236e-09,-4.12305e-13,13214,5.1306], Tmin=(321.722,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 354,
    label = "O[CH]OCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84419,0.0144421,3.95052e-05,-7.56517e-08,3.85713e-11,-50613.7,10.3631], Tmin=(10,'K'), Tmax=(664.5,'K')),
            NASAPolynomial(coeffs=[3.01848,0.0296585,-1.79723e-05,5.21754e-09,-5.83517e-13,-50730.2,12.3071], Tmin=(664.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-420.845,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 355,
    label = "COC([O])(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7521,0.0230452,2.11251e-05,-5.86201e-08,3.2145e-11,-75089.1,10.1974], Tmin=(10,'K'), Tmax=(685.875,'K')),
            NASAPolynomial(coeffs=[4.85075,0.0288079,-1.80937e-05,5.37069e-09,-6.09256e-13,-75526,3.22457], Tmin=(685.875,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-624.353,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 7.232 kJ/mol
""",
    rank = 5,
)

entry(
    index = 356,
    label = "OOC[C](F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67314,0.0339523,-2.41966e-05,7.77835e-09,-7.8449e-13,-45381.5,11.2811], Tmin=(10,'K'), Tmax=(1206.28,'K')),
            NASAPolynomial(coeffs=[9.65188,0.0181141,-9.46002e-06,2.37411e-09,-2.32363e-13,-47113.9,-19.8866], Tmin=(1206.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-377.333,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.464 kJ/mol
""",
    rank = 5,
)

entry(
    index = 357,
    label = "F[CH]OCDCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {8,S}
6 C u0 p0 c0 {5,D} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82744,0.0268296,-5.90879e-06,-8.91865e-09,4.42815e-12,-37009,11.5993], Tmin=(10,'K'), Tmax=(1081.39,'K')),
            NASAPolynomial(coeffs=[8.36775,0.0201749,-1.07429e-05,2.73238e-09,-2.69955e-13,-38583.9,-13.4016], Tmin=(1081.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-307.678,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 358,
    label = "CC[C](C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78599,0.028801,7.00545e-06,-1.9196e-08,6.64218e-12,-19684.8,8.19014], Tmin=(10,'K'), Tmax=(1176.04,'K')),
            NASAPolynomial(coeffs=[6.67866,0.0327626,-1.56492e-05,3.62421e-09,-3.2994e-13,-21319.5,-10.2918], Tmin=(1176.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.654,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 359,
    label = "ODCCC(F)F",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87987,0.0248328,4.05937e-06,-1.76762e-08,6.89585e-12,-73352.1,10.4412], Tmin=(10,'K'), Tmax=(1094.32,'K')),
            NASAPolynomial(coeffs=[7.68,0.0238308,-1.22334e-05,3.01197e-09,-2.8914e-13,-74955.5,-11.7607], Tmin=(1094.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-609.837,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.282 kJ/mol
""",
    rank = 5,
)

entry(
    index = 360,
    label = "[CH]DC(F)CO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6 O u0 p2 c0 {5,S} {9,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89673,0.00689585,0.000117429,-2.77583e-07,1.98294e-10,-10442.4,10.4304], Tmin=(10,'K'), Tmax=(467.003,'K')),
            NASAPolynomial(coeffs=[3.40574,0.0303195,-1.95351e-05,6.05923e-09,-7.20561e-13,-10606.1,10.1816], Tmin=(467.003,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.8404,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 361,
    label = "C[C]DC(O)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {9,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7024,0.025322,-3.14934e-06,-1.5048e-08,8.68951e-12,-15007.7,9.39136], Tmin=(10,'K'), Tmax=(768.829,'K')),
            NASAPolynomial(coeffs=[4.52073,0.0262882,-1.52258e-05,4.26094e-09,-4.62756e-13,-15287.9,4.65453], Tmin=(768.829,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.814,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 362,
    label = "F[CH]C1DCDC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {4,D} {6,D}
6 C u0 p0 c0 {4,S} {5,D} {7,S}
7 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79254,0.0174945,3.83133e-05,-1.11328e-07,7.66114e-11,28628.8,11.2156], Tmin=(10,'K'), Tmax=(536.065,'K')),
            NASAPolynomial(coeffs=[5.00245,0.0226174,-1.56179e-05,4.98592e-09,-5.98417e-13,28295.8,4.23641], Tmin=(536.065,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 363,
    label = "CO[C](F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95408,0.0327053,-1.44441e-05,1.26278e-09,4.36411e-13,-54076.4,9.8406], Tmin=(10,'K'), Tmax=(1626.58,'K')),
            NASAPolynomial(coeffs=[20.4106,0.00336021,2.35921e-06,-1.41981e-09,2.02518e-13,-60901.5,-82.0816], Tmin=(1626.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-449.629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.865 kJ/mol
""",
    rank = 5,
)

entry(
    index = 364,
    label = "[O]C(F)DCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91688,0.00544625,7.70392e-05,-1.85065e-07,1.30244e-10,-53330.3,10.2258], Tmin=(10,'K'), Tmax=(487.865,'K')),
            NASAPolynomial(coeffs=[4.1463,0.0192208,-1.34471e-05,4.36026e-09,-5.31217e-13,-53539,7.37418], Tmin=(487.865,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-443.432,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.259 kJ/mol
""",
    rank = 5,
)

entry(
    index = 365,
    label = "ODC(F)[CH]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81405,0.0273314,-7.66379e-06,-6.91426e-09,3.6961e-12,-57513.3,12.0913], Tmin=(10,'K'), Tmax=(1099.46,'K')),
            NASAPolynomial(coeffs=[8.4363,0.0199783,-1.05426e-05,2.65981e-09,-2.60955e-13,-59101.7,-13.2478], Tmin=(1099.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-478.165,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 366,
    label = "F[C]1COC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99647,-0.000424073,9.83169e-05,-1.63283e-07,8.55085e-11,-10625.7,9.43899], Tmin=(10,'K'), Tmax=(588.739,'K')),
            NASAPolynomial(coeffs=[0.386452,0.0355799,-2.26556e-05,6.81324e-09,-7.80871e-13,-10399.5,23.2535], Tmin=(588.739,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.3608,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.166 kJ/mol
""",
    rank = 5,
)

entry(
    index = 367,
    label = "CDC([O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {8,S} {9,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u1 p2 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80872,0.0132013,0.000142041,-3.77311e-07,2.86373e-10,-80953.9,12.4457], Tmin=(10,'K'), Tmax=(462.166,'K')),
            NASAPolynomial(coeffs=[5.11768,0.0330701,-2.3699e-05,7.82377e-09,-9.65031e-13,-81408.1,3.5364], Tmin=(462.166,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-673.115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.802 kJ/mol
""",
    rank = 5,
)

entry(
    index = 368,
    label = "OOC[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65978,0.029909,-1.73515e-05,2.63859e-09,7.87178e-13,-19509.5,10.9198], Tmin=(10,'K'), Tmax=(1018.55,'K')),
            NASAPolynomial(coeffs=[6.68358,0.0221802,-1.20755e-05,3.18189e-09,-3.27131e-13,-20340.6,-4.77965], Tmin=(1018.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-162.239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.695 kJ/mol
""",
    rank = 5,
)

entry(
    index = 369,
    label = "FCDC1OO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92718,0.00446436,7.21448e-05,-1.56767e-07,1.00056e-10,-5238.11,8.51271], Tmin=(10,'K'), Tmax=(535.904,'K')),
            NASAPolynomial(coeffs=[4.00228,0.0195281,-1.37515e-05,4.49202e-09,-5.51236e-13,-5470.52,6.10394], Tmin=(535.904,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.5769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.949 kJ/mol
""",
    rank = 5,
)

entry(
    index = 370,
    label = "[O]CDC(F)CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75702,0.0268494,-6.80551e-06,-7.66273e-09,3.99796e-12,-50058,11.4869], Tmin=(10,'K'), Tmax=(1061.25,'K')),
            NASAPolynomial(coeffs=[7.30053,0.0219832,-1.19274e-05,3.09295e-09,-3.1154e-13,-51288.2,-8.07167], Tmin=(1061.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-416.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.174 kJ/mol
""",
    rank = 5,
)

entry(
    index = 371,
    label = "OCDCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96117,0.00223267,6.45162e-05,-1.15369e-07,6.36654e-11,-38122.5,8.16832], Tmin=(10,'K'), Tmax=(571.031,'K')),
            NASAPolynomial(coeffs=[2.02728,0.024364,-1.61696e-05,5.15709e-09,-6.27755e-13,-38041.6,15.1891], Tmin=(571.031,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-316.985,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.3 kJ/mol
""",
    rank = 5,
)

entry(
    index = 372,
    label = "[C]#CC(C)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86977,0.0114098,8.69227e-05,-2.46009e-07,2.22532e-10,36621.8,10.096], Tmin=(10,'K'), Tmax=(282.138,'K')),
            NASAPolynomial(coeffs=[2.45543,0.0314616,-1.9684e-05,5.89367e-09,-6.7799e-13,36701.6,15.1297], Tmin=(282.138,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (304.495,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.593 kJ/mol
""",
    rank = 5,
)

entry(
    index = 373,
    label = "F[C]DC1CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89046,0.00867372,5.47914e-05,-1.20705e-07,7.70765e-11,18355.5,9.90004], Tmin=(10,'K'), Tmax=(515.527,'K')),
            NASAPolynomial(coeffs=[3.14984,0.0236205,-1.54683e-05,4.77082e-09,-5.59566e-13,18309.6,11.7966], Tmin=(515.527,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.617 kJ/mol
""",
    rank = 5,
)

entry(
    index = 374,
    label = "CC([O])C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72434,0.0249917,2.66332e-05,-6.08409e-08,3.02043e-11,-57401,11.4472], Tmin=(10,'K'), Tmax=(724.213,'K')),
            NASAPolynomial(coeffs=[3.71897,0.0367518,-2.20204e-05,6.31218e-09,-6.97647e-13,-57707.9,9.34752], Tmin=(724.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-477.286,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.397 kJ/mol
""",
    rank = 5,
)

entry(
    index = 375,
    label = "ODC(O)[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90875,0.00578119,8.82759e-05,-2.01775e-07,1.35636e-10,-52210.2,10.1518], Tmin=(10,'K'), Tmax=(510.591,'K')),
            NASAPolynomial(coeffs=[4.1767,0.022341,-1.51889e-05,4.88851e-09,-5.963e-13,-52480.7,6.65741], Tmin=(510.591,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-434.126,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.9 kJ/mol
""",
    rank = 5,
)

entry(
    index = 376,
    label = "CDCCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93481,0.016836,3.73755e-05,-5.23044e-08,1.90334e-11,-24630.8,9.51885], Tmin=(10,'K'), Tmax=(963.759,'K')),
            NASAPolynomial(coeffs=[3.22208,0.036538,-1.93489e-05,4.96073e-09,-4.97393e-13,-25271,8.89679], Tmin=(963.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.968 kJ/mol
""",
    rank = 5,
)

entry(
    index = 377,
    label = "CC(C)[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6358,0.0307519,1.84506e-05,-4.65638e-08,2.17362e-11,-44460.5,8.77847], Tmin=(10,'K'), Tmax=(771.331,'K')),
            NASAPolynomial(coeffs=[2.934,0.0438037,-2.52351e-05,7.01444e-09,-7.56955e-13,-44632.2,10.167], Tmin=(771.331,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-369.703,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.854 kJ/mol
""",
    rank = 5,
)

entry(
    index = 378,
    label = "OCCDC(F)F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74564,0.0225379,3.19739e-05,-7.73756e-08,4.32508e-11,-65297.4,10.9643], Tmin=(10,'K'), Tmax=(635.498,'K')),
            NASAPolynomial(coeffs=[3.81725,0.0334785,-2.07377e-05,6.1279e-09,-6.9504e-13,-65536.5,8.84142], Tmin=(635.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-542.946,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.356 kJ/mol
""",
    rank = 5,
)

entry(
    index = 379,
    label = "FCC1[C]DC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 C u1 p0 c0 {3,S} {5,D}
5 C u0 p0 c0 {3,S} {4,D} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93773,0.00417042,0.000110085,-2.40314e-07,1.65515e-10,34700.7,10.5488], Tmin=(10,'K'), Tmax=(449.729,'K')),
            NASAPolynomial(coeffs=[1.89907,0.0328933,-2.10388e-05,6.42191e-09,-7.50241e-13,34777,17.5643], Tmin=(449.729,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (288.51,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.887 kJ/mol
""",
    rank = 5,
)

entry(
    index = 380,
    label = "C#CO[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85456,0.0111275,9.01967e-05,-2.74196e-07,2.3575e-10,12021.4,10.1311], Tmin=(10,'K'), Tmax=(409.376,'K')),
            NASAPolynomial(coeffs=[4.6293,0.0216639,-1.47535e-05,4.75541e-09,-5.80281e-13,11806.2,5.23231], Tmin=(409.376,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.9524,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 381,
    label = "CDC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90506,0.00575076,9.81479e-05,-2.07485e-07,1.29795e-10,-26788.9,9.99868], Tmin=(10,'K'), Tmax=(544.119,'K')),
            NASAPolynomial(coeffs=[3.84927,0.0270846,-1.83458e-05,5.91814e-09,-7.25822e-13,-27092.5,7.38763], Tmin=(544.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-222.769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.222 kJ/mol
""",
    rank = 5,
)

entry(
    index = 382,
    label = "CDCD[C]CF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64386,0.0351869,-6.53873e-05,1.21015e-07,-9.29258e-11,15223.5,10.839], Tmin=(10,'K'), Tmax=(425.219,'K')),
            NASAPolynomial(coeffs=[3.48557,0.0292056,-1.79356e-05,5.30365e-09,-6.04891e-13,15304.5,12.2614], Tmin=(425.219,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (126.566,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.408 kJ/mol
""",
    rank = 5,
)

entry(
    index = 383,
    label = "FCCDCOF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  O u0 p2 c0 {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77235,0.0270249,2.83272e-06,-2.08731e-08,9.34658e-12,-25900.5,10.5713], Tmin=(10,'K'), Tmax=(953.177,'K')),
            NASAPolynomial(coeffs=[6.35087,0.0273714,-1.52862e-05,4.09077e-09,-4.24734e-13,-26899.3,-4.40598], Tmin=(953.177,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-215.334,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 384,
    label = "ODC[CH]C(F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80129,0.0229805,1.10893e-05,-3.29095e-08,1.5305e-11,-52339.2,11.7394], Tmin=(10,'K'), Tmax=(851.457,'K')),
            NASAPolynomial(coeffs=[5.68353,0.0260853,-1.54276e-05,4.3318e-09,-4.68147e-13,-53092.8,0.418215], Tmin=(851.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-435.165,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.908 kJ/mol
""",
    rank = 5,
)

entry(
    index = 385,
    label = "FOC1D[C]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52265,0.0442523,-0.000108885,1.58308e-07,-9.04671e-11,22825.9,11.0564], Tmin=(10,'K'), Tmax=(489.876,'K')),
            NASAPolynomial(coeffs=[6.19795,0.0172753,-1.0567e-05,3.12207e-09,-3.56343e-13,22625.4,0.687277], Tmin=(489.876,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (189.764,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 386,
    label = "ODC[C]DCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73604,0.0281276,-7.33658e-05,1.85727e-07,-1.78764e-10,-817.152,10.2881], Tmin=(10,'K'), Tmax=(355.783,'K')),
            NASAPolynomial(coeffs=[3.31489,0.0236541,-1.56829e-05,4.89414e-09,-5.80106e-13,-728.904,12.7037], Tmin=(355.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-6.79823,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 387,
    label = "CC1(F)[CH]O1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {2,S} {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93282,0.00402222,0.000100167,-1.93391e-07,1.14751e-10,-14605.1,8.70231], Tmin=(10,'K'), Tmax=(540.684,'K')),
            NASAPolynomial(coeffs=[1.9117,0.033504,-2.1932e-05,6.85783e-09,-8.19728e-13,-14598.9,15.2463], Tmin=(540.684,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.459,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.903 kJ/mol
""",
    rank = 5,
)

entry(
    index = 388,
    label = "FC1DCCC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9411,0.00343266,0.00010948,-1.96676e-07,1.09695e-10,-29697.4,10.1391], Tmin=(10,'K'), Tmax=(553.876,'K')),
            NASAPolynomial(coeffs=[0.2685,0.0421482,-2.83888e-05,9.01268e-09,-1.08513e-12,-29477.6,23.9992], Tmin=(553.876,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-246.943,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 389,
    label = "FCDC1[C]DC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {5,D}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79254,0.0174945,3.83133e-05,-1.11328e-07,7.66114e-11,28628.8,11.2156], Tmin=(10,'K'), Tmax=(536.065,'K')),
            NASAPolynomial(coeffs=[5.00245,0.0226174,-1.56179e-05,4.98592e-09,-5.98417e-13,28295.8,4.23641], Tmin=(536.065,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 390,
    label = "CC(F)(F)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8042,0.0152123,0.000133103,-3.85177e-07,3.2435e-10,-78128.6,9.283], Tmin=(10,'K'), Tmax=(405.772,'K')),
            NASAPolynomial(coeffs=[4.02382,0.0353189,-2.35542e-05,7.46872e-09,-9.00394e-13,-78329.7,6.16227], Tmin=(405.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-649.595,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 391,
    label = "F[C]DCCCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89073,0.0263959,5.89113e-06,-1.95757e-08,7.31425e-12,-17614.2,11.3296], Tmin=(10,'K'), Tmax=(1123.36,'K')),
            NASAPolynomial(coeffs=[8.07392,0.0260038,-1.2951e-05,3.09902e-09,-2.89559e-13,-19469.2,-13.4115], Tmin=(1123.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-146.399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 392,
    label = "FC1DCOC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92799,0.00418634,9.31229e-05,-1.77692e-07,1.021e-10,-39521.2,10.091], Tmin=(10,'K'), Tmax=(571.184,'K')),
            NASAPolynomial(coeffs=[2.36473,0.0315856,-2.20351e-05,7.1428e-09,-8.7089e-13,-39611,14.4081], Tmin=(571.184,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-328.628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 393,
    label = "ODCDC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89088,0.00799656,6.91467e-05,-2.15177e-07,1.84631e-10,-38979.6,8.78533], Tmin=(10,'K'), Tmax=(421.772,'K')),
            NASAPolynomial(coeffs=[5.07224,0.0134762,-9.67457e-06,3.1948e-09,-3.95302e-13,-39227.6,2.34666], Tmin=(421.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-324.097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.533 kJ/mol
""",
    rank = 5,
)

entry(
    index = 394,
    label = "ODCCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91472,0.00853893,0.000105267,-4.2895e-07,5.84379e-10,-2397.03,9.72591], Tmin=(10,'K'), Tmax=(185.349,'K')),
            NASAPolynomial(coeffs=[3.22437,0.0234373,-1.53034e-05,4.71725e-09,-5.54055e-13,-2371.44,11.8929], Tmin=(185.349,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-19.8973,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 395,
    label = "CC1[C]DC1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91296,0.00744105,9.92834e-05,-2.48767e-07,2.02679e-10,37601.7,8.92464], Tmin=(10,'K'), Tmax=(313.45,'K')),
            NASAPolynomial(coeffs=[1.94931,0.0324993,-2.06307e-05,6.27211e-09,-7.31563e-13,37724.8,16.1201], Tmin=(313.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (312.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 396,
    label = "FC1[CH]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09356,-0.00897454,0.000136307,-2.43003e-07,1.39486e-10,11544.7,8.8662], Tmin=(10,'K'), Tmax=(556.06,'K')),
            NASAPolynomial(coeffs=[1.53702,0.0289143,-1.84986e-05,5.65581e-09,-6.60766e-13,11527.6,16.989], Tmin=(556.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.9752,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 397,
    label = "FCC1DC[CH]1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 C u1 p0 c0 {3,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89873,0.0154021,2.6752e-05,-4.55107e-08,1.89468e-11,30528.6,10.226], Tmin=(10,'K'), Tmax=(861.671,'K')),
            NASAPolynomial(coeffs=[4.15442,0.0269205,-1.54169e-05,4.22712e-09,-4.48636e-13,30012.9,6.2935], Tmin=(861.671,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (253.853,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 398,
    label = "O[C](F)CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79094,0.0184372,1.9745e-05,-5.35435e-08,3.0745e-11,-56221,10.6098], Tmin=(10,'K'), Tmax=(633.134,'K')),
            NASAPolynomial(coeffs=[4.11028,0.0248594,-1.54654e-05,4.58577e-09,-5.21514e-13,-56430.6,7.87926], Tmin=(633.134,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-467.474,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.318 kJ/mol
""",
    rank = 5,
)

entry(
    index = 399,
    label = "CC(F)C[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73557,0.0329471,4.63689e-06,-2.23375e-08,8.89271e-12,-41727.7,11.5968], Tmin=(10,'K'), Tmax=(1050.86,'K')),
            NASAPolynomial(coeffs=[6.60956,0.0355978,-1.85453e-05,4.67572e-09,-4.61414e-13,-43082.1,-5.98146], Tmin=(1050.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-346.922,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 400,
    label = "OC1(F)CDC1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {7,S}
5 C u0 p0 c0 {2,S} {4,D} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91759,0.00474662,9.09552e-05,-1.7647e-07,1.0162e-10,-16038.4,8.80201], Tmin=(10,'K'), Tmax=(585.294,'K')),
            NASAPolynomial(coeffs=[3.28552,0.0285251,-1.98541e-05,6.54736e-09,-8.15619e-13,-16297.7,8.66553], Tmin=(585.294,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.386,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 401,
    label = "OC1DC(F)[CH]1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {2,S} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91455,0.00527333,8.55488e-05,-1.87088e-07,1.20649e-10,15974.5,9.88403], Tmin=(10,'K'), Tmax=(529.987,'K')),
            NASAPolynomial(coeffs=[4.01953,0.0227309,-1.55125e-05,5.00804e-09,-6.12689e-13,15707.1,7.02619], Tmin=(529.987,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 402,
    label = "CDC([CH]F)OF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {8,S} {9,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 O u0 p2 c0 {2,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82116,0.0126507,0.000134729,-3.66153e-07,2.86302e-10,-8187.56,11.9006], Tmin=(10,'K'), Tmax=(446.232,'K')),
            NASAPolynomial(coeffs=[4.81411,0.0314918,-2.18592e-05,7.10904e-09,-8.70574e-13,-8552.38,4.81657], Tmin=(446.232,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-68.0916,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 403,
    label = "CD[C]C(O)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 O u0 p2 c0 {3,S} {9,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88504,0.00864782,0.000113618,-2.93733e-07,2.31709e-10,-15897.6,10.4119], Tmin=(10,'K'), Tmax=(413.06,'K')),
            NASAPolynomial(coeffs=[3.04383,0.0311396,-2.01542e-05,6.25201e-09,-7.41821e-13,-15950.5,12.2451], Tmin=(413.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.18,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 404,
    label = "FCC1CO1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9631,0.00221169,9.84063e-05,-1.72646e-07,9.77411e-11,-34383,9.93939], Tmin=(10,'K'), Tmax=(457.237,'K')),
            NASAPolynomial(coeffs=[-0.331209,0.039814,-2.50653e-05,7.54646e-09,-8.72501e-13,-33990.6,27.2924], Tmin=(457.237,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-285.892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.986 kJ/mol
""",
    rank = 5,
)

entry(
    index = 405,
    label = "C[C]DC(F)OF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58313,0.0361944,-2.98112e-05,1.26975e-08,-2.21521e-12,-507.385,10.5076], Tmin=(10,'K'), Tmax=(1275.77,'K')),
            NASAPolynomial(coeffs=[8.66447,0.0202626,-1.10793e-05,2.90903e-09,-2.97082e-13,-1803.92,-15.2446], Tmin=(1275.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.25979,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 406,
    label = "CDC(F)OO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p2 c0 {4,S} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8887,0.00735038,0.000106823,-2.58391e-07,1.84378e-10,-30812.6,9.73321], Tmin=(10,'K'), Tmax=(480.22,'K')),
            NASAPolynomial(coeffs=[4.18553,0.0259888,-1.73371e-05,5.51791e-09,-6.6802e-13,-31084.5,5.98443], Tmin=(480.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.213,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 407,
    label = "C[CH]CC(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {13,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55283,0.0474061,-0.000111321,2.95646e-07,-2.78645e-10,-44941.5,10.8883], Tmin=(10,'K'), Tmax=(392.277,'K')),
            NASAPolynomial(coeffs=[1.13783,0.0491164,-3.02372e-05,8.9301e-09,-1.01568e-12,-44575.8,22.5266], Tmin=(392.277,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-373.679,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.316 kJ/mol
""",
    rank = 5,
)

entry(
    index = 408,
    label = "[O]C(O)DCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {6,S}
4 C u0 p0 c0 {2,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90875,0.00578119,8.82759e-05,-2.01775e-07,1.35636e-10,-52428.1,10.1518], Tmin=(10,'K'), Tmax=(510.591,'K')),
            NASAPolynomial(coeffs=[4.1767,0.022341,-1.51889e-05,4.88851e-09,-5.963e-13,-52698.7,6.65741], Tmin=(510.591,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-435.938,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.425 kJ/mol
""",
    rank = 5,
)

entry(
    index = 409,
    label = "CC(F)(F)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 O u0 p2 c0 {2,S} {6,S}
6 O u1 p2 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82708,0.0132058,0.000107671,-2.85529e-07,2.19487e-10,-58842.9,10.0865], Tmin=(10,'K'), Tmax=(441.881,'K')),
            NASAPolynomial(coeffs=[3.7887,0.0324765,-2.19817e-05,6.99288e-09,-8.4194e-13,-59024.2,8.1498], Tmin=(441.881,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-489.26,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 410,
    label = "FC1DCCO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0963,-0.00885206,0.000133884,-2.29824e-07,1.2618e-10,-20443.6,9.08157], Tmin=(10,'K'), Tmax=(583.832,'K')),
            NASAPolynomial(coeffs=[1.37513,0.0303832,-1.9826e-05,6.10495e-09,-7.14274e-13,-20476.8,17.7397], Tmin=(583.832,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-169.989,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.584 kJ/mol
""",
    rank = 5,
)

entry(
    index = 411,
    label = "C[CH]CDCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79855,0.0199488,3.0276e-05,-5.44221e-08,2.38093e-11,-8204.32,9.39013], Tmin=(10,'K'), Tmax=(794.588,'K')),
            NASAPolynomial(coeffs=[2.8746,0.035683,-2.03487e-05,5.60646e-09,-6.00322e-13,-8407.37,11.4336], Tmin=(794.588,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-68.2212,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.688 kJ/mol
""",
    rank = 5,
)

entry(
    index = 412,
    label = "[CH]DC(F)OO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 O u0 p2 c0 {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85892,0.00956634,0.000102984,-2.7837e-07,2.12272e-10,1176.88,10.3195], Tmin=(10,'K'), Tmax=(468.772,'K')),
            NASAPolynomial(coeffs=[5.52474,0.0208337,-1.46076e-05,4.82239e-09,-5.9925e-13,740.722,0.558735], Tmin=(468.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.7631,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 413,
    label = "C#CC(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91461,0.00535556,8.59351e-05,-1.92024e-07,1.26823e-10,-24271.1,9.49376], Tmin=(10,'K'), Tmax=(516.944,'K')),
            NASAPolynomial(coeffs=[4.01934,0.0223483,-1.50308e-05,4.80583e-09,-5.84495e-13,-24519.8,6.75682], Tmin=(516.944,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-201.827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.58 kJ/mol
""",
    rank = 5,
)

entry(
    index = 414,
    label = "[O]C1(F)CC1",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91748,0.00499583,0.000105351,-2.12637e-07,1.30149e-10,-21519.3,10.2641], Tmin=(10,'K'), Tmax=(537.481,'K')),
            NASAPolynomial(coeffs=[2.6426,0.0324457,-2.13845e-05,6.73786e-09,-8.10538e-13,-21641.7,13.2096], Tmin=(537.481,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 415,
    label = "FOC1CDC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87528,0.00834543,0.000113628,-2.7764e-07,1.99274e-10,4668.99,10.9524], Tmin=(10,'K'), Tmax=(476.046,'K')),
            NASAPolynomial(coeffs=[4.04154,0.0288816,-2.01912e-05,6.5481e-09,-7.972e-13,4404.63,7.6634], Tmin=(476.046,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.7972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 416,
    label = "FCCCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {14,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94343,0.0331095,9.96838e-06,-2.56917e-08,9.02648e-12,-90469.5,11.3706], Tmin=(10,'K'), Tmax=(1181.7,'K')),
            NASAPolynomial(coeffs=[10.5953,0.0315853,-1.47436e-05,3.28283e-09,-2.83751e-13,-93507.4,-28.0332], Tmin=(1181.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-752.119,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.419 kJ/mol
""",
    rank = 5,
)

entry(
    index = 417,
    label = "FC1D[C]C1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94213,0.00338605,6.62158e-05,-1.30716e-07,7.67417e-11,16229.2,9.89853], Tmin=(10,'K'), Tmax=(570.119,'K')),
            NASAPolynomial(coeffs=[3.33069,0.020935,-1.48412e-05,4.86065e-09,-5.96925e-13,16083.5,10.615], Tmin=(570.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (134.914,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 418,
    label = "F[C]1COO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9556,0.00252035,7.16136e-05,-1.27212e-07,6.90302e-11,-3705.66,9.85591], Tmin=(10,'K'), Tmax=(583.17,'K')),
            NASAPolynomial(coeffs=[1.67798,0.0280832,-1.97061e-05,6.41217e-09,-7.83615e-13,-3609.04,18.1666], Tmin=(583.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.8307,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.711 kJ/mol
""",
    rank = 5,
)

entry(
    index = 419,
    label = "CDCO[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85063,0.0148898,3.5991e-05,-6.70169e-08,3.24526e-11,-15693.7,10.2327], Tmin=(10,'K'), Tmax=(711.706,'K')),
            NASAPolynomial(coeffs=[3.28241,0.0291855,-1.75377e-05,5.04245e-09,-5.58722e-13,-15894,10.8055], Tmin=(711.706,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.496,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.621 kJ/mol
""",
    rank = 5,
)

entry(
    index = 420,
    label = "COC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88197,0.0186944,1.30285e-05,-2.65697e-08,1.04527e-11,-46344.1,10.273], Tmin=(10,'K'), Tmax=(973.299,'K')),
            NASAPolynomial(coeffs=[5.27602,0.0243608,-1.32664e-05,3.47048e-09,-3.53254e-13,-47155.2,0.81242], Tmin=(973.299,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-385.296,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.799 kJ/mol
""",
    rank = 5,
)

entry(
    index = 421,
    label = "CC1O[C]1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94641,0.00349396,0.000105867,-2.20366e-07,1.45353e-10,-12934.6,9.12818], Tmin=(10,'K'), Tmax=(463.262,'K')),
            NASAPolynomial(coeffs=[1.58367,0.0333206,-2.12287e-05,6.45297e-09,-7.51406e-13,-12816.8,17.6174], Tmin=(463.262,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-107.554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.232 kJ/mol
""",
    rank = 5,
)

entry(
    index = 422,
    label = "CDCCOF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84577,0.0176467,2.86077e-05,-5.00892e-08,2.14152e-11,-3534.89,9.79245], Tmin=(10,'K'), Tmax=(825.732,'K')),
            NASAPolynomial(coeffs=[3.47063,0.0313628,-1.79235e-05,4.92977e-09,-5.26028e-13,-3878.59,9.07413], Tmin=(825.732,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.3835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 423,
    label = "F[C]DC1CC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94328,0.00342732,9.77102e-05,-1.86529e-07,1.10824e-10,28695.7,9.42059], Tmin=(10,'K'), Tmax=(527.18,'K')),
            NASAPolynomial(coeffs=[1.48834,0.0337523,-2.1859e-05,6.76812e-09,-8.02072e-13,28792,18.1509], Tmin=(527.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.569,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 424,
    label = "F[C]1CDCC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90254,0.00600006,0.00011531,-2.42111e-07,1.52798e-10,-8506.27,11.0421], Tmin=(10,'K'), Tmax=(526.65,'K')),
            NASAPolynomial(coeffs=[2.9312,0.0339822,-2.30747e-05,7.35336e-09,-8.86362e-13,-8689.7,12.3925], Tmin=(526.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-70.7575,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 425,
    label = "[CH2]C#CCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64386,0.0351869,-6.53873e-05,1.21015e-07,-9.29258e-11,15009,10.1459], Tmin=(10,'K'), Tmax=(425.219,'K')),
            NASAPolynomial(coeffs=[3.48557,0.0292056,-1.79356e-05,5.30365e-09,-6.04891e-13,15090,11.5683], Tmin=(425.219,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (124.782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.6 kJ/mol
""",
    rank = 5,
)

entry(
    index = 426,
    label = "CC(F)(F)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  O u1 p2 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82836,0.014322,0.000140504,-3.99293e-07,3.47178e-10,-59973.9,10.1125], Tmin=(10,'K'), Tmax=(366.488,'K')),
            NASAPolynomial(coeffs=[2.59825,0.041531,-2.72723e-05,8.52383e-09,-1.01602e-12,-59976.3,13.5495], Tmin=(366.488,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-498.636,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.333 kJ/mol
""",
    rank = 5,
)

entry(
    index = 427,
    label = "F[CH]C1DCDC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {4,D} {6,D}
6 C u0 p0 c0 {4,S} {5,D} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85986,0.017313,5.32445e-06,-2.02502e-08,9.42495e-12,50679.2,10.4277], Tmin=(10,'K'), Tmax=(883.091,'K')),
            NASAPolynomial(coeffs=[5.66214,0.0178982,-1.05301e-05,2.9373e-09,-3.15276e-13,50019.8,0.0253511], Tmin=(883.091,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (421.382,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 428,
    label = "OC(O)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 O u0 p2 c0 {2,S} {7,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94627,0.00316449,6.9764e-05,-1.34796e-07,7.90164e-11,-78993.3,8.34264], Tmin=(10,'K'), Tmax=(560.073,'K')),
            NASAPolynomial(coeffs=[2.92896,0.0225965,-1.4864e-05,4.72512e-09,-5.74567e-13,-79070.2,10.9573], Tmin=(560.073,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-656.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.415 kJ/mol
""",
    rank = 5,
)

entry(
    index = 429,
    label = "CO[C]DCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66933,0.0355797,-0.000109191,2.84964e-07,-2.60387e-10,-6120.69,9.47484], Tmin=(10,'K'), Tmax=(389.27,'K')),
            NASAPolynomial(coeffs=[2.25313,0.0311722,-1.91488e-05,5.63512e-09,-6.38473e-13,-5866.78,16.8161], Tmin=(389.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-50.9019,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.046 kJ/mol
""",
    rank = 5,
)

entry(
    index = 430,
    label = "ODCDC[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81255,0.0178368,7.92748e-05,-3.79692e-07,4.72757e-10,-11474.5,10.1961], Tmin=(10,'K'), Tmax=(293.642,'K')),
            NASAPolynomial(coeffs=[4.63927,0.0213748,-1.43984e-05,4.61532e-09,-5.6239e-13,-11586.9,6.13425], Tmin=(293.642,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.3822,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.653 kJ/mol
""",
    rank = 5,
)

entry(
    index = 431,
    label = "FCDC1CC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96887,0.00199891,0.000110256,-2.07909e-07,1.27258e-10,-1008.28,8.62724], Tmin=(10,'K'), Tmax=(423.177,'K')),
            NASAPolynomial(coeffs=[-0.0736685,0.040376,-2.63639e-05,8.2453e-09,-9.86474e-13,-667.623,24.6362], Tmin=(423.177,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.38933,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.992 kJ/mol
""",
    rank = 5,
)

entry(
    index = 432,
    label = "F[C]1CCO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0281,-0.00284252,0.00010677,-1.7233e-07,8.77839e-11,-17115.1,10.0779], Tmin=(10,'K'), Tmax=(616.662,'K')),
            NASAPolynomial(coeffs=[0.445651,0.0353537,-2.2526e-05,6.787e-09,-7.79158e-13,-16957.7,23.3232], Tmin=(616.662,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-142.314,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.232 kJ/mol
""",
    rank = 5,
)

entry(
    index = 433,
    label = "[CH2]C1OC1F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5 O u0 p2 c0 {4,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91832,0.00490415,0.000104354,-2.08135e-07,1.25812e-10,-15717.8,9.12873], Tmin=(10,'K'), Tmax=(544.268,'K')),
            NASAPolynomial(coeffs=[2.60169,0.0325778,-2.15154e-05,6.79509e-09,-8.19509e-13,-15841,12.2309], Tmin=(544.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.716,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.821 kJ/mol
""",
    rank = 5,
)

entry(
    index = 434,
    label = "OC(F)(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92109,0.00460818,7.22805e-05,-1.49742e-07,8.97309e-11,-111277,8.21717], Tmin=(10,'K'), Tmax=(579.139,'K')),
            NASAPolynomial(coeffs=[4.35877,0.0198934,-1.4728e-05,5.00259e-09,-6.31669e-13,-111635,3.69396], Tmin=(579.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-925.246,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.793 kJ/mol
""",
    rank = 5,
)

entry(
    index = 435,
    label = "CC(C)([O])F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  O u1 p2 c0 {2,S}
5  F u0 p3 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90844,0.00660302,0.000149856,-3.68e-07,2.85914e-10,-37968.1,7.90125], Tmin=(10,'K'), Tmax=(403.7,'K')),
            NASAPolynomial(coeffs=[2.06766,0.0391489,-2.42312e-05,7.27166e-09,-8.43726e-13,-37936,13.6683], Tmin=(403.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.682,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 436,
    label = "OCDCCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7943,0.0186117,2.72103e-05,-5.31019e-08,2.50616e-11,-41585.2,9.7524], Tmin=(10,'K'), Tmax=(727.627,'K')),
            NASAPolynomial(coeffs=[2.86525,0.0323178,-1.87713e-05,5.26872e-09,-5.73811e-13,-41677.6,12.3749], Tmin=(727.627,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-345.777,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.868 kJ/mol
""",
    rank = 5,
)

entry(
    index = 437,
    label = "OC(F)DCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91105,0.0054675,8.59438e-05,-1.88514e-07,1.21328e-10,-61079.1,9.3792], Tmin=(10,'K'), Tmax=(534.276,'K')),
            NASAPolynomial(coeffs=[4.20844,0.0223951,-1.53565e-05,4.98874e-09,-6.13803e-13,-61384.3,5.5725], Tmin=(534.276,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-507.871,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 438,
    label = "CC([CH]F)DCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {2,D} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.899,0.0113436,0.000268434,-1.32279e-06,2.25357e-09,-31086.8,9.88103], Tmin=(10,'K'), Tmax=(147.584,'K')),
            NASAPolynomial(coeffs=[2.82939,0.0403335,-2.62087e-05,8.15987e-09,-9.72202e-13,-31055.3,12.9948], Tmin=(147.584,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-258.158,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.766 kJ/mol
""",
    rank = 5,
)

entry(
    index = 439,
    label = "CDCOOF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90015,0.0065412,0.000104857,-2.45053e-07,1.70908e-10,4858.85,9.91334], Tmin=(10,'K'), Tmax=(483.731,'K')),
            NASAPolynomial(coeffs=[3.69648,0.0272282,-1.82174e-05,5.77555e-09,-6.95153e-13,4656.22,8.44993], Tmin=(483.731,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (40.3774,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 440,
    label = "OD[C]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89236,0.00895772,1.91649e-05,-3.79639e-08,1.95758e-11,-22812.9,8.98154], Tmin=(10,'K'), Tmax=(640.209,'K')),
            NASAPolynomial(coeffs=[3.1521,0.0176551,-1.07542e-05,3.12718e-09,-3.50007e-13,-22801.6,11.571], Tmin=(640.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.692,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.019 kJ/mol
""",
    rank = 5,
)

entry(
    index = 441,
    label = "O[CH]C(O)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
5 O u0 p2 c0 {4,S} {9,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90083,0.00615845,0.00011037,-2.37486e-07,1.5308e-10,-55697,10.3944], Tmin=(10,'K'), Tmax=(521.637,'K')),
            NASAPolynomial(coeffs=[3.46848,0.0304814,-1.9981e-05,6.31011e-09,-7.62353e-13,-55937.7,9.45923], Tmin=(521.637,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-463.123,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.654 kJ/mol
""",
    rank = 5,
)

entry(
    index = 442,
    label = "FCC1O[C]1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u1 p0 c0 {3,S} {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87945,0.0179664,2.70302e-05,-5.11787e-08,2.255e-11,-33094.9,11.1177], Tmin=(10,'K'), Tmax=(834.756,'K')),
            NASAPolynomial(coeffs=[5.01173,0.0273037,-1.62763e-05,4.5937e-09,-4.98196e-13,-33798.3,2.7788], Tmin=(834.756,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-275.143,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.183 kJ/mol
""",
    rank = 5,
)

entry(
    index = 443,
    label = "CCDCF",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96623,0.00211228,8.53659e-05,-1.58969e-07,9.69119e-11,-22620.6,7.68897], Tmin=(10,'K'), Tmax=(421.105,'K')),
            NASAPolynomial(coeffs=[0.901641,0.031225,-1.83451e-05,5.23481e-09,-5.8136e-13,-22362.6,19.8231], Tmin=(421.105,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.09,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.023 kJ/mol
""",
    rank = 5,
)

entry(
    index = 444,
    label = "CD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u1 p0 c0 {1,D} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05992,-0.005862,7.42223e-05,-1.36302e-07,8.22101e-11,11968.7,7.18151], Tmin=(10,'K'), Tmax=(518.064,'K')),
            NASAPolynomial(coeffs=[2.56835,0.0142493,-8.893e-06,2.67783e-09,-3.10143e-13,12007.9,12.2834], Tmin=(518.064,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.5083,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.689 kJ/mol
""",
    rank = 5,
)

entry(
    index = 445,
    label = "FC#CC(F)(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79995,0.0142399,0.000114851,-3.41951e-07,2.77346e-10,-67432,10.64], Tmin=(10,'K'), Tmax=(448.301,'K')),
            NASAPolynomial(coeffs=[6.14203,0.0236237,-1.78672e-05,6.08786e-09,-7.66424e-13,-67946.2,-2.17396], Tmin=(448.301,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-560.679,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.739 kJ/mol
""",
    rank = 5,
)

entry(
    index = 446,
    label = "CD[C]C(C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78447,0.0188969,5.19827e-05,-1.19611e-07,7.86743e-11,2259.4,10.5031], Tmin=(10,'K'), Tmax=(397.996,'K')),
            NASAPolynomial(coeffs=[1.79099,0.0389321,-2.35277e-05,6.87307e-09,-7.76574e-13,2418.08,18.2839], Tmin=(397.996,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.7694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 447,
    label = "FCC1OO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95776,0.00280803,9.42267e-05,-1.98131e-07,1.33119e-10,-28309,10.0247], Tmin=(10,'K'), Tmax=(444.21,'K')),
            NASAPolynomial(coeffs=[1.706,0.0297435,-1.92145e-05,5.86762e-09,-6.83405e-13,-28174.6,18.3214], Tmin=(444.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-235.38,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.194 kJ/mol
""",
    rank = 5,
)

entry(
    index = 448,
    label = "COCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83491,0.0152313,7.56228e-05,-2.79087e-07,3.2738e-10,-3900.83,9.00748], Tmin=(10,'K'), Tmax=(216.223,'K')),
            NASAPolynomial(coeffs=[3.11832,0.0284879,-1.63426e-05,4.4661e-09,-4.70369e-13,-3869.84,11.3672], Tmin=(216.223,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.4286,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.111 kJ/mol
""",
    rank = 5,
)

entry(
    index = 449,
    label = "F[CH]CCDCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82117,0.0288051,2.16912e-06,-1.80789e-08,7.36245e-12,-24040.8,11.6744], Tmin=(10,'K'), Tmax=(1072.67,'K')),
            NASAPolynomial(coeffs=[7.72065,0.0274184,-1.42869e-05,3.58115e-09,-3.50225e-13,-25634.2,-10.9395], Tmin=(1072.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-199.847,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.582 kJ/mol
""",
    rank = 5,
)

entry(
    index = 450,
    label = "F[C]1OCO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02983,-0.00289378,8.67246e-05,-1.40473e-07,7.11523e-11,-32148.3,9.17377], Tmin=(10,'K'), Tmax=(633.457,'K')),
            NASAPolynomial(coeffs=[1.60189,0.0268541,-1.78546e-05,5.51593e-09,-6.42803e-13,-32130,17.4956], Tmin=(633.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-267.305,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.268 kJ/mol
""",
    rank = 5,
)

entry(
    index = 451,
    label = "O[C](O)CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86591,0.01054,0.000113574,-3.17792e-07,2.6794e-10,-54641.4,9.7804], Tmin=(10,'K'), Tmax=(391.76,'K')),
            NASAPolynomial(coeffs=[3.37474,0.0304553,-1.97314e-05,6.1423e-09,-7.31678e-13,-54717.3,10.2304], Tmin=(391.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-454.308,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 452,
    label = "[CH2]C1CC1F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {5,S} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91215,0.005419,0.000129158,-2.60466e-07,1.62048e-10,1969.9,9.48471], Tmin=(10,'K'), Tmax=(517.025,'K')),
            NASAPolynomial(coeffs=[1.76113,0.0404259,-2.56866e-05,7.89788e-09,-9.35193e-13,1946.86,16.0694], Tmin=(517.025,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (16.3502,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 453,
    label = "C#CC(F)[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {8,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {3,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64722,0.0301708,3.53411e-05,-1.45504e-07,1.15322e-10,-26227.1,12.4362], Tmin=(10,'K'), Tmax=(490.748,'K')),
            NASAPolynomial(coeffs=[5.86138,0.0303614,-2.0987e-05,6.74455e-09,-8.15705e-13,-26664,1.09266], Tmin=(490.748,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-218.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.402 kJ/mol
""",
    rank = 5,
)

entry(
    index = 454,
    label = "O[CH]COF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8332,0.0140622,8.59496e-05,-2.39445e-07,1.95107e-10,-13607,10.5702], Tmin=(10,'K'), Tmax=(402.635,'K')),
            NASAPolynomial(coeffs=[3.23059,0.031337,-2.04599e-05,6.3732e-09,-7.57707e-13,-13649.9,11.793], Tmin=(402.635,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-113.133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.468 kJ/mol
""",
    rank = 5,
)

entry(
    index = 455,
    label = "CC([O])CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81286,0.0193038,3.05291e-05,-5.20967e-08,2.18108e-11,-29486,10.3894], Tmin=(10,'K'), Tmax=(833.442,'K')),
            NASAPolynomial(coeffs=[2.88757,0.0355984,-2.01315e-05,5.49152e-09,-5.82311e-13,-29743.5,12.215], Tmin=(833.442,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.159,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 456,
    label = "[O]CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08151,-0.00616932,5.83735e-05,-8.35862e-08,3.87788e-11,-26616.8,7.61107], Tmin=(10,'K'), Tmax=(675.064,'K')),
            NASAPolynomial(coeffs=[1.83593,0.0158409,-9.8744e-06,2.91313e-09,-3.2854e-13,-26511.9,16.0933], Tmin=(675.064,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-221.296,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.222 kJ/mol
""",
    rank = 5,
)

entry(
    index = 457,
    label = "ODCC(F)CF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85178,0.0271368,-3.75327e-06,-9.04321e-09,3.80275e-12,-68311.5,10.4654], Tmin=(10,'K'), Tmax=(1196.81,'K')),
            NASAPolynomial(coeffs=[9.04619,0.0209949,-1.01166e-05,2.33403e-09,-2.09975e-13,-70358.3,-18.8846], Tmin=(1196.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-567.941,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.1 kJ/mol
""",
    rank = 5,
)

entry(
    index = 458,
    label = "CDC(F)OC",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92001,0.00690147,0.000103599,-2.31569e-07,1.67708e-10,-40015.9,8.44357], Tmin=(10,'K'), Tmax=(353.816,'K')),
            NASAPolynomial(coeffs=[1.27934,0.0367554,-2.2968e-05,6.91277e-09,-8.00819e-13,-39829.1,18.4396], Tmin=(353.816,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-332.709,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.668 kJ/mol
""",
    rank = 5,
)

entry(
    index = 459,
    label = "[CH2]OCDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {8,S}
6 C u0 p0 c0 {5,D} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77414,0.0195282,3.09405e-05,-8.18843e-08,5.22644e-11,-12598.3,9.97004], Tmin=(10,'K'), Tmax=(533.901,'K')),
            NASAPolynomial(coeffs=[3.35852,0.0299154,-1.86768e-05,5.58718e-09,-6.42069e-13,-12657.6,10.7435], Tmin=(533.901,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-104.774,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.39 kJ/mol
""",
    rank = 5,
)

entry(
    index = 460,
    label = "FOC1[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {3,S} {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9229,0.00457664,8.33286e-05,-1.69728e-07,1.02413e-10,10204.1,10.0636], Tmin=(10,'K'), Tmax=(559.737,'K')),
            NASAPolynomial(coeffs=[3.52526,0.0247905,-1.73958e-05,5.68645e-09,-6.98941e-13,9976.49,9.32028], Tmin=(559.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.8117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.227 kJ/mol
""",
    rank = 5,
)

entry(
    index = 461,
    label = "CDCDCOF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86511,0.0106404,8.64899e-05,-2.30416e-07,1.80646e-10,18103.9,9.67888], Tmin=(10,'K'), Tmax=(425.033,'K')),
            NASAPolynomial(coeffs=[3.49255,0.0271924,-1.79645e-05,5.63585e-09,-6.72958e-13,18017.7,9.77132], Tmin=(425.033,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (150.52,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 462,
    label = "C#COF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90705,0.00602322,6.34376e-05,-1.66444e-07,1.21002e-10,26885.3,7.9715], Tmin=(10,'K'), Tmax=(501.518,'K')),
            NASAPolynomial(coeffs=[5.60697,0.0111604,-7.84379e-06,2.63994e-09,-3.36579e-13,26479.6,-1.40053], Tmin=(501.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (223.514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.174 kJ/mol
""",
    rank = 5,
)

entry(
    index = 463,
    label = "FCDCDCCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8198,0.027284,-2.91253e-06,-1.10052e-08,4.75555e-12,-24345.3,10.7156], Tmin=(10,'K'), Tmax=(1116.67,'K')),
            NASAPolynomial(coeffs=[7.92008,0.0232803,-1.18858e-05,2.9199e-09,-2.80207e-13,-25927.1,-12.5009], Tmin=(1116.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.148 kJ/mol
""",
    rank = 5,
)

entry(
    index = 464,
    label = "C[C]DCC(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74052,0.0323146,-8.91963e-06,-6.43465e-09,3.34473e-12,-24897.7,10.2926], Tmin=(10,'K'), Tmax=(1155.1,'K')),
            NASAPolynomial(coeffs=[8.44439,0.0257126,-1.29258e-05,3.13768e-09,-2.98341e-13,-26630.6,-15.8765], Tmin=(1155.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.999,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.929 kJ/mol
""",
    rank = 5,
)

entry(
    index = 465,
    label = "[O]C(F)DCCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {7,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81405,0.0273314,-7.66379e-06,-6.91426e-09,3.6961e-12,-57437.9,12.0913], Tmin=(10,'K'), Tmax=(1099.46,'K')),
            NASAPolynomial(coeffs=[8.4363,0.0199783,-1.05426e-05,2.65981e-09,-2.60955e-13,-59026.2,-13.2478], Tmin=(1099.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-477.538,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 466,
    label = "CCC[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86424,0.0255868,1.65747e-05,-2.89464e-08,9.937e-12,-16444.2,9.24625], Tmin=(10,'K'), Tmax=(1111.69,'K')),
            NASAPolynomial(coeffs=[5.82888,0.0344524,-1.6888e-05,4.0142e-09,-3.74749e-13,-17865.6,-4.86862], Tmin=(1111.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.682,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.959 kJ/mol
""",
    rank = 5,
)

entry(
    index = 467,
    label = "[CH]DC(F)OC",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93606,0.00651676,0.000180948,-7.18951e-07,9.802e-10,-8055.16,8.90112], Tmin=(10,'K'), Tmax=(184.816,'K')),
            NASAPolynomial(coeffs=[2.79173,0.0312843,-2.00751e-05,6.19811e-09,-7.34533e-13,-8012.87,12.4897], Tmin=(184.816,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-66.9266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.673 kJ/mol
""",
    rank = 5,
)

entry(
    index = 468,
    label = "[CH2]CDCDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,D}
6 C u0 p0 c0 {5,D} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86068,0.0116397,7.92726e-05,-1.93534e-07,1.41426e-10,15099.3,9.61666], Tmin=(10,'K'), Tmax=(433.057,'K')),
            NASAPolynomial(coeffs=[2.63757,0.0316579,-2.02712e-05,6.2089e-09,-7.28188e-13,15123.4,13.5497], Tmin=(433.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.536,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 469,
    label = "FCDC1[C]DC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {5,D}
5 C u0 p0 c0 {3,S} {4,D} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84658,0.0151018,1.90816e-05,-4.54877e-08,2.37636e-11,50138.6,9.95565], Tmin=(10,'K'), Tmax=(707.407,'K')),
            NASAPolynomial(coeffs=[4.56948,0.0206011,-1.29079e-05,3.81715e-09,-4.31289e-13,49796.5,5.02281], Tmin=(707.407,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (416.863,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 470,
    label = "CCDC[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74542,0.0221524,2.48921e-05,-5.10931e-08,2.39447e-11,-8174.45,9.14843], Tmin=(10,'K'), Tmax=(736.014,'K')),
            NASAPolynomial(coeffs=[2.68141,0.0362891,-2.09444e-05,5.84632e-09,-6.33928e-13,-8244.11,12.4183], Tmin=(736.014,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-67.9917,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.791 kJ/mol
""",
    rank = 5,
)

entry(
    index = 471,
    label = "CDCDCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85195,0.0117966,0.000107187,-3.72796e-07,3.65101e-10,43653.3,9.36523], Tmin=(10,'K'), Tmax=(365.447,'K')),
            NASAPolynomial(coeffs=[5.02025,0.0200488,-1.30441e-05,4.07739e-09,-4.88953e-13,43427.4,2.98269], Tmin=(365.447,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (362.971,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.649 kJ/mol
""",
    rank = 5,
)

entry(
    index = 472,
    label = "CC([O])(F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u1 p2 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85312,0.0144035,0.000154152,-5.24843e-07,5.86226e-10,-59324.1,11.0606], Tmin=(10,'K'), Tmax=(227.109,'K')),
            NASAPolynomial(coeffs=[2.29071,0.0419213,-2.75939e-05,8.65434e-09,-1.03517e-12,-59253.1,16.2823], Tmin=(227.109,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-493.219,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.333 kJ/mol
""",
    rank = 5,
)

entry(
    index = 473,
    label = "ODC(F)CDCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {7,S}
5 C u0 p0 c0 {4,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81414,0.0157972,4.43126e-05,-1.04996e-07,6.43794e-11,-64582,10.5435], Tmin=(10,'K'), Tmax=(570.946,'K')),
            NASAPolynomial(coeffs=[3.98522,0.0269989,-1.76949e-05,5.4469e-09,-6.36854e-13,-64803.7,8.04408], Tmin=(570.946,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-536.995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.412 kJ/mol
""",
    rank = 5,
)

entry(
    index = 474,
    label = "OCC(F)OF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70749,0.0256482,2.37377e-05,-6.93026e-08,4.0668e-11,-61047.7,10.8941], Tmin=(10,'K'), Tmax=(625.995,'K')),
            NASAPolynomial(coeffs=[4.25585,0.0331685,-2.06984e-05,6.15273e-09,-7.01161e-13,-61332.4,6.78018], Tmin=(625.995,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-507.617,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 475,
    label = "FCOC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94912,0.0202911,1.05855e-05,-2.39745e-08,9.19129e-12,-104940,10.5092], Tmin=(10,'K'), Tmax=(1048.01,'K')),
            NASAPolynomial(coeffs=[7.30878,0.0215813,-1.1461e-05,2.89948e-09,-2.84619e-13,-106419,-9.55452], Tmin=(1048.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-872.456,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 6.001 kJ/mol
""",
    rank = 5,
)

entry(
    index = 476,
    label = "OC(DCF)OF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81456,0.0133833,0.000119756,-3.46673e-07,2.81574e-10,-44471.5,10.754], Tmin=(10,'K'), Tmax=(438.275,'K')),
            NASAPolynomial(coeffs=[5.35932,0.0265785,-1.88187e-05,6.20721e-09,-7.67774e-13,-44869,1.58518], Tmin=(438.275,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-369.769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.066 kJ/mol
""",
    rank = 5,
)

entry(
    index = 477,
    label = "[O]CDCC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80129,0.0229805,1.10893e-05,-3.29095e-08,1.5305e-11,-52012.7,11.7394], Tmin=(10,'K'), Tmax=(851.457,'K')),
            NASAPolynomial(coeffs=[5.68353,0.0260853,-1.54276e-05,4.3318e-09,-4.68147e-13,-52766.3,0.418215], Tmin=(851.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-432.45,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.398 kJ/mol
""",
    rank = 5,
)

entry(
    index = 478,
    label = "FC#C[CH]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89735,0.0076552,7.66671e-05,-2.35089e-07,2.05217e-10,5847.78,10.0295], Tmin=(10,'K'), Tmax=(405.778,'K')),
            NASAPolynomial(coeffs=[4.6928,0.0155124,-1.04086e-05,3.31154e-09,-4.01025e-13,5653.99,5.3169], Tmin=(405.778,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.6235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (124.717,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.452 kJ/mol
""",
    rank = 5,
)

entry(
    index = 479,
    label = "FCDCD[C]CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61825,0.0388245,-7.30762e-05,1.38937e-07,-1.14964e-10,-5996.07,11.8621], Tmin=(10,'K'), Tmax=(376.213,'K')),
            NASAPolynomial(coeffs=[3.8154,0.0311706,-2.04001e-05,6.32579e-09,-7.47472e-13,-5971.58,11.6264], Tmin=(376.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-49.8576,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.024 kJ/mol
""",
    rank = 5,
)

entry(
    index = 480,
    label = "FC#CO[CH]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74876,0.0220632,6.28088e-05,-2.87396e-07,3.06468e-10,-647.281,11.3846], Tmin=(10,'K'), Tmax=(356.875,'K')),
            NASAPolynomial(coeffs=[5.39394,0.0221921,-1.57807e-05,5.2123e-09,-6.4592e-13,-882.952,3.48602], Tmin=(356.875,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.36193,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 481,
    label = "FOCCDC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71406,0.0333168,-8.08596e-06,-1.35418e-08,7.55413e-12,-51072.7,12.1524], Tmin=(10,'K'), Tmax=(951.974,'K')),
            NASAPolynomial(coeffs=[8.1459,0.0262448,-1.51414e-05,4.1435e-09,-4.37093e-13,-52439.9,-11.7593], Tmin=(951.974,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-424.63,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 482,
    label = "FCCC(F)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79309,0.035803,-6.72782e-06,-1.12516e-08,5.14086e-12,-68761,11.4895], Tmin=(10,'K'), Tmax=(1149.32,'K')),
            NASAPolynomial(coeffs=[10.2318,0.0272726,-1.37075e-05,3.30336e-09,-3.10503e-13,-71157.6,-24.4572], Tmin=(1149.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-571.666,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 483,
    label = "[O]CDC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91837,0.00566358,7.61578e-05,-1.91663e-07,1.42998e-10,-46872.4,10.1487], Tmin=(10,'K'), Tmax=(452.609,'K')),
            NASAPolynomial(coeffs=[3.8128,0.0196706,-1.35924e-05,4.35455e-09,-5.25496e-13,-46996.8,9.09496], Tmin=(452.609,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-389.729,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.485 kJ/mol
""",
    rank = 5,
)

entry(
    index = 484,
    label = "F[C]DCOCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75078,0.027209,-8.09532e-06,-6.33336e-09,3.55423e-12,-28989.9,11.2931], Tmin=(10,'K'), Tmax=(1065.96,'K')),
            NASAPolynomial(coeffs=[7.34744,0.021762,-1.17575e-05,3.04113e-09,-3.05816e-13,-30214,-8.43363], Tmin=(1065.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-241.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.554 kJ/mol
""",
    rank = 5,
)

entry(
    index = 485,
    label = "FCC1DC(F)[CH]1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u1 p0 c0 {3,S} {4,S} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81511,0.02437,3.32708e-06,-2.05867e-08,9.26249e-12,9033.36,11.5335], Tmin=(10,'K'), Tmax=(950.646,'K')),
            NASAPolynomial(coeffs=[6.62675,0.0237813,-1.34823e-05,3.64077e-09,-3.80121e-13,7990.81,-4.56047], Tmin=(950.646,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.1303,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 486,
    label = "[CH2]C(DCF)CF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  F u0 p3 c0 {5,S}
7  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
8  F u0 p3 c0 {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7409,0.0226279,4.64643e-05,-1.04694e-07,5.9566e-11,-30288.3,11.6889], Tmin=(10,'K'), Tmax=(604.271,'K')),
            NASAPolynomial(coeffs=[3.22516,0.0385094,-2.39074e-05,7.08848e-09,-8.06949e-13,-30453.6,12.0338], Tmin=(604.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-251.867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 487,
    label = "C[C]1CC1(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76384,0.0222101,4.1848e-05,-8.64464e-08,4.41753e-11,-19801.1,10.1626], Tmin=(10,'K'), Tmax=(685.65,'K')),
            NASAPolynomial(coeffs=[3.52221,0.0377491,-2.30574e-05,6.71689e-09,-7.52155e-13,-20100.1,8.81524], Tmin=(685.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-164.661,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.771 kJ/mol
""",
    rank = 5,
)

entry(
    index = 488,
    label = "OCDCOF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48228,0.0499363,-0.000131109,2.14651e-07,-1.38017e-10,-60436.6,10.9689], Tmin=(10,'K'), Tmax=(447.058,'K')),
            NASAPolynomial(coeffs=[5.81519,0.0219911,-1.36182e-05,4.06079e-09,-4.66502e-13,-60574.5,2.3825], Tmin=(447.058,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-502.514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.447 kJ/mol
""",
    rank = 5,
)

entry(
    index = 489,
    label = "C[C]DC(C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72053,0.0286721,-5.85417e-06,-5.91144e-09,2.55405e-12,1044.36,8.14324], Tmin=(10,'K'), Tmax=(1256.44,'K')),
            NASAPolynomial(coeffs=[7.53492,0.0251143,-1.18567e-05,2.71215e-09,-2.43972e-13,-591.841,-13.8266], Tmin=(1256.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.66519,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 490,
    label = "FCDC1CO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94744,0.00313489,8.50385e-05,-1.61143e-07,9.43397e-11,-13340.4,9.27425], Tmin=(10,'K'), Tmax=(540.537,'K')),
            NASAPolynomial(coeffs=[1.88046,0.0296212,-1.95158e-05,6.10844e-09,-7.28852e-13,-13280.4,16.4624], Tmin=(540.537,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.938,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 491,
    label = "F[C]1CCC1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00828,-0.00137555,0.000122094,-1.99395e-07,1.03518e-10,-216.739,9.57343], Tmin=(10,'K'), Tmax=(587.211,'K')),
            NASAPolynomial(coeffs=[-0.753917,0.0441008,-2.73749e-05,8.10701e-09,-9.2044e-13,117.776,28.0992], Tmin=(587.211,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1.81617,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.705 kJ/mol
""",
    rank = 5,
)

entry(
    index = 492,
    label = "ODC[C](F)CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75702,0.0268494,-6.80551e-06,-7.66273e-09,3.99796e-12,-49598.9,11.4869], Tmin=(10,'K'), Tmax=(1061.25,'K')),
            NASAPolynomial(coeffs=[7.30053,0.0219832,-1.19274e-05,3.09295e-09,-3.1154e-13,-50829.1,-8.07167], Tmin=(1061.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-412.383,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.832 kJ/mol
""",
    rank = 5,
)

entry(
    index = 493,
    label = "CC(O)(O)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  F u0 p3 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8839,0.00742788,0.000127432,-2.87104e-07,1.94066e-10,-85510.2,8.20826], Tmin=(10,'K'), Tmax=(498.759,'K')),
            NASAPolynomial(coeffs=[3.61995,0.0331913,-2.11669e-05,6.57951e-09,-7.88435e-13,-85778,6.34957], Tmin=(498.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-711.002,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.868 kJ/mol
""",
    rank = 5,
)

entry(
    index = 494,
    label = "CDCOCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96046,0.00274026,0.000119304,-2.55123e-07,1.80241e-10,-39839.8,9.82681], Tmin=(10,'K'), Tmax=(361.666,'K')),
            NASAPolynomial(coeffs=[0.863871,0.0369892,-2.27459e-05,6.72876e-09,-7.6766e-13,-39615.9,21.6166], Tmin=(361.666,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-331.249,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.668 kJ/mol
""",
    rank = 5,
)

entry(
    index = 495,
    label = "CC(F)DCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u1 p0 c0 {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81675,0.0183227,0.000178611,-8.74307e-07,1.24369e-09,-894.817,10.1594], Tmin=(10,'K'), Tmax=(245.55,'K')),
            NASAPolynomial(coeffs=[4.35264,0.0301997,-1.9823e-05,6.20498e-09,-7.42164e-13,-983.258,7.06156], Tmin=(245.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.41686,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 496,
    label = "C[C](F)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76793,0.0288754,-4.94805e-06,-7.71063e-09,3.30558e-12,-34783.4,9.53949], Tmin=(10,'K'), Tmax=(1198.68,'K')),
            NASAPolynomial(coeffs=[7.70798,0.0251526,-1.20837e-05,2.81767e-09,-2.58335e-13,-36405.1,-13.0075], Tmin=(1198.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 497,
    label = "[C]#CC#CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90063,0.00749627,6.44203e-05,-2.18996e-07,2.02658e-10,81536.9,6.1291], Tmin=(10,'K'), Tmax=(397.687,'K')),
            NASAPolynomial(coeffs=[5.21584,0.0103381,-6.91265e-06,2.19464e-09,-2.66658e-13,81305.2,-0.601016], Tmin=(397.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (677.941,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.818 kJ/mol
""",
    rank = 5,
)

entry(
    index = 498,
    label = "F[C]DC1OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85528,0.0115169,4.15542e-05,-1.38985e-07,1.16648e-10,27172.2,9.28045], Tmin=(10,'K'), Tmax=(438.888,'K')),
            NASAPolynomial(coeffs=[4.83175,0.0147419,-1.09061e-05,3.64598e-09,-4.52371e-13,26969.8,4.04338], Tmin=(438.888,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (225.915,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 499,
    label = "OCC(F)DCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71614,0.0245777,2.71187e-05,-7.66922e-08,4.66302e-11,-61765.4,10.7958], Tmin=(10,'K'), Tmax=(588.181,'K')),
            NASAPolynomial(coeffs=[3.83946,0.0335825,-2.09489e-05,6.24222e-09,-7.13806e-13,-61950.1,8.81893], Tmin=(588.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-513.582,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 500,
    label = "[CH]DCC#CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88117,0.00839244,9.84774e-05,-2.74015e-07,2.20214e-10,49501.9,9.81952], Tmin=(10,'K'), Tmax=(436.848,'K')),
            NASAPolynomial(coeffs=[4.79937,0.0204879,-1.34557e-05,4.24255e-09,-5.12177e-13,49226,3.91099], Tmin=(436.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (411.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.704 kJ/mol
""",
    rank = 5,
)

entry(
    index = 501,
    label = "CDCDCC(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78244,0.0187786,5.3715e-05,-1.20344e-07,7.15534e-11,-31397.9,11.0323], Tmin=(10,'K'), Tmax=(572.823,'K')),
            NASAPolynomial(coeffs=[3.26893,0.0350614,-2.21717e-05,6.67068e-09,-7.68161e-13,-31547.3,11.4053], Tmin=(572.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-261.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.101 kJ/mol
""",
    rank = 5,
)

entry(
    index = 502,
    label = "FC1DCOC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07821,-0.00752543,0.000130004,-2.27892e-07,1.27743e-10,-14918.3,9.12989], Tmin=(10,'K'), Tmax=(569.812,'K')),
            NASAPolynomial(coeffs=[1.42352,0.0302152,-1.96395e-05,6.02951e-09,-7.0423e-13,-14925.9,17.7225], Tmin=(569.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.051,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 503,
    label = "FC#CO[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63193,0.0317515,6.68776e-06,-1.02058e-07,9.47747e-11,-27106.6,11.8954], Tmin=(10,'K'), Tmax=(481.073,'K')),
            NASAPolynomial(coeffs=[7.02051,0.0212439,-1.56375e-05,5.22119e-09,-6.47373e-13,-27637.1,-4.09787], Tmin=(481.073,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-225.409,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.087 kJ/mol
""",
    rank = 5,
)

entry(
    index = 504,
    label = "OC(O)DCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {7,S}
4 C u0 p0 c0 {2,D} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88714,0.00720337,0.000103962,-2.43405e-07,1.66687e-10,-59078.1,9.38487], Tmin=(10,'K'), Tmax=(506.022,'K')),
            NASAPolynomial(coeffs=[4.5788,0.0247843,-1.64755e-05,5.28083e-09,-6.46226e-13,-59443.2,3.60337], Tmin=(506.022,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-491.233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.528 kJ/mol
""",
    rank = 5,
)

entry(
    index = 505,
    label = "CC([O])OF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 O u1 p2 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77724,0.0198104,2.48987e-05,-5.99935e-08,3.25609e-11,-12750.7,10.4436], Tmin=(10,'K'), Tmax=(656.174,'K')),
            NASAPolynomial(coeffs=[3.78737,0.0291296,-1.78492e-05,5.22536e-09,-5.88204e-13,-12954,8.86013], Tmin=(656.174,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.043,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 506,
    label = "O[CH]CCF",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.859,0.0119083,7.979e-05,-1.56683e-07,9.27982e-11,-34836,10.4489], Tmin=(10,'K'), Tmax=(515.185,'K')),
            NASAPolynomial(coeffs=[1.23745,0.0399744,-2.43803e-05,7.17228e-09,-8.14483e-13,-34668.2,20.3643], Tmin=(515.185,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.954 kJ/mol
""",
    rank = 5,
)

entry(
    index = 507,
    label = "CC[C](O)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {11,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77698,0.019807,4.87837e-05,-1.16442e-07,7.82572e-11,-38956.3,9.5079], Tmin=(10,'K'), Tmax=(389.928,'K')),
            NASAPolynomial(coeffs=[1.94996,0.0385489,-2.33133e-05,6.82266e-09,-7.72338e-13,-38813.9,16.6015], Tmin=(389.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-323.916,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 508,
    label = "CDCC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9278,0.0045117,0.00010604,-2.17989e-07,1.38127e-10,-18646.5,10.7673], Tmin=(10,'K'), Tmax=(506.948,'K')),
            NASAPolynomial(coeffs=[2.19104,0.0328868,-2.13294e-05,6.59856e-09,-7.8033e-13,-18658.9,16.1069], Tmin=(506.948,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-155.057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.13 kJ/mol
""",
    rank = 5,
)

entry(
    index = 509,
    label = "CDC(C)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89925,0.00877643,0.00013932,-3.76705e-07,3.36116e-10,-8902.9,9.46485], Tmin=(10,'K'), Tmax=(285.053,'K')),
            NASAPolynomial(coeffs=[1.67424,0.0399987,-2.49766e-05,7.54125e-09,-8.7749e-13,-8776.05,17.4067], Tmin=(285.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-74.0097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 510,
    label = "CDCDCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83051,0.0163747,3.44252e-05,-6.08534e-08,2.78011e-11,-4191.22,9.80055], Tmin=(10,'K'), Tmax=(744.226,'K')),
            NASAPolynomial(coeffs=[2.66851,0.0327571,-1.9025e-05,5.32847e-09,-5.78687e-13,-4298.99,13.1773], Tmin=(744.226,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-34.8582,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.513 kJ/mol
""",
    rank = 5,
)

entry(
    index = 511,
    label = "FOC1[CH]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9168,0.00492168,0.000104653,-2.05147e-07,1.2139e-10,26914.8,10.3028], Tmin=(10,'K'), Tmax=(557.383,'K')),
            NASAPolynomial(coeffs=[2.54941,0.0334532,-2.25035e-05,7.19218e-09,-8.73643e-13,26776.5,13.492], Tmin=(557.383,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (223.749,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.522 kJ/mol
""",
    rank = 5,
)

entry(
    index = 512,
    label = "FCDCDCOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7049,0.0273427,-8.23952e-06,-1.37241e-08,9.38624e-12,-2286.23,10.8299], Tmin=(10,'K'), Tmax=(783.57,'K')),
            NASAPolynomial(coeffs=[6.31292,0.0220852,-1.35964e-05,3.95434e-09,-4.40295e-13,-2942.25,-2.6943], Tmin=(783.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-19.0337,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 513,
    label = "OC1(F)CC1F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8897,0.00666424,0.000126303,-2.60044e-07,1.60297e-10,-61102.9,10.243], Tmin=(10,'K'), Tmax=(542.867,'K')),
            NASAPolynomial(coeffs=[3.01973,0.0372734,-2.51375e-05,8.04525e-09,-9.77581e-13,-61365.1,10.6245], Tmin=(542.867,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-508.079,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 514,
    label = "C#CCF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95303,0.00294449,7.14931e-05,-1.46622e-07,9.33052e-11,1093.56,8.15196], Tmin=(10,'K'), Tmax=(502.995,'K')),
            NASAPolynomial(coeffs=[2.77978,0.0218778,-1.36065e-05,4.12449e-09,-4.84491e-13,1090.11,11.7984], Tmin=(502.995,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.07876,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.629 kJ/mol
""",
    rank = 5,
)

entry(
    index = 515,
    label = "ODCC(F)OF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78341,0.0289329,-1.90855e-05,4.98996e-09,-2.01301e-13,-47882.5,11.0031], Tmin=(10,'K'), Tmax=(1262.22,'K')),
            NASAPolynomial(coeffs=[10.1453,0.0137142,-6.87341e-06,1.64215e-09,-1.52669e-13,-49882.3,-22.7306], Tmin=(1262.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-398.108,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 516,
    label = "CC1D[C]C1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84462,0.0148674,3.3761e-05,-6.25445e-08,3.00732e-11,28424.3,8.9822], Tmin=(10,'K'), Tmax=(710.284,'K')),
            NASAPolynomial(coeffs=[3.03283,0.0292689,-1.74117e-05,4.97011e-09,-5.47943e-13,28291.6,10.8754], Tmin=(710.284,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (236.32,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 517,
    label = "CDC(F)CC",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84101,0.0143376,6.35355e-05,-1.06496e-07,5.13861e-11,-27348.9,8.70926], Tmin=(10,'K'), Tmax=(660.088,'K')),
            NASAPolynomial(coeffs=[0.889115,0.0427554,-2.49706e-05,7.0589e-09,-7.74548e-13,-27188.6,19.9866], Tmin=(660.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-227.41,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.1 kJ/mol
""",
    rank = 5,
)

entry(
    index = 518,
    label = "C[CH]C(F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49032,0.0544922,-0.000159418,4.1096e-07,-3.72972e-10,-40210.2,12.3629], Tmin=(10,'K'), Tmax=(392.732,'K')),
            NASAPolynomial(coeffs=[1.3068,0.0486391,-2.9766e-05,8.7384e-09,-9.88512e-13,-39822.1,23.6145], Tmin=(392.732,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-334.344,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.695 kJ/mol
""",
    rank = 5,
)

entry(
    index = 519,
    label = "CDC(C)F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97213,0.00177519,9.02681e-05,-1.69366e-07,1.03722e-10,-24951.3,7.17634], Tmin=(10,'K'), Tmax=(420.456,'K')),
            NASAPolynomial(coeffs=[0.718483,0.0327534,-2.0337e-05,6.14767e-09,-7.1979e-13,-24677.9,20.0517], Tmin=(420.456,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-207.464,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.588 kJ/mol
""",
    rank = 5,
)

entry(
    index = 520,
    label = "FOOCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71335,0.0363975,-1.82077e-05,-1.40287e-09,2.64545e-12,-59381.8,11.9936], Tmin=(10,'K'), Tmax=(1081.79,'K')),
            NASAPolynomial(coeffs=[10.0727,0.0225203,-1.23281e-05,3.2086e-09,-3.23331e-13,-61321.5,-21.7926], Tmin=(1081.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-493.708,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 521,
    label = "[CH]DC(F)CC",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,D}
2  H u0 p0 c0 {1,S}
3  C u0 p0 c0 {1,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84568,0.0134316,8.84856e-05,-2.08791e-07,1.54351e-10,3987.61,9.32354], Tmin=(10,'K'), Tmax=(347.935,'K')),
            NASAPolynomial(coeffs=[1.57159,0.0395754,-2.42235e-05,7.16644e-09,-8.18808e-13,4145.86,17.8939], Tmin=(347.935,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (33.1496,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 522,
    label = "CC([O])DCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u1 p2 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76825,0.0213548,9.71652e-06,-2.93853e-08,1.41013e-11,-29515.9,9.60504], Tmin=(10,'K'), Tmax=(791.741,'K')),
            NASAPolynomial(coeffs=[4.19847,0.0269573,-1.56299e-05,4.36194e-09,-4.71742e-13,-29827.8,6.09076], Tmin=(791.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.426,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.07 kJ/mol
""",
    rank = 5,
)

entry(
    index = 523,
    label = "[C]#CCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92541,0.00604454,3.40389e-05,-6.35963e-08,3.46077e-11,42757.7,8.83468], Tmin=(10,'K'), Tmax=(585.971,'K')),
            NASAPolynomial(coeffs=[2.80537,0.0188223,-1.18076e-05,3.51047e-09,-3.99646e-13,42800.8,12.8878], Tmin=(585.971,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (355.495,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.216 kJ/mol
""",
    rank = 5,
)

entry(
    index = 524,
    label = "OC(DCF)CF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77793,0.0189243,6.6659e-05,-1.72493e-07,1.23012e-10,-64300.6,10.766], Tmin=(10,'K'), Tmax=(466.309,'K')),
            NASAPolynomial(coeffs=[3.13987,0.035586,-2.29278e-05,7.04044e-09,-8.26243e-13,-64362.7,12.0532], Tmin=(466.309,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-534.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.517 kJ/mol
""",
    rank = 5,
)

entry(
    index = 525,
    label = "[O]C#CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94586,0.00365374,4.27902e-05,-1.12422e-07,8.43807e-11,3778.88,8.20012], Tmin=(10,'K'), Tmax=(470.056,'K')),
            NASAPolynomial(coeffs=[4.44459,0.00926182,-6.54475e-06,2.13708e-09,-2.62419e-13,3623.15,5.01278], Tmin=(470.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (31.4106,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.744 kJ/mol
""",
    rank = 5,
)

entry(
    index = 526,
    label = "FC1O[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {2,S} {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0462,-0.00418415,9.37493e-05,-1.51782e-07,7.70123e-11,-34002.7,9.81726], Tmin=(10,'K'), Tmax=(635.977,'K')),
            NASAPolynomial(coeffs=[1.67844,0.0269637,-1.80558e-05,5.6086e-09,-6.56269e-13,-34030.3,17.5841], Tmin=(635.977,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-282.722,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.262 kJ/mol
""",
    rank = 5,
)

entry(
    index = 527,
    label = "CC([O])(F)OF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u1 p2 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 O u0 p2 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82777,0.0123547,0.000131075,-3.54925e-07,2.785e-10,-37817.7,11.1577], Tmin=(10,'K'), Tmax=(440.585,'K')),
            NASAPolynomial(coeffs=[4.44287,0.0320593,-2.2108e-05,7.14121e-09,-8.69834e-13,-38117.3,5.90897], Tmin=(440.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-314.447,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 528,
    label = "F[CH]C#CCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61825,0.0388245,-7.30762e-05,1.38937e-07,-1.14964e-10,-5855.27,11.8621], Tmin=(10,'K'), Tmax=(376.213,'K')),
            NASAPolynomial(coeffs=[3.8154,0.0311706,-2.04001e-05,6.32579e-09,-7.47472e-13,-5830.77,11.6264], Tmin=(376.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-48.6868,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.926 kJ/mol
""",
    rank = 5,
)

entry(
    index = 529,
    label = "CC(CF)CF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81266,0.0290715,1.76477e-05,-3.24197e-08,1.13538e-11,-63434.6,9.3275], Tmin=(10,'K'), Tmax=(1095.47,'K')),
            NASAPolynomial(coeffs=[5.98528,0.0386384,-1.94143e-05,4.71752e-09,-4.49313e-13,-64960.7,-6.14496], Tmin=(1095.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-527.386,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.474 kJ/mol
""",
    rank = 5,
)

entry(
    index = 530,
    label = "FC1DCCDC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 C u0 p0 c0 {2,S} {4,D} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93977,0.00338999,8.34352e-05,-1.49901e-07,8.1471e-11,26481.1,7.72101], Tmin=(10,'K'), Tmax=(597.491,'K')),
            NASAPolynomial(coeffs=[1.94309,0.0309797,-2.15345e-05,7.06149e-09,-8.74393e-13,26465.8,14.201], Tmin=(597.491,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.058 kJ/mol
""",
    rank = 5,
)

entry(
    index = 531,
    label = "OC#C[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76546,0.0218937,7.04115e-05,-3.77951e-07,4.70906e-10,3010.53,10.0773], Tmin=(10,'K'), Tmax=(309.936,'K')),
            NASAPolynomial(coeffs=[5.43631,0.0197565,-1.32639e-05,4.26606e-09,-5.22412e-13,2813.65,2.46837], Tmin=(309.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.0565,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.555 kJ/mol
""",
    rank = 5,
)

entry(
    index = 532,
    label = "F[C]DCOOF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68489,0.029248,-1.71656e-05,-6.8044e-09,8.04671e-12,15613.9,12.2932], Tmin=(10,'K'), Tmax=(754.119,'K')),
            NASAPolynomial(coeffs=[7.43189,0.0179699,-1.18325e-05,3.5977e-09,-4.13115e-13,14804.3,-6.34724], Tmin=(754.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (129.792,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 533,
    label = "OC1(F)OC1F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89232,0.00654636,0.0001059,-2.278e-07,1.43749e-10,-82388.8,10.1716], Tmin=(10,'K'), Tmax=(542.917,'K')),
            NASAPolynomial(coeffs=[4.05322,0.0287926,-2.03014e-05,6.66188e-09,-8.20875e-13,-82751.6,6.31327], Tmin=(542.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-685.057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 534,
    label = "CC(F)D[C]O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,D} {5,S}
5 O u0 p2 c0 {4,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88907,0.00863872,0.000129115,-3.72839e-07,3.30932e-10,-13710.7,9.06595], Tmin=(10,'K'), Tmax=(369.752,'K')),
            NASAPolynomial(coeffs=[3.34609,0.0298074,-1.88088e-05,5.73945e-09,-6.74839e-13,-13775.1,9.7315], Tmin=(369.752,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-113.985,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 535,
    label = "FC1D[C]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97411,0.00149413,5.29283e-05,-9.24853e-08,5.03575e-11,42696.1,8.27749], Tmin=(10,'K'), Tmax=(557.971,'K')),
            NASAPolynomial(coeffs=[1.90318,0.0214756,-1.45936e-05,4.68478e-09,-5.70183e-13,42847.2,16.3439], Tmin=(557.971,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (354.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 536,
    label = "FCCC(F)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86715,0.0340966,8.54223e-06,-2.54384e-08,9.26003e-12,-86680.3,11.0887], Tmin=(10,'K'), Tmax=(1143.66,'K')),
            NASAPolynomial(coeffs=[9.3296,0.0341554,-1.667e-05,3.91015e-09,-3.58308e-13,-89183,-21.4769], Tmin=(1143.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-720.631,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.007 kJ/mol
""",
    rank = 5,
)

entry(
    index = 537,
    label = "C#CC(F)CF",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {7,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78601,0.0185002,7.42929e-05,-2.01851e-07,1.54709e-10,-25282.1,10.6568], Tmin=(10,'K'), Tmax=(427.257,'K')),
            NASAPolynomial(coeffs=[3.03353,0.0359165,-2.32634e-05,7.18449e-09,-8.47708e-13,-25312.5,12.5394], Tmin=(427.257,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-210.215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 538,
    label = "OD[C]COF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77461,0.0212136,-5.48434e-06,-9.98611e-09,6.23707e-12,-5230.11,10.4981], Tmin=(10,'K'), Tmax=(830.674,'K')),
            NASAPolynomial(coeffs=[5.6814,0.0180938,-1.07977e-05,3.06371e-09,-3.34513e-13,-5756.05,0.39373], Tmin=(830.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.5009,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 539,
    label = "[CH]DCOF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {6,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93158,0.00416179,6.72687e-05,-1.44787e-07,9.16212e-11,30461.4,8.89814], Tmin=(10,'K'), Tmax=(542.252,'K')),
            NASAPolynomial(coeffs=[4.10513,0.0178878,-1.22115e-05,3.96399e-09,-4.88391e-13,30221.9,6.13281], Tmin=(542.252,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (253.246,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 540,
    label = "F[CH]CDC(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80686,0.0151136,0.000100311,-3.06546e-07,2.61323e-10,-50373,11.3485], Tmin=(10,'K'), Tmax=(412.309,'K')),
            NASAPolynomial(coeffs=[4.60447,0.0276804,-1.92768e-05,6.25825e-09,-7.64801e-13,-50611.4,6.11424], Tmin=(412.309,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-418.825,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.328 kJ/mol
""",
    rank = 5,
)

entry(
    index = 541,
    label = "OC(O)C(F)F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  O u0 p2 c0 {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83577,0.0126084,0.000118701,-3.04377e-07,2.31677e-10,-103109,10.7734], Tmin=(10,'K'), Tmax=(436.249,'K')),
            NASAPolynomial(coeffs=[3.21416,0.0361919,-2.38807e-05,7.48426e-09,-8.92721e-13,-103225,11.3062], Tmin=(436.249,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-857.307,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.635 kJ/mol
""",
    rank = 5,
)

entry(
    index = 542,
    label = "O[C](O)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {6,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92202,0.00496073,7.01502e-05,-1.64083e-07,1.11815e-10,-54277.4,8.7436], Tmin=(10,'K'), Tmax=(509.583,'K')),
            NASAPolynomial(coeffs=[4.42881,0.016834,-1.14594e-05,3.72651e-09,-4.58882e-13,-54534.9,4.62091], Tmin=(509.583,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-451.31,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.327 kJ/mol
""",
    rank = 5,
)

entry(
    index = 543,
    label = "[O]CCCF",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94138,0.0156615,3.73379e-05,-5.42812e-08,2.05788e-11,-29533.6,10.2006], Tmin=(10,'K'), Tmax=(926.916,'K')),
            NASAPolynomial(coeffs=[3.52327,0.0337988,-1.84442e-05,4.84918e-09,-4.96591e-13,-30157.7,8.40112], Tmin=(926.916,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.506,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.663 kJ/mol
""",
    rank = 5,
)

entry(
    index = 544,
    label = "OCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u1 p0 c0 {2,D} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93951,0.00416054,6.7472e-05,-1.63305e-07,1.19866e-10,-5558.04,9.04708], Tmin=(10,'K'), Tmax=(450.755,'K')),
            NASAPolynomial(coeffs=[3.5494,0.0177744,-1.1615e-05,3.6306e-09,-4.32883e-13,-5626.01,9.47423], Tmin=(450.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.2193,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.843 kJ/mol
""",
    rank = 5,
)

entry(
    index = 545,
    label = "FCD[C]COF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81642,0.0315358,-2.01441e-05,5.69765e-09,-5.16697e-13,4077.22,11.4454], Tmin=(10,'K'), Tmax=(1492.39,'K')),
            NASAPolynomial(coeffs=[13.2438,0.0110272,-4.31474e-06,7.63492e-10,-4.81239e-14,733.324,-39.5868], Tmin=(1492.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (33.9037,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 546,
    label = "OC1DC[C]1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92084,0.00462622,8.10315e-05,-1.63322e-07,9.68679e-11,10644.3,9.71928], Tmin=(10,'K'), Tmax=(575.039,'K')),
            NASAPolynomial(coeffs=[3.81554,0.0237259,-1.67014e-05,5.5291e-09,-6.89268e-13,10352.7,7.52854], Tmin=(575.039,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.4689,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 547,
    label = "OC(F)CDCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81062,0.0155819,8.18568e-05,-1.94106e-07,1.31671e-10,-67342.5,10.7553], Tmin=(10,'K'), Tmax=(488.916,'K')),
            NASAPolynomial(coeffs=[3.00294,0.0360246,-2.33071e-05,7.16842e-09,-8.41459e-13,-67428.9,12.3829], Tmin=(488.916,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-559.941,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 548,
    label = "C[C](O)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74827,0.0237817,1.53697e-05,-3.4471e-08,1.47989e-11,-36726,9.41176], Tmin=(10,'K'), Tmax=(854.062,'K')),
            NASAPolynomial(coeffs=[3.57162,0.0339565,-1.89175e-05,5.10797e-09,-5.37724e-13,-37036.7,8.2403], Tmin=(854.062,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-305.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 549,
    label = "[C]#CC(F)OF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73841,0.0305358,-2.95234e-05,1.49849e-08,-3.18104e-12,34775.6,11.067], Tmin=(10,'K'), Tmax=(1027.02,'K')),
            NASAPolynomial(coeffs=[6.82111,0.0185294,-1.19878e-05,3.60215e-09,-4.10242e-13,34142.4,-3.88746], Tmin=(1027.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.128,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 550,
    label = "O[C]DCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94418,0.0035424,6.44835e-05,-1.41792e-07,9.39357e-11,-7692.11,9.05945], Tmin=(10,'K'), Tmax=(503.644,'K')),
            NASAPolynomial(coeffs=[3.57927,0.0177726,-1.16484e-05,3.65703e-09,-4.38388e-13,-7799.08,9.14283], Tmin=(503.644,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.9712,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.145 kJ/mol
""",
    rank = 5,
)

entry(
    index = 551,
    label = "[O]OCCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94236,0.0174497,1.35336e-05,-2.45494e-08,8.9889e-12,-26358.9,10.1885], Tmin=(10,'K'), Tmax=(1048.9,'K')),
            NASAPolynomial(coeffs=[5.92413,0.0224815,-1.16656e-05,2.90947e-09,-2.83069e-13,-27467.1,-2.76823], Tmin=(1048.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-219.11,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.341 kJ/mol
""",
    rank = 5,
)

entry(
    index = 552,
    label = "F[CH]C(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83096,0.0158952,1.89993e-05,-4.86325e-08,2.66522e-11,-57675.2,10.7699], Tmin=(10,'K'), Tmax=(677.45,'K')),
            NASAPolynomial(coeffs=[4.60467,0.0208959,-1.32605e-05,3.96408e-09,-4.51968e-13,-57999.6,5.71788], Tmin=(677.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-479.558,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.534 kJ/mol
""",
    rank = 5,
)

entry(
    index = 553,
    label = "FCD[C]C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67253,0.0301771,3.21473e-07,-4.09551e-08,2.73634e-11,-67842.5,11.2836], Tmin=(10,'K'), Tmax=(677.169,'K')),
            NASAPolynomial(coeffs=[7.02681,0.0239963,-1.61851e-05,5.02493e-09,-5.87339e-13,-68609.4,-5.89918], Tmin=(677.169,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-564.113,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 554,
    label = "C[C](C)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53493,0.0502482,-0.000162549,4.2652e-07,-3.7587e-10,-18401.5,7.91734], Tmin=(10,'K'), Tmax=(412.928,'K')),
            NASAPolynomial(coeffs=[0.315228,0.0472345,-2.73557e-05,7.66084e-09,-8.33356e-13,-17844,24.1336], Tmin=(412.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.014,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.156 kJ/mol
""",
    rank = 5,
)

entry(
    index = 555,
    label = "FC1DC[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {2,S} {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92933,0.00409135,7.90398e-05,-1.5425e-07,8.93661e-11,2146.06,9.40535], Tmin=(10,'K'), Tmax=(580.23,'K')),
            NASAPolynomial(coeffs=[3.29982,0.024943,-1.7552e-05,5.77702e-09,-7.15449e-13,1941.16,9.7045], Tmin=(580.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (17.8134,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.36 kJ/mol
""",
    rank = 5,
)

entry(
    index = 556,
    label = "CDCDC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78588,0.0185241,1.46865e-05,-5.55865e-08,3.81225e-11,-11568.5,10.4738], Tmin=(10,'K'), Tmax=(551.886,'K')),
            NASAPolynomial(coeffs=[4.48034,0.0212399,-1.37567e-05,4.21454e-09,-4.92055e-13,-11763.2,6.46707], Tmin=(551.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.2121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.927 kJ/mol
""",
    rank = 5,
)

entry(
    index = 557,
    label = "[O]OCDC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78376,0.0186805,3.35004e-05,-9.99918e-08,6.70124e-11,-32106.5,11.4305], Tmin=(10,'K'), Tmax=(560.935,'K')),
            NASAPolynomial(coeffs=[5.34478,0.0222635,-1.54294e-05,4.92618e-09,-5.90456e-13,-32513.1,2.73852], Tmin=(560.935,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-266.982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.295 kJ/mol
""",
    rank = 5,
)

entry(
    index = 558,
    label = "CC(C)C(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {14,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67337,0.0277177,3.38362e-05,-6.33208e-08,2.78667e-11,-68739,8.62218], Tmin=(10,'K'), Tmax=(774.196,'K')),
            NASAPolynomial(coeffs=[1.63512,0.0489313,-2.79624e-05,7.7172e-09,-8.2786e-13,-68743.5,15.8663], Tmin=(774.196,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-571.56,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.491 kJ/mol
""",
    rank = 5,
)

entry(
    index = 559,
    label = "[C]#CCOF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80091,0.0178009,1.19356e-05,-3.88607e-08,2.19565e-11,59893.7,10.2464], Tmin=(10,'K'), Tmax=(680.675,'K')),
            NASAPolynomial(coeffs=[4.73341,0.0207567,-1.31679e-05,3.93327e-09,-4.4812e-13,59571.4,4.67088], Tmin=(680.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (497.962,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.995 kJ/mol
""",
    rank = 5,
)

entry(
    index = 560,
    label = "FOC1DCC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91956,0.00506472,9.75854e-05,-2.10161e-07,1.36884e-10,29226.7,9.62063], Tmin=(10,'K'), Tmax=(508.11,'K')),
            NASAPolynomial(coeffs=[3.09785,0.0279643,-1.85227e-05,5.82073e-09,-6.96244e-13,29098.1,10.9414], Tmin=(508.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (242.981,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 561,
    label = "[O]C(F)CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89192,0.011763,4.0595e-05,-7.42083e-08,3.65635e-11,-52426.7,10.3988], Tmin=(10,'K'), Tmax=(700.292,'K')),
            NASAPolynomial(coeffs=[3.55393,0.025949,-1.60418e-05,4.69946e-09,-5.27493e-13,-52679.8,9.76341], Tmin=(700.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-435.907,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 562,
    label = "OC1C(F)C1F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88497,0.00779784,0.00013598,-3.19457e-07,2.28563e-10,-55696.6,10.5731], Tmin=(10,'K'), Tmax=(458.511,'K')),
            NASAPolynomial(coeffs=[2.77767,0.0371632,-2.45526e-05,7.68547e-09,-9.14839e-13,-55802.2,12.793], Tmin=(458.511,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-463.105,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 563,
    label = "FC(F)[C]1OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 O u0 p2 c0 {4,S} {6,S}
6 O u0 p2 c0 {4,S} {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82432,0.0209536,4.20411e-06,-2.5816e-08,1.34293e-11,-27264.3,10.581], Tmin=(10,'K'), Tmax=(826.626,'K')),
            NASAPolynomial(coeffs=[6.64807,0.0185074,-1.1713e-05,3.43785e-09,-3.83115e-13,-28114.4,-4.8225], Tmin=(826.626,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-226.682,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.742 kJ/mol
""",
    rank = 5,
)

entry(
    index = 564,
    label = "FCDCO[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76172,0.0331046,-1.68681e-05,-1.51231e-09,2.60778e-12,-63561.9,12.0182], Tmin=(10,'K'), Tmax=(1077.91,'K')),
            NASAPolynomial(coeffs=[10.0806,0.0191376,-1.06261e-05,2.78747e-09,-2.82092e-13,-65475,-21.4957], Tmin=(1077.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-528.455,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.403 kJ/mol
""",
    rank = 5,
)

entry(
    index = 565,
    label = "O[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02441,-0.00246112,5.55407e-05,-9.79607e-08,5.51772e-11,-29210.7,7.59482], Tmin=(10,'K'), Tmax=(565.498,'K')),
            NASAPolynomial(coeffs=[2.85857,0.0137567,-8.62173e-06,2.60735e-09,-3.02575e-13,-29206.3,11.4278], Tmin=(565.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-242.878,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.39 kJ/mol
""",
    rank = 5,
)

entry(
    index = 566,
    label = "CDC(F)CF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94082,0.00384218,0.000105878,-2.22248e-07,1.46815e-10,-44978.8,9.91984], Tmin=(10,'K'), Tmax=(470.46,'K')),
            NASAPolynomial(coeffs=[1.82649,0.0326889,-2.07534e-05,6.30756e-09,-7.35621e-13,-44900.2,17.2475], Tmin=(470.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-373.987,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.23 kJ/mol
""",
    rank = 5,
)

entry(
    index = 567,
    label = "CC(DCF)OF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {2,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68338,0.0276492,2.41286e-05,-8.86592e-08,6.33887e-11,-28221.4,9.71823], Tmin=(10,'K'), Tmax=(507.365,'K')),
            NASAPolynomial(coeffs=[3.99192,0.0342046,-2.18247e-05,6.63798e-09,-7.72582e-13,-28368.4,7.29902], Tmin=(507.365,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-234.676,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 568,
    label = "OOCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90969,0.00776025,3.95023e-05,-7.56359e-08,4.1988e-11,-43694.9,8.6082], Tmin=(10,'K'), Tmax=(578.101,'K')),
            NASAPolynomial(coeffs=[2.75361,0.021958,-1.342e-05,3.9415e-09,-4.46111e-13,-43664.8,12.6563], Tmin=(578.101,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-363.314,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.244 kJ/mol
""",
    rank = 5,
)

entry(
    index = 569,
    label = "[O]C(F)C#CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76083,0.0200599,4.16837e-05,-1.478e-07,1.18981e-10,-8343.11,11.5256], Tmin=(10,'K'), Tmax=(468.544,'K')),
            NASAPolynomial(coeffs=[5.32572,0.0223427,-1.57029e-05,5.10626e-09,-6.23023e-13,-8661.45,3.32999], Tmin=(468.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.3893,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 570,
    label = "F[C]1COC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93073,0.00421986,0.000107626,-2.11907e-07,1.28481e-10,-36978.6,11.4121], Tmin=(10,'K'), Tmax=(524.682,'K')),
            NASAPolynomial(coeffs=[1.64335,0.0359865,-2.4154e-05,7.58246e-09,-9.0067e-13,-36935.8,19.0927], Tmin=(524.682,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-307.482,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 571,
    label = "CO[CH]C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71156,0.0337108,-1.30053e-05,-2.47332e-09,2.06915e-12,-55115.8,10.1484], Tmin=(10,'K'), Tmax=(1198,'K')),
            NASAPolynomial(coeffs=[8.91762,0.0247024,-1.2211e-05,2.91942e-09,-2.73796e-13,-56964.1,-18.4164], Tmin=(1198,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-458.257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.204 kJ/mol
""",
    rank = 5,
)

entry(
    index = 572,
    label = "CC(DO)C(F)(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  F u0 p3 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.619,0.0349954,-7.98578e-06,-2.10183e-08,1.35467e-11,-102816,9.9155], Tmin=(10,'K'), Tmax=(774.114,'K')),
            NASAPolynomial(coeffs=[6.63639,0.0298598,-1.8295e-05,5.30832e-09,-5.9044e-13,-103596,-5.89264], Tmin=(774.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-854.893,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.074 kJ/mol
""",
    rank = 5,
)

entry(
    index = 573,
    label = "FCCCDC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80277,0.0322192,3.8145e-06,-2.24979e-08,9.20765e-12,-72652.8,11.7035], Tmin=(10,'K'), Tmax=(1052.66,'K')),
            NASAPolynomial(coeffs=[8.11941,0.0311403,-1.64841e-05,4.18672e-09,-4.14134e-13,-74410.6,-13.3761], Tmin=(1052.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-604.022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.135 kJ/mol
""",
    rank = 5,
)

entry(
    index = 574,
    label = "COO[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17665,0.0895986,-0.000441555,1.04145e-06,-8.58517e-10,-47406.2,11.5464], Tmin=(10,'K'), Tmax=(394.936,'K')),
            NASAPolynomial(coeffs=[4.43515,0.0271831,-1.58483e-05,4.39652e-09,-4.70065e-13,-47118.2,11.5481], Tmin=(394.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-394.188,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.085 kJ/mol
""",
    rank = 5,
)

entry(
    index = 575,
    label = "[CH]DC(F)CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89252,0.00809219,8.72318e-05,-2.06757e-07,1.47037e-10,-13547.3,10.4363], Tmin=(10,'K'), Tmax=(460.925,'K')),
            NASAPolynomial(coeffs=[3.09179,0.0277681,-1.82178e-05,5.66762e-09,-6.71443e-13,-13608.7,12.2127], Tmin=(460.925,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-112.651,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 576,
    label = "FC1OC(F)O1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 O u0 p2 c0 {2,S} {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95256,0.00269832,8.57809e-05,-1.50271e-07,8.0931e-11,-86802.9,8.86779], Tmin=(10,'K'), Tmax=(576.059,'K')),
            NASAPolynomial(coeffs=[0.747866,0.0350465,-2.47387e-05,8.05471e-09,-9.82837e-13,-86601.2,21.1071], Tmin=(576.059,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-721.742,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.964 kJ/mol
""",
    rank = 5,
)

entry(
    index = 577,
    label = "OC[CH]CF",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77762,0.0225617,2.03803e-05,-4.0751e-08,1.73493e-11,-31543.7,10.5419], Tmin=(10,'K'), Tmax=(851.007,'K')),
            NASAPolynomial(coeffs=[3.62295,0.0341373,-1.91452e-05,5.19262e-09,-5.48233e-13,-31910.2,8.955], Tmin=(851.007,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-262.272,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.663 kJ/mol
""",
    rank = 5,
)

entry(
    index = 578,
    label = "[CH2]C(DO)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95357,0.00266379,5.79574e-05,-1.08991e-07,6.16187e-11,-31328.9,7.93544], Tmin=(10,'K'), Tmax=(584.381,'K')),
            NASAPolynomial(coeffs=[3.07892,0.0195584,-1.3406e-05,4.3619e-09,-5.38103e-13,-31413,10.0917], Tmin=(584.381,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-260.504,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.289 kJ/mol
""",
    rank = 5,
)

entry(
    index = 579,
    label = "FCC1DC[C]1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 C u1 p0 c0 {3,S} {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83526,0.02204,1.24935e-05,-3.2661e-08,1.44985e-11,6823.65,11.5492], Tmin=(10,'K'), Tmax=(887.053,'K')),
            NASAPolynomial(coeffs=[5.91315,0.0254389,-1.4846e-05,4.11365e-09,-4.39172e-13,5952.65,-1.05805], Tmin=(887.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (56.7569,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 580,
    label = "FOCC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81261,0.0242207,5.19045e-06,-2.37001e-08,1.07417e-11,-64609.2,10.8659], Tmin=(10,'K'), Tmax=(924.366,'K')),
            NASAPolynomial(coeffs=[6.47833,0.0243729,-1.40224e-05,3.83486e-09,-4.04734e-13,-65601.4,-4.48588], Tmin=(924.366,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-537.171,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 581,
    label = "FC[C](F)CF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04307,0.0301324,-1.37275e-05,1.27014e-09,4.10121e-13,-58996,11.1409], Tmin=(10,'K'), Tmax=(1631.32,'K')),
            NASAPolynomial(coeffs=[21.3157,-0.000942506,4.47614e-06,-1.9313e-09,2.513e-13,-66132,-85.2416], Tmin=(1631.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-490.517,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.455 kJ/mol
""",
    rank = 5,
)

entry(
    index = 582,
    label = "FCC1[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {3,S} {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95523,0.00275759,9.78653e-05,-1.8549e-07,1.11232e-10,-8827.58,10.5173], Tmin=(10,'K'), Tmax=(501.177,'K')),
            NASAPolynomial(coeffs=[0.935261,0.0349405,-2.26396e-05,6.97382e-09,-8.20548e-13,-8626.34,21.9883], Tmin=(501.177,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.411,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.33 kJ/mol
""",
    rank = 5,
)

entry(
    index = 583,
    label = "[O]OCDCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87244,0.0126571,3.0203e-05,-6.33412e-08,3.34873e-11,-9113.4,10.2406], Tmin=(10,'K'), Tmax=(673.141,'K')),
            NASAPolynomial(coeffs=[4.21936,0.0214674,-1.36557e-05,4.08884e-09,-4.66672e-13,-9406.42,6.87461], Tmin=(673.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-75.7873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.577 kJ/mol
""",
    rank = 5,
)

entry(
    index = 584,
    label = "[O]C(F)DCO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 O u0 p2 c0 {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92552,0.0045005,8.12036e-05,-1.69071e-07,1.04744e-10,-55966.2,9.98948], Tmin=(10,'K'), Tmax=(544.455,'K')),
            NASAPolynomial(coeffs=[3.58818,0.0233653,-1.59153e-05,5.12671e-09,-6.25839e-13,-56172.4,9.18142], Tmin=(544.455,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-465.357,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.264 kJ/mol
""",
    rank = 5,
)

entry(
    index = 585,
    label = "CC([CH]F)OF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61082,0.0369623,-1.79254e-05,-5.4592e-10,2.15712e-12,-19662.6,11.679], Tmin=(10,'K'), Tmax=(1049.43,'K')),
            NASAPolynomial(coeffs=[7.73054,0.0281402,-1.51503e-05,3.93881e-09,-3.99596e-13,-20906.1,-10.2002], Tmin=(1049.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.504,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 586,
    label = "OC(O)CF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  O u0 p2 c0 {2,S} {8,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92459,0.0051309,0.00012446,-2.79695e-07,1.979e-10,-76195.1,9.82563], Tmin=(10,'K'), Tmax=(442.145,'K')),
            NASAPolynomial(coeffs=[1.93668,0.0357942,-2.25816e-05,6.87041e-09,-8.03094e-13,-76143.3,16.3923], Tmin=(442.145,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-633.53,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.872 kJ/mol
""",
    rank = 5,
)

entry(
    index = 587,
    label = "C[C](F)C#CF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81675,0.0183228,0.000178613,-8.74334e-07,1.24375e-09,-913.889,10.1594], Tmin=(10,'K'), Tmax=(245.545,'K')),
            NASAPolynomial(coeffs=[4.35262,0.0301998,-1.9823e-05,6.20501e-09,-7.42168e-13,-1002.33,7.06169], Tmin=(245.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.57543,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 588,
    label = "ODC1[C]DC1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94088,0.0035497,5.6805e-05,-1.20966e-07,7.50892e-11,20717.8,9.62064], Tmin=(10,'K'), Tmax=(553.884,'K')),
            NASAPolynomial(coeffs=[4.07538,0.0156606,-1.14215e-05,3.79507e-09,-4.69955e-13,20502.2,7.23971], Tmin=(553.884,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.518 kJ/mol
""",
    rank = 5,
)

entry(
    index = 589,
    label = "CC[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87869,0.0139532,2.98338e-05,-4.44266e-08,1.73118e-11,-13395.8,8.22483], Tmin=(10,'K'), Tmax=(873.898,'K')),
            NASAPolynomial(coeffs=[2.3388,0.0311029,-1.69411e-05,4.48314e-09,-4.63893e-13,-13512.4,13.2395], Tmin=(873.898,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-111.369,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.505 kJ/mol
""",
    rank = 5,
)

entry(
    index = 590,
    label = "[CH]DCCCF",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,D}
2  H u0 p0 c0 {1,S}
3  C u0 p0 c0 {1,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84153,0.0197314,2.67175e-05,-4.50459e-08,1.79944e-11,4571.45,10.2857], Tmin=(10,'K'), Tmax=(893.685,'K')),
            NASAPolynomial(coeffs=[3.55088,0.0339218,-1.87343e-05,4.99864e-09,-5.19651e-13,4108.68,8.7755], Tmin=(893.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.0276,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.916 kJ/mol
""",
    rank = 5,
)

entry(
    index = 591,
    label = "COCF",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9915,0.0111128,2.10731e-05,-2.59722e-08,8.16114e-12,-50770,7.15246], Tmin=(10,'K'), Tmax=(1144.77,'K')),
            NASAPolynomial(coeffs=[4.58572,0.0221187,-1.04896e-05,2.39111e-09,-2.12977e-13,-51763.3,0.461326], Tmin=(1144.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-422.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.944 kJ/mol
""",
    rank = 5,
)

entry(
    index = 592,
    label = "O[C]DC(F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89549,0.00700812,8.17483e-05,-2.12367e-07,1.57575e-10,-30482.6,10.2065], Tmin=(10,'K'), Tmax=(475.546,'K')),
            NASAPolynomial(coeffs=[4.86371,0.0179012,-1.266e-05,4.16567e-09,-5.14425e-13,-30790,3.99174], Tmin=(475.546,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-253.466,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.797 kJ/mol
""",
    rank = 5,
)

entry(
    index = 593,
    label = "F[C]1CCC1F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92976,0.00429616,0.000129022,-2.48341e-07,1.49463e-10,-23781.7,11.506], Tmin=(10,'K'), Tmax=(514.58,'K')),
            NASAPolynomial(coeffs=[0.528214,0.044637,-2.90886e-05,8.99205e-09,-1.06034e-12,-23615.6,23.8683], Tmin=(514.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-197.756,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 594,
    label = "CCO[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87557,0.0296326,-3.90735e-06,-9.44269e-09,3.84556e-12,-59222.3,9.65803], Tmin=(10,'K'), Tmax=(1239.03,'K')),
            NASAPolynomial(coeffs=[10.2825,0.0217806,-9.93601e-06,2.15955e-09,-1.81945e-13,-61794.9,-26.5998], Tmin=(1239.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-492.361,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.896 kJ/mol
""",
    rank = 5,
)

entry(
    index = 595,
    label = "CC1(F)[C]DC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,D}
5 C u0 p0 c0 {2,S} {4,D} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91904,0.00499514,0.000105841,-2.18379e-07,1.37326e-10,28816.9,8.63927], Tmin=(10,'K'), Tmax=(521.094,'K')),
            NASAPolynomial(coeffs=[2.65974,0.0317842,-2.05608e-05,6.39155e-09,-7.62242e-13,28715.7,11.6632], Tmin=(521.094,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (239.571,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 596,
    label = "OCDC[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91077,0.00541468,0.000105848,-2.17448e-07,1.34567e-10,-26091.5,10.0343], Tmin=(10,'K'), Tmax=(538.062,'K')),
            NASAPolynomial(coeffs=[3.0628,0.0312267,-2.04945e-05,6.47591e-09,-7.83076e-13,-26282.6,10.9756], Tmin=(538.062,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-216.969,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.75 kJ/mol
""",
    rank = 5,
)

entry(
    index = 597,
    label = "C#CC(F)(F)[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {9,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 C u1 p0 c0 {3,S} {7,S} {8,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.609,0.0321009,7.8129e-05,-2.9517e-07,2.51353e-10,-51144.4,12.446], Tmin=(10,'K'), Tmax=(452.734,'K')),
            NASAPolynomial(coeffs=[7.30278,0.0310383,-2.29574e-05,7.72076e-09,-9.63783e-13,-51802.4,-6.02074], Tmin=(452.734,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-425.266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.878 kJ/mol
""",
    rank = 5,
)

entry(
    index = 598,
    label = "[CH]DCCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96641,0.0021254,8.21446e-05,-1.59048e-07,9.86297e-11,8887.7,9.22367], Tmin=(10,'K'), Tmax=(475.53,'K')),
            NASAPolynomial(coeffs=[1.51195,0.0282833,-1.77533e-05,5.37717e-09,-6.27839e-13,9058.82,18.5853], Tmin=(475.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.8881,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.522 kJ/mol
""",
    rank = 5,
)

entry(
    index = 599,
    label = "FCDCCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81797,0.0309957,8.46909e-06,-2.81045e-08,1.13841e-11,-75695,11.8373], Tmin=(10,'K'), Tmax=(1020.41,'K')),
            NASAPolynomial(coeffs=[7.68996,0.0321849,-1.73388e-05,4.47554e-09,-4.49169e-13,-77337.4,-11.0964], Tmin=(1020.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-629.312,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.874 kJ/mol
""",
    rank = 5,
)

entry(
    index = 600,
    label = "OD[C]CCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91075,0.0200976,3.79874e-06,-1.34126e-08,4.89101e-12,-27695.1,10.3612], Tmin=(10,'K'), Tmax=(1157.32,'K')),
            NASAPolynomial(coeffs=[7.08337,0.0197689,-9.56124e-06,2.22472e-09,-2.0239e-13,-29141.8,-8.48589], Tmin=(1157.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-230.235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.064 kJ/mol
""",
    rank = 5,
)

entry(
    index = 601,
    label = "FC#C[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81157,0.0146788,8.11017e-05,-2.82662e-07,2.57201e-10,-17674.6,10.7872], Tmin=(10,'K'), Tmax=(405.886,'K')),
            NASAPolynomial(coeffs=[5.58389,0.0188171,-1.40342e-05,4.7393e-09,-5.93746e-13,-17996.4,1.64263], Tmin=(405.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-146.952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.595 kJ/mol
""",
    rank = 5,
)

entry(
    index = 602,
    label = "F[C]DCC(F)(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74308,0.0212427,6.37337e-05,-1.85537e-07,1.33076e-10,-69475.7,11.237], Tmin=(10,'K'), Tmax=(515.445,'K')),
            NASAPolynomial(coeffs=[5.79676,0.027622,-1.97743e-05,6.46722e-09,-7.89396e-13,-69983.8,-0.185499], Tmin=(515.445,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-577.693,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 603,
    label = "C#CC(F)OF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82457,0.0128452,0.000114926,-3.30676e-07,2.69442e-10,-5559.51,10.6729], Tmin=(10,'K'), Tmax=(432.475,'K')),
            NASAPolynomial(coeffs=[4.93434,0.0270028,-1.88839e-05,6.16739e-09,-7.57466e-13,-5883.89,3.60863], Tmin=(432.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.2332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 604,
    label = "F[C]1CDC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93537,0.00373588,6.77168e-05,-1.34005e-07,7.79705e-11,12164.9,9.83089], Tmin=(10,'K'), Tmax=(583.777,'K')),
            NASAPolynomial(coeffs=[3.66105,0.0207823,-1.50543e-05,5.02298e-09,-6.26079e-13,11938.5,8.79318], Tmin=(583.777,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.831 kJ/mol
""",
    rank = 5,
)

entry(
    index = 605,
    label = "[CH]DC(C)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.944,0.00349571,8.53512e-05,-1.73906e-07,1.09924e-10,6864.13,7.84012], Tmin=(10,'K'), Tmax=(506.229,'K')),
            NASAPolynomial(coeffs=[2.51035,0.0263282,-1.63917e-05,4.97335e-09,-5.84699e-13,6861.87,12.3247], Tmin=(506.229,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.0548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 606,
    label = "C[C](F)OCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59985,0.0429717,-0.000114394,3.08796e-07,-2.9679e-10,-59090.8,10.8965], Tmin=(10,'K'), Tmax=(376.381,'K')),
            NASAPolynomial(coeffs=[1.83243,0.041283,-2.60756e-05,7.84861e-09,-9.05378e-13,-58812.7,19.6226], Tmin=(376.381,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-491.321,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.865 kJ/mol
""",
    rank = 5,
)

entry(
    index = 607,
    label = "C#CC(F)D[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {3,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82467,0.0125042,0.000112403,-3.38473e-07,2.808e-10,22720.4,11.0808], Tmin=(10,'K'), Tmax=(437.962,'K')),
            NASAPolynomial(coeffs=[6.03537,0.0210018,-1.4958e-05,4.96216e-09,-6.17979e-13,22251.6,-0.900443], Tmin=(437.962,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (188.896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.427 kJ/mol
""",
    rank = 5,
)

entry(
    index = 608,
    label = "[C]#CC(F)CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75098,0.0270987,-6.07652e-06,-9.48954e-09,4.92073e-12,15903.8,11.2087], Tmin=(10,'K'), Tmax=(1014.62,'K')),
            NASAPolynomial(coeffs=[7.08173,0.0227487,-1.26273e-05,3.34465e-09,-3.43359e-13,14775.9,-7.13593], Tmin=(1014.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.236,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 609,
    label = "[O]CCOF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85334,0.0187418,1.80684e-05,-3.66022e-08,1.565e-11,-7649.21,10.4231], Tmin=(10,'K'), Tmax=(872.284,'K')),
            NASAPolynomial(coeffs=[4.75355,0.026325,-1.5111e-05,4.14784e-09,-4.40487e-13,-8251.8,3.64922], Tmin=(872.284,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.5827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 610,
    label = "OC[C](O)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {9,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90342,0.00648539,0.000115738,-2.71122e-07,1.9338e-10,-52999,10.5313], Tmin=(10,'K'), Tmax=(462.264,'K')),
            NASAPolynomial(coeffs=[3.10086,0.0308687,-1.99703e-05,6.20198e-09,-7.36624e-13,-53111.2,11.7686], Tmin=(462.264,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-440.674,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.037 kJ/mol
""",
    rank = 5,
)

entry(
    index = 611,
    label = "C[C](CF)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4008,0.066393,-0.000268218,7.14372e-07,-6.47133e-10,-40382.9,11.4095], Tmin=(10,'K'), Tmax=(387.22,'K')),
            NASAPolynomial(coeffs=[0.797234,0.0490475,-2.9649e-05,8.57794e-09,-9.56571e-13,-39849.6,25.7827], Tmin=(387.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-335.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.905 kJ/mol
""",
    rank = 5,
)

entry(
    index = 612,
    label = "FCD[C]CCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u1 p0 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58086,0.0461404,-0.000152909,4.3049e-07,-4.16579e-10,-18016,12.0377], Tmin=(10,'K'), Tmax=(371.913,'K')),
            NASAPolynomial(coeffs=[1.46075,0.0418589,-2.64074e-05,7.92562e-09,-9.11214e-13,-17671,22.6872], Tmin=(371.913,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.811,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 613,
    label = "FC1DC[CH]C1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9427,0.00335575,9.57322e-05,-1.75807e-07,9.97692e-11,14179.7,9.76288], Tmin=(10,'K'), Tmax=(554.639,'K')),
            NASAPolynomial(coeffs=[1.27097,0.0349799,-2.32101e-05,7.32551e-09,-8.80744e-13,14286,19.3643], Tmin=(554.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (117.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 614,
    label = "CO[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88431,0.0195027,7.8825e-07,-1.12899e-08,4.5958e-12,-54204.3,8.4176], Tmin=(10,'K'), Tmax=(1091.3,'K')),
            NASAPolynomial(coeffs=[6.72241,0.0179635,-9.27891e-06,2.30241e-09,-2.22887e-13,-55351.5,-7.94076], Tmin=(1091.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-450.652,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.93 kJ/mol
""",
    rank = 5,
)

entry(
    index = 615,
    label = "FCOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97303,0.00163955,5.66317e-05,-1.06074e-07,6.25169e-11,-37414.2,8.78835], Tmin=(10,'K'), Tmax=(513.345,'K')),
            NASAPolynomial(coeffs=[2.18061,0.0206392,-1.3592e-05,4.22288e-09,-4.99041e-13,-37296.5,15.5946], Tmin=(513.345,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-311.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 616,
    label = "CC(O)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81951,0.0165671,0.000100171,-3.0845e-07,3.01557e-10,-33037.8,10.4755], Tmin=(10,'K'), Tmax=(260.687,'K')),
            NASAPolynomial(coeffs=[2.42328,0.037991,-2.31032e-05,6.80512e-09,-7.74982e-13,-32965,15.3344], Tmin=(260.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.685,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 617,
    label = "COC(F)D[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {3,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60572,0.0376517,-6.02092e-05,9.41533e-08,-6.68323e-11,-25731.9,10.3296], Tmin=(10,'K'), Tmax=(428.375,'K')),
            NASAPolynomial(coeffs=[3.85205,0.0307283,-1.97773e-05,6.03624e-09,-7.03743e-13,-25710.6,9.84517], Tmin=(428.375,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-213.957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.554 kJ/mol
""",
    rank = 5,
)

entry(
    index = 618,
    label = "FCD[C]C(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79104,0.0263788,-1.105e-05,-3.68758e-09,2.90749e-12,-39173.9,11.414], Tmin=(10,'K'), Tmax=(1050.43,'K')),
            NASAPolynomial(coeffs=[8.10078,0.0177452,-9.82798e-06,2.58581e-09,-2.63207e-13,-40508.4,-11.6326], Tmin=(1050.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-325.694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 619,
    label = "OC(F)DCDCF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u0 p0 c0 {4,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77273,0.0190463,5.23545e-05,-1.58834e-07,1.20788e-10,-42860.2,10.9488], Tmin=(10,'K'), Tmax=(473.403,'K')),
            NASAPolynomial(coeffs=[4.61778,0.0265791,-1.80057e-05,5.72253e-09,-6.87701e-13,-43104.6,5.76731], Tmin=(473.403,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-356.381,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 620,
    label = "[C]#CCCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9215,0.0204675,3.15045e-06,-1.2851e-08,4.69518e-12,37400.1,9.84043], Tmin=(10,'K'), Tmax=(1172.92,'K')),
            NASAPolynomial(coeffs=[7.53053,0.0191145,-9.12916e-06,2.09153e-09,-1.86975e-13,35799.9,-11.359], Tmin=(1172.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.001,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.179 kJ/mol
""",
    rank = 5,
)

entry(
    index = 621,
    label = "CDC(F)OF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91173,0.00542318,8.73276e-05,-1.90335e-07,1.22003e-10,-25030.8,9.71637], Tmin=(10,'K'), Tmax=(534.036,'K')),
            NASAPolynomial(coeffs=[4.04998,0.0233261,-1.61526e-05,5.25041e-09,-6.44143e-13,-25315.6,6.60767], Tmin=(534.036,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-208.147,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 622,
    label = "[O]C(F)OF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91831,0.00514514,7.785e-05,-1.76491e-07,1.17061e-10,-30540.5,10.5003], Tmin=(10,'K'), Tmax=(516.46,'K')),
            NASAPolynomial(coeffs=[4.04401,0.0206235,-1.4888e-05,4.8983e-09,-6.00323e-13,-30772.9,7.8527], Tmin=(516.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-253.952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 623,
    label = "CC(C)D[C]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,D} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75961,0.0195752,5.46863e-05,-1.492e-07,1.19911e-10,3279.66,8.12645], Tmin=(10,'K'), Tmax=(320.376,'K')),
            NASAPolynomial(coeffs=[2.49083,0.0354164,-1.94828e-05,5.13818e-09,-5.25089e-13,3360.96,12.8034], Tmin=(320.376,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.2349,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.447 kJ/mol
""",
    rank = 5,
)

entry(
    index = 624,
    label = "FCDCC(F)(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7626,0.0201702,6.55134e-05,-1.66224e-07,1.08534e-10,-100197,10.5195], Tmin=(10,'K'), Tmax=(549.417,'K')),
            NASAPolynomial(coeffs=[4.94342,0.0318592,-2.17837e-05,6.90604e-09,-8.24549e-13,-100633,2.7435], Tmin=(549.417,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-833.125,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.679 kJ/mol
""",
    rank = 5,
)

entry(
    index = 625,
    label = "FC1[C]DC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08948,-0.00866993,0.000113134,-2.07103e-07,1.21737e-10,35019,8.615], Tmin=(10,'K'), Tmax=(551.518,'K')),
            NASAPolynomial(coeffs=[2.56767,0.0201144,-1.34207e-05,4.22049e-09,-5.0257e-13,34917,12.6043], Tmin=(551.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (291.153,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 626,
    label = "CCCDCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89039,0.0181544,3.4428e-05,-5.03301e-08,1.87284e-11,-25459.4,8.69921], Tmin=(10,'K'), Tmax=(942.41,'K')),
            NASAPolynomial(coeffs=[3.0187,0.0370399,-1.98018e-05,5.13082e-09,-5.19888e-13,-25969.5,9.27512], Tmin=(942.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.251 kJ/mol
""",
    rank = 5,
)

entry(
    index = 627,
    label = "OD[C]C(DO)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88581,0.00872216,6.51059e-05,-2.1284e-07,1.90466e-10,-38687.8,10.1522], Tmin=(10,'K'), Tmax=(403.597,'K')),
            NASAPolynomial(coeffs=[4.86779,0.0139717,-1.00855e-05,3.33687e-09,-4.12754e-13,-38889.1,4.79407], Tmin=(403.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-321.666,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 628,
    label = "FC[C]1OO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8963,0.0145115,1.45626e-05,-3.11303e-08,1.38586e-11,-2153.5,9.51617], Tmin=(10,'K'), Tmax=(851.232,'K')),
            NASAPolynomial(coeffs=[5.10011,0.0190296,-1.1329e-05,3.18964e-09,-3.45004e-13,-2727.08,1.73705], Tmin=(851.232,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-17.8892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.976 kJ/mol
""",
    rank = 5,
)

entry(
    index = 629,
    label = "FC1OOC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92926,0.00420452,9.55818e-05,-1.86603e-07,1.10345e-10,-53468.6,9.9773], Tmin=(10,'K'), Tmax=(550.595,'K')),
            NASAPolynomial(coeffs=[2.25887,0.0318665,-2.20788e-05,7.07994e-09,-8.53378e-13,-53520,14.9019], Tmin=(550.595,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-444.591,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 630,
    label = "CC#C[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61494,0.0381247,-8.45387e-05,1.61406e-07,-1.21369e-10,14042,11.3501], Tmin=(10,'K'), Tmax=(432.787,'K')),
            NASAPolynomial(coeffs=[3.57638,0.0285996,-1.72772e-05,5.03974e-09,-5.68584e-13,14137.9,12.573], Tmin=(432.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.742,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.096 kJ/mol
""",
    rank = 5,
)

entry(
    index = 631,
    label = "FC1[CH]CC1F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91502,0.00516235,0.000132277,-2.58954e-07,1.5644e-10,-23352.2,11.2762], Tmin=(10,'K'), Tmax=(526.96,'K')),
            NASAPolynomial(coeffs=[1.1408,0.0440045,-2.89099e-05,9.00839e-09,-1.06974e-12,-23306.8,20.5401], Tmin=(526.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.192,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 632,
    label = "OD[C]C(F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84562,0.0159154,2.75125e-06,-1.87413e-08,9.9821e-12,-47229.3,10.927], Tmin=(10,'K'), Tmax=(796.551,'K')),
            NASAPolynomial(coeffs=[5.41171,0.0152162,-9.42485e-06,2.74211e-09,-3.04758e-13,-47706.1,2.30094], Tmin=(796.551,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-392.693,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.716 kJ/mol
""",
    rank = 5,
)

entry(
    index = 633,
    label = "FOCOC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85361,0.0321717,-9.84609e-06,-6.99663e-09,3.8105e-12,-86480.4,11.6676], Tmin=(10,'K'), Tmax=(1158.15,'K')),
            NASAPolynomial(coeffs=[10.9798,0.0199884,-1.01641e-05,2.45253e-09,-2.29386e-13,-88964.6,-27.3569], Tmin=(1158.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-718.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 634,
    label = "CDCC#CF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90856,0.00675158,0.000107737,-2.90148e-07,2.39208e-10,18938.5,9.19371], Tmin=(10,'K'), Tmax=(400.064,'K')),
            NASAPolynomial(coeffs=[3.44297,0.0255965,-1.61233e-05,4.91024e-09,-5.76552e-13,18862.2,9.59416], Tmin=(400.064,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.467,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.975 kJ/mol
""",
    rank = 5,
)

entry(
    index = 635,
    label = "C[C](C)C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {13,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45813,0.0580165,-0.000182998,4.64046e-07,-4.13014e-10,-46352.2,9.55774], Tmin=(10,'K'), Tmax=(395.549,'K')),
            NASAPolynomial(coeffs=[1.38756,0.0482197,-2.92921e-05,8.54193e-09,-9.60814e-13,-45947.9,20.666], Tmin=(395.549,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-385.412,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.748 kJ/mol
""",
    rank = 5,
)

entry(
    index = 636,
    label = "FCDC1CDC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 C u0 p0 c0 {3,S} {4,D} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92929,0.00414517,8.8437e-05,-1.71324e-07,1.00073e-10,24306.1,8.24948], Tmin=(10,'K'), Tmax=(565.304,'K')),
            NASAPolynomial(coeffs=[2.75296,0.0286025,-1.92692e-05,6.18135e-09,-7.54185e-13,24181.3,10.9735], Tmin=(565.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (202.063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.217 kJ/mol
""",
    rank = 5,
)

entry(
    index = 637,
    label = "ODCC(F)DCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92262,0.00843095,0.000177881,-8.0622e-07,1.24668e-09,-52335.5,10.2105], Tmin=(10,'K'), Tmax=(162.919,'K')),
            NASAPolynomial(coeffs=[3.04381,0.0300079,-2.0783e-05,6.73134e-09,-8.22846e-13,-52306.9,12.8556], Tmin=(162.919,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-435.028,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 638,
    label = "FCC1[CH]C1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96461,0.00229596,0.000124993,-2.39262e-07,1.49119e-10,7259.45,10.5317], Tmin=(10,'K'), Tmax=(412.386,'K')),
            NASAPolynomial(coeffs=[-0.410271,0.0446541,-2.87999e-05,8.91128e-09,-1.05704e-12,7620.93,27.7706], Tmin=(412.386,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.3526,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.993 kJ/mol
""",
    rank = 5,
)

entry(
    index = 639,
    label = "[O]C#CC(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76654,0.0222306,3.98813e-07,-2.45124e-08,1.47504e-11,-31811.8,11.5575], Tmin=(10,'K'), Tmax=(739.623,'K')),
            NASAPolynomial(coeffs=[5.96794,0.01944,-1.24273e-05,3.71076e-09,-4.2125e-13,-32386.7,-0.0843771], Tmin=(739.623,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-264.518,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.034 kJ/mol
""",
    rank = 5,
)

entry(
    index = 640,
    label = "OCC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88009,0.010189,6.30742e-05,-1.22784e-07,7.00266e-11,-79984.3,9.79854], Tmin=(10,'K'), Tmax=(565.33,'K')),
            NASAPolynomial(coeffs=[2.31547,0.0312628,-1.93831e-05,5.75396e-09,-6.56481e-13,-79967.2,15.0408], Tmin=(565.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-665.048,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.418 kJ/mol
""",
    rank = 5,
)

entry(
    index = 641,
    label = "FC1[CH]OC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91604,0.00510319,0.000111084,-2.24264e-07,1.37444e-10,-39739,11.1815], Tmin=(10,'K'), Tmax=(532.847,'K')),
            NASAPolynomial(coeffs=[2.30452,0.035107,-2.37864e-05,7.54448e-09,-9.04706e-13,-39821.4,15.5563], Tmin=(532.847,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-330.438,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 642,
    label = "FC#CCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,T}
3  C u0 p0 c0 {2,T} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63307,0.0329428,-4.43297e-06,-2.38791e-08,1.46535e-11,-45630.9,11.9823], Tmin=(10,'K'), Tmax=(754.587,'K')),
            NASAPolynomial(coeffs=[5.90564,0.030459,-1.85054e-05,5.34854e-09,-5.94052e-13,-46246.1,-0.145701], Tmin=(754.587,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-379.433,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.122 kJ/mol
""",
    rank = 5,
)

entry(
    index = 643,
    label = "CDCC(F)OF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76236,0.0222762,3.20353e-05,-7.28322e-08,3.81747e-11,-29663.8,10.7259], Tmin=(10,'K'), Tmax=(686.427,'K')),
            NASAPolynomial(coeffs=[4.13751,0.0332025,-2.04948e-05,6.01438e-09,-6.76964e-13,-30024.2,6.80696], Tmin=(686.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-246.664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 644,
    label = "ODC[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96505,0.0022331,6.11099e-05,-1.25957e-07,8.13176e-11,-22519.3,8.77893], Tmin=(10,'K'), Tmax=(483.098,'K')),
            NASAPolynomial(coeffs=[2.69324,0.0193497,-1.24864e-05,3.82493e-09,-4.47694e-13,-22473.3,13.1939], Tmin=(483.098,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-187.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.527 kJ/mol
""",
    rank = 5,
)

entry(
    index = 645,
    label = "ODC[CH]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97122,0.0018237,9.05724e-05,-1.69884e-07,1.03512e-10,-26497.1,10.1988], Tmin=(10,'K'), Tmax=(423.226,'K')),
            NASAPolynomial(coeffs=[0.636188,0.0333685,-2.13163e-05,6.50097e-09,-7.60038e-13,-26215,23.4182], Tmin=(423.226,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.317,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.164 kJ/mol
""",
    rank = 5,
)

entry(
    index = 646,
    label = "CC1[CH]C1F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93605,0.0039616,0.000124095,-2.40765e-07,1.47226e-10,6964.33,9.16379], Tmin=(10,'K'), Tmax=(502.355,'K')),
            NASAPolynomial(coeffs=[0.696115,0.0420951,-2.6602e-05,8.10272e-09,-9.50063e-13,7134.2,21.0149], Tmin=(502.355,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.8849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 647,
    label = "CCC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {13,S}
4  F u0 p3 c0 {3,S}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71968,0.0342913,-1.95427e-07,-1.67704e-08,6.8098e-12,-40425.9,11.53], Tmin=(10,'K'), Tmax=(1095.39,'K')),
            NASAPolynomial(coeffs=[7.23044,0.0341752,-1.74331e-05,4.3085e-09,-4.1748e-13,-41957.2,-9.2062], Tmin=(1095.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-336.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 648,
    label = "OC(O)D[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {7,S}
4 C u1 p0 c0 {2,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90695,0.00571058,8.71273e-05,-1.92129e-07,1.2372e-10,-27529.4,10.1114], Tmin=(10,'K'), Tmax=(536.614,'K')),
            NASAPolynomial(coeffs=[4.36592,0.0223591,-1.55113e-05,5.08201e-09,-6.28496e-13,-27867.6,5.49041], Tmin=(536.614,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-228.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.598 kJ/mol
""",
    rank = 5,
)

entry(
    index = 649,
    label = "CC([CH]F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70788,0.0335403,1.52745e-06,-1.81934e-08,7.23084e-12,-39253.8,11.3964], Tmin=(10,'K'), Tmax=(1088.91,'K')),
            NASAPolynomial(coeffs=[6.79199,0.0349398,-1.79343e-05,4.45668e-09,-4.33969e-13,-40680.1,-7.21034], Tmin=(1088.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-326.364,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.588 kJ/mol
""",
    rank = 5,
)

entry(
    index = 650,
    label = "FCC1CDC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {3,S} {4,D} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95264,0.00290541,0.000107762,-2.01633e-07,1.19719e-10,6191.17,9.90525], Tmin=(10,'K'), Tmax=(502.794,'K')),
            NASAPolynomial(coeffs=[0.473066,0.0389993,-2.50138e-05,7.69369e-09,-9.0763e-13,6434.74,23.2423], Tmin=(502.794,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (51.4608,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.55 kJ/mol
""",
    rank = 5,
)

entry(
    index = 651,
    label = "[CH]DCCOF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80222,0.0173946,3.77467e-05,-8.38441e-08,4.73369e-11,25808.7,10.5732], Tmin=(10,'K'), Tmax=(610.759,'K')),
            NASAPolynomial(coeffs=[3.46048,0.030002,-1.86828e-05,5.54839e-09,-6.32129e-13,25657.1,10.4702], Tmin=(610.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (214.558,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 652,
    label = "[CH2]CC(O)F",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  O u0 p2 c0 {5,S} {11,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90456,0.00918345,0.000183457,-6.29805e-07,7.30086e-10,-37268.1,10.3155], Tmin=(10,'K'), Tmax=(218.017,'K')),
            NASAPolynomial(coeffs=[2.25307,0.0394837,-2.50149e-05,7.67128e-09,-9.05343e-13,-37196.1,15.7674], Tmin=(218.017,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-309.837,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 653,
    label = "FC1(F)CDC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {4,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94448,0.00306951,7.29411e-05,-1.29576e-07,6.89268e-11,-19609.7,7.87002], Tmin=(10,'K'), Tmax=(615.997,'K')),
            NASAPolynomial(coeffs=[2.21476,0.0278031,-2.01643e-05,6.76967e-09,-8.49163e-13,-19652.8,13.2976], Tmin=(615.997,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.071,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.672 kJ/mol
""",
    rank = 5,
)

entry(
    index = 654,
    label = "C[C](F)CDCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84998,0.0158396,0.000192153,-8.70835e-07,1.3301e-09,-33204,9.95496], Tmin=(10,'K'), Tmax=(165.018,'K')),
            NASAPolynomial(coeffs=[2.86307,0.0397623,-2.53061e-05,7.70426e-09,-8.99082e-13,-33171.4,12.9381], Tmin=(165.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-275.954,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 655,
    label = "C#CC(DO)F",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91133,0.005581,7.53935e-05,-1.76898e-07,1.19612e-10,-16780.6,9.23933], Tmin=(10,'K'), Tmax=(519.096,'K')),
            NASAPolynomial(coeffs=[4.7754,0.0173868,-1.20758e-05,3.96027e-09,-4.91249e-13,-17119.1,3.24107], Tmin=(519.096,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-139.548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.506 kJ/mol
""",
    rank = 5,
)

entry(
    index = 656,
    label = "FCC(F)COF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  O u0 p2 c0 {5,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77063,0.0359819,-6.72613e-06,-1.16573e-08,5.38962e-12,-64098.4,11.3411], Tmin=(10,'K'), Tmax=(1127.49,'K')),
            NASAPolynomial(coeffs=[9.75548,0.0282688,-1.44506e-05,3.54476e-09,-3.39196e-13,-66307.3,-22.0612], Tmin=(1127.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-532.904,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 657,
    label = "CDCDC(O)F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {8,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8969,0.00693732,0.000105016,-2.57616e-07,1.88285e-10,-20149.8,9.55278], Tmin=(10,'K'), Tmax=(464.777,'K')),
            NASAPolynomial(coeffs=[3.95777,0.0255104,-1.6559e-05,5.17309e-09,-6.19232e-13,-20361.7,7.08679], Tmin=(464.777,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-167.551,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 658,
    label = "CC1DC(F)[CH]1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {2,S} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83102,0.0144471,4.33119e-05,-8.86218e-08,4.95386e-11,29460.8,9.07553], Tmin=(10,'K'), Tmax=(586.772,'K')),
            NASAPolynomial(coeffs=[2.65056,0.030617,-1.87888e-05,5.52654e-09,-6.25817e-13,29459.5,12.9497], Tmin=(586.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (244.927,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.891 kJ/mol
""",
    rank = 5,
)

entry(
    index = 659,
    label = "F[C]1CDC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09467,-0.009076,0.000115817,-2.11e-07,1.23168e-10,33065.8,7.94871], Tmin=(10,'K'), Tmax=(557.769,'K')),
            NASAPolynomial(coeffs=[2.64819,0.0201657,-1.35653e-05,4.29146e-09,-5.13039e-13,32933.7,11.4516], Tmin=(557.769,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (274.913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.921 kJ/mol
""",
    rank = 5,
)

entry(
    index = 660,
    label = "FCCDC(F)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70371,0.0372355,-2.22479e-05,3.6115e-09,7.4118e-13,-50237.3,11.7923], Tmin=(10,'K'), Tmax=(1170.59,'K')),
            NASAPolynomial(coeffs=[10.8244,0.0205955,-1.07817e-05,2.6948e-09,-2.61885e-13,-52431.4,-25.9335], Tmin=(1170.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-417.683,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 661,
    label = "OOCDC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71524,0.0243533,3.31954e-05,-1.28117e-07,1.01402e-10,-50139.2,10.9626], Tmin=(10,'K'), Tmax=(483.024,'K')),
            NASAPolynomial(coeffs=[5.30721,0.0259708,-1.77905e-05,5.69109e-09,-6.86596e-13,-50465.6,2.65339], Tmin=(483.024,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-416.907,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.955 kJ/mol
""",
    rank = 5,
)

entry(
    index = 662,
    label = "OCOCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90929,0.0173395,2.07963e-05,-3.33746e-08,1.23474e-11,-72940.7,9.65965], Tmin=(10,'K'), Tmax=(988.748,'K')),
            NASAPolynomial(coeffs=[4.48429,0.027895,-1.47594e-05,3.77531e-09,-3.77369e-13,-73684.1,3.70797], Tmin=(988.748,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-606.425,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 663,
    label = "CDC(O)[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {9,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8864,0.00698382,0.00011336,-2.46685e-07,1.58507e-10,-25446.9,9.86318], Tmin=(10,'K'), Tmax=(533.1,'K')),
            NASAPolynomial(coeffs=[4.15396,0.0296093,-1.96128e-05,6.28118e-09,-7.69863e-13,-25825.4,5.45766], Tmin=(533.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.615,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 664,
    label = "F[CH]C1CC1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94461,0.00329628,0.000116847,-2.11461e-07,1.20446e-10,1605.49,10.2867], Tmin=(10,'K'), Tmax=(530.94,'K')),
            NASAPolynomial(coeffs=[-0.0763225,0.0442035,-2.87103e-05,8.95849e-09,-1.07074e-12,1882.85,25.7308], Tmin=(530.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.3272,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.965 kJ/mol
""",
    rank = 5,
)

entry(
    index = 665,
    label = "CCCOF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86858,0.0217103,2.30896e-05,-3.70102e-08,1.33957e-11,-19675.8,8.65082], Tmin=(10,'K'), Tmax=(1011.46,'K')),
            NASAPolynomial(coeffs=[4.34229,0.0346309,-1.80109e-05,4.5401e-09,-4.48309e-13,-20528.3,2.6192], Tmin=(1011.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 666,
    label = "OC(F)COF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  O u0 p2 c0 {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7033,0.0273949,1.1199e-05,-4.19684e-08,2.23504e-11,-61299.9,11.17], Tmin=(10,'K'), Tmax=(735.615,'K')),
            NASAPolynomial(coeffs=[4.98389,0.0313118,-1.89743e-05,5.48347e-09,-6.09462e-13,-61782.7,3.38418], Tmin=(735.615,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-509.703,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 667,
    label = "[O]OC#CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85927,0.0106223,7.3696e-05,-2.57433e-07,2.36528e-10,28966.1,9.83445], Tmin=(10,'K'), Tmax=(406.358,'K')),
            NASAPolynomial(coeffs=[5.75801,0.0125018,-9.1719e-06,3.08903e-09,-3.88267e-13,28641.9,0.294273], Tmin=(406.358,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (240.841,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.032 kJ/mol
""",
    rank = 5,
)

entry(
    index = 668,
    label = "FC1D[C]CC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07283,-0.00662215,0.000127953,-2.12221e-07,1.12426e-10,24476.1,9.7892], Tmin=(10,'K'), Tmax=(596.089,'K')),
            NASAPolynomial(coeffs=[0.580722,0.0349285,-2.21949e-05,6.69267e-09,-7.70682e-13,24570.6,22.1301], Tmin=(596.089,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.496,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 669,
    label = "F[C]1CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08323,-0.00730834,9.34073e-05,-1.56062e-07,8.36418e-11,-6345.61,8.78156], Tmin=(10,'K'), Tmax=(598.088,'K')),
            NASAPolynomial(coeffs=[2.09748,0.020651,-1.35285e-05,4.17073e-09,-4.87869e-13,-6370.62,15.1462], Tmin=(598.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-52.7656,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.198 kJ/mol
""",
    rank = 5,
)

entry(
    index = 670,
    label = "[O]OCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98061,0.00133001,6.2593e-05,-1.31515e-07,9.07287e-11,-23997.1,9.65682], Tmin=(10,'K'), Tmax=(371.237,'K')),
            NASAPolynomial(coeffs=[2.24888,0.0199891,-1.28003e-05,3.87685e-09,-4.48259e-13,-23868.5,16.2954], Tmin=(371.237,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-199.524,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 671,
    label = "FC1OO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07977,-0.00679951,7.82002e-05,-1.28316e-07,6.72361e-11,-29891.3,8.13429], Tmin=(10,'K'), Tmax=(617.786,'K')),
            NASAPolynomial(coeffs=[2.55736,0.0165448,-1.12274e-05,3.52568e-09,-4.16455e-13,-29960.6,12.6628], Tmin=(617.786,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-248.533,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.579 kJ/mol
""",
    rank = 5,
)

entry(
    index = 672,
    label = "COCOF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63806,0.0394786,-0.000131542,3.5346e-07,-3.23053e-10,-30441.6,8.92092], Tmin=(10,'K'), Tmax=(394.176,'K')),
            NASAPolynomial(coeffs=[1.55972,0.0355533,-2.14101e-05,6.1921e-09,-6.91466e-13,-30083.5,19.478], Tmin=(394.176,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-253.12,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 673,
    label = "FCDCCDCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8288,0.0191538,3.37549e-05,-6.41545e-08,2.97022e-11,-34780.1,9.9138], Tmin=(10,'K'), Tmax=(770.401,'K')),
            NASAPolynomial(coeffs=[4.00537,0.0323235,-1.93138e-05,5.50237e-09,-6.03672e-13,-35225.3,6.39495], Tmin=(770.401,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.178,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.245 kJ/mol
""",
    rank = 5,
)

entry(
    index = 674,
    label = "FCDCOC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81772,0.0302858,-2.85565e-06,-1.57053e-08,7.29364e-12,-89374.1,12.0397], Tmin=(10,'K'), Tmax=(1034.53,'K')),
            NASAPolynomial(coeffs=[8.85448,0.0241443,-1.3283e-05,3.47203e-09,-3.51123e-13,-91129.7,-15.8791], Tmin=(1034.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-743.052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.738 kJ/mol
""",
    rank = 5,
)

entry(
    index = 675,
    label = "C[C]1OC1(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81921,0.015294,6.5262e-05,-1.47239e-07,9.13198e-11,-40748.6,9.96361], Tmin=(10,'K'), Tmax=(552.33,'K')),
            NASAPolynomial(coeffs=[3.63565,0.0318048,-2.08066e-05,6.40999e-09,-7.50766e-13,-40959.9,8.64389], Tmin=(552.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-338.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.979 kJ/mol
""",
    rank = 5,
)

entry(
    index = 676,
    label = "FCC1D[C]C1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85976,0.0227271,6.43309e-06,-2.2319e-08,9.4087e-12,8598.14,11.2432], Tmin=(10,'K'), Tmax=(982.443,'K')),
            NASAPolynomial(coeffs=[6.72654,0.0232281,-1.29179e-05,3.42421e-09,-3.51485e-13,7447.38,-5.52641], Tmin=(982.443,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (71.5255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.779 kJ/mol
""",
    rank = 5,
)

entry(
    index = 677,
    label = "C[CH]CDC(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63859,0.0306669,5.79336e-06,-3.39422e-08,1.82943e-11,-33288.8,10.3642], Tmin=(10,'K'), Tmax=(729.758,'K')),
            NASAPolynomial(coeffs=[4.23774,0.035571,-2.11176e-05,6.01785e-09,-6.62598e-13,-33594.3,6.16851], Tmin=(729.758,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.82,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.999 kJ/mol
""",
    rank = 5,
)

entry(
    index = 678,
    label = "FCD[C]CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88769,0.0202311,-2.10066e-06,-7.71563e-09,3.20926e-12,-13461.2,10.1289], Tmin=(10,'K'), Tmax=(1170.78,'K')),
            NASAPolynomial(coeffs=[7.5455,0.0162869,-8.00505e-06,1.8861e-09,-1.73402e-13,-14903.8,-10.598], Tmin=(1170.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-111.896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 679,
    label = "OC#COF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82099,0.0141229,8.4777e-05,-3.15346e-07,3.05281e-10,7089.43,9.74134], Tmin=(10,'K'), Tmax=(386.131,'K')),
            NASAPolynomial(coeffs=[5.83897,0.016047,-1.13798e-05,3.78424e-09,-4.72886e-13,6763.41,-0.277711], Tmin=(386.131,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (58.956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.119 kJ/mol
""",
    rank = 5,
)

entry(
    index = 680,
    label = "CDC(F)C([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
5 O u1 p2 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81172,0.0163088,6.27834e-05,-1.41971e-07,8.64663e-11,-40969.4,11.7322], Tmin=(10,'K'), Tmax=(571.11,'K')),
            NASAPolynomial(coeffs=[4.00598,0.0315353,-2.07738e-05,6.42132e-09,-7.53095e-13,-41262.1,8.53556], Tmin=(571.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-340.672,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 681,
    label = "ODCDCC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78677,0.0188667,3.00048e-05,-7.87197e-08,4.73509e-11,-58621.8,11.0382], Tmin=(10,'K'), Tmax=(605.759,'K')),
            NASAPolynomial(coeffs=[4.51597,0.0259129,-1.68147e-05,5.13205e-09,-5.95775e-13,-58927.7,6.08945], Tmin=(605.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-487.439,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.72 kJ/mol
""",
    rank = 5,
)

entry(
    index = 682,
    label = "C#CC(F)(F)[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {9,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 C u1 p0 c0 {3,S} {7,S} {8,S}
7 H u0 p0 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71848,0.0213989,0.000138301,-4.53184e-07,3.97637e-10,-26371.4,12.325], Tmin=(10,'K'), Tmax=(417.1,'K')),
            NASAPolynomial(coeffs=[6.49078,0.0303793,-2.19029e-05,7.3163e-09,-9.13404e-13,-26912.1,-2.33431], Tmin=(417.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-219.267,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 683,
    label = "[O]C(F)CDCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80505,0.0221626,1.7485e-05,-4.39644e-08,2.10196e-11,-40536.8,11.7834], Tmin=(10,'K'), Tmax=(803.321,'K')),
            NASAPolynomial(coeffs=[5.47682,0.0270852,-1.64419e-05,4.71845e-09,-5.19174e-13,-41232.8,1.42384], Tmin=(803.321,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-337.039,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 684,
    label = "CC(F)[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  O u0 p2 c0 {4,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89725,0.00896326,0.000137251,-3.70558e-07,3.29738e-10,-36142.8,10.3669], Tmin=(10,'K'), Tmax=(285.872,'K')),
            NASAPolynomial(coeffs=[1.6889,0.0398619,-2.48709e-05,7.5055e-09,-8.72971e-13,-36016.5,18.2556], Tmin=(285.872,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-300.495,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 685,
    label = "FCOOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85415,0.0172238,7.59977e-06,-2.45159e-08,1.16542e-11,-31714.6,9.83122], Tmin=(10,'K'), Tmax=(845.185,'K')),
            NASAPolynomial(coeffs=[5.50911,0.0185939,-1.11639e-05,3.16701e-09,-3.44756e-13,-32323,0.180953], Tmin=(845.185,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-263.683,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 686,
    label = "CCC([O])(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  O u1 p2 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  F u0 p3 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78923,0.0176221,8.08405e-05,-1.81529e-07,1.15551e-10,-62198,10.3362], Tmin=(10,'K'), Tmax=(519.013,'K')),
            NASAPolynomial(coeffs=[2.66756,0.0403878,-2.57661e-05,7.8276e-09,-9.09608e-13,-62271.7,13.1797], Tmin=(519.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-517.173,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.333 kJ/mol
""",
    rank = 5,
)

entry(
    index = 687,
    label = "ODC(F)CCF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90806,0.0252153,9.27679e-07,-1.32043e-08,5.06605e-12,-79293.4,10.542], Tmin=(10,'K'), Tmax=(1174.63,'K')),
            NASAPolynomial(coeffs=[8.84518,0.021156,-1.01745e-05,2.33991e-09,-2.09536e-13,-81333,-17.8164], Tmin=(1174.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-659.233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.44 kJ/mol
""",
    rank = 5,
)

entry(
    index = 688,
    label = "FC1C[CH]O1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u0 p2 c0 {2,S} {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03376,-0.00346145,0.000114866,-1.90379e-07,9.95469e-11,-17582.4,10.0142], Tmin=(10,'K'), Tmax=(606.363,'K')),
            NASAPolynomial(coeffs=[0.756028,0.0351251,-2.25538e-05,6.84639e-09,-7.91183e-13,-17496.8,21.616], Tmin=(606.363,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-146.202,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.903 kJ/mol
""",
    rank = 5,
)

entry(
    index = 689,
    label = "OOC(F)CF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68866,0.0307416,-7.39441e-06,-1.12005e-08,6.26062e-12,-69872.1,10.8474], Tmin=(10,'K'), Tmax=(934.787,'K')),
            NASAPolynomial(coeffs=[6.49323,0.0272099,-1.53175e-05,4.14226e-09,-4.34721e-13,-70766.5,-4.47315], Tmin=(934.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-580.96,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 690,
    label = "FC#COC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63467,0.0318325,-6.52663e-06,-3.85715e-08,3.1696e-11,-53452.6,11.9127], Tmin=(10,'K'), Tmax=(590.073,'K')),
            NASAPolynomial(coeffs=[6.40288,0.0243955,-1.64184e-05,5.13923e-09,-6.07499e-13,-53976.5,-1.65314], Tmin=(590.073,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-444.475,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.006 kJ/mol
""",
    rank = 5,
)

entry(
    index = 691,
    label = "FCC1CDC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {3,S} {4,D} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83614,0.0172914,4.37762e-05,-8.14246e-08,3.93322e-11,-13871.5,10.7986], Tmin=(10,'K'), Tmax=(720.503,'K')),
            NASAPolynomial(coeffs=[3.49795,0.0336572,-2.04581e-05,5.91923e-09,-6.58201e-13,-14198.8,9.70955], Tmin=(720.503,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.343,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.058 kJ/mol
""",
    rank = 5,
)

entry(
    index = 692,
    label = "[O]C(DO)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05923,-0.00575269,7.32109e-05,-1.34544e-07,7.81605e-11,-45632,8.90938], Tmin=(10,'K'), Tmax=(570.176,'K')),
            NASAPolynomial(coeffs=[3.48218,0.0118365,-8.68516e-06,2.86324e-09,-3.49671e-13,-45786.3,9.4389], Tmin=(570.176,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-379.415,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 693,
    label = "CDCC(F)(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89321,0.00668269,0.000118506,-2.5788e-07,1.67762e-10,-77711.2,9.58715], Tmin=(10,'K'), Tmax=(515.917,'K')),
            NASAPolynomial(coeffs=[3.34086,0.03305,-2.2366e-05,7.12677e-09,-8.6023e-13,-77948.2,9.03784], Tmin=(515.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-646.16,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.84 kJ/mol
""",
    rank = 5,
)

entry(
    index = 694,
    label = "[CH2]OC(O)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 O u0 p2 c0 {5,S} {9,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85494,0.0119109,0.000107495,-3.11122e-07,2.7015e-10,-52299.7,10.3472], Tmin=(10,'K'), Tmax=(378.477,'K')),
            NASAPolynomial(coeffs=[3.32459,0.0308012,-2.00251e-05,6.24224e-09,-7.44036e-13,-52354.7,11.1335], Tmin=(378.477,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-434.835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.229 kJ/mol
""",
    rank = 5,
)

entry(
    index = 695,
    label = "CDC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u1 p2 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95357,0.00266334,5.79358e-05,-1.0892e-07,6.1561e-11,-31756.1,8.62817], Tmin=(10,'K'), Tmax=(584.543,'K')),
            NASAPolynomial(coeffs=[3.07806,0.0195599,-1.34071e-05,4.36224e-09,-5.38143e-13,-31840,10.7882], Tmin=(584.543,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-264.055,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.153 kJ/mol
""",
    rank = 5,
)

entry(
    index = 696,
    label = "CC(F)DC[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81786,0.0180847,0.000128356,-4.62076e-07,5.35091e-10,-32840.4,10.0979], Tmin=(10,'K'), Tmax=(219.291,'K')),
            NASAPolynomial(coeffs=[2.57821,0.0406966,-2.63143e-05,8.13321e-09,-9.61558e-13,-32786,14.1975], Tmin=(219.291,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-273.024,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 697,
    label = "FCOC(F)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50037,0.0554385,-0.000197942,5.63912e-07,-5.52672e-10,-103131,12.1155], Tmin=(10,'K'), Tmax=(363.721,'K')),
            NASAPolynomial(coeffs=[1.22617,0.0476547,-3.0598e-05,9.29598e-09,-1.07813e-12,-102749,23.7691], Tmin=(363.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-857.503,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.065 kJ/mol
""",
    rank = 5,
)

entry(
    index = 698,
    label = "CD[C]CDC(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72006,0.0250253,5.04193e-05,-1.95496e-07,1.78845e-10,-9829.54,11.2664], Tmin=(10,'K'), Tmax=(395.479,'K')),
            NASAPolynomial(coeffs=[4.40346,0.0309526,-2.07604e-05,6.585e-09,-7.92845e-13,-9984,7.33391], Tmin=(395.479,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.7246,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.93 kJ/mol
""",
    rank = 5,
)

entry(
    index = 699,
    label = "FC#CC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80225,0.016177,5.33131e-05,-1.63963e-07,1.28949e-10,-38890.6,10.8784], Tmin=(10,'K'), Tmax=(457.931,'K')),
            NASAPolynomial(coeffs=[4.65561,0.0230294,-1.5995e-05,5.16109e-09,-6.265e-13,-39118.8,5.79013], Tmin=(457.931,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-323.371,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.46 kJ/mol
""",
    rank = 5,
)

entry(
    index = 700,
    label = "F[CH]CDCCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78995,0.0263378,1.32014e-05,-3.33459e-08,1.40509e-11,-30460.8,11.3174], Tmin=(10,'K'), Tmax=(926.199,'K')),
            NASAPolynomial(coeffs=[5.60104,0.0320337,-1.79149e-05,4.80867e-09,-5.01023e-13,-31376.1,-0.411247], Tmin=(926.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-253.244,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.353 kJ/mol
""",
    rank = 5,
)

entry(
    index = 701,
    label = "OC1CDC1F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91896,0.00489611,9.31951e-05,-1.91622e-07,1.18095e-10,-9369.41,9.28746], Tmin=(10,'K'), Tmax=(542.859,'K')),
            NASAPolynomial(coeffs=[3.28123,0.0274267,-1.83318e-05,5.84884e-09,-7.10554e-13,-9562.92,9.55451], Tmin=(542.859,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.9312,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.163 kJ/mol
""",
    rank = 5,
)

entry(
    index = 702,
    label = "FC1(F)[C]DC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,D}
5 C u0 p0 c0 {2,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93775,0.003487,6.61767e-05,-1.25064e-07,6.9323e-11,8876.96,9.31967], Tmin=(10,'K'), Tmax=(611.753,'K')),
            NASAPolynomial(coeffs=[3.45785,0.021872,-1.62882e-05,5.5449e-09,-7.01129e-13,8650.37,9.0672], Tmin=(611.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.779,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 703,
    label = "OC1D[C]C1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91332,0.00569382,8.89284e-05,-2.09024e-07,1.4622e-10,15405.7,10.1257], Tmin=(10,'K'), Tmax=(483.006,'K')),
            NASAPolynomial(coeffs=[3.76931,0.0231329,-1.56839e-05,5.00601e-09,-6.04303e-13,15230.1,8.75391], Tmin=(483.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (128.072,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 704,
    label = "CCCC(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {14,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86857,0.0270092,2.52684e-05,-4.14453e-08,1.47872e-11,-67777.2,9.61536], Tmin=(10,'K'), Tmax=(1044.65,'K')),
            NASAPolynomial(coeffs=[5.42118,0.0399706,-2.04906e-05,5.08179e-09,-4.93584e-13,-69133.2,-2.88054], Tmin=(1044.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-563.472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.912 kJ/mol
""",
    rank = 5,
)

entry(
    index = 705,
    label = "OCCDCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81569,0.0159752,4.31009e-05,-8.40649e-08,4.4521e-11,-40421.1,9.75838], Tmin=(10,'K'), Tmax=(614.523,'K')),
            NASAPolynomial(coeffs=[2.27198,0.0339954,-2.03442e-05,5.87396e-09,-6.55905e-13,-40381.9,15.2295], Tmin=(614.523,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-336.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.825 kJ/mol
""",
    rank = 5,
)

entry(
    index = 706,
    label = "FC1DC[CH]1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9642,0.00199421,5.45987e-05,-9.52508e-08,5.04834e-11,35215.6,8.1351], Tmin=(10,'K'), Tmax=(603.589,'K')),
            NASAPolynomial(coeffs=[2.25621,0.0217235,-1.53324e-05,5.07373e-09,-6.31593e-13,35268.6,14.2438], Tmin=(603.589,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (292.782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.707 kJ/mol
""",
    rank = 5,
)

entry(
    index = 707,
    label = "CC1(F)OC1F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90637,0.00624087,0.000131725,-2.95025e-07,2.04294e-10,-66044.6,9.22578], Tmin=(10,'K'), Tmax=(462.785,'K')),
            NASAPolynomial(coeffs=[2.1378,0.0380444,-2.48948e-05,7.71579e-09,-9.10811e-13,-66057.8,14.4845], Tmin=(462.785,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-549.142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.486 kJ/mol
""",
    rank = 5,
)

entry(
    index = 708,
    label = "C[C](F)C(O)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  O u0 p2 c0 {4,S} {11,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63696,0.0324905,-1.04572e-06,-2.36678e-08,1.27853e-11,-62049.9,11.6821], Tmin=(10,'K'), Tmax=(802.141,'K')),
            NASAPolynomial(coeffs=[5.21905,0.0334776,-1.94906e-05,5.45744e-09,-5.91668e-13,-62589.3,2.61823], Tmin=(802.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-515.944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 709,
    label = "ODCDCCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8499,0.0151734,1.92308e-05,-3.84689e-08,1.7641e-11,-32010.9,9.74967], Tmin=(10,'K'), Tmax=(780.601,'K')),
            NASAPolynomial(coeffs=[3.80664,0.0239338,-1.40111e-05,3.93429e-09,-4.27227e-13,-32264.3,8.2813], Tmin=(780.601,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-266.159,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.541 kJ/mol
""",
    rank = 5,
)

entry(
    index = 710,
    label = "OC(F)C#CF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82637,0.0131988,0.000112869,-3.43949e-07,2.97157e-10,-35911.2,10.7837], Tmin=(10,'K'), Tmax=(407.521,'K')),
            NASAPolynomial(coeffs=[4.8032,0.0261667,-1.78866e-05,5.77235e-09,-7.04707e-13,-36178.2,4.64999], Tmin=(407.521,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-298.581,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 711,
    label = "[CH]DC(F)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80789,0.0130075,0.000133329,-3.58712e-07,2.70482e-10,-67993.8,11.2171], Tmin=(10,'K'), Tmax=(473.808,'K')),
            NASAPolynomial(coeffs=[5.92256,0.0284836,-2.11786e-05,7.14667e-09,-8.93831e-13,-68568.3,-1.35325], Tmin=(473.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-565.365,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 712,
    label = "FOCCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79908,0.0342724,-1.22963e-06,-1.75545e-08,7.47032e-12,-69673.5,11.8323], Tmin=(10,'K'), Tmax=(1087.46,'K')),
            NASAPolynomial(coeffs=[9.18808,0.0294947,-1.53913e-05,3.84911e-09,-3.74903e-13,-71735.1,-18.7085], Tmin=(1087.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-579.248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 713,
    label = "CDCCF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99084,0.000348412,8.67086e-05,-1.4953e-07,8.43489e-11,-21038.8,8.58638], Tmin=(10,'K'), Tmax=(456.482,'K')),
            NASAPolynomial(coeffs=[0.300586,0.0326839,-1.95424e-05,5.6385e-09,-6.29208e-13,-20701.9,23.4959], Tmin=(456.482,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-174.934,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.452 kJ/mol
""",
    rank = 5,
)

entry(
    index = 714,
    label = "CCC([O])F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  O u1 p2 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83516,0.0167669,4.34903e-05,-7.31999e-08,3.28393e-11,-35248,10.4209], Tmin=(10,'K'), Tmax=(752.787,'K')),
            NASAPolynomial(coeffs=[2.30688,0.0371446,-2.15377e-05,6.01816e-09,-6.5204e-13,-35365.2,15.0532], Tmin=(752.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-293.074,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 715,
    label = "CDC([O])OF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u1 p2 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8868,0.00744281,9.6534e-05,-2.39858e-07,1.72355e-10,-11466.3,10.1218], Tmin=(10,'K'), Tmax=(486.446,'K')),
            NASAPolynomial(coeffs=[4.76779,0.0219179,-1.5075e-05,4.88658e-09,-5.99067e-13,-11809,3.86501], Tmin=(486.446,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.3602,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 716,
    label = "CC1[C](F)C1F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76809,0.0195943,5.64232e-05,-1.18356e-07,6.6929e-11,-14872.2,10.0983], Tmin=(10,'K'), Tmax=(587.711,'K')),
            NASAPolynomial(coeffs=[2.50245,0.0398116,-2.47916e-05,7.36234e-09,-8.39036e-13,-14923.8,13.8267], Tmin=(587.711,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-123.688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 717,
    label = "C[CH]C(O)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  O u0 p2 c0 {4,S} {11,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72436,0.0263544,8.78043e-06,-2.7647e-08,1.21629e-11,-37885.7,10.9821], Tmin=(10,'K'), Tmax=(880.134,'K')),
            NASAPolynomial(coeffs=[4.34265,0.0328919,-1.82923e-05,4.92653e-09,-5.17084e-13,-38356.5,6.02138], Tmin=(880.134,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.01,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.796 kJ/mol
""",
    rank = 5,
)

entry(
    index = 718,
    label = "FCCDC(F)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84889,0.0354257,-9.10834e-06,-6.88383e-09,3.27858e-12,-70208.2,11.4047], Tmin=(10,'K'), Tmax=(1268.52,'K')),
            NASAPolynomial(coeffs=[12.2435,0.0226233,-1.01319e-05,2.14799e-09,-1.75376e-13,-73437.6,-35.4255], Tmin=(1268.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-583.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.346 kJ/mol
""",
    rank = 5,
)

entry(
    index = 719,
    label = "CCDC([O])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u1 p2 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80608,0.0188663,1.78447e-05,-3.89388e-08,1.79971e-11,-36915.8,9.26369], Tmin=(10,'K'), Tmax=(786.089,'K')),
            NASAPolynomial(coeffs=[3.88553,0.0275413,-1.60334e-05,4.48533e-09,-4.85791e-13,-37208.8,7.11522], Tmin=(786.089,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-306.946,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 720,
    label = "[O]C(CF)OF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76155,0.0281698,-5.2382e-06,-1.31114e-08,6.90803e-12,-32503.2,11.4758], Tmin=(10,'K'), Tmax=(955.375,'K')),
            NASAPolynomial(coeffs=[7.39482,0.0231154,-1.32503e-05,3.60801e-09,-3.79138e-13,-33661,-8.31276], Tmin=(955.375,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-270.234,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 721,
    label = "FOCDC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77819,0.0190773,3.4884e-05,-1.05763e-07,7.18946e-11,-45640,10.8935], Tmin=(10,'K'), Tmax=(554.748,'K')),
            NASAPolynomial(coeffs=[5.4651,0.0223315,-1.56035e-05,5.00955e-09,-6.02818e-13,-46064.4,1.61088], Tmin=(554.748,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-379.507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 722,
    label = "FCC(OF)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68725,0.0385743,-2.51422e-05,6.0283e-09,2.38368e-14,-44493.5,11.4994], Tmin=(10,'K'), Tmax=(1199.33,'K')),
            NASAPolynomial(coeffs=[11.3399,0.0199014,-1.03556e-05,2.57133e-09,-2.48277e-13,-46821.8,-28.8653], Tmin=(1199.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-369.93,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.289 kJ/mol
""",
    rank = 5,
)

entry(
    index = 723,
    label = "F[C]1CC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09865,-0.00874179,0.000123108,-2.05713e-07,1.10812e-10,10441,8.19623], Tmin=(10,'K'), Tmax=(587.677,'K')),
            NASAPolynomial(coeffs=[1.10058,0.0291839,-1.84114e-05,5.55515e-09,-6.41599e-13,10490.9,18.4925], Tmin=(587.677,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.8044,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.166 kJ/mol
""",
    rank = 5,
)

entry(
    index = 724,
    label = "FC1D[C]CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02656,-0.00309022,9.86244e-05,-1.73954e-07,9.6086e-11,14596.5,9.72446], Tmin=(10,'K'), Tmax=(586.783,'K')),
            NASAPolynomial(coeffs=[2.19329,0.0258237,-1.72551e-05,5.38113e-09,-6.33976e-13,14529,15.1834], Tmin=(586.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (121.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 725,
    label = "CDCDC[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90013,0.00709097,0.000120723,-3.0281e-07,2.32927e-10,13786.8,10.2951], Tmin=(10,'K'), Tmax=(425.503,'K')),
            NASAPolynomial(coeffs=[3.08036,0.0308703,-1.97666e-05,6.08097e-09,-7.17691e-13,13711.1,11.8397], Tmin=(425.503,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.626,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.315 kJ/mol
""",
    rank = 5,
)

entry(
    index = 726,
    label = "CCDCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58541,0.0401737,-8.80922e-05,1.54783e-07,-1.08093e-10,22923,9.50776], Tmin=(10,'K'), Tmax=(452.028,'K')),
            NASAPolynomial(coeffs=[3.96785,0.0277013,-1.65464e-05,4.7867e-09,-5.36796e-13,22981.2,8.99336], Tmin=(452.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (190.58,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 727,
    label = "CCCD[C]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u1 p0 c0 {3,D} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85227,0.0205651,1.98118e-05,-3.38432e-08,1.26775e-11,4808.62,9.35065], Tmin=(10,'K'), Tmax=(979.618,'K')),
            NASAPolynomial(coeffs=[4.18747,0.0318663,-1.68931e-05,4.3384e-09,-4.35865e-13,4135.01,4.63749], Tmin=(979.618,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (40.0082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.447 kJ/mol
""",
    rank = 5,
)

entry(
    index = 728,
    label = "FC(F)C1CO1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93411,0.00430061,0.000125178,-2.61901e-07,1.72934e-10,-61207,11.1867], Tmin=(10,'K'), Tmax=(464.366,'K')),
            NASAPolynomial(coeffs=[1.16882,0.0395749,-2.57655e-05,7.91874e-09,-9.2638e-13,-61073.7,21.0767], Tmin=(464.366,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-508.916,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.465 kJ/mol
""",
    rank = 5,
)

entry(
    index = 729,
    label = "[C]#CC(DO)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89789,0.00743812,5.6859e-05,-1.57132e-07,1.21023e-10,25757.5,9.96732], Tmin=(10,'K'), Tmax=(458.399,'K')),
            NASAPolynomial(coeffs=[4.49668,0.0152207,-1.11721e-05,3.7107e-09,-4.58006e-13,25565.9,6.05491], Tmin=(458.399,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (214.149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.878 kJ/mol
""",
    rank = 5,
)

entry(
    index = 730,
    label = "CC([O])(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u1 p2 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91408,0.00530425,9.77674e-05,-2.07792e-07,1.32367e-10,-58465.9,9.00872], Tmin=(10,'K'), Tmax=(525.593,'K')),
            NASAPolynomial(coeffs=[3.35374,0.0278249,-1.86065e-05,5.9038e-09,-7.12681e-13,-58659.2,8.95279], Tmin=(525.593,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-486.141,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 731,
    label = "CCCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99231,0.0215915,3.03269e-05,-4.012e-08,1.28643e-11,-39725.6,8.28408], Tmin=(10,'K'), Tmax=(1140.32,'K')),
            NASAPolynomial(coeffs=[5.75096,0.0365492,-1.71389e-05,3.87685e-09,-3.4329e-13,-41500.3,-6.45411], Tmin=(1140.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-330.221,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.997 kJ/mol
""",
    rank = 5,
)

entry(
    index = 732,
    label = "F[CH]C1CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 O u0 p2 c0 {4,S} {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8687,0.0127077,4.78705e-05,-8.79869e-08,4.46023e-11,-11658.5,10.0545], Tmin=(10,'K'), Tmax=(664.648,'K')),
            NASAPolynomial(coeffs=[2.91435,0.0302894,-1.85253e-05,5.40843e-09,-6.07038e-13,-11793.1,12.3017], Tmin=(664.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.9495,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.27 kJ/mol
""",
    rank = 5,
)

entry(
    index = 733,
    label = "CDCCDCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94516,0.00347565,0.000112351,-2.2347e-07,1.40987e-10,-11557,9.73154], Tmin=(10,'K'), Tmax=(482.478,'K')),
            NASAPolynomial(coeffs=[1.11118,0.0370236,-2.32008e-05,7.0141e-09,-8.17203e-13,-11400.6,20.1259], Tmin=(482.478,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.1046,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.48 kJ/mol
""",
    rank = 5,
)

entry(
    index = 734,
    label = "CC[C]DCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90816,0.0237813,6.65567e-06,-1.70386e-08,5.86462e-12,4316.33,9.46568], Tmin=(10,'K'), Tmax=(1195.09,'K')),
            NASAPolynomial(coeffs=[7.7504,0.0245202,-1.13404e-05,2.52164e-09,-2.18954e-13,2426.82,-13.8187], Tmin=(1195.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.929,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 735,
    label = "COCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61633,0.0409842,-0.000135063,3.69646e-07,-3.26151e-10,-49964.3,8.71488], Tmin=(10,'K'), Tmax=(425.427,'K')),
            NASAPolynomial(coeffs=[-0.449535,0.0446026,-2.57899e-05,7.18125e-09,-7.75665e-13,-49305.1,28.5364], Tmin=(425.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-415.437,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.338 kJ/mol
""",
    rank = 5,
)

entry(
    index = 736,
    label = "FC1[C]DCC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92969,0.0040568,0.000102355,-1.88962e-07,1.06143e-10,548.158,10.8013], Tmin=(10,'K'), Tmax=(573.126,'K')),
            NASAPolynomial(coeffs=[1.48857,0.037005,-2.55203e-05,8.22355e-09,-9.99463e-13,566.653,18.9397], Tmin=(573.126,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.52722,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.779 kJ/mol
""",
    rank = 5,
)

entry(
    index = 737,
    label = "FCOCF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06222,0.0147292,1.64487e-05,-2.39425e-08,7.87358e-12,-76621.3,8.69297], Tmin=(10,'K'), Tmax=(1157.01,'K')),
            NASAPolynomial(coeffs=[7.20157,0.019036,-8.78898e-06,1.92427e-09,-1.62564e-13,-78362.5,-11.2955], Tmin=(1157.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-636.99,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.363 kJ/mol
""",
    rank = 5,
)

entry(
    index = 738,
    label = "CC(F)[C](O)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  O u0 p2 c0 {4,S} {11,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85581,0.0164969,0.000223776,-1.17602e-06,2.10525e-09,-62097.1,11.0554], Tmin=(10,'K'), Tmax=(140.54,'K')),
            NASAPolynomial(coeffs=[3.03414,0.0398831,-2.58266e-05,8.00281e-09,-9.48525e-13,-62074,13.4071], Tmin=(140.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-515.934,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 739,
    label = "[CH2]C(O)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {4,S} {8,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91808,0.00532534,9.52735e-05,-2.16719e-07,1.49146e-10,-33203,9.56499], Tmin=(10,'K'), Tmax=(485.042,'K')),
            NASAPolynomial(coeffs=[3.49349,0.0250372,-1.58163e-05,4.87038e-09,-5.78845e-13,-33352.5,9.34054], Tmin=(485.042,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.083,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.096 kJ/mol
""",
    rank = 5,
)

entry(
    index = 740,
    label = "CD[C]CF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88317,0.0116903,2.50523e-05,-4.20793e-08,1.83835e-11,7618.82,9.11412], Tmin=(10,'K'), Tmax=(776.894,'K')),
            NASAPolynomial(coeffs=[2.8928,0.024328,-1.39033e-05,3.83927e-09,-4.12022e-13,7545.21,12.1779], Tmin=(776.894,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.343,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.297 kJ/mol
""",
    rank = 5,
)

entry(
    index = 741,
    label = "FC1DCC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94616,0.00306306,7.30908e-05,-1.34008e-07,7.41861e-11,-13966.4,9.12706], Tmin=(10,'K'), Tmax=(588.513,'K')),
            NASAPolynomial(coeffs=[2.36828,0.0263787,-1.84281e-05,6.0179e-09,-7.40146e-13,-13998.7,14.0504], Tmin=(588.513,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116.147,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.672 kJ/mol
""",
    rank = 5,
)

entry(
    index = 742,
    label = "C[CH]OCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64926,0.0378716,-0.000105409,2.90332e-07,-2.69751e-10,-33055.7,9.4952], Tmin=(10,'K'), Tmax=(400.769,'K')),
            NASAPolynomial(coeffs=[1.0787,0.0397993,-2.38128e-05,6.86285e-09,-7.64942e-13,-32659.1,21.9236], Tmin=(400.769,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.853,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.044 kJ/mol
""",
    rank = 5,
)

entry(
    index = 743,
    label = "CDCO[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7864,0.0218709,2.09589e-05,-5.22525e-08,2.63723e-11,-42487.8,10.7209], Tmin=(10,'K'), Tmax=(746.693,'K')),
            NASAPolynomial(coeffs=[5.05315,0.0279954,-1.72792e-05,5.04299e-09,-5.63452e-13,-43036.8,2.56953], Tmin=(746.693,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-353.275,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.855 kJ/mol
""",
    rank = 5,
)

entry(
    index = 744,
    label = "CC1OC1(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90953,0.00587397,0.000129244,-2.80825e-07,1.8823e-10,-66632.3,9.25697], Tmin=(10,'K'), Tmax=(479.536,'K')),
            NASAPolynomial(coeffs=[2.09793,0.0380641,-2.48706e-05,7.70048e-09,-9.08677e-13,-66654.9,14.618], Tmin=(479.536,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-554.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.486 kJ/mol
""",
    rank = 5,
)

entry(
    index = 745,
    label = "OC#CC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60443,0.03301,-3.00375e-05,1.43918e-08,-2.8372e-12,-41587.1,11.1062], Tmin=(10,'K'), Tmax=(1147.28,'K')),
            NASAPolynomial(coeffs=[8.04615,0.017524,-9.79051e-06,2.62657e-09,-2.73489e-13,-42606.3,-10.9328], Tmin=(1147.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-345.817,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.112 kJ/mol
""",
    rank = 5,
)

entry(
    index = 746,
    label = "[CH]DCC(O)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5 O u0 p2 c0 {4,S} {9,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90209,0.00634092,0.000114267,-2.57801e-07,1.75798e-10,-15053,10.4889], Tmin=(10,'K'), Tmax=(488.103,'K')),
            NASAPolynomial(coeffs=[3.2597,0.0308188,-2.00023e-05,6.23366e-09,-7.43485e-13,-15219.2,10.7828], Tmin=(488.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-125.181,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 747,
    label = "FC1C[CH]C1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96199,0.00234573,0.000117437,-2.12315e-07,1.23994e-10,419.769,10.1419], Tmin=(10,'K'), Tmax=(442.886,'K')),
            NASAPolynomial(coeffs=[-0.84271,0.0457577,-2.96537e-05,9.18708e-09,-1.08932e-12,845.183,29.4067], Tmin=(442.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.47761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 748,
    label = "ODCD[C]C(F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76654,0.0222306,3.99012e-07,-2.45133e-08,1.47512e-11,-31221.3,11.5575], Tmin=(10,'K'), Tmax=(739.611,'K')),
            NASAPolynomial(coeffs=[5.96788,0.0194401,-1.24275e-05,3.71082e-09,-4.21259e-13,-31796.2,-0.0840208], Tmin=(739.611,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.993 kJ/mol
""",
    rank = 5,
)

entry(
    index = 749,
    label = "FOOC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79395,0.020833,1.32994e-05,-4.73437e-08,2.69305e-11,-58145.1,10.8105], Tmin=(10,'K'), Tmax=(708.778,'K')),
            NASAPolynomial(coeffs=[6.19748,0.0204224,-1.36689e-05,4.20589e-09,-4.87436e-13,-58816.2,-2.28854], Tmin=(708.778,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-483.463,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 750,
    label = "ODCDCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8529,0.0134147,4.48717e-05,-2.18942e-07,2.56613e-10,13346.5,9.20515], Tmin=(10,'K'), Tmax=(321.722,'K')),
            NASAPolynomial(coeffs=[4.71225,0.0139603,-1.00311e-05,3.3236e-09,-4.12305e-13,13233.1,5.1306], Tmin=(321.722,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.986,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 751,
    label = "CO[C](C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67177,0.0316207,-3.81301e-05,8.49398e-08,-7.43389e-11,-32493,8.42327], Tmin=(10,'K'), Tmax=(457.317,'K')),
            NASAPolynomial(coeffs=[1.50621,0.0387869,-2.30127e-05,6.59892e-09,-7.33527e-13,-32171.8,18.5228], Tmin=(457.317,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-270.172,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.72 kJ/mol
""",
    rank = 5,
)

entry(
    index = 752,
    label = "[O]CC(O)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 O u0 p2 c0 {3,S} {9,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84604,0.0127181,7.57608e-05,-1.83638e-07,1.3028e-10,-49497,10.5471], Tmin=(10,'K'), Tmax=(457.338,'K')),
            NASAPolynomial(coeffs=[2.8766,0.0316097,-2.03522e-05,6.25018e-09,-7.33804e-13,-49517.2,13.2752], Tmin=(457.338,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-411.554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 753,
    label = "CDCC(O)F",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  F u0 p3 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92783,0.00448192,0.000113891,-2.29047e-07,1.43065e-10,-44853.5,9.7906], Tmin=(10,'K'), Tmax=(508.959,'K')),
            NASAPolynomial(coeffs=[1.77206,0.0361595,-2.2896e-05,7.00843e-09,-8.2588e-13,-44825,16.8601], Tmin=(508.959,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-372.956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 754,
    label = "CDC(F)O[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {8,S} {9,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78064,0.0207063,3.20515e-05,-7.62576e-08,4.17081e-11,-40212,11.7437], Tmin=(10,'K'), Tmax=(667.088,'K')),
            NASAPolynomial(coeffs=[4.63765,0.0294239,-1.87076e-05,5.60679e-09,-6.40783e-13,-40634.6,5.64522], Tmin=(667.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-334.367,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 755,
    label = "CO[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7779,0.0236871,-6.969e-05,1.9566e-07,-1.78195e-10,-26310,7.96978], Tmin=(10,'K'), Tmax=(416.972,'K')),
            NASAPolynomial(coeffs=[1.51852,0.0270605,-1.59901e-05,4.54358e-09,-4.99642e-13,-25962.5,18.8014], Tmin=(416.972,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-218.761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.199 kJ/mol
""",
    rank = 5,
)

entry(
    index = 756,
    label = "FCOC(F)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83992,0.0342019,-1.69508e-05,6.61079e-10,1.18341e-12,-83934.3,11.5327], Tmin=(10,'K'), Tmax=(1290.61,'K')),
            NASAPolynomial(coeffs=[12.7703,0.0162717,-7.4408e-06,1.60079e-09,-1.32219e-13,-87051.2,-36.9743], Tmin=(1290.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-697.831,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 757,
    label = "F[C]DCCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81387,0.0175009,1.16267e-05,-2.82837e-08,1.28358e-11,-13703.2,10.3995], Tmin=(10,'K'), Tmax=(825.342,'K')),
            NASAPolynomial(coeffs=[4.19686,0.0235584,-1.37648e-05,3.84354e-09,-4.14627e-13,-14035.9,6.99243], Tmin=(825.342,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-113.944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 758,
    label = "CC(F)DCOF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  O u0 p2 c0 {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69023,0.0269083,2.74373e-05,-9.28361e-08,6.46203e-11,-29040,9.83288], Tmin=(10,'K'), Tmax=(518.118,'K')),
            NASAPolynomial(coeffs=[3.99071,0.0342638,-2.18687e-05,6.64815e-09,-7.7317e-13,-29201,7.32758], Tmin=(518.118,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-241.484,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 759,
    label = "ODC(F)CO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81016,0.0171641,1.65996e-05,-4.0465e-08,2.07671e-11,-71798.7,9.76018], Tmin=(10,'K'), Tmax=(704.043,'K')),
            NASAPolynomial(coeffs=[3.87546,0.0242954,-1.45783e-05,4.19318e-09,-4.65207e-13,-71993.8,8.14758], Tmin=(704.043,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-596.988,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.681 kJ/mol
""",
    rank = 5,
)

entry(
    index = 760,
    label = "FOC[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75963,0.0270103,-8.82155e-06,-9.29662e-09,5.87065e-12,-39784.4,10.9043], Tmin=(10,'K'), Tmax=(925.907,'K')),
            NASAPolynomial(coeffs=[7.49546,0.019845,-1.17515e-05,3.28046e-09,-3.51514e-13,-40860.8,-8.90857], Tmin=(925.907,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-330.781,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 761,
    label = "[CH2]C(F)OF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 O u0 p2 c0 {4,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84592,0.0116821,0.000103264,-2.9395e-07,2.41499e-10,-17736.4,10.5013], Tmin=(10,'K'), Tmax=(419.734,'K')),
            NASAPolynomial(coeffs=[4.23181,0.0268344,-1.81771e-05,5.81595e-09,-7.04846e-13,-17934.7,6.99872], Tmin=(419.734,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 762,
    label = "ODC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91688,0.00544625,7.70392e-05,-1.85065e-07,1.30244e-10,-52684.4,10.2258], Tmin=(10,'K'), Tmax=(487.865,'K')),
            NASAPolynomial(coeffs=[4.1463,0.0192208,-1.34471e-05,4.36026e-09,-5.31217e-13,-52893.1,7.37418], Tmin=(487.865,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-438.061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.306 kJ/mol
""",
    rank = 5,
)

entry(
    index = 763,
    label = "CDC(F)CDCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88913,0.00756954,0.000134978,-3.17839e-07,2.28957e-10,-35688.8,10.6503], Tmin=(10,'K'), Tmax=(452.942,'K')),
            NASAPolynomial(coeffs=[2.67561,0.036966,-2.42352e-05,7.5509e-09,-8.96344e-13,-35770.5,13.4285], Tmin=(452.942,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-296.748,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.039 kJ/mol
""",
    rank = 5,
)

entry(
    index = 764,
    label = "CDC([O])CF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u1 p2 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89564,0.00802462,9.27578e-05,-2.06557e-07,1.40493e-10,-27041.7,10.5127], Tmin=(10,'K'), Tmax=(467.342,'K')),
            NASAPolynomial(coeffs=[2.38078,0.0321643,-2.05866e-05,6.29065e-09,-7.35616e-13,-27022.1,15.3632], Tmin=(467.342,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-224.851,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.718 kJ/mol
""",
    rank = 5,
)

entry(
    index = 765,
    label = "ODC1CDC1F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94489,0.00320523,6.41581e-05,-1.25053e-07,7.26537e-11,-3889.11,8.97311], Tmin=(10,'K'), Tmax=(574.628,'K')),
            NASAPolynomial(coeffs=[3.27317,0.020608,-1.4492e-05,4.73822e-09,-5.82537e-13,-4022.03,10.0133], Tmin=(574.628,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.359,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.221 kJ/mol
""",
    rank = 5,
)

entry(
    index = 766,
    label = "COC[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83167,0.0255399,2.47395e-06,-1.34823e-08,4.84466e-12,-26149.5,9.15699], Tmin=(10,'K'), Tmax=(1198.12,'K')),
            NASAPolynomial(coeffs=[7.40516,0.0253447,-1.19735e-05,2.73161e-09,-2.44339e-13,-27848,-12.2439], Tmin=(1198.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-217.4,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.738 kJ/mol
""",
    rank = 5,
)

entry(
    index = 767,
    label = "CDCOF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.956,0.00256729,6.77826e-05,-1.25379e-07,7.1292e-11,-704.93,8.26873], Tmin=(10,'K'), Tmax=(561.19,'K')),
            NASAPolynomial(coeffs=[2.30163,0.0241185,-1.59074e-05,5.029e-09,-6.07442e-13,-672.925,13.9252], Tmin=(561.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.87953,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 768,
    label = "[CH]DC(F)F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95334,0.00262608,4.83144e-05,-9.22756e-08,5.16672e-11,-10879.3,8.58603], Tmin=(10,'K'), Tmax=(608.321,'K')),
            NASAPolynomial(coeffs=[3.74439,0.0153968,-1.12777e-05,3.82958e-09,-4.85609e-13,-11064.7,7.75701], Tmin=(608.321,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-90.4763,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.112 kJ/mol
""",
    rank = 5,
)

entry(
    index = 769,
    label = "FOC1DCC1F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87285,0.00853835,0.000114292,-2.81144e-07,2.02865e-10,3274.04,10.9245], Tmin=(10,'K'), Tmax=(474.153,'K')),
            NASAPolynomial(coeffs=[4.08534,0.0289045,-2.02366e-05,6.56729e-09,-7.99902e-13,3004.81,7.43126], Tmin=(474.153,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.1994,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 770,
    label = "FCDC(CF)CF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81981,0.0349713,-7.52554e-06,-8.71239e-09,3.94989e-12,-69960.8,11.3696], Tmin=(10,'K'), Tmax=(1219.96,'K')),
            NASAPolynomial(coeffs=[10.9637,0.0250018,-1.181e-05,2.66884e-09,-2.34927e-13,-72705.1,-28.6194], Tmin=(1219.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-581.646,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.225 kJ/mol
""",
    rank = 5,
)

entry(
    index = 771,
    label = "CD[C]OC(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77555,0.0246966,6.34948e-06,-2.81197e-08,1.36006e-11,-39181.9,11.4095], Tmin=(10,'K'), Tmax=(851.93,'K')),
            NASAPolynomial(coeffs=[5.96723,0.0256748,-1.52137e-05,4.28053e-09,-4.63445e-13,-39964.3,-1.21295], Tmin=(851.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-325.774,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.256 kJ/mol
""",
    rank = 5,
)

entry(
    index = 772,
    label = "O[C](F)OCF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77148,0.0209739,2.94871e-05,-7.26653e-08,4.039e-11,-77438.2,11.4826], Tmin=(10,'K'), Tmax=(655.523,'K')),
            NASAPolynomial(coeffs=[4.46581,0.0293519,-1.85496e-05,5.54444e-09,-6.33018e-13,-77800.3,6.35879], Tmin=(655.523,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-643.886,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 773,
    label = "CC(C)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72367,0.0254586,2.47711e-05,-4.55552e-08,1.86381e-11,-16935.6,8.34838], Tmin=(10,'K'), Tmax=(859.431,'K')),
            NASAPolynomial(coeffs=[2.43673,0.0421927,-2.31884e-05,6.19391e-09,-6.4661e-13,-17111.2,12.0536], Tmin=(859.431,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.824,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.008 kJ/mol
""",
    rank = 5,
)

entry(
    index = 774,
    label = "FCDC(F)OCF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78426,0.0335373,-1.45711e-05,-2.25296e-09,2.30241e-12,-83205.9,12.0157], Tmin=(10,'K'), Tmax=(1173.74,'K')),
            NASAPolynomial(coeffs=[10.5291,0.0204068,-1.03853e-05,2.52303e-09,-2.38476e-13,-85468.1,-24.4965], Tmin=(1173.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-691.782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.29 kJ/mol
""",
    rank = 5,
)

entry(
    index = 775,
    label = "O[C](CF)CF",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78479,0.0304338,-3.35772e-06,-1.21334e-08,5.27617e-12,-58773.9,10.8889], Tmin=(10,'K'), Tmax=(1108.33,'K')),
            NASAPolynomial(coeffs=[8.05224,0.0265064,-1.35713e-05,3.35082e-09,-3.23452e-13,-60424.6,-13.3172], Tmin=(1108.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-488.647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 776,
    label = "[CH]DC1CC1F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92801,0.00418557,9.88139e-05,-1.85764e-07,1.06182e-10,27925.9,9.74001], Tmin=(10,'K'), Tmax=(568.926,'K')),
            NASAPolynomial(coeffs=[2.03541,0.0338811,-2.26902e-05,7.24821e-09,-8.81768e-13,27876,15.4722], Tmin=(568.926,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.159,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 777,
    label = "FC1D[C]CC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93245,0.00393893,0.000102191,-1.9012e-07,1.08144e-10,1689.29,10.7849], Tmin=(10,'K'), Tmax=(562.389,'K')),
            NASAPolynomial(coeffs=[1.43936,0.0366451,-2.49818e-05,7.97706e-09,-9.63005e-13,1732.91,19.2724], Tmin=(562.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (14.0172,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.779 kJ/mol
""",
    rank = 5,
)

entry(
    index = 778,
    label = "FC[C]1OC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87893,0.020218,1.62415e-05,-3.49448e-08,1.47383e-11,-34808.3,11.0633], Tmin=(10,'K'), Tmax=(913.602,'K')),
            NASAPolynomial(coeffs=[5.88802,0.0251778,-1.44874e-05,3.95943e-09,-4.1747e-13,-35749.5,-1.58977], Tmin=(913.602,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.377,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.979 kJ/mol
""",
    rank = 5,
)

entry(
    index = 779,
    label = "F[CH]COCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57812,0.0458391,-0.000139332,3.81156e-07,-3.65741e-10,-52815.6,12.0442], Tmin=(10,'K'), Tmax=(373.167,'K')),
            NASAPolynomial(coeffs=[1.74911,0.0415849,-2.63251e-05,7.92871e-09,-9.14506e-13,-52512.9,21.2911], Tmin=(373.167,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-439.148,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.329 kJ/mol
""",
    rank = 5,
)

entry(
    index = 780,
    label = "[O]C1CC1F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87111,0.0226857,-1.70113e-06,-9.01936e-09,3.64807e-12,-22250.6,10.4058], Tmin=(10,'K'), Tmax=(1174.67,'K')),
            NASAPolynomial(coeffs=[7.7023,0.0191361,-9.29495e-06,2.17264e-09,-1.98603e-13,-23805.9,-11.483], Tmin=(1174.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-184.975,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 781,
    label = "FCC1[CH]C1F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {3,S} {4,S} {7,S} {11,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83581,0.0176252,5.54754e-05,-1.00166e-07,4.8472e-11,-15235.1,11.3303], Tmin=(10,'K'), Tmax=(710.871,'K')),
            NASAPolynomial(coeffs=[3.13862,0.0382502,-2.32878e-05,6.75089e-09,-7.52038e-13,-15558,11.4877], Tmin=(710.871,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.681,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 782,
    label = "FC1CDCO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08466,-0.00762935,0.000125284,-2.1006e-07,1.11961e-10,-20481.7,9.07745], Tmin=(10,'K'), Tmax=(603.199,'K')),
            NASAPolynomial(coeffs=[1.38105,0.0305478,-2.00057e-05,6.16797e-09,-7.21347e-13,-20523.9,17.7006], Tmin=(603.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-170.304,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.605 kJ/mol
""",
    rank = 5,
)

entry(
    index = 783,
    label = "CDC1CC1F",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94994,0.00295635,0.000104133,-1.86913e-07,1.05329e-10,-200.026,8.45256], Tmin=(10,'K'), Tmax=(537.915,'K')),
            NASAPolynomial(coeffs=[0.282101,0.0399598,-2.61821e-05,8.21659e-09,-9.85976e-13,53.8162,22.5652], Tmin=(537.915,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1.6833,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.308 kJ/mol
""",
    rank = 5,
)

entry(
    index = 784,
    label = "FCC1DCO1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84416,0.022637,-8.47572e-06,-1.63045e-09,1.2516e-12,3094.86,9.26821], Tmin=(10,'K'), Tmax=(1301.04,'K')),
            NASAPolynomial(coeffs=[8.99371,0.0137717,-6.28685e-06,1.36376e-09,-1.14628e-13,1165.27,-19.1966], Tmin=(1301.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.7379,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 785,
    label = "FC1[CH]CC1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96101,0.00234407,0.000113194,-1.9834e-07,1.11763e-10,748.099,10.1339], Tmin=(10,'K'), Tmax=(459.387,'K')),
            NASAPolynomial(coeffs=[-1.09464,0.0463029,-3.01392e-05,9.372e-09,-1.11434e-12,1213.25,30.599], Tmin=(459.387,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.20457,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 786,
    label = "CC(F)[CH]CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73595,0.0328805,4.94386e-06,-2.27543e-08,9.06555e-12,-40487.7,11.7799], Tmin=(10,'K'), Tmax=(1046.76,'K')),
            NASAPolynomial(coeffs=[6.56673,0.035699,-1.86349e-05,4.70745e-09,-4.65376e-13,-41827.4,-5.57469], Tmin=(1046.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-336.612,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.856 kJ/mol
""",
    rank = 5,
)

entry(
    index = 787,
    label = "FOCDC(F)OF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 O u0 p2 c0 {4,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57383,0.0374727,-1.86438e-05,-2.60674e-08,2.55712e-11,-27327,12.0421], Tmin=(10,'K'), Tmax=(620.65,'K')),
            NASAPolynomial(coeffs=[7.76072,0.023496,-1.63004e-05,5.18208e-09,-6.17525e-13,-28097.2,-8.17831], Tmin=(620.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-227.263,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.112 kJ/mol
""",
    rank = 5,
)

entry(
    index = 788,
    label = "CC(D[C]F)CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u1 p0 c0 {2,D} {4,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69434,0.0321095,-1.02092e-05,-4.06585e-09,2.34894e-12,-18515.7,10.2648], Tmin=(10,'K'), Tmax=(1222.51,'K')),
            NASAPolynomial(coeffs=[8.47432,0.0251692,-1.23678e-05,2.93215e-09,-2.72479e-13,-20334.6,-16.415], Tmin=(1222.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.961,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 789,
    label = "C#CO[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83183,0.0117428,0.000109944,-3.14495e-07,2.49773e-10,-14340.9,10.8327], Tmin=(10,'K'), Tmax=(453.783,'K')),
            NASAPolynomial(coeffs=[5.79843,0.0221439,-1.61211e-05,5.40609e-09,-6.75835e-13,-14804.9,-0.247684], Tmin=(453.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.729 kJ/mol
""",
    rank = 5,
)

entry(
    index = 790,
    label = "CC(F)DCDCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80313,0.020345,9.81148e-05,-4.26229e-07,5.82759e-10,-26598.7,9.50582], Tmin=(10,'K'), Tmax=(185.505,'K')),
            NASAPolynomial(coeffs=[3.11205,0.0352463,-2.23757e-05,6.78092e-09,-7.87142e-13,-26573,11.6757], Tmin=(185.505,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-221.112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.403 kJ/mol
""",
    rank = 5,
)

entry(
    index = 791,
    label = "FCD[C]CC(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u1 p0 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {11,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53704,0.0503145,-0.000147323,4.06711e-07,-4.0965e-10,-45476.9,13.1866], Tmin=(10,'K'), Tmax=(348.012,'K')),
            NASAPolynomial(coeffs=[2.31577,0.0436218,-2.91269e-05,9.12857e-09,-1.08481e-12,-45266.4,19.5929], Tmin=(348.012,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-378.126,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 792,
    label = "ODCDC(O)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {6,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88664,0.00781637,8.35557e-05,-2.32039e-07,1.81945e-10,-39125.3,9.3854], Tmin=(10,'K'), Tmax=(456.071,'K')),
            NASAPolynomial(coeffs=[5.19911,0.0164859,-1.13318e-05,3.68592e-09,-4.54224e-13,-39454.9,1.78296], Tmin=(456.071,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-325.32,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 793,
    label = "[O]C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93325,0.00383746,5.97868e-05,-1.222e-07,7.16726e-11,-78115,8.76058], Tmin=(10,'K'), Tmax=(593.814,'K')),
            NASAPolynomial(coeffs=[4.34347,0.0168935,-1.31537e-05,4.55261e-09,-5.78738e-13,-78442.7,4.64683], Tmin=(593.814,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-649.514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.184 kJ/mol
""",
    rank = 5,
)

entry(
    index = 794,
    label = "CCDCOF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78633,0.0204735,2.08924e-05,-4.32031e-08,1.95639e-11,-4985.9,8.72067], Tmin=(10,'K'), Tmax=(790.633,'K')),
            NASAPolynomial(coeffs=[3.5226,0.0314101,-1.80741e-05,5.01478e-09,-5.3991e-13,-5244.32,8.03309], Tmin=(790.633,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.4666,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 795,
    label = "CDC1OC1F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9472,0.00302061,8.22588e-05,-1.48038e-07,8.15685e-11,-18925.6,8.23714], Tmin=(10,'K'), Tmax=(577.848,'K')),
            NASAPolynomial(coeffs=[1.63773,0.0309083,-2.10263e-05,6.7645e-09,-8.25003e-13,-18857.4,16.3932], Tmin=(577.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.38,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.605 kJ/mol
""",
    rank = 5,
)

entry(
    index = 796,
    label = "CCDC[C](F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63859,0.0306669,5.79336e-06,-3.39422e-08,1.82943e-11,-32967.2,9.67103], Tmin=(10,'K'), Tmax=(729.758,'K')),
            NASAPolynomial(coeffs=[4.23774,0.035571,-2.11176e-05,6.01785e-09,-6.62598e-13,-33272.7,5.47537], Tmin=(729.758,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.146,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.366 kJ/mol
""",
    rank = 5,
)

entry(
    index = 797,
    label = "[CH2]C(F)DCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,D}
5 F u0 p3 c0 {4,S}
6 C u0 p0 c0 {4,D} {7,S} {8,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90506,0.00575076,9.81479e-05,-2.07485e-07,1.29795e-10,-27091.8,9.30553], Tmin=(10,'K'), Tmax=(544.119,'K')),
            NASAPolynomial(coeffs=[3.84927,0.0270846,-1.83458e-05,5.91814e-09,-7.25822e-13,-27395.5,6.69448], Tmin=(544.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-225.289,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.403 kJ/mol
""",
    rank = 5,
)

entry(
    index = 798,
    label = "ODCOCF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99263,0.01351,1.5034e-05,-2.37908e-08,8.43127e-12,-69058.6,9.33644], Tmin=(10,'K'), Tmax=(1063.19,'K')),
            NASAPolynomial(coeffs=[5.72846,0.0190185,-9.72292e-06,2.38336e-09,-2.27735e-13,-70108.1,-2.34423], Tmin=(1063.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-574.131,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.725 kJ/mol
""",
    rank = 5,
)

entry(
    index = 799,
    label = "COCDC(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74916,0.0286387,-5.19118e-06,-1.01307e-08,4.88295e-12,-57821.6,9.67529], Tmin=(10,'K'), Tmax=(1046.7,'K')),
            NASAPolynomial(coeffs=[6.98347,0.0253678,-1.35289e-05,3.47583e-09,-3.48376e-13,-58996.6,-8.45434], Tmin=(1046.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-480.748,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.081 kJ/mol
""",
    rank = 5,
)

entry(
    index = 800,
    label = "C[C]1C(F)C1F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7923,0.0289914,2.94667e-06,-1.9886e-08,8.28458e-12,-15922.3,9.45865], Tmin=(10,'K'), Tmax=(1031.62,'K')),
            NASAPolynomial(coeffs=[7.10754,0.0288811,-1.54232e-05,3.9602e-09,-3.96231e-13,-17284.5,-9.92547], Tmin=(1031.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.774 kJ/mol
""",
    rank = 5,
)

entry(
    index = 801,
    label = "FC[C]1CC1F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {6,S} {11,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89628,0.0232099,2.05173e-05,-3.85887e-08,1.50258e-11,-15372.2,11.6346], Tmin=(10,'K'), Tmax=(978.004,'K')),
            NASAPolynomial(coeffs=[6.15146,0.0307662,-1.68079e-05,4.39754e-09,-4.46849e-13,-16615.8,-3.29788], Tmin=(978.004,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.753,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.788 kJ/mol
""",
    rank = 5,
)

entry(
    index = 802,
    label = "C#COCF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88817,0.00899322,9.37834e-05,-2.59373e-07,2.17952e-10,-12805.6,9.66835], Tmin=(10,'K'), Tmax=(386.424,'K')),
            NASAPolynomial(coeffs=[3.23425,0.026683,-1.72757e-05,5.36325e-09,-6.3711e-13,-12836.6,11.1464], Tmin=(386.424,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.466,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.906 kJ/mol
""",
    rank = 5,
)

entry(
    index = 803,
    label = "OC(O)[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 O u0 p2 c0 {2,S} {9,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86159,0.0101308,0.000122286,-3.3176e-07,2.67224e-10,-51642.9,10.6907], Tmin=(10,'K'), Tmax=(420.968,'K')),
            NASAPolynomial(coeffs=[3.89952,0.0298508,-1.9531e-05,6.14021e-09,-7.37139e-13,-51824,8.42724], Tmin=(420.968,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-429.387,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.665 kJ/mol
""",
    rank = 5,
)

entry(
    index = 804,
    label = "CCC(F)D[C]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  F u0 p3 c0 {3,S}
5  C u1 p0 c0 {3,D} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65731,0.0321236,-8.41788e-06,-7.26883e-09,3.79167e-12,-16021.9,10.3332], Tmin=(10,'K'), Tmax=(1082.69,'K')),
            NASAPolynomial(coeffs=[6.71994,0.0289416,-1.5277e-05,3.89271e-09,-3.87633e-13,-17161.8,-6.88688], Tmin=(1082.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.231,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 805,
    label = "FC1D[C]OC1F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u1 p0 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91188,0.00543508,9.2279e-05,-1.99408e-07,1.27352e-10,-4149.72,10.9178], Tmin=(10,'K'), Tmax=(529.58,'K')),
            NASAPolynomial(coeffs=[3.61637,0.0261341,-1.86562e-05,6.0905e-09,-7.42465e-13,-4377.38,9.71064], Tmin=(529.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-34.5319,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 806,
    label = "[CH]DC1OC1F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92473,0.00438581,8.04812e-05,-1.60004e-07,9.40493e-11,11219.1,9.56131], Tmin=(10,'K'), Tmax=(576.102,'K')),
            NASAPolynomial(coeffs=[3.56392,0.0243811,-1.71199e-05,5.63843e-09,-6.99694e-13,10970.5,8.58402], Tmin=(576.102,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.2498,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.683 kJ/mol
""",
    rank = 5,
)

entry(
    index = 807,
    label = "[CH2]OC#CF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {7,S}
7 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82803,0.0132828,0.000112068,-3.92726e-07,3.75823e-10,22984,9.06291], Tmin=(10,'K'), Tmax=(383.862,'K')),
            NASAPolynomial(coeffs=[5.91422,0.0182611,-1.17871e-05,3.69728e-09,-4.47079e-13,22627,-1.56823], Tmin=(383.862,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (191.113,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.408 kJ/mol
""",
    rank = 5,
)

entry(
    index = 808,
    label = "CC(C)(O)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  F u0 p3 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90574,0.00647142,0.000155064,-3.57671e-07,2.5999e-10,-64859.1,7.17239], Tmin=(10,'K'), Tmax=(434.475,'K')),
            NASAPolynomial(coeffs=[1.83604,0.0421574,-2.55588e-05,7.58367e-09,-8.75435e-13,-64836.2,13.6257], Tmin=(434.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-539.277,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 809,
    label = "ODCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94585,0.00365462,4.27919e-05,-1.12437e-07,8.43984e-11,4751.57,8.20017], Tmin=(10,'K'), Tmax=(470.027,'K')),
            NASAPolynomial(coeffs=[4.44476,0.00926151,-6.54451e-06,2.137e-09,-2.62409e-13,4595.83,5.01209], Tmin=(470.027,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.498,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.724 kJ/mol
""",
    rank = 5,
)

entry(
    index = 810,
    label = "[O]C(DCF)OF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75227,0.02042,4.8872e-05,-1.75311e-07,1.46069e-10,-32464.5,11.3423], Tmin=(10,'K'), Tmax=(451.632,'K')),
            NASAPolynomial(coeffs=[5.41957,0.0228619,-1.63937e-05,5.39881e-09,-6.6433e-13,-32790.6,2.68087], Tmin=(451.632,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-269.941,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.387 kJ/mol
""",
    rank = 5,
)

entry(
    index = 811,
    label = "OCDCC(F)F",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75501,0.0210034,4.79115e-05,-1.19225e-07,7.59183e-11,-68947,10.8935], Tmin=(10,'K'), Tmax=(538.377,'K')),
            NASAPolynomial(coeffs=[3.43756,0.0347399,-2.20613e-05,6.67663e-09,-7.73375e-13,-69077.7,10.697], Tmin=(538.377,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-573.289,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.52 kJ/mol
""",
    rank = 5,
)

entry(
    index = 812,
    label = "CD[C]C(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83885,0.0142716,3.75013e-05,-8.11734e-08,4.58621e-11,-18458.1,10.4107], Tmin=(10,'K'), Tmax=(609.426,'K')),
            NASAPolynomial(coeffs=[3.56485,0.0261281,-1.6438e-05,4.9137e-09,-5.6227e-13,-18611.5,10.0645], Tmin=(609.426,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.286 kJ/mol
""",
    rank = 5,
)

entry(
    index = 813,
    label = "FOC1CDC1",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 C u0 p0 c0 {3,S} {4,D} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92432,0.00445742,9.15769e-05,-1.79907e-07,1.06141e-10,24436.6,9.72043], Tmin=(10,'K'), Tmax=(562.43,'K')),
            NASAPolynomial(coeffs=[2.87649,0.0290691,-1.98267e-05,6.38934e-09,-7.79791e-13,24283.1,11.7598], Tmin=(562.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.147,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 814,
    label = "CC(DO)[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76825,0.0213548,9.71652e-06,-2.93853e-08,1.41013e-11,-29370.2,9.60504], Tmin=(10,'K'), Tmax=(791.741,'K')),
            NASAPolynomial(coeffs=[4.19847,0.0269573,-1.56299e-05,4.36194e-09,-4.71742e-13,-29682,6.09076], Tmin=(791.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-244.215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.209 kJ/mol
""",
    rank = 5,
)

entry(
    index = 815,
    label = "CD[C]C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85712,0.00977478,0.000117109,-3.00452e-07,2.23627e-10,-47174.6,10.264], Tmin=(10,'K'), Tmax=(464.89,'K')),
            NASAPolynomial(coeffs=[4.462,0.0284203,-2.00055e-05,6.5279e-09,-7.98905e-13,-47488.6,5.03728], Tmin=(464.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-392.253,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.838 kJ/mol
""",
    rank = 5,
)

entry(
    index = 816,
    label = "C#CC(O)F",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 O u0 p2 c0 {3,S} {8,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89526,0.0066003,0.000100897,-2.29504e-07,1.53614e-10,-22054.2,9.39105], Tmin=(10,'K'), Tmax=(514.458,'K')),
            NASAPolynomial(coeffs=[4.34808,0.0249629,-1.64477e-05,5.24127e-09,-6.39697e-13,-22390.4,4.69288], Tmin=(514.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-183.4,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.892 kJ/mol
""",
    rank = 5,
)

entry(
    index = 817,
    label = "C#CC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {8,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4 F u0 p3 c0 {3,S}
5 C u1 p0 c0 {3,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78496,0.0168351,0.000122333,-3.85168e-07,3.39644e-10,-1276.75,11.477], Tmin=(10,'K'), Tmax=(400.855,'K')),
            NASAPolynomial(coeffs=[4.91938,0.0302742,-2.06043e-05,6.63877e-09,-8.10042e-13,-1566.62,4.55988], Tmin=(400.855,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.6099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.34 kJ/mol
""",
    rank = 5,
)

entry(
    index = 818,
    label = "FC1CDCC1F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94024,0.00346347,0.000109545,-1.95772e-07,1.08381e-10,-30013.4,9.4669], Tmin=(10,'K'), Tmax=(559.51,'K')),
            NASAPolynomial(coeffs=[0.22795,0.0425467,-2.88627e-05,9.21144e-09,-1.11308e-12,-29794.3,23.4663], Tmin=(559.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.571,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 819,
    label = "ODC(O)CF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {6,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93995,0.00374196,8.99153e-05,-1.83485e-07,1.15581e-10,-72675.1,9.87592], Tmin=(10,'K'), Tmax=(508.409,'K')),
            NASAPolynomial(coeffs=[2.38528,0.0281924,-1.82732e-05,5.652e-09,-6.68241e-13,-72674.9,14.7715], Tmin=(508.409,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-604.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.141 kJ/mol
""",
    rank = 5,
)

entry(
    index = 820,
    label = "[O]C(F)DCDO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,D}
5 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88581,0.00872216,6.51059e-05,-2.1284e-07,1.90466e-10,-38612.3,10.1522], Tmin=(10,'K'), Tmax=(403.597,'K')),
            NASAPolynomial(coeffs=[4.86779,0.0139717,-1.00855e-05,3.33687e-09,-4.12754e-13,-38813.6,4.79407], Tmin=(403.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-321.038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 821,
    label = "[CH]DCDCDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {4,D} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84579,0.0115536,0.000105727,-3.38354e-07,3.02185e-10,37509.3,10.0747], Tmin=(10,'K'), Tmax=(403.821,'K')),
            NASAPolynomial(coeffs=[5.43815,0.0196567,-1.30597e-05,4.1648e-09,-5.07295e-13,37186,1.42605], Tmin=(403.821,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.875,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 822,
    label = "[CH2]C(F)OC",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68758,0.029279,-3.23319e-06,-1.17082e-08,5.3093e-12,-31584.6,9.3248], Tmin=(10,'K'), Tmax=(1016.7,'K')),
            NASAPolynomial(coeffs=[5.41179,0.0302057,-1.5976e-05,4.10671e-09,-4.13663e-13,-32333.7,-0.98185], Tmin=(1016.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-262.625,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.984 kJ/mol
""",
    rank = 5,
)

entry(
    index = 823,
    label = "COC(F)[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  F u0 p3 c0 {3,S}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82184,0.0357122,-2.0122e-05,5.03338e-09,-4.05978e-13,-53114.4,11.1878], Tmin=(10,'K'), Tmax=(1721.59,'K')),
            NASAPolynomial(coeffs=[19.3347,0.00600435,2.42377e-07,-7.15026e-10,1.18381e-13,-59394.6,-74.8066], Tmin=(1721.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-441.651,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.329 kJ/mol
""",
    rank = 5,
)

entry(
    index = 824,
    label = "CC(O)D[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {9,S}
4 C u1 p0 c0 {2,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89062,0.0101685,0.000159598,-6.09145e-07,7.30775e-10,-11670.7,8.96065], Tmin=(10,'K'), Tmax=(269.843,'K')),
            NASAPolynomial(coeffs=[3.44525,0.0294916,-1.85302e-05,5.63986e-09,-6.62238e-13,-11692.9,9.66773], Tmin=(269.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.0158,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 825,
    label = "C#CCDCF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9024,0.00637331,0.000101652,-2.38716e-07,1.67133e-10,10133,9.0569], Tmin=(10,'K'), Tmax=(485.105,'K')),
            NASAPolynomial(coeffs=[3.93895,0.0252964,-1.63038e-05,5.08085e-09,-6.0878e-13,9903.23,6.57557], Tmin=(485.105,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.2291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.397 kJ/mol
""",
    rank = 5,
)

entry(
    index = 826,
    label = "C[C](C)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  F u0 p3 c0 {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77628,0.0185482,1.44082e-05,-2.64232e-08,1.02524e-11,-16952.3,6.53796], Tmin=(10,'K'), Tmax=(900.34,'K')),
            NASAPolynomial(coeffs=[2.35695,0.0310953,-1.68939e-05,4.45437e-09,-4.59383e-13,-16949.7,11.8316], Tmin=(900.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.969,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.641 kJ/mol
""",
    rank = 5,
)

entry(
    index = 827,
    label = "OC1[CH]C1F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91281,0.00516113,0.000104582,-2.07053e-07,1.23223e-10,-7470.14,10.0454], Tmin=(10,'K'), Tmax=(558.499,'K')),
            NASAPolynomial(coeffs=[2.83811,0.0325493,-2.18622e-05,7.00925e-09,-8.54906e-13,-7657.2,11.8548], Tmin=(558.499,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-62.1448,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 828,
    label = "C#C[C](F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77088,0.0199162,5.37572e-05,-2.66761e-07,2.91666e-10,-2659.39,9.64824], Tmin=(10,'K'), Tmax=(359.413,'K')),
            NASAPolynomial(coeffs=[5.83119,0.0162829,-1.16124e-05,3.87043e-09,-4.84068e-13,-2932.12,0.0828738], Tmin=(359.413,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-22.0932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.254 kJ/mol
""",
    rank = 5,
)

entry(
    index = 829,
    label = "C#CC([CH2])F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {8,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 F u0 p3 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84952,0.0107555,0.000131481,-3.65937e-07,2.97414e-10,21556.3,10.4464], Tmin=(10,'K'), Tmax=(427.959,'K')),
            NASAPolynomial(coeffs=[4.72494,0.0279828,-1.79616e-05,5.59886e-09,-6.71428e-13,21248.7,4.24743], Tmin=(427.959,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (179.223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.091 kJ/mol
""",
    rank = 5,
)

entry(
    index = 830,
    label = "F[CH]OCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00039,0.0169916,6.02419e-06,-1.48079e-08,5.28913e-12,-52165.4,10.415], Tmin=(10,'K'), Tmax=(1161.77,'K')),
            NASAPolynomial(coeffs=[7.87122,0.0155171,-7.37582e-06,1.66338e-09,-1.45076e-13,-53864.7,-12.2826], Tmin=(1161.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-433.669,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 831,
    label = "OC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96747,0.00184422,5.34257e-05,-9.41624e-08,5.09197e-11,-82879.5,8.30121], Tmin=(10,'K'), Tmax=(583.36,'K')),
            NASAPolynomial(coeffs=[2.23772,0.0209619,-1.43918e-05,4.66467e-09,-5.71575e-13,-82801.2,14.6556], Tmin=(583.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-689.114,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.855 kJ/mol
""",
    rank = 5,
)

entry(
    index = 832,
    label = "OC(F)DCCF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8056,0.0181524,4.73166e-05,-9.59382e-08,5.07192e-11,-67544.5,11.3191], Tmin=(10,'K'), Tmax=(654.024,'K')),
            NASAPolynomial(coeffs=[3.44226,0.0342066,-2.12271e-05,6.26729e-09,-7.09497e-13,-67792.8,10.6562], Tmin=(654.024,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-561.621,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 833,
    label = "CDCDCDCF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90881,0.00635806,0.000104597,-2.61628e-07,1.98709e-10,15556.8,9.31092], Tmin=(10,'K'), Tmax=(437.405,'K')),
            NASAPolynomial(coeffs=[3.47372,0.0260218,-1.6625e-05,5.11202e-09,-6.03998e-13,15444.8,9.33501], Tmin=(437.405,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (129.34,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.288 kJ/mol
""",
    rank = 5,
)

entry(
    index = 834,
    label = "C[C]DCCF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66319,0.0347036,-7.23724e-05,1.87884e-07,-1.69732e-10,2592.69,9.33862], Tmin=(10,'K'), Tmax=(421.583,'K')),
            NASAPolynomial(coeffs=[1.22172,0.0394156,-2.34828e-05,6.74964e-09,-7.51182e-13,2962.53,20.9534], Tmin=(421.583,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.5474,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.011 kJ/mol
""",
    rank = 5,
)

entry(
    index = 835,
    label = "CDCC(F)DCF",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84303,0.012444,9.96837e-05,-2.3406e-07,1.6316e-10,-33352.3,10.4435], Tmin=(10,'K'), Tmax=(467.585,'K')),
            NASAPolynomial(coeffs=[2.68748,0.0366262,-2.37559e-05,7.32743e-09,-8.62561e-13,-33400.5,13.4687], Tmin=(467.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-277.324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.093 kJ/mol
""",
    rank = 5,
)

entry(
    index = 836,
    label = "C[C](O)C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66224,0.0320717,-2.4264e-06,-1.87691e-08,9.52097e-12,-63945.5,10.5467], Tmin=(10,'K'), Tmax=(886.56,'K')),
            NASAPolynomial(coeffs=[5.75203,0.0319999,-1.81364e-05,4.94905e-09,-5.24299e-13,-64683.8,-1.35754], Tmin=(886.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-531.691,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 837,
    label = "[O]CDCDCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73604,0.0281276,-7.33658e-05,1.85727e-07,-1.78764e-10,-741.669,10.2881], Tmin=(10,'K'), Tmax=(355.783,'K')),
            NASAPolynomial(coeffs=[3.31489,0.0236541,-1.56829e-05,4.89414e-09,-5.80106e-13,-653.422,12.7037], Tmin=(355.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-6.17063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 838,
    label = "OCDC(O)F",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {8,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89987,0.00615295,9.84987e-05,-2.14944e-07,1.38155e-10,-59583.4,9.28489], Tmin=(10,'K'), Tmax=(533.909,'K')),
            NASAPolynomial(coeffs=[4.1873,0.0256682,-1.72061e-05,5.54562e-09,-6.81317e-13,-59923,5.18632], Tmin=(533.909,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-495.438,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.528 kJ/mol
""",
    rank = 5,
)

entry(
    index = 839,
    label = "FCDC(F)OOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 O u0 p2 c0 {3,S} {6,S}
6 O u0 p2 c0 {5,S} {7,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5995,0.0355787,-1.43779e-05,-2.77212e-08,2.41594e-11,-37954.2,12.0894], Tmin=(10,'K'), Tmax=(644.259,'K')),
            NASAPolynomial(coeffs=[7.62617,0.0234497,-1.61059e-05,5.07677e-09,-6.00738e-13,-38740.1,-7.6397], Tmin=(644.259,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.619,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 840,
    label = "CC1DC[C]1F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {4,S} {9,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85455,0.0127088,5.1302e-05,-1.0062e-07,5.54379e-11,26462.3,9.06556], Tmin=(10,'K'), Tmax=(597.648,'K')),
            NASAPolynomial(coeffs=[2.64208,0.0307648,-1.89661e-05,5.59505e-09,-6.34663e-13,26429.7,12.8056], Tmin=(597.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.998,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.757 kJ/mol
""",
    rank = 5,
)

entry(
    index = 841,
    label = "C[C]DCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92685,0.0149344,7.26385e-06,-1.4417e-08,5.01007e-12,7035.83,7.89259], Tmin=(10,'K'), Tmax=(1128.55,'K')),
            NASAPolynomial(coeffs=[5.52548,0.0181633,-8.85046e-06,2.08622e-09,-1.92891e-13,6108.56,-2.52281], Tmin=(1128.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (58.5253,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 842,
    label = "FCDC(CF)OF",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  F u0 p3 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65974,0.0379398,-2.39663e-05,4.91039e-09,4.44605e-13,-48019.5,11.8612], Tmin=(10,'K'), Tmax=(1135.68,'K')),
            NASAPolynomial(coeffs=[10.1768,0.021811,-1.1678e-05,2.98866e-09,-2.97253e-13,-49939.9,-22.3469], Tmin=(1135.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-399.256,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 843,
    label = "[CH2]C(O)DCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,D}
5 O u0 p2 c0 {4,S} {8,S}
6 C u0 p0 c0 {4,D} {7,S} {9,S}
7 F u0 p3 c0 {6,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8864,0.00698382,0.00011336,-2.46685e-07,1.58507e-10,-25446.9,9.17004], Tmin=(10,'K'), Tmax=(533.1,'K')),
            NASAPolynomial(coeffs=[4.15396,0.0296093,-1.96128e-05,6.28118e-09,-7.69863e-13,-25825.4,4.76451], Tmin=(533.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.615,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 844,
    label = "FCC1DCC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95989,0.0135422,3.50755e-05,-5.07942e-08,1.93526e-11,6713.68,9.33843], Tmin=(10,'K'), Tmax=(921.714,'K')),
            NASAPolynomial(coeffs=[3.64952,0.0300564,-1.64829e-05,4.35059e-09,-4.4688e-13,6126.62,7.31552], Tmin=(921.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.8695,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 845,
    label = "[O]CDCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96504,0.00223397,6.11099e-05,-1.25963e-07,8.13247e-11,-22822.9,8.77893], Tmin=(10,'K'), Tmax=(483.091,'K')),
            NASAPolynomial(coeffs=[2.69359,0.0193489,-1.24856e-05,3.82459e-09,-4.47646e-13,-22776.9,13.1923], Tmin=(483.091,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.323 kJ/mol
""",
    rank = 5,
)

entry(
    index = 846,
    label = "FCCO[C](F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51195,0.0538702,-0.000187479,5.30977e-07,-5.30945e-10,-80527.1,12.5231], Tmin=(10,'K'), Tmax=(350.403,'K')),
            NASAPolynomial(coeffs=[2.00012,0.044017,-2.92419e-05,9.11331e-09,-1.07745e-12,-80254.7,20.6063], Tmin=(350.403,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-669.555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 847,
    label = "[O]C(O)F",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {6,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95945,0.00229111,5.58813e-05,-1.01055e-07,5.52755e-11,-48242.6,8.77663], Tmin=(10,'K'), Tmax=(594.19,'K')),
            NASAPolynomial(coeffs=[2.6663,0.0205371,-1.42648e-05,4.67042e-09,-5.77026e-13,-48257.4,12.9249], Tmin=(594.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-401.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 848,
    label = "CCD[C]CF",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u1 p0 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66824,0.0348056,-7.80631e-05,2.10704e-07,-1.94406e-10,3694.01,9.32956], Tmin=(10,'K'), Tmax=(413.115,'K')),
            NASAPolynomial(coeffs=[1.12276,0.0396376,-2.36623e-05,6.81174e-09,-7.58956e-13,4073.41,21.4062], Tmin=(413.115,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.7036,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.331 kJ/mol
""",
    rank = 5,
)

entry(
    index = 849,
    label = "FC1CDCC1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08621,-0.00735985,0.00013514,-2.14106e-07,1.08309e-10,-6391.88,9.20884], Tmin=(10,'K'), Tmax=(621.742,'K')),
            NASAPolynomial(coeffs=[-0.227836,0.0396921,-2.49326e-05,7.45422e-09,-8.52294e-13,-6228.42,24.9719], Tmin=(621.742,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.151,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.227 kJ/mol
""",
    rank = 5,
)

entry(
    index = 850,
    label = "C#CC(F)(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8653,0.00842938,0.000103376,-2.47504e-07,1.67599e-10,-52764.8,9.14969], Tmin=(10,'K'), Tmax=(526.551,'K')),
            NASAPolynomial(coeffs=[5.73537,0.0223445,-1.63744e-05,5.53975e-09,-6.99453e-13,-53351.6,-2.3747], Tmin=(526.551,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-438.753,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.855 kJ/mol
""",
    rank = 5,
)

entry(
    index = 851,
    label = "CCDCCF",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  F u0 p3 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82855,0.0204732,2.56785e-05,-3.94206e-08,1.43042e-11,-25106.8,8.38851], Tmin=(10,'K'), Tmax=(983.707,'K')),
            NASAPolynomial(coeffs=[3.16444,0.0365882,-1.93495e-05,4.95791e-09,-4.97192e-13,-25625.2,8.28253], Tmin=(983.707,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-208.731,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 1.415 kJ/mol
""",
    rank = 5,
)

entry(
    index = 852,
    label = "FC1[CH]CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 O u0 p2 c0 {2,S} {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95729,0.00255541,9.50302e-05,-1.72479e-07,9.86177e-11,-14976.6,10.1026], Tmin=(10,'K'), Tmax=(523.377,'K')),
            NASAPolynomial(coeffs=[0.549688,0.0363552,-2.40706e-05,7.54592e-09,-9.00152e-13,-14726.1,23.3211], Tmin=(523.377,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.539,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.139 kJ/mol
""",
    rank = 5,
)

entry(
    index = 853,
    label = "C#COOF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84719,0.0103331,9.43305e-05,-2.71158e-07,2.1152e-10,34199.6,9.73036], Tmin=(10,'K'), Tmax=(473.062,'K')),
            NASAPolynomial(coeffs=[6.58561,0.0154118,-1.12971e-05,3.86037e-09,-4.9303e-13,33624.6,-4.77021], Tmin=(473.062,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (284.327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 854,
    label = "OCDCD[C]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87011,0.00981112,9.32752e-05,-2.78008e-07,2.38367e-10,5772.82,10.0924], Tmin=(10,'K'), Tmax=(406.737,'K')),
            NASAPolynomial(coeffs=[4.47078,0.0214577,-1.44125e-05,4.60536e-09,-5.58973e-13,5578.76,5.94989], Tmin=(406.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.0001,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 855,
    label = "FCC1C[C]1F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {3,S} {4,S} {6,S}
6  F u0 p3 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87779,0.0172817,4.80273e-05,-8.01765e-08,3.52607e-11,-15569.5,11.1963], Tmin=(10,'K'), Tmax=(793.174,'K')),
            NASAPolynomial(coeffs=[3.47609,0.0367277,-2.16918e-05,6.11247e-09,-6.64184e-13,-16053.8,9.58689], Tmin=(793.174,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-129.434,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 856,
    label = "CC(C)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  F u0 p3 c0 {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90916,0.00634724,8.05679e-05,-1.38794e-07,7.62611e-11,-39941,6.47502], Tmin=(10,'K'), Tmax=(470.295,'K')),
            NASAPolynomial(coeffs=[0.148155,0.0383356,-2.14578e-05,5.83183e-09,-6.18701e-13,-39587.2,21.7825], Tmin=(470.295,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-332.115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.367 kJ/mol
""",
    rank = 5,
)

entry(
    index = 857,
    label = "CDC(F)CD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {9,S}
5 C u1 p0 c0 {4,D} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84722,0.0113792,0.000112407,-2.88651e-07,2.18003e-10,-4336.03,11.2387], Tmin=(10,'K'), Tmax=(446.409,'K')),
            NASAPolynomial(coeffs=[3.62699,0.0323264,-2.17338e-05,6.88722e-09,-8.27181e-13,-4505.42,10.0061], Tmin=(446.409,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-36.0649,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 858,
    label = "CCD[C]F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u1 p0 c0 {2,D} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89968,0.00987898,3.05874e-05,-4.91531e-08,2.17103e-11,7904.62,8.00727], Tmin=(10,'K'), Tmax=(748.088,'K')),
            NASAPolynomial(coeffs=[2.46372,0.0249052,-1.42758e-05,3.9576e-09,-4.26451e-13,7913.85,13.1439], Tmin=(748.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.7183,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.14 kJ/mol
""",
    rank = 5,
)

entry(
    index = 859,
    label = "[O]CC(F)DCF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {3,D} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76434,0.0197744,6.04222e-05,-1.7294e-07,1.30711e-10,-34874.9,11.4031], Tmin=(10,'K'), Tmax=(454.424,'K')),
            NASAPolynomial(coeffs=[3.72188,0.0323968,-2.16738e-05,6.81397e-09,-8.12197e-13,-34997.5,10.1829], Tmin=(454.424,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 860,
    label = "[O]C(DCF)CF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 F u0 p3 c0 {3,S}
5 C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72596,0.0250146,7.34851e-06,-3.32647e-08,1.7646e-11,-49482.8,11.4785], Tmin=(10,'K'), Tmax=(755.427,'K')),
            NASAPolynomial(coeffs=[5.06547,0.0275334,-1.67379e-05,4.83413e-09,-5.36267e-13,-49959.5,3.5766], Tmin=(755.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-411.448,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.801 kJ/mol
""",
    rank = 5,
)

entry(
    index = 861,
    label = "FCC[C](F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85935,0.0254589,4.33237e-06,-1.93329e-08,7.79911e-12,-62433.7,10.7977], Tmin=(10,'K'), Tmax=(1054.63,'K')),
            NASAPolynomial(coeffs=[7.44257,0.0247994,-1.31214e-05,3.32609e-09,-3.28145e-13,-63908.7,-10.0892], Tmin=(1054.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-519.059,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.047 kJ/mol
""",
    rank = 5,
)

entry(
    index = 862,
    label = "CC[CH]C(F)F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {13,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77428,0.0332593,2.15695e-06,-1.84357e-08,7.14949e-12,-43852.6,10.8892], Tmin=(10,'K'), Tmax=(1121.62,'K')),
            NASAPolynomial(coeffs=[7.8772,0.0329067,-1.64683e-05,3.98551e-09,-3.78033e-13,-45671.2,-13.38], Tmin=(1121.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-364.579,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 7.086 kJ/mol
""",
    rank = 5,
)

entry(
    index = 863,
    label = "ODCC(F)F",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86339,0.0151887,9.38707e-06,-2.31192e-08,1.01687e-11,-66767.2,9.86831], Tmin=(10,'K'), Tmax=(877.326,'K')),
            NASAPolynomial(coeffs=[4.83706,0.0189473,-1.10554e-05,3.06537e-09,-3.27723e-13,-67253.5,3.5003], Tmin=(877.326,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-555.129,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.32 kJ/mol
""",
    rank = 5,
)

entry(
    index = 864,
    label = "FCCC(F)F",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90038,0.0222495,2.03222e-05,-3.64677e-08,1.38226e-11,-87344.8,10.6091], Tmin=(10,'K'), Tmax=(997.111,'K')),
            NASAPolynomial(coeffs=[5.79886,0.0306619,-1.64452e-05,4.23627e-09,-4.24905e-13,-88520.2,-2.54003], Tmin=(997.111,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-726.17,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.226 kJ/mol
""",
    rank = 5,
)

entry(
    index = 865,
    label = "CDC1CDC1F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93288,0.00387937,8.61359e-05,-1.62711e-07,9.27895e-11,24519.5,8.11604], Tmin=(10,'K'), Tmax=(576.658,'K')),
            NASAPolynomial(coeffs=[2.55849,0.0289713,-1.96036e-05,6.32046e-09,-7.74911e-13,24419.3,11.7471], Tmin=(576.658,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.366 kJ/mol
""",
    rank = 5,
)

entry(
    index = 866,
    label = "FCDCC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80214,0.0200363,2.48872e-05,-5.57996e-08,2.76955e-11,-70958.9,10.8047], Tmin=(10,'K'), Tmax=(738.943,'K')),
            NASAPolynomial(coeffs=[4.5191,0.0285284,-1.74674e-05,5.07202e-09,-5.64927e-13,-71402.7,5.27697], Tmin=(738.943,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-589.998,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.122 kJ/mol
""",
    rank = 5,
)

entry(
    index = 867,
    label = "C[CH]C(DO)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80608,0.0188663,1.78447e-05,-3.89388e-08,1.79971e-11,-36991.3,9.26369], Tmin=(10,'K'), Tmax=(786.089,'K')),
            NASAPolynomial(coeffs=[3.88553,0.0275413,-1.60334e-05,4.48533e-09,-4.85791e-13,-37284.3,7.11522], Tmin=(786.089,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-307.573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 868,
    label = "FC#CC[CH]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83133,0.0189719,0.000171566,-9.51279e-07,1.58156e-09,5942.89,11.2383], Tmin=(10,'K'), Tmax=(202.076,'K')),
            NASAPolynomial(coeffs=[3.83999,0.0319008,-2.1649e-05,6.97312e-09,-8.52622e-13,5915.79,10.5485], Tmin=(202.076,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (49.5048,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 4.669 kJ/mol
""",
    rank = 5,
)

entry(
    index = 869,
    label = "CDC(F)C(F)(F)F",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {8,S} {9,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83518,0.0110923,0.000137745,-3.45812e-07,2.51901e-10,-99420.1,10.5863], Tmin=(10,'K'), Tmax=(474.871,'K')),
            NASAPolynomial(coeffs=[4.53858,0.0337265,-2.3962e-05,7.85324e-09,-9.6288e-13,-99809,4.32621], Tmin=(474.871,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-826.655,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.89 kJ/mol
""",
    rank = 5,
)

entry(
    index = 870,
    label = "OC[CH]F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87378,0.0113902,4.18638e-05,-9.5621e-08,6.46287e-11,-28271.7,9.54361], Tmin=(10,'K'), Tmax=(385.146,'K')),
            NASAPolynomial(coeffs=[2.43966,0.0262846,-1.61445e-05,4.78879e-09,-5.48107e-13,-28161.2,15.0941], Tmin=(385.146,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-235.07,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.543 kJ/mol
""",
    rank = 5,
)

entry(
    index = 871,
    label = "CC#CC(F)F",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,T}
3  C u0 p0 c0 {2,T} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8493,0.031916,-1.81122e-05,4.58207e-09,-3.79721e-13,-30301.4,10.7279], Tmin=(10,'K'), Tmax=(1727.62,'K')),
            NASAPolynomial(coeffs=[17.9884,0.00482175,5.13287e-07,-7.14815e-10,1.13215e-13,-36028.9,-67.6526], Tmin=(1727.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-251.969,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.836 kJ/mol
""",
    rank = 5,
)

entry(
    index = 872,
    label = "[CH]DCCDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,D} {8,S}
5 C u0 p0 c0 {4,D} {6,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92091,0.00494226,0.000106624,-2.22649e-07,1.42272e-10,18553.4,10.2216], Tmin=(10,'K'), Tmax=(510.038,'K')),
            NASAPolynomial(coeffs=[2.57251,0.0318505,-2.05475e-05,6.36248e-09,-7.5535e-13,18478.5,13.7364], Tmin=(510.038,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (154.238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.253 kJ/mol
""",
    rank = 5,
)

entry(
    index = 873,
    label = "OCO[C](F)F",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76633,0.0229659,1.64269e-05,-4.64969e-08,2.39773e-11,-75894.7,10.8795], Tmin=(10,'K'), Tmax=(742.789,'K')),
            NASAPolynomial(coeffs=[5.07975,0.0277148,-1.70363e-05,4.96346e-09,-5.54219e-13,-76415.9,2.73829], Tmin=(742.789,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-631.041,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.769 kJ/mol
""",
    rank = 5,
)

entry(
    index = 874,
    label = "FC#CCDCF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 C u0 p0 c0 {4,D} {6,S} {8,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8245,0.0140872,8.67307e-05,-2.5547e-07,2.12075e-10,-3995.66,10.7447], Tmin=(10,'K'), Tmax=(416.49,'K')),
            NASAPolynomial(coeffs=[4.15361,0.027089,-1.83063e-05,5.83672e-09,-7.05136e-13,-4163.25,7.76232], Tmin=(416.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.2241,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.57 kJ/mol
""",
    rank = 5,
)

entry(
    index = 875,
    label = "C[C]DC(F)F",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79335,0.0217919,-4.37296e-06,-7.39967e-09,3.67642e-12,-16664.5,9.26402], Tmin=(10,'K'), Tmax=(1030.14,'K')),
            NASAPolynomial(coeffs=[6.0731,0.0194739,-1.05121e-05,2.73083e-09,-2.76439e-13,-17480.9,-3.48493], Tmin=(1030.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-138.556,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

entry(
    index = 876,
    label = "[C]#CCDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,S} {7,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84288,0.0219933,-1.41484e-05,4.2676e-09,-4.72653e-13,50420.6,9.73308], Tmin=(10,'K'), Tmax=(1566.68,'K')),
            NASAPolynomial(coeffs=[10.198,0.008151,-3.17705e-06,5.69953e-10,-3.75521e-14,48136.8,-24.7131], Tmin=(1566.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (419.212,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.317 kJ/mol
""",
    rank = 5,
)

entry(
    index = 877,
    label = "FC1CC(F)O1",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95496,0.00267336,0.000109217,-1.94067e-07,1.0865e-10,-67896.6,9.93873], Tmin=(10,'K'), Tmax=(525.533,'K')),
            NASAPolynomial(coeffs=[-0.466111,0.0438471,-2.9777e-05,9.4953e-09,-1.14569e-12,-67535.8,27.4351], Tmin=(525.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-564.542,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 5.486 kJ/mol
""",
    rank = 5,
)

entry(
    index = 878,
    label = "[CH]DCDCF",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9073,0.00621607,7.54633e-05,-1.97405e-07,1.48211e-10,19672.6,8.53809], Tmin=(10,'K'), Tmax=(471.969,'K')),
            NASAPolynomial(coeffs=[4.94469,0.015244,-9.86379e-06,3.11955e-09,-3.80639e-13,19376.2,2.20958], Tmin=(471.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (163.551,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.21 kJ/mol
""",
    rank = 5,
)

entry(
    index = 879,
    label = "OO[CH]CF",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91053,0.0101301,0.000192322,-9.31686e-07,1.54752e-09,-20418.4,10.4002], Tmin=(10,'K'), Tmax=(151.501,'K')),
            NASAPolynomial(coeffs=[3.09483,0.0316666,-2.09075e-05,6.60356e-09,-7.9591e-13,-20393.7,12.7961], Tmin=(151.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-169.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.966 kJ/mol
""",
    rank = 5,
)

entry(
    index = 880,
    label = "CD[C]OCF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86016,0.0197654,8.36555e-06,-2.0904e-08,8.25179e-12,-11128.7,10.2942], Tmin=(10,'K'), Tmax=(1000.58,'K')),
            NASAPolynomial(coeffs=[5.45415,0.0235812,-1.2628e-05,3.25981e-09,-3.28211e-13,-11957.7,0.0546239], Tmin=(1000.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.5051,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 3.046 kJ/mol
""",
    rank = 5,
)

entry(
    index = 881,
    label = "OC(F)DCOF",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {8,S}
5 O u0 p2 c0 {4,S} {6,S}
6 F u0 p3 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56705,0.047048,3.99933e-05,-7.29537e-07,1.37942e-09,-91810.7,12.2202], Tmin=(10,'K'), Tmax=(237.577,'K')),
            NASAPolynomial(coeffs=[6.90145,0.0234495,-1.64706e-05,5.44571e-09,-6.78747e-13,-92061,-1.00672], Tmin=(237.577,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-763.329,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""Average of 50 error canceling reactions with G4 level of theory""",
    longDesc = 
u"""
Standard deviation of Hf298 from 50 G4 rxns was 2.936 kJ/mol
""",
    rank = 5,
)

entry(
    index = 882,
    label = "CCO[CH]F",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93905,0.0230006,8.35247e-06,-1.82753e-08,6.15996e-12,-31822,9.18448], Tmin=(10,'K'), Tmax=(1204.1,'K')),
            NASAPolynomial(coeffs=[8.00705,0.0239693,-1.08956e-05,2.37041e-09,-2.0051e-13,-33851.6,-15.5564], Tmin=(1204.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-264.535,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 calculation',
    referenceType = "theory",
    shortDesc = u"""G4 with BACs""",
    longDesc = 
u"""

""",
    rank = 5,
)

