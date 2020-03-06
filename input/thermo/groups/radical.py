#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "Radical",
    group = "OR{RJ, RJ2_triplet, RJ3, RJ4}",
    thermo = u'RJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "RJ",
    group = 
"""
1 * R u1
""",
    thermo = u'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10000,
    label = "RJ4",
    group = 
"""
1 * R u4
""",
    thermo = u'CJ4',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CJ",
    group = 
"""
1 * C u1
""",
    thermo = u'CsJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CsJ",
    group = 
"""
1 * Cs u1
""",
    thermo = u'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30000,
    label = "CJ4",
    group = 
"""
1 * C u4
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (493.90,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""Dummy group if forbidden C u4 is created in edge""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CH3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol','+|-',0.1),
        S298 = (0.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Cs_P_ClCl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   Cl u0 {1,S}
4   Cl u0 {1,S}
""",
    thermo = u'CsCsJ(Cl)(Cl)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CsCsJ(Cl)(Cl)",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cl u0 {1,S}
4   Cl u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.311,-0.918,-1.488,-2.003,-2.854,-3.497,-4.495],'cal/(mol*K)'),
        H298 = (95.72,'kcal/mol'),
        S298 = (1.242,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculations""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "RCCJ(Cl)(Cl)",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cl u0 {2,S}
7   Cl u0 {2,S}
""",
    thermo = u'Cs_P_ClCl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Cs_P_Cl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   Cl u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.554,-0.087,-0.767,-1.403,-2.452,-3.228,-4.393],'cal/(mol*K)'),
        H298 = (98.211,'kcal/mol'),
        S298 = (2.964,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculations""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CsCsJ(Cl)",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   Cl u0 {1,S}
""",
    thermo = u'Cs_P_Cl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "RCCJ(Cl)",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   Cl u0 {2,S}
""",
    thermo = u'Cs_P_Cl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cs_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 13,
    label = "C=C(O)CJ",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-2.3,-4.6,-7.1,-11,-13.5,-16.6],'J/(mol*K)'),
        H298 = (376.8,'kJ/mol'),
        S298 = (-3.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 14,
    label = "CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (3.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CJC(C)OC",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   O2s u0 {1,S} {7,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,1.8,-2,-5.5,-11,-14.7,-19.8],'J/(mol*K)'),
        H298 = (429.9,'kJ/mol'),
        S298 = (7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 16,
    label = "CJC(C)2O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,1.1,-2.1,-5.1,-9.7,-13.1,-18.5],'J/(mol*K)'),
        H298 = (431.1,'kJ/mol'),
        S298 = (5.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 17,
    label = "C=CC(C)(O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.5,-2.7,-5.5,-7.9,-11.8,-14.6,-19],'J/(mol*K)'),
        H298 = (431.9,'kJ/mol'),
        S298 = (9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 18,
    label = "C=CC(O)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,0.9,-2.4,-5.2,-9.7,-13,-18.1],'J/(mol*K)'),
        H298 = (432.3,'kJ/mol'),
        S298 = (6.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 19,
    label = "CJC(C)(C=O)O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.6,5.1,2.3,-0.9,-6.8,-11.3,-17.8],'J/(mol*K)'),
        H298 = (430.9,'kJ/mol'),
        S298 = (3.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 20,
    label = "CJC(O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
r       Tdat = 
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
inx2, {1,S} {8,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-0.2,-2,-4,-8.1,-11.6,-17.2],'J/(mol*K)'),
    
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 22,
    label = "CsJ-HCsH-O2sHCs-HF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {8,S}
4   O2s u0 p2 c0 {1,S} {9,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "CsJ-HHCs-HO2sCs-HHF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3  * Cs  u1 p0 c0 {1,S} {8,S} {9,S}
4    O2s u0 p2 c0 {1,S} {10,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "CJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
5   H   u0 {S",
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 25,
    label = "CJC(C)2C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.9,2.5,-1.1,-4.4,-9.7,-13.6,-19],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (7.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 26,
    label = "CJC(C=O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.5,0.6,-1.9,-6.9,-10.9,-17.1],'J/(mol*K)'),
        H298 = (427,'kJ/mol'),
        S298 = (8.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 27,
    label = "C=CC(C=O)2CJ",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs  u1 {1,S} {6,S} {7,S}
3    CO  u0 {1,S} {9,D}
4    CO  u0 {1,S} {10,D}
5    Cd  u0 {1,S} {8,D}
6    H   u0 {2,S}
7    H   u0 {2,S}
8    C   u0 {5,D}
9    O2d u0 {3,D}
10   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,2.4,-0.6,-3.5,-8.4,-12.1,-17.6],'J/(mol*K)'),
        H298 = (429.8,'kJ/mol'),
        S298 = (5.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 28,
    label = "C=CC(C)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,0.6,-2.7,-5.8,-10.8,-14.4,-19.3],'J/(mol*K)'),
        H298 = (430.6,'kJ/mol'),
        S298 = (9.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 29,
    label = "CJC(C)C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6,0.2,-3,-5.8,-10.5,-14.1,-19.3],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 30,
    label = "C=C(C=O)CJ",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,D}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8,-1.2,-2.4,-4.4,-8.2,-11.3,-15.9],'J/(mol*K)'),
        H298 = (374,'kJ/mol'),
        S298 = (-16.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 31,
    label = "CJCC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {5,S} {6,S}
2   C   u0 {1,S} {3,S}
3   Cd  u0 {2,S} {4,D}
4   Cdd u0 {3,D} {7,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3,-5.8,-8.1,-10.1,-13.4,-15.9,-19.9],'J/(mol*K)'),
        H298 = (420.3,'kJ/mol'),
    ), = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 32,
    label = "CJC(C)C=C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.2,-0.5,-4.1,-7.2,-11.8,-15,-19.5],'J/(mol*K)'),
        H298 = (430.1,'kJ/mol'),
        S298 = (9.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 33,
    label = "C=C(CJ)C=C=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {5,D}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,D}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-5.6,-5.7,-6.4,-8.2,-10,-12.8],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (-8.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 34,
    label = "CsCsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "CCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Cpdan
1 ,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""
""",
)

entry(
    index = 37,
    label = "CsJ-CsHH-CsHH-F1s",
u"""0 c
3   Cs  u0 p0 c0 {1,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "CsJ-CsHH-CsHH-F1sF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3 * Cs  u1 p0 c0 {1,S} {8,S} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "CsJ-HCsH-HHCs-HF1sO2s",
    group = 
muliplicityp0 
4    H   u0 p0 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    O2s u0 p2 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
u"""

""",
)
entry(
    index = 40,
    label = "CsJ-HHCs-HCdH-CdH-F1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
 3   Cs  40 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.52872,1.59571,-1.06176,-3.97638,-9.20618,-12.5431,-17.8507],'J/(mol*K)'),
        H298 = (
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 41,
    labe
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.44777,0.565935,-2.25791,-4.76744,-8.96853,-12.2217,-17.2041],'J/(mol*K)'),
        H298 = (428.894,'kJ/mol'),
        S298 = (2.98534,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "CsJ-CsHH-F1sF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.7854,0.378473,-2.54116,-5.02367,-8.44478,-10.9752,-15.2104],'J/(mol*K)'),
        H298 = (435.935,'kJ/mol'),
        S298 = (-6.64947,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "Benzyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492,0.642,0.109,-0.656,-1.606,-2.293,-4.101],'cal/(mol*K)'),
        H298 = (90.788,'kcal/mol','+|-',2.4),
        S298 = (-5.163,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted From  Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
[CH2]C1C=CC=CC=1
""",
)

entry(
    index = 46,
    label = "Allyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (-2.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C=CC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],'cal/(mol*K)'),
        H298 = (80,'kcal/mol'),
        S298 = (-1.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "CTCC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Ct u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],'cal/(mol*K)'),
        H298 = (81,'kcal/mol'),
        S298 = (-3.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "CJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
    thermo = ThermoData(
        Tdata = ([300,415.6],'J/(mol*K)'),
        H298 = (373.5,'kJ/mol'),
        S298 = (-1.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 50,
    label = "CsJ-HHCd-CdCs-F1sH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S} {8,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CsJ-HHCd-CsCd-HHF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S} {8,S}
4   Cs  u0 p0 c0 {1,S} {9,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "CsJ-CdHH-CsCd-F1sHHH",
    group = 
"""
multiplicity [2]
1    Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2    Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3  * Cs  u1 p0 c0 {1,S} {7,S} {8,S}
4    Cd  u0 p0 c0 {1,D} {9,S} {10,S}
5    H   u0 p0 c0 {2,S}
6    H   u0 p0 c0 {2,S}
7    H   u0 p0 c0 {3,S}
8    H   u0 p0 c0 {3,S}
9    F1s u0 p3 c0 {4,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CsJ-HCdH-F1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "CsJ-HCdH-F1sCd",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CsJ-CdHH-CdF1s-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CsJ-HHCd-CdH-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99366,-3.00222,-4.41883,-6.27365,-9.85766,-13.0515,-18.7774],'J/(mol*K)'),
        H298 = (365.641,'kJ/mol'),
        S298 = (-7.8332,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CsJ-HCdH-HCd-HCs-F1sH",
    group = 
"""
multiplicity [2]
1    Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2    Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {7,S} {8,S}
4  * Cs  u1 p0 c0 {2,S} {9,S} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {2,S}
7    F1s u0 p3 c0 {3,S}
8    H   u0 p0 c0 {3,S}
9    H   u0 p0 c0 {4,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15233,-2.7263,-3.99622,-5.98375,-10.7146,-13.532,-18.3585],'J/(mol*K)'),
        H298 = (362.293,'kJ/mol'),
        S298 = (-1.17539,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CsJ-HHCd-CddH-Cd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
4   Cd  u0 p0 c0 {3,D} {8,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],'cal/(mol*K)'),
        H298 = (89.4,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5,1.1,-0.4,-2.3,-6.1,-9.2,-14.4],'J/(mol*K)'),
        H298 = (402.4,'kJ/mol'),
        S298 = (-7.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 61,
    label = "C2JC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],'cal/(mol*K)'),
        H298 = (94.4,'kcal/mol'),
        S298 = (-1.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "CsJ-COHH-CsO2d-HF1s",
    group = 
"""
multiplicity [2]
1   CO  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cs  u1 p0 c0 {1,S} {7,S} {8,S}
4   O2d u0 p2 c0 {1,D}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "Cs_S_Cl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   Cl u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.121,-0.686,-1.327,-1.847,-2.674,-3.316,-4.388],'cal/(mol*K)'),
        H298 = (96.662,'kcal/mol'),
        S298 = (3.769,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "(Cs)2ClCsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cl u0 {1,S}
""",
    thermo = u'Cs_S_Cl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Cs_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
esc = 
u"""

""",
)
entry(
    index = 66,
    label = "CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 67,
    label = "C=CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.2,2.4,1,-1.8,-4.5,-9.8],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-19.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 68,
""",hortDesc = u"""
    longDesc 

entry(
    index = 70,
    label = "CsJ-CsCsH-HF1sHHO2sH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  * Cs  u1 p0 c0 {1,S} {2,S} {10,S}
4    O2s u0 p2 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {2,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "CCJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 72,
    label = "CCJC(C)=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   C   u0 {1,S} {6,S}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-4,-6.2,-7.9,-10.8,-12.9,-16.9],'J/(mol*K)'),
        H298 = (365.4,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 73,
    label = "(Cs)2CsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cs_S',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "cyclopentene-4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "bicyclo[2.1.1]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (104.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.2,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "bicyclo[2.1.0]pent-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
""",
)

entry(
    index = 78,
    label = "bicyclo[1.1.1]pentane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "tricyclo[1.1.1.0(1,3)]pentane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (111.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "bicyclo[2.1.1]hexane-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
      
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)
 u,}{= 

""",
)

entry(
    index = 84,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {7,S}
2   Cs u0 {1,S} {3,S} {4,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {5,S}
5   C  u0 {1,S} {4,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "bicyclo[2.1.0]pentane-secondary-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "bicyclo[1.1.0]butane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {5,S}
4   Cs u0 {1,S} {2,S}
5   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "bicyclo[3.1.0]hexane-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "bicyclo[3.1.1]heptane-C6",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "bicyclo[2.2.2]octane-C2",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "tricyclo[2.2.2.0(1,4)]octane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "cyclobutane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "bicyclo[2.1.0]pentane-secondary-C4",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {5,S} {6,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "bicyclo[2.2.0]hexane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {7,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "bicyclo[3.2.0]heptane-C5-6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "bicyclo[3.1.1]heptane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
u7  Cs u0 {3,
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    lone"""
S3 *,   u0 {= ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
      0mC

""",
)
entry(
    index = 108,
    label = "7-norbornyl",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "2-norbornyl",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S} {8,S}
2 * Cs u1 {1,S} {5,S} {9,S}
3   Cs u0 {4,S} {5,S} {7,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {3,S} {6,S}
u9   H  0 {2,S} oD-P, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

    index = 116,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        S298 = (4.51,)H
)

entry(
    index = 112,
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "cycloheptane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (92.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "bicyclo[3.2.0]heptane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "bicyclo[3.2.0]heptane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S}
3 * Cs u1 {4,S} {5,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "bicyclo[3.1.1]heptane-C3",
    group = 
"""
1   Cs u0 {4,S} {5,S} {7,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "octahydro-pentalene-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {8,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   C  u0 {4,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "octahydro-pentalene-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {5,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "bicyclo[4.2.0]octane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {5,S}
5   C  u0 {2,S} {4,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "bicyclo[4.2.0]octane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {8,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "CCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "RCCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (5.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "CsJ-CsCsH-HHHHCsH-HF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  * Cs  u1 p0 c0 {1,S} {2,S} {10,S}
4    Cs  u0 p0 c0 {1,S} {11,S} {12,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {2,S}
10   H   u0 p0 c0 {3,S}
11   F1s u0 p3 c0 {4,S}
12   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.29062,0.160003,-1.82679,-4.72633,-10.2156,-13.159,-17.6847],'J/(mol*K)'),
        H298 = (408.985,'kJ/mol'),
        S298 = (5.90423,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "RCCJCC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    C  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "cyclopentane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {6,S} {7,S}
2    Cs u0 {3,S} {5,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S} {5,S}
5    C  u0 {2,S} {4,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (96.4,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "cyclohexane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2    Cs u0 {3,S} {5,S} {9,S} {10,S}
3  * Cs u1 {1,S} {2,S} {11,S}
4    C  u0 {1,S} {6,S}
5    C  u0 {2,S} {6,S}
6    C  u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {2,S}
10   H  u0 {2,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "CsJ-CsHCs-F1sCsHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cs  u0 p0 c0 {2,S} {8,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "CsJ-CsHCs-HHCsF1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cs  u0 p0 c0 {2,S} {8,S} {9,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.21605,-0.807235,-3.29302,-5.872,-10.3708,-13.5034,-18.411],'J/(mol*K)'),
        H298 = (426.099,'kJ/mol'),
        S298 = (8.61395,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "CsJ-CsCsH-HHCsHHF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  * Cs  u1 p0 c0 {1,S} {2,S} {10,S}
4    Cs  u0 p0 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {2,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "CsJ-CsHCs-HCsHF1sHH-H",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  * Cs  u1 p0 c0 {1,S} {2,S} {10,S}
4    Cs  u0 p0 c0 {1,S} {11,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {2,S}
10   H   u0 p0 c0 {3,S}
11   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "CsJ-HCsCs-HF1sCsHHH-HH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  * Cs  u1 p0 c0 {1,S} {2,S} {10,S}
4    Cs  u0 p0 c0 {1,S} {11,S} {12,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {2,S}
10   H   u0 p0 c0 {3,S}
11   H   u0 p0 c0 {4,S}
12   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.913041,-0.366994,-2.30817,-5.00445,-10.212,-13.2644,-17.8113],'J/(mol*K)'),
        H298 = (417.157,'kJ/mol'),
        S298 = (18.8763,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "CsJ-CsHCs-F1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.52002,-0.450195,-2.61224,-5.14321,-9.8271,-12.9876,-17.9878],'J/(mol*K)'),
        H298 = (417.741,'kJ/mol'),
        S298 = (7.23418,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "CsJ-HCsCs-F1sF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "CsJ-HCsCs-HF1sF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "CsJ-HCsCs-F1sHHF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {6,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {3,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "CsJ-CsCsH-HF1sHF1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cs  u0 p0 c0 {2,S} {8,S} {9,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.730434,-0.393532,-2.67709,-5.60513,-10.6461,-13.1435,-17.9455],'J/(mol*K)'),
        H298 = (426.528,'kJ/mol'),
        S298 = (14.9159,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "Benzyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0448,-1.3002,-2.199,-2.5546,-2.5872,-2.8074,-5.6336],'cal/(mol*K)'),
        H298 = (88.064,'kcal/mol','+|-',2.4),
        S298 = (-4.8554,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted From Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[CH]C1C=CC=CC=1
CC[CH]C1C=CC=CC=1
CCC[CH]C1C=CC=CC=1
CCCC[CH]C1C=CC=CC=1
CCCCC[CH]C1C=CC=CC=1
""",
)

entry(
    index = 140,
    label = "Indenyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   Cd u0 {1,S} {5,D}
4   Cb u0 {2,B} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.36,-0.72,-1.23,-1.77,-2.7,-3.43,-4.54],'cal/(mol*K)'),
        H298 = (81.62,'kcal/mol'),
        S298 = (0.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""A.G. Vandeputte CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "Benzyl_S_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T]}
4   Cb u0 {2,B} {5,S}
5   C  u0 {3,[S,D,T]} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.054016,-0.57486,-1.16181,-1.58687,-2.40332,-3.15038,-4.41676],'cal/(mol*K)','+|-',[0.20119,0.20119,0.20119,0.20119,0.20119,0.20119,0.20119]),
        H298 = (88.5038,'kcal/mol','+|-',0.737851),
        S298 = (3.11253,'cal/(mol*K)','+|-',0.434935),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CC[CH]C2=C1
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 142,
    label = "Benzyl_S_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
6   C  u0 {4,S} {5,[S,D,T,B]}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881557,-1.19162,-1.64981,-2.00346,-2.50574,-3.09492,-4.34126],'cal/(mol*K)','+|-',[0.318445,0.318445,0.318445,0.318445,0.318445,0.318445,0.318445]),
        H298 = (86.3797,'kcal/mol','+|-',1.14843),
        S298 = (1.33063,'cal/(mol*K)','+|-',0.744626),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CCC[CH]C2=C1
CC1CC[CH]C2=CC=CC=C21
CCC1CC[CH]C2=CC=CC=C21
""",
)

entry(
    index = 143,
    label = "Benzyl_S_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,B]}
4   Cb u0 {2,B} {6,S}
5   Cd u0 {3,[S,D,B]} {6,D}
6   Cd u0 {4,S} {5,D}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.762975,-1.09193,-1.45447,-1.90836,-2.74844,-3.44654,-4.57653],'cal/(mol*K)','+|-',[0.226952,0.226952,0.226952,0.226952,0.226952,0.226952,0.226952]),
        H298 = (31.5652,'kcal/mol','+|-',0.869131),
        S298 = (1.4331,'cal/(mol*K)','+|-',0.350884),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2C=CC[CH]C2=C1
C[C]1CC=CC2=CC=CC=C12
CC[C]1CC=CC2=CC=CC=C12
""",
)

entry(
    index = 144,
    label = "Benzyl_S_Fused7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   C  u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
6   C  u0 {4,S} {7,[S,D,T,B]}
7   C  u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-1.64,-1.86,-2.18,-2.74,-3.34,-4.5],'cal/(mol*K)','+|-',[1.4792,1.4792,1.4792,1.4792,1.4792,1.4792,1.4792]),
        H298 = (92.1,'kcal/mol','+|-',5.4578),
        S298 = (4.72,'cal/(mol*K)','+|-',4.205),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCC[CH]C2=C1
""",
)

entry(
    index = 145,
    label = "Allyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "Aromatic_pi_S_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {2,D} {6,S}
5   Cd u0 {3,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.013276,-1.28931,-2.31258,-2.92159,-3.39846,-3.6762,-4.8642],'cal/(mol*K)','+|-',[0.023461,0.023461,0.023461,0.023461,0.023461,0.023461,0.023461]),
        H298 = (75.4692,'kcal/mol','+|-',0.139824),
        S298 = (1.48461,'cal/(mol*K)','+|-',0.036353),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1
CC1[CH]CC=CC=1
CC1C=CC[CH]C=1
CC1[CH]C=CC=C1
""",
)

entry(
    index = 147,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {7,S}
2 * Cs u1 {1,S} {4,S} {8,S}
3   Cd u0 {1,S} {5,D} {9,S}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S}
8   H  u0 {2,S}
9   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.104911,-1.14065,-2.32405,-3.03895,-3.75201,-4.05481,-5.14193],'cal/(mol*K)','+|-',[0.061305,0.061305,0.061305,0.061305,0.061305,0.061305,0.061305]),
        H298 = (75.5447,'kcal/mol','+|-',0.399656),
        S298 = (2.79083,'cal/(mol*K)','+|-',0.079011),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1C
CC1[CH]C(C)C=CC=1
CC1C=CC(C)[CH]C=1
CC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 148,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {7,S}
2  * Cs u1 {1,S} {4,S} {8,S}
3    Cd u0 {1,S} {5,D} {9,S}
4    Cd u0 {2,S} {6,D}
5    Cd u0 {3,D} {6,S}
6    Cd u0 {4,D} {5,S}
7    C  u0 {1,S} {10,S}
8    H  u0 {2,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.453462,-1.20244,-2.43607,-2.95615,-3.47107,-3.9488,-5.03407],'cal/(mol*K)','+|-',[0.068504,0.068504,0.068504,0.068504,0.068504,0.068504,0.068504]),
        H298 = (74.982,'kcal/mol','+|-',0.417781),
        S298 = (1.24362,'cal/(mol*K)','+|-',0.106961),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1[CH]C=CC=C1C
CCC1[CH]C(C)=CC=C1
CCC1[CH]C=C(C)C=C1
CCC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 149,
    label = "Aromatic_pi_S_(fused5)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3  * Cs u1 {1,S} {7,S} {10,S}
4    C  u0 {1,S} {9,S}
5    Cd u0 {2,D} {8,S}
6    C  u0 {2,S} {9,S}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    C  u0 {4,S} {6,S}
10   H  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 150,
    label = "Aromatic_pi_S_(fused6)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3  * Cs u1 {1,S} {7,S} {11,S}
4    C  u0 {1,S} {9,S}
5    Cd u0 {2,D} {8,S}
6    C  u0 {2,S} {10,S}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    C  u0 {4,S} {10,S}
10   C  u0 {6,S} {9,S}
11   H  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 151,
    label = "Aromatic_pi_S_(fused7)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3  * Cs u1 {1,S} {7,S} {12,S}
4    C  u0 {1,S} {9,S}
5    Cd u0 {2,D} {8,S}
6    C  u0 {2,S} {10,S}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    C  u0 {4,S} {11,S}
10   C  u0 {6,S} {11,S}
11   C  u0 {9,S} {10,S}
12   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.084287,-0.439484,-1.00984,-1.6168,-2.48415,-3.29208,-4.57923],'cal/(mol*K)','+|-',[1.08001,1.08001,1.08001,1.08001,1.08001,1.08001,1.08001]),
        H298 = (76.4252,'kcal/mol','+|-',4.19016),
        S298 = (0.527688,'cal/(mol*K)','+|-',2.02975),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCCCC2[CH]1
C1=CC=C2CCCCC(C)C2[CH]1
""",
)

entry(
    index = 152,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S}
2  * Cs u1 {1,S} {6,S} {14,S}
3    Cd u0 {1,S} {7,D} {15,S}
4    Cb u0 {5,S} {8,B} {9,B}
5    C  u0 {1,S} {4,S}
6    Cd u0 {2,S} {10,D}
7    Cd u0 {3,D} {10,S}
8    Cb u0 {4,B} {11,B}
9    Cb u0 {4,B} {12,B}
10   Cd u0 {6,D} {7,S}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {2,S}
15   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.831072,-0.828879,-1.89888,-2.14323,-2.47359,-2.80572,-3.59479],'cal/(mol*K)','+|-',[0.208059,0.208059,0.208059,0.208059,0.208059,0.208059,0.208059]),
        H298 = (74.1331,'kcal/mol','+|-',0.742606),
        S298 = (-0.854817,'cal/(mol*K)','+|-',0.322012),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 153,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {6,B} {7,B}
4  * Cs u1 {1,S} {8,S} {15,S}
5    Cd u0 {1,S} {9,D} {16,S}
6    Cb u0 {3,B} {11,B}
7    Cb u0 {3,B} {12,B}
8    Cd u0 {4,S} {10,D}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {8,D} {9,S}
11   Cb u0 {6,B} {13,B}
12   Cb u0 {7,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
16   C  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67718,-0.360591,-1.61836,-2.06586,-2.45313,-2.74791,-3.50658],'cal/(mol*K)','+|-',[0.245046,0.245046,0.245046,0.245046,0.245046,0.245046,0.245046]),
        H298 = (74.3294,'kcal/mol','+|-',0.850906),
        S298 = (-3.58784,'cal/(mol*K)','+|-',0.338262),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 154,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D} {8,S}
3   Cs u0 {1,S} {5,S} {9,S}
4   Cd u0 {2,D} {6,S}
5   Cd u0 {3,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 155,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {8,S}
2    Cs u0 {1,S} {4,S} {7,S}
3    Cd u0 {1,S} {5,D} {9,S}
4    Cd u0 {2,S} {6,D}
5    Cd u0 {3,D} {6,S}
6    Cd u0 {4,D} {5,S}
7    C  u0 {2,S} {10,S}
8    H  u0 {1,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 156,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S}
2  * Cs u1 {1,S} {4,S} {14,S}
3    Cb u0 {5,S} {8,B} {9,B}
4    Cd u0 {2,S} {7,D} {15,S}
5    C  u0 {1,S} {3,S}
6    Cd u0 {1,S} {10,D}
7    Cd u0 {4,D} {10,S}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {6,D} {7,S}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 157,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1",
    group = 
"""
1    Cs u0 {2,S} {3,S} {6,S}
2    Cs u0 {1,S} {4,S} {15,S}
3  * Cs u1 {1,S} {5,S} {14,S}
4    Cb u0 {2,S} {7,B} {8,B}
5    Cd u0 {3,S} {9,D} {16,S}
6    Cd u0 {1,S} {10,D}
7    Cb u0 {4,B} {11,B}
8    Cb u0 {4,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {3,S}
15   C  u0 {2,S}
16   C  u0 {5,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 158,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2",
    group = 
"""
1   Cs u0 {2,S} {4,S} {8,S}
2 * Cs u1 {1,S} {5,S} {7,S}
3   Cd u0 {4,D} {6,S} {9,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   H  u0 {2,S}
8   C  u0 {1,S}
9   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 159,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2",
    group = 
"""
1    Cs u0 {2,S} {4,S} {7,S}
2  * Cs u1 {1,S} {5,S} {8,S}
3    Cd u0 {4,D} {6,S} {9,S}
4    Cd u0 {1,S} {3,D}
5    Cd u0 {2,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {1,S} {10,S}
8    H  u0 {2,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 160,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2",
    group = 
"""
1    Cs u0 {3,S} {5,S} {6,S}
2    Cb u0 {5,S} {9,B} {10,B}
3  * Cs u1 {1,S} {7,S} {14,S}
4    Cd u0 {6,D} {8,S} {15,S}
5    C  u0 {1,S} {2,S}
6    Cd u0 {1,S} {4,D}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {2,B} {11,B}
10   Cb u0 {2,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {3,S}
15   C  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 161,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {8,B} {9,B}
4  * Cs u1 {1,S} {7,S} {15,S}
5    Cd u0 {6,D} {10,S} {16,S}
6    Cd u0 {1,S} {5,D}
7    Cd u0 {4,S} {10,D}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {5,S} {7,D}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
16   C  u0 {5,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 162,
    label = "Aromatic_pi_S_(CH3_CH3_Para)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {7,S}
2   Cs u0 {1,S} {5,S} {8,S}
3   Cd u0 {4,D} {6,S} {9,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 163,
    label = "Aromatic_pi_S_(CH3_C2H5_Para)_1_3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2  * Cs u1 {1,S} {4,S} {8,S}
3    Cd u0 {4,D} {6,S} {9,S}
4    Cd u0 {2,S} {3,D}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {1,S} {10,S}
8    H  u0 {2,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 164,
    label = "Aromatic_pi_S_(CH3_Benzyl_Para)_1_3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2  * Cs u1 {1,S} {6,S} {14,S}
3    Cb u0 {5,S} {9,B} {10,B}
4    Cd u0 {6,D} {8,S} {15,S}
5    C  u0 {1,S} {3,S}
6    Cd u0 {2,S} {4,D}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 165,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {7,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {8,B} {9,B}
4  * Cs u1 {1,S} {6,S} {15,S}
5    Cd u0 {6,D} {10,S} {16,S}
6    Cd u0 {4,S} {5,D}
7    Cd u0 {1,S} {10,D}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {5,S} {7,D}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
16   C  u0 {5,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 166,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {7,S} {8,S}
2 * Cs u1 {1,S} {4,S} {9,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S}
8   C  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 167,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {9,S}
3   C  u0 {1,S} {4,S}
4   C  u0 {1,S} {3,S}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {2,S} {8,D}
7   Cd u0 {5,D} {8,S}
8   Cd u0 {6,D} {7,S}
9   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.48192,0.127981,-0.882314,-1.47156,-2.2164,-3.23195,-4.40182],'cal/(mol*K)','+|-',[0.7049,0.7049,0.7049,0.7049,0.7049,0.7049,0.7049]),
        H298 = (70.66,'kcal/mol','+|-',4.28202),
        S298 = (-1.77936,'cal/(mol*K)','+|-',1.91485),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCCC1CC12C=C[CH]C=C2
""",
)

entry(
    index = 168,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S} {8,S}
2  * Cs u1 {1,S} {4,S} {9,S}
3    Cd u0 {1,S} {6,D}
4    Cd u0 {2,S} {7,D}
5    C  u0 {1,S} {10,S}
6    Cd u0 {3,D} {7,S}
7    Cd u0 {4,D} {6,S}
8    C  u0 {1,S}
9    H  u0 {2,S}
10   C  u0 {5,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"

entry(
    index = 169,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3",
    group = 
"""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCC1CCC12C=C[CH]C=C2
""",
)

entry(
    index = 170,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u1 {1,S} {6,S} {11,S}
3    Cd u0 {1,S} {7,D}
4    C  u0 {1,S} {9,S}
5    C  u0 {1,S} {8,S}
6    Cd u0 {2,S} {10,D}
7    Cd u0 {3,D} {10,S}
 9    C u0 {4,S} {8,S}
10   Cd u0 {6,D} {7,S}
11   H  u0 {2,S}
""",
    thermo = ThermoD
      d = 
1   
entry(
    index = 172,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {14,S}
2  * Cs u1 {1,S} {6,S} {15,S}
3    Cb u0 {4,S} {7,B} {8,B}
4    C  u0 {1,S} {3,S}
5    Cd u0 {1,S} {9,D}
6    Cd u0 {2,S} {10,D}
7    Cb u0 {3,B} {11,B}
8    Cb u0 {3,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 173,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {14,S}
2    Cs u0 {1,S} {3,S} {15,S}
3    Cb u0 {2,S} {7,B} {8,B}
4  * Cs u1 {1,S} {6,S} {16,S}
5    Cd u0 {1,S} {9,D}
6    Cd u0 {4,S} {10,D}
7    Cb u0 {3,B} {11,B}
8    Cb u0 {3,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   C  u0 {2,S}
16   H  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 174,
    label = "CJ-Cd-Benzene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {2,D} {6,S}
5   Cb u0 {3,S} {6,B}
6   Cb u0 {4,S} {5,B}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.038694,-0.486795,-1.26614,-1.94355,-2.84643,-3.50953,-4.60995],'cal/(mol*K)','+|-',[0.244001,0.244001,0.244001,0.244001,0.244001,0.244001,0.244001]),
        H298 = (80.0557,'kcal/mol','+|-',0.913362),
        S298 = (1.93251,'cal/(mol*K)','+|-',0.367823),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2C=C[CH]CC2=C1
CC1[CH]C=CC2=CC=CC=C12
CC1=C[CH]CC2=CC=CC=C12
CCC1[CH]C=CC2=CC=CC=C12
CCC1=C[CH]CC2=CC=CC=C12
""",
)

entry(
    index = 175,
    label = "CJ-Cd-Benzene7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {2,D} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cb u0 {4,S} {7,B}
7   Cb u0 {5,S} {6,B}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.5,-1,-1.5,-2.5,-3.3,-4.5],'cal/(mol*K)','+|-',[2.4642,2.4642,2.4642,2.4642,2.4642,2.4642,2.4642]),
        H298 = (80.7,'kcal/mol','+|-',7.3256),
        S298 = (1,'cal/(mol*K)','+|-',3.8642),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CC[CH]C=CC2=C1
""",
)

entry(
    index = 176,
    label = "cyclobutene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (91.2,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "cyclopentene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.3,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Furuyama, S.; Golden, D. M.; Benson, S. W., "Kinetic Study of the Gas-Phase Reaction c-C5H8+I2 c-C5H6+2HI. Heat of Formation and the Stabilization Energy of the Cyclopentenyl Radical,"Int. J. Chem. Kinet. 1970, 2, 93-99. S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "cyclohexene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {6,S}
5   Cd u0 {3,D} {6,S}
6   C  u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Alfassi, Z. B.; Feldman, L., "The Kinetics of Radiation-Induced Hydrogen Abstraction by Trichloromethyl Radicals in the Liquid Phase: Cyclohexene," Int. J. Chem. Kinet. 1981, 13, 771-783. S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "CsJ-HCsCd-F1sHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cd  u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "CsJ-HCdCs-CdF1sHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd  u0 p0 c0 {2,S} {8,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   Cd  u0 p0 c0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "CsJ-HCsCd-HHCdHF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd  u0 p0 c0 {2,S} {8,D} {9,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   Cd  u0 p0 c0 {3,D}
9   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "CsJ-CsCdH-F1sHHCdH-F1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {3,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D} {9,S}
4    Cd  u0 p0 c0 {3,D} {10,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {3,S}
10   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "CsJ-HCdCs-F1sCdHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   Cd  u0 p0 c0 {1,S} {5,D} {8,S}
4   H   u0 p0 c0 {1,S}
5   Cd  u0 p0 c0 {3,D}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "CsJ-CdCsH-F1sHCdHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd  u0 p0 c0 {2,S} {8,D} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   Cd  u0 p0 c0 {3,D}
9   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "CsJ-CdHCs-HCdF1sHH-H",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {3,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D} {9,S}
4    Cd  u0 p0 c0 {3,D} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
9    F1s u0 p3 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "CsJ-CsHCd-HHHHCd-F1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {3,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D} {9,S}
4    Cd  u0 p0 c0 {3,D} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {3,S}
10   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0288619,-1.41526,-3.54682,-6.11369,-11.0377,-13.7413,-18.3907],'J/(mol*K)'),
        H298 = (361.549,'kJ/mol'),
        S298 = (-5.04371,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "C=CCJC=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (76,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "Aromatic_pi_S_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {6,S}
5   Cd u0 {3,D} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = u'Aromatic_pi_S_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 189,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_4",
    group = 
"""
1   Cd u0 {2,S} {4,D} {7,S}
2   Cs u0 {1,S} {5,S} {8,S}
3 * Cs u1 {4,S} {6,S} {9,S}
4   Cd u0 {1,D} {3,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   C  u0 {1,S}
8   C  u0 {2,S}
9   H  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 190,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2    Cd u0 {1,S} {4,D} {8,S}
3  * Cs u1 {4,S} {6,S} {9,S}
4    Cd u0 {2,D} {3,S}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {1,S} {10,S}
8    C  u0 {2,S}
9    H  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 191,
    label = "Aromatic_pi_S_(fused5)_1_4",
    group = 
"""
1    Cd u0 {2,S} {4,D} {6,S}
2    Cs u0 {1,S} {5,S} {7,S}
3  * Cs u1 {4,S} {8,S} {10,S}
4    Cd u0 {1,D} {3,S}
5    Cd u0 {2,S} {8,D}
6    C  u0 {1,S} {9,S}
7    C  u0 {2,S} {9,S}
8    Cd u0 {3,S} {5,D}
9    C  u0 {6,S} {7,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.748775,0.045256,-0.710099,-1.36165,-2.51235,-3.30599,-4.5709],'cal/(mol*K)','+|-',[0.098378,0.098378,0.098378,0.098378,0.098378,0.098378,0.098378]),
        H298 = (74.4829,'kcal/mol','+|-',1.11628),
        S298 = (0.780097,'cal/(mol*K)','+|-',0.163349),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
""",
)

entry(
    index = 192,
    label = "Aromatic_pi_S_(fused6)_1_4",
    group = 
"""
1    Cd u0 {2,S} {4,D} {6,S}
2    Cs u0 {1,S} {5,S} {7,S}
3  * Cs u1 {4,S} {8,S} {11,S}
4    Cd u0 {1,D} {3,S}
5    Cd u0 {2,S} {8,D}
6    C  u0 {1,S} {10,S}
7    C  u0 {2,S} {9,S}
8    Cd u0 {3,S} {5,D}
9    C  u0 {7,S} {10,S}
10   C  u0 {6,S} {9,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.01284,-0.508381,-1.05994,-1.55009,-2.56531,-3.36004,-4.58598],'cal/(mol*K)','+|-',[0.129371,0.129371,0.129371,0.129371,0.129371,0.129371,0.129371]),
        H298 = (73.7347,'kcal/mol','+|-',1.66562),
        S298 = (0.399676,'cal/(mol*K)','+|-',0.285184),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 193,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2    Cd u0 {1,S} {6,D} {14,S}
3    Cb u0 {5,S} {9,B} {10,B}
4  * Cs u1 {6,S} {8,S} {15,S}
5    C  u0 {1,S} {3,S}
6    Cd u0 {2,D} {4,S}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 194,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4",
    group = 
"""
1    Cs u0 {2,S} {4,S} {7,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {8,B} {9,B}
4    Cd u0 {1,S} {6,D} {15,S}
5  * Cs u1 {6,S} {10,S} {16,S}
6    Cd u0 {4,D} {5,S}
7    Cd u0 {1,S} {10,D}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {5,S} {7,D}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   C  u0 {4,S}
16   H  u0 {5,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 195,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_4",
    group = 
"""
1   Cd u0 {2,S} {4,D} {8,S}
2 * Cs u1 {1,S} {5,S} {7,S}
3   Cs u0 {4,S} {6,S} {9,S}
4   Cd u0 {1,D} {3,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   H  u0 {2,S}
8   C  u0 {1,S}
9   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 196,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_4",
    group = 
"""
1    Cd u0 {3,S} {4,D} {9,S}
2    Cs u0 {4,S} {5,S} {7,S}
3  * Cs u1 {1,S} {6,S} {8,S}
4    Cd u0 {1,D} {2,S}
5    Cd u0 {2,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {2,S} {10,S}
8    H  u0 {3,S}
9    C  u0 {1,S}
10   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 197,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4",
    group = 
"""
1    Cs u0 {5,S} {6,S} {7,S}
2    Cb u0 {6,S} {9,B} {10,B}
3    Cd u0 {4,S} {5,D} {15,S}
4  * Cs u1 {3,S} {8,S} {14,S}
5    Cd u0 {1,S} {3,D}
6    C  u0 {1,S} {2,S}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {2,B} {11,B}
10   Cb u0 {2,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {4,S}
15   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 198,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4",
    group = 
"""
1    Cs u0 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {9,B} {10,B}
4    Cd u0 {5,S} {6,D} {16,S}
5  * Cs u1 {4,S} {8,S} {15,S}
6    Cd u0 {1,S} {4,D}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {5,S}
16   C  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 199,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_4",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S} {8,S}
2 * Cs u1 {5,S} {6,S} {9,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {2,S} {3,D}
6   Cd u0 {2,S} {4,D}
7   C  u0 {1,S}
8   C  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 200,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs u1 {7,S} {8,S} {9,S}
3   C  u0 {1,S} {4,S}
4   C  u0 {1,S} {3,S}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {1,S} {8,D}
7   Cd u0 {2,S} {5,D}
8   Cd u0 {2,S} {6,D}
9   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
""",
)

entry(
    index = 201,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2  * Cs u1 {5,S} {6,S} {9,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {1,S} {6,D}
5    Cd u0 {2,S} {3,D}
6    Cd u0 {2,S} {4,D}
7    C  u0 {1,S} {10,S}
8    C  u0 {1,S}
9    H  u0 {2,S}
10   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 202,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2  * Cs u1 {7,S} {8,S} {10,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    C  u0 {1,S} {9,S}
6    C  u0 {1,S} {9,S}
7    Cd u0 {2,S} {3,D}
8    Cd u0 {2,S} {4,D}
9    C  u0 {5,S} {6,S}
10   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
""",
)

entry(
    index = 203,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2  * Cs u1 {7,S} {8,S} {11,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    C  u0 {1,S} {10,S}
6    C  u0 {1,S} {9,S}
7    Cd u0 {2,S} {3,D}
8    Cd u0 {2,S} {4,D}
9    C  u0 {6,S} {10,S}
10   C  u0 {5,S} {9,S}
11   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
""",
)

entry(
    index = 204,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2  * Cs u1 {7,S} {8,S} {12,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    C  u0 {1,S} {10,S}
6    C  u0 {1,S} {9,S}
7    Cd u0 {2,S} {3,D}
8    Cd u0 {2,S} {4,D}
9    C  u0 {6,S} {11,S}
10   C  u0 {5,S} {11,S}
11   C  u0 {9,S} {10,S}
12   H  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
""",
)

entry(
    index = 205,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4",
    group = 
"""
1    Cs u0 {4,S} {5,S} {6,S} {14,S}
2    Cb u0 {4,S} {9,B} {10,B}
3  * Cs u1 {7,S} {8,S} {15,S}
4    C  u0 {1,S} {2,S}
5    Cd u0 {1,S} {7,D}
6    Cd u0 {1,S} {8,D}
7    Cd u0 {3,S} {5,D}
8    Cd u0 {3,S} {6,D}
9    Cb u0 {2,B} {11,B}
10   Cb u0 {2,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   H  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 206,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S} {14,S}
2    Cs u0 {1,S} {3,S} {15,S}
3    Cb u0 {2,S} {9,B} {10,B}
4  * Cs u1 {7,S} {8,S} {16,S}
5    Cd u0 {1,S} {7,D}
6    Cd u0 {1,S} {8,D}
7    Cd u0 {4,S} {5,D}
8    Cd u0 {4,S} {6,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   C  u0 {2,S}
16   H  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 207,
    label = "cyclopropenyl-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (90.6,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""DeFrees, D. J.; McIver, R. T., Jr.; Hehre, W. J., "Heats of Formation of Gaseous Free Radicals via Ion Cyclotron Double Resonance Spectroscopy," J. Am. Chem. Soc. 1980, 102, 3334-3338, DOI: 10.1021/ja00530a005 S, Cp copied from C=CCJC=C""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "1,3-cyclopentadiene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.157,0.892,-0.937,-2.776,-4.931,-3.793,-4.855],'cal/(mol*K)'),
        H298 = (84.912,'kcal/mol'),
        S298 = (-2.047,'cal/(mol*K)'),
    ),
    shortDesc = u"""Combined experimental and theoretical results of Tranter for 1,2-CPD'yl""",
    longDesc = 
u"""
Absolute Enthalpy of formation at 298 K from experiment (1998 Kern and Tranter).
All other  values from theory (2001 Kiefer and Tranter).
""",
)

entry(
    index = 209,
    label = "C=CCJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-3.8,-3.7,-4.3,-6.1,-8.1,-11.5],'J/(mol*K)'),
        H298 = (318,'kJ/mol'),
        S298 = (-22,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 210,
    label = "Sec_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (-0.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "CCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-3.4,-3.4,-4.2,-6.7,-9.2,-13.9],'J/(mol*K)'),
        H298 = (379.1,'kJ/mol'),
        S298 = (-5.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 212,
    label = "CCJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],'cal/(mol*K)'),
        H298 = (91.9,'kcal/mol'),
        S298 = (-2.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "C=OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,1.5,0.9,0,-2.5,-5.1,-10.2],'J/(mol*K)'),
        H298 = (382.7,'kJ/mol'),
        S298 = (-13,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 214,
    label = "Cs_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = u'Tertalkyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "CCJ(C)CO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.8,-9.3,-10.3,-11,-12.4,-13.7,-16.1],'J/(mol*K)'),
        H298 = (369.4,'kJ/mol'),
        S298 = (-0.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 216,
    label = "C2CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],'cal/(mol*K)'),
        H298 = (97.2,'kcal/mol'),
        S298 = (7.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "Tertalkyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (96.5,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "bicyclo[1.1.0]butane-tertiary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (113.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "bicyclo[2.1.0]pentane-tertiary",
    group = 
1 * Cs u1 {3,S} {4, {
""",
    thermo = ThermoData(,'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (106.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "bicyclo[3.1.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "bicyclo[2.2.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "bicyclo[2.1.1]hexane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "bridgehead_norbornyl",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (107.42,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "bicyclo[3.2.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "bicyclo[4.1.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "bicyclo[3.1.1]heptane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (103.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "octahydro-pentalene-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   C  u0 {4,S} {5,S}
8   C  u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (95.7,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "bicyclo[4.2.0]octane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   C  u0 {5,S} {8,S}
8   C  u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "bicyclo[2.2.2]octane-C1",
    group = 
"""
1 * Cs u1 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (101.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "CsJ-CsCsCs-F1sHHHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {5,S} {8,S}
4   Cs  u0 p0 c0 {1,S} {9,S}
5   F1s u0 p3 c0 {3,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "CsJ-CsCsCs-HHF1sHHH",
    group = 
"""
multiplicity [2]
1  * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2    Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {8,S} {9,S}
4    Cs  u0 p0 c0 {1,S} {5,S} {10,S}
5    F1s u0 p3 c0 {4,S}
6    H   u0 p0 c0 {2,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.225255,-2.69645,-5.28604,-7.68668,-10.8092,-13.2789,-18.2619],'J/(mol*K)'),
        H298 = (405.804,'kJ/mol'),
        S298 = (5.78735,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "CsJ-CsCsCs-HHHHHHF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3    Cs  u0 p0 c0 {2,S} {8,S} {9,S}
4    Cs  u0 p0 c0 {2,S} {10,S} {11,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
11   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "CsJ-CsCsCs-HHHHF1sHF1sH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2    Cs  u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  * Cs  u1 p0 c0 {1,S} {2,S} {4,S}
4    Cs  u0 p0 c0 {3,S} {11,S} {12,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {1,S}
9    H   u0 p0 c0 {2,S}
10   H   u0 p0 c0 {2,S}
11   H   u0 p0 c0 {4,S}
12   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.945274,-2.3596,-4.12642,-6.62307,-11.2748,-13.7094,-17.8058],'J/(mol*K)'),
        H298 = (411.121,'kJ/mol'),
        S298 = (19.5818,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "Benzyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],'cal/(mol*K)'),
        H298 = (83.8,'kcal/mol'),
        S298 = (-5.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "Benzyl_T_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,B,T]}
4   Cb u0 {2,B} {5,S}
5   C  u0 {3,[S,B,T]} {4,S}
6   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.457289,-1.56269,-2.22771,-2.42903,-2.80968,-3.48772,-4.25286],'cal/(mol*K)','+|-',[0.282803,0.282803,0.282803,0.282803,0.282803,0.282803,0.282803]),
        H298 = (85.4498,'kcal/mol','+|-',1.02262),
        S298 = (4.37066,'cal/(mol*K)','+|-',0.608769),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 237,
    label = "Benzyl_T_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
6   C  u0 {4,S} {5,[S,D,T,B]}
7   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148032,-0.974235,-1.84864,-2.42284,-3.01207,-3.46526,-4.43708],'cal/(mol*K)','+|-',[0.514226,0.514226,0.514226,0.514226,0.514226,0.514226,0.514226]),
        H298 = (84.72,'kcal/mol','+|-',1.82377),
        S298 = (1.70208,'cal/(mol*K)','+|-',1.17522),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[C]1CCCC2=CC=CC=C21
CC[C]1CCCC2=CC=CC=C21
""",
)

entry(
    index = 238,
    label = "Benzyl_T_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   Cd u0 {3,[S,D,T,B]} {6,D}
6   Cd u0 {4,S} {5,D}
7   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.264274,-0.237466,-0.864612,-1.639,-2.84087,-3.59047,-4.6789],'cal/(mol*K)','+|-',[0.546927,0.546927,0.546927,0.546927,0.546927,0.546927,0.546927]),
        H298 = (83.3368,'kcal/mol','+|-',2.01563),
        S298 = (2.12045,'cal/(mol*K)','+|-',0.802466),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC[CH]C2=CC=CC=C12
CCC1=CC[CH]C2=CC=CC=C12
""",
)

entry(
    index = 239,
    label = "CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.1,-10,-11.8,-12.9,-14.1,-15.1,-16.9],'J/(mol*K)'),
        H298 = (361.8,'kJ/mol'),
        S298 = (3.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 240,
    label = "C=CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.8,-8.2,-8.9,-9.3,-10.1,-11,-12.9],'J/(mol*K)'),
        H298 = (313.4,'kJ/mol'),
        S298 = (0.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 241,
    label = "C=CCJ(C=C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.7,-9.3,-8.1,-7.2,-6.8,-7.2,-8.8],'J/(mol*K)'),
        H298 = (287.1,'kJ/mol'),
        S298 = (-27.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 242,
    label = "Allyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],'cal/(mol*K)'),
        H298 = (83.4,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "Aromatic_pi_T_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {6,D}
5   Cd u0 {2,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S}
""",
    thermo = u'Aromatic_pi_S_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 244,
    label = "Aromatic_pi_T_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S} {8,S}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {3,D} {5,S}
7   C  u0 {1,S}
8   C  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 245,
    label = "Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {7,S}
2 * Cs u1 {1,S} {4,S} {8,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S} {9,S}
8   C  u0 {2,S}
9   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
(
    index = 246,
    
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cd u0 {1,S} {8,D}
4   Cd u0 {2,S} {9,D}
u6  C  u0aav
Unce2/["  
  2S
1    Cs u0 {3,S} {4,S} {5,S}
2    Cb u0 {4,S} {7,B} {8,B}
3  * Cs u1 {1,S} {6,S} {14,S}
4    C  u0 {1,S} {2,S}
5    Cd u0 {1,S} {9,D}
6    Cd u0 {3,S} {10,D}
7    Cb u0 {2,B} {11,B}
8    Cb u0 {2,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 249,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {6,B} {7,B}
4  * Cs u1 {1,S} {8,S} {15,S}
5    Cd u0 {1,S} {9,D}
6    Cb u0 {3,B} {11,B}
7    Cb u0 {3,B} {12,B}
8    Cd u0 {4,S} {10,D}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {8,D} {9,S}
11   Cb u0 {6,B} {13,B}
12   Cb u0 {7,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 250,
    label = "Aromatic_pi_T_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {4,D}
4   
6   Cs u0 {4,S} {5,S}
7   C  u0 {1,S}
""",
    thermo = u'Aromatic_pi_S_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 251,
    label = "Aromatic_pi_T_(CH3_CH3_Para)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D} {8,S}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {2,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cd u0 {3,D} {5,S}
7   C  u0 {1,S}
8   C  u0 {2,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 252,
    label = "Aromatic_pi_T_(CH3_C2H5_Para)_1_4",
    group = 
"""
1   Cd u0 {2,S} {3,D} {7,S}
2 * Cs u1 {1,S} {4,S} {8,S}
3   Cd u0 {1,D} {5,S}
4   Cd u0 {2,S} {6,D}
5   Cs u0 {3,S} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S} {9,S}
8   C  u0 {2,S}
9   C  u0 {7,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 253,
    label = "Aromatic_pi_T_(CH3_Benzyl_Para)_1_4",
    group = 
"""
1    Cd u0 {3,S} {4,S} {5,D}
2    Cb u0 {4,S} {7,B} {8,B}
3  * Cs u1 {1,S} {6,S} {14,S}
4    C  u0 {1,S} {2,S}
5    Cd u0 {1,D} {9,S}
6    Cd u0 {3,S} {10,D}
7    Cb u0 {2,B} {11,B}
8    Cb u0 {2,B} {12,B}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {3,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 254,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4",
    group = 
"""
1    Cd u0 {2,S} {4,S} {5,D}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {6,B} {7,B}
4  * Cs u1 {1,S} {8,S} {15,S}
5    Cd u0 {1,D} {9,S}
6    Cb u0 {3,B} {11,B}
7    Cb u0 {3,B} {12,B}
8    Cd u0 {4,S} {10,D}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {8,D} {9,S}
11   Cb u0 {6,B} {13,B}
12   Cb u0 {7,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 255,
    label = "bicyclo[2.1.0]pent-2-ene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (112.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "bicyclo[2.1.1]hex-2-ene-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "C=CCJ(C)C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.2,-10.5,-9.4,-9,-9.1,-9.7,-11.5],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-17.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 259,
    label = "C=CCJ(C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10,-7.5,-6.1,-5.5,-5.6,-6.4,-8.5],'J/(mol*K)'),
        H298 = (307.4,'kJ/mol'),
        S298 = (-27.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 260,
    label = "Tert_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],'cal/(mol*K)'),
        H298 = (84.5,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "C2CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   R   u0 {2,S}
""",
    thermo = u'C2CJCHO',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "C2CJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],'cal/(mol*K)'),
        H298 = (89.8,'kcal/mol'),
        S298 = (-1.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9,3.7,1.6,-0.9,-5.9,-10.3,-17.5],'J/(mol*K)'),
        H298 = (413.3,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 264,
    label = "CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],'cal/(mol*K)'),
        H298 = (96.51,'kcal/mol'),
        S298 = (0.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = u'CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = u'CsJOCH3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "CsJOCH3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "CsJOCC",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],'cal/(mol*K)'),
        H298 = (96.83,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "CsJOCC2",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],'cal/(mol*K)'),
        H298 = (96.16,'kcal/mol'),
        S298 = (-0.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "CsJOCC3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],'cal/(mol*K)'),
        H298 = (95.75,'kcal/mol'),
        S298 = (0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "CsOJCF",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S} {6,S}
6   F1s u0 {5,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "CsOJCF2",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S} {6,S} {7,S}
6   F1s u0 {5,S}
7   F1s u0 {5,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = u'CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],'cal/(mol*K)'),
        H298 = (100.88,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],'cal/(mol*K)'),
        H298 = (100.48,'kcal/mol'),
        S298 = (-0.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "C=COCJ",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   Cd  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-7.2,-8.9,-10.6,-13.6,-15.9,-19.7],'J/(mol*K)'),
        H298 = (409.4,'kJ/mol'),
        S298 = (13.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 278,
    label = "CsJ-HO2sH-Cd-HCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2 * Cs  u1 p0 c0 {3,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {8,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.975213,0.413228,-1.68739,-4.50771,-9.8313,-13.463,-18.2415],'J/(mol*K)'),
        H298 = (399.944,'kJ/mol'),
        S298 = (-4.72668,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol'),
        S298 = (-1.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],'cal/(mol*K)'),
        H298 = (98.91,'kcal/mol'),
        S298 = (-1.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],'cal/(mol*K)'),
        H298 = (98.34,'kcal/mol'),
        S298 = (-1.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "CCsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.4,-1.5,-3.9,-8.6,-12.5,-18.7],'J/(mol*K)'),
        H298 = (402,'kJ/mol'),
        S298 = (3.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 283,
    label = "CCsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = u'CCsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "C=CCJ(O)C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S} {6,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.7,-8.4,-10,-11,-12.1,-13.1,-15.5],'J/(mol*K)'),
        H298 = (328.3,'kJ/mol'),
        S298 = (4.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 285,
    label = "CCsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],'cal/(mol*K)'),
        H298 = (95.41,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "CsJ-HCsO2s-CsHHH-F1sH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {4,S} {8,S}
3    Cs  u0 p0 c0 {4,S} {9,S} {10,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
9    F1s u0 p3 c0 {3,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.63714,-1.09929,-3.84668,-6.29133,-10.3747,-13.5395,-18.5104],'J/(mol*K)'),
        H298 = (403.584,'kJ/mol'),
        S298 = (-0.510507,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "CsJ-CsO2sH-F1sHF1sCs",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   O2s u0 p2 c0 {2,S} {8,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   Cs  u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "CsJ-HO2sCs-F1sCsHF1s-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {8,S}
3   O2s u0 p2 c0 {2,S} {4,S}
4   Cs  u0 p0 c0 {3,S} {9,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   H   u0 p0 c0 {1,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "CCsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   H       u0 {1,S}
5   [CO,Cd] u0 {2,S}
""",
    thermo = u'CCsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "CCsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],'cal/(mol*K)'),
        H298 = (98.7,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "CCsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],'cal/(mol*K)'),
        H298 = (98.87,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "CCsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "C=CCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-3.9,-3,-3.2,-5.7,-8.6,-13.8],'J/(mol*K)'),
        H298 = (333.9,'kJ/mol'),
        S298 = (-7.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 294,
    label = "CsJ-CdO2sH-HCdH-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs  u1 p0 c0 {1,S} {4,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S}
4   O2s u0 p2 c0 {2,S} {8,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
8   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.47612,-2.66839,-4.51823,-6.74243,-10.5113,-13.7472,-19.2283],'J/(mol*K)'),
        H298 = (332.411,'kJ/mol'),
        S298 = (-4.50984,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.3,-5.6,-7.4,-9.8,-11.2,-14],'J/(mol*K)'),
        H298 = (356.6,'kJ/mol'),
        S298 = (0.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 296,
    label = "CCsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],'cal/(mol*K)'),
        H298 = (95.39,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "FCCsJOH",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {5,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {3,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.436904,-1.5406,-4.20769,-6.59898,-10.6093,-13.7631,-18.7627],'J/(mol*K)'),
        H298 = (400.326,'kJ/mol'),
        S298 = (8.22834,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "CsJ-O2sCsH-HCsHH-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {8,S}
4   O2s u0 p2 c0 {2,S} {9,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    label = "CsJ-CsO2sH-CsHHH-F1sH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  * Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {8,S} {9,S}
4    O2s u0 p2 c0 {2,S} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    F1s u0 p3 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.238955,-1.33532,-4.26212,-7.2368,-10.9527,-13.5813,-18.7173],'J/(mol*K)'),
        H298 = (392.803,'kJ/mol'),
        S298 = (4.16363,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "CCsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "CCsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],'cal/(mol*K)'),
        H298 = (97.19,'kcal/mol'),
        S298 = (0.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "CCsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "C2CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2,-7.1,-10.7,-13.4,-16.6,-18.5,-21.2],'J/(mol*K)'),
        H298 = (398.4,'kJ/mol'),
        S298 = (14.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 304,
    label = "C2CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],'cal/(mol*K)'),
        H298 = (94.5,'kcal/mol'),
        S298 = (2.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "CsJ-CsO2sCs-F1sHHHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {7,S} {8,S}
4   O2s u0 p2 c0 {1,S} {9,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "CsJ-CsCsO2s-HHHF1sHF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3    Cs  u0 p0 c0 {2,S} {8,S} {9,S}
4    O2s u0 p2 c0 {2,S} {10,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    F1s u0 p3 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "C2CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = u'C2CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

entry(
    index = 236,
    label = "S2J-(Cs-Cb)",
    group =
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0    {1,S} {3,S}
3   Cb  u0    {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.29,-3.84,-4.16,-4.58,-5.31,-5.90,-6.84],'cal/(mol*K)'),
        H298 = (86.83,'kcal/mol'),
        S298 = (-4.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 308,
    label = "C2CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (3.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "C2CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   C       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = u'C2CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "C2CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (4.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "C2CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],'cal/(mol*K)'),
        H298 = (99.97,'kcal/mol'),
        S298 = (4.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "C2CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],'cal/(mol*K)'),
        H298 = (100.25,'kcal/mol'),
        S298 = (4.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "C2CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (2.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "C2CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],'cal/(mol*K)'),
        H298 = (96.74,'kcal/mol'),
        S298 = (2.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "C2CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],'cal/(mol*K)'),
        H298 = (96.58,'kcal/mol'),
        S298 = (2.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "CsJ-S",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   R   u0 {1,S}
4   R   u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "CsJ-SsHH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.07,-0.32,-0.73,-1.22,-2.18,-2.99,-4.27],'cal/(mol*K)'),
        H298 = (95.34,'kcal/mol'),
        S298 = (1.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "CsJ-CSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "CsJ-CsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.79,-1.36,-1.9,-2.82,-3.53,-4.64],'cal/(mol*K)'),
        H298 = (92.87,'kcal/mol'),
        S298 = (1.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "CsJ-CtSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26,-0.02,-0.47,-0.97,-1.95,-2.77,-4.12],'cal/(mol*K)'),
        H298 = (83.48,'kcal/mol'),
        S298 = (-0.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "CsJ-CbSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.38,-0.65,-1.01,-1.75,-2.4,-3.57],'cal/(mol*K)'),
        H298 = (84.88,'kcal/mol'),
        S298 = (-0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "CsJ-CdSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21,-2.77,-2.39,-2.24,-2.39,-2.74,-3.56],'cal/(mol*K)'),
        H298 = (81.92,'kcal/mol'),
        S298 = (0.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "CsJ-C=SSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75,-2.93,-2.07,-1.54,-1.2,-1.31,-2.01],'cal/(mol*K)'),
        H298 = (71.51,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "CsJ-CCS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "CsJ-CsCsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72,-2.04,-2.88,-3.4,-3.99,-4.36,-4.96],'cal/(mol*K)'),
        H298 = (92.32,'kcal/mol'),
        S298 = (3.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "CsJ-CsCtSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.99,-1.64,-2.18,-2.62,-3.3,-3.82,-4.65],'cal/(mol*K)'),
        H298 = (81.17,'kcal/mol'),
        S298 = (3.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "CsJ-CsCbSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.26,-2.53,-2.75,-3.12,-3.49,-4.43],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "CsJ-CsCdSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-4.74,-4.81,-4.59,-4.17,-3.99,-4.12],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 329,
    label = "CsJ-CsC=SSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86,-3.83,-3.41,-2.93,-2.28,-2.07,-2.36],'cal/(mol*K)'),
        H298 = (69.17,'kcal/mol'),
        S298 = (-1.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "CsJ-SS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   R   u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "CsJ-SsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-4,-3.64,-3.53,-3.68,-4,-4.72],'cal/(mol*K)'),
        H298 = (90.16,'kcal/mol'),
        S298 = (1.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "CsJ-CSS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "CsJ-CsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36,-4,-4.17,-4.24,-4.37,-4.55,-5],'cal/(mol*K)'),
        H298 = (89.98,'kcal/mol'),
        S298 = (5.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "CsJ-CtSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "CsJ-CbSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "CsJ-CdSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "CsJ-C=SSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "CsJ-SsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "CCsJOS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = u'CCsJOHSH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "CCsJOHSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   S2s u0 {1,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21,-2.38,-2.47,-2.55,-2.89,-3.33,-4.54],'cal/(mol*K)'),
        H298 = (92.6,'kcal/mol'),
        S298 = (1.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC CBS-QB3 1d-hr""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'CCsJN',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "CCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-1.4,-1.9,-2.8,-3.4,-4.5],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (2.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "C2CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = u'CCsJN',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "OCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-8.2,-14.4,-17.5,-19.4,-20.1,-21.5],'J/(mol*K)'),
        H298 = (408.4,'kJ/mol'),
        S298 = (15.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 345,
    label = "CsJ-HO2sO2s-CsH-F1sH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {3,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S} {8,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.49317,-2.20366,-4.00939,-6.66465,-11.5142,-13.9611,-18.5054],'J/(mol*K)'),
        H298 = (403.187,'kJ/mol'),
        S298 = (-0.177736,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "CsJ-CdF1sCs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   Cd  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "CsJ-CsF1sCd-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "CsJ-CsF1sCd-HH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   Cd  u0 p0 c0 {1,S} {6,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 349,
    label = "CsJ-F1sCsCd-HHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {7,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "CsJ-CsCdF1s-HHHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd  u0 p0 c0 {2,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "CsJ-CdF1sCs-CdHHHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd  u0 p0 c0 {2,S} {8,D} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   Cd  u0 p0 c0 {3,D}
9   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "CsJ-CsF1sCd-HHHHCd-H",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  * Cs  u1 p0 c0 {1,S} {3,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D} {9,S}
4    Cd  u0 p0 c0 {3,D} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    F1s u0 p3 c0 {2,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "CsJ-CsF1sO2s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5419,-1.4716,-4.38832,-6.96311,-11.046,-13.9602,-18.6455],'J/(mol*K)'),
        H298 = (371.915,'kJ/mol'),
        S298 = (16.3228,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "CsJ-F1sO2sCs-Cs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "CsJ-F1sO2sCs-CsF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {4,S} {6,S}
3   Cs  u0 p0 c0 {1,S}
4   O2s u0 p2 c0 {2,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "CsJ-F1sO2sCs-HCsF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "CsJ-O2sF1sCs-HHF1sCs",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   O2s u0 p2 c0 {2,S} {8,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "CsJ-CsF1sO2s-F1sCsHH-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {8,S}
4   O2s u0 p2 c0 {2,S} {9,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "CsJ-CsF1sO2s-HF1sCsH-HH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  * Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {8,S} {9,S}
4    O2s u0 p2 c0 {2,S} {10,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "CsJ-CsF1sF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18697,-3.62345,-5.97295,-8.12456,-11.5364,-13.9614,-17.8512],'J/(mol*K)'),
        H298 = (422.159,'kJ/mol'),
        S298 = (-3.96949,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 361,
    label = "CsJ-CsF1sF1s-O2s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "CsJ-F1sCsF1s-O2sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "CsJ-CsF1sF1s-O2sHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.401588,-3.15393,-5.55172,-7.62364,-11.4059,-14.3736,-18.7683],'J/(mol*K)'),
        H298 = (425.858,'kJ/mol'),
        S298 = (5.94026,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "CsJ-F1sF1sCs-O2sHH-Cs",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
8   Cs  u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "CsJ-CsF1sF1s-HHO2s-Cs-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {7,S} {8,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {3,S} {9,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   F1s u0 p3 c0 {2,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "CsJ-F1sF1sCs-HHO2s-Cs-HH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  * Cs  u1 p0 c0 {1,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {4,S} {9,S} {10,S}
4    O2s u0 p2 c0 {1,S} {3,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "CsJ-F1sF1sCd",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "CsJ-F1sF1sCd-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,S} {5,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.95143,-1.28086,-4.70886,-7.02064,-10.8359,-13.9129,-18.852],'J/(mol*K)'),
        H298 = (397.751,'kJ/mol'),
        S298 = (3.73565,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "CsJ-CdF1sF1s-CdH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "CsJ-CdF1sF1s-HCd-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10954,-0.13761,-3.27503,-6.12779,-10.1937,-13.4156,-18.8019],'J/(mol*K)'),
        H298 = (384.917,'kJ/mol'),
        S298 = (-2.16228,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "CsJ-F1sF1sCd-CdH-HCs",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3 * Cs  u1 p0 c0 {1,S} {7,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
8   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "CsJ-F1sF1sCd-CdH-CsH-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3 * Cs  u1 p0 c0 {1,S} {7,S} {8,S}
4   Cs  u0 p0 c0 {2,S} {9,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
8   F1s u0 p3 c0 {3,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "CsJ-F1sCdF1s-CdH-CsH-HH",
    group = 
"""
multiplicity [2]
1    Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2    Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {7,S} {8,S}
4  * Cs  u1 p0 c0 {2,S} {9,S} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {2,S}
7    H   u0 p0 c0 {3,S}
8    H   u0 p0 c0 {3,S}
9    F1s u0 p3 c0 {4,S}
10   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "CsJ-F1sCsCs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "CsJ-F1sCsCs-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.506445,-2.57339,-5.36908,-7.7225,-11.3498,-13.8635,-18.6123],'J/(mol*K)'),
        H298 = (410.091,'kJ/mol'),
        S298 = (-6.04417,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "CsJ-CsCsF1s-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3   Cs  u0 p0 c0 {2,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "CsJ-F1sCsCs-F1sHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {7,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.580768,-2.63683,-5.06467,-7.54805,-11.4261,-14.0485,-18.6325],'J/(mol*K)'),
        H298 = (413.167,'kJ/mol'),
        S298 = (6.44671,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 378,
    label = "CsJ-CsF1sCs-F1sHHF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {6,S} {8,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {3,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "CsJ-F1sCsCs-HF1sHHF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cs  u0 p0 c0 {2,S} {8,S} {9,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.68234,-1.37324,-4.73157,-7.8829,-12.3907,-14.279,-18.3579],'J/(mol*K)'),
        H298 = (410.97,'kJ/mol'),
        S298 = (19.449,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 380,
    label = "CsJ-CsCtF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   Ct  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 381,
    label = "CsJ-CsCtF1s-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   Ct  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 382,
    label = "CsJ-F1sCtCs-HCt",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {6,S}
3   Ct  u0 p0 c0 {1,S} {5,T}
4   F1s u0 p3 c0 {1,S}
5   Ct  u0 p0 c0 {3,T}
6   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 383,
    label = "CsJ-CsCtF1s-CtHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Ct  u0 p0 c0 {1,S} {7,T}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   Ct  u0 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 384,
    label = "CsJ-F1sCsCt-HCtHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Ct  u0 p0 c0 {2,S} {8,T}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   Ct  u0 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 385,
    label = "CsJ-HF1sO2s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.807182,-1.44394,-3.86644,-6.33626,-10.6866,-13.7109,-18.3738],'J/(mol*K)'),
        H298 = (390.331,'kJ/mol'),
        S298 = (8.96061,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 386,
    label = "CsJ-F1sO2sH-Cd",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   Cd  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.753307,-2.5245,-4.30328,-6.3332,-10.6325,-13.9669,-18.3903],'J/(mol*K)'),
        H298 = (416.482,'kJ/mol'),
        S298 = (6.42234,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 387,
    label = "CsJ-HF1sO2s-Cd-F1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {4,S} {5,S}
2   O2s u0 p2 c0 {1,S} {3,S}
3   Cd  u0 p0 c0 {2,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 388,
    label = "CsJ-HF1sO2s-Cd-F1sCd",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2 * Cs  u1 p0 c0 {3,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 389,
    label = "CsJ-F1sHO2s-Cd-F1sCd-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2 * Cs  u1 p0 c0 {3,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {8,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.260117,-1.7977,-4.26717,-6.73779,-10.5729,-13.5226,-18.3962],'J/(mol*K)'),
        H298 = (423.834,'kJ/mol'),
        S298 = (10.6238,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 390,
    label = "CsJ-COF1sCs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   CO  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 391,
    label = "CsJ-F1sCsCO-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   CO  u0 p0 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 392,
    label = "CsJ-COCsF1s-HO2d",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   CO  u0 p0 c0 {1,S} {5,D} {6,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
6   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 393,
    label = "CsJ-COCsF1s-O2dHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   CO  u0 p0 c0 {1,S} {5,D} {6,S}
3   Cs  u0 p0 c0 {1,S} {7,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 394,
    label = "CsJ-CsCOF1s-O2dHHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   CO  u0 p0 c0 {1,S} {7,D} {8,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   O2d u0 p2 c0 {3,D}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4657,-5.02801,-6.79092,-8.66803,-12.3998,-15.4542,-19.0429],'J/(mol*K)'),
        H298 = (373.043,'kJ/mol'),
        S298 = (8.03329,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 395,
    label = "CsJ-F1sF1sCt",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Ct  u0 p0 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 396,
    label = "CsJ-F1sCtF1s-Ct",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Ct  u0 p0 c0 {1,S} {5,T}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   Ct  u0 p0 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.24733,-2.07517,-5.05046,-7.34114,-11.14,-14.0613,-18.6224],'J/(mol*K)'),
        H298 = (397.115,'kJ/mol'),
        S298 = (7.76055,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 397,
    label = "CsJ-CtF1sF1s-Ct-Cs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {4,S} {5,S}
2   Ct  u0 p0 c0 {1,S} {3,T}
3   Ct  u0 p0 c0 {2,T} {6,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.494207,-2.46941,-4.8125,-7.005,-10.873,-13.9968,-18.7845],'J/(mol*K)'),
        H298 = (398.247,'kJ/mol'),
        S298 = (6.02188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 398,
    label = "CsJ-CtF1sF1s-Ct-Cs-F1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {5,S} {6,S}
2   Ct  u0 p0 c0 {1,S} {3,T}
3   Ct  u0 p0 c0 {2,T} {4,S}
4   Cs  u0 p0 c0 {3,S} {7,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 399,
    label = "CsJ-F1sCtF1s-Ct-Cs-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {4,S} {7,S} {8,S}
3   Ct  u0 p0 c0 {1,S} {4,T}
4   Ct  u0 p0 c0 {2,S} {3,T}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.897026,-1.94623,-4.64083,-7.057,-11.1243,-14.2861,-19.094],'J/(mol*K)'),
        H298 = (389.392,'kJ/mol'),
        S298 = (-11.515,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 400,
    label = "CsJ-CtHF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Ct  u0 p0 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 401,
    label = "CsJ-CtF1sH-Ct",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Ct  u0 p0 c0 {1,S} {5,T}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   Ct  u0 p0 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.04856,0.445723,-2.78943,-5.58413,-10.1337,-13.53,-18.5463],'J/(mol*K)'),
        H298 = (374.194,'kJ/mol'),
        S298 = (7.79147,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 402,
    label = "CsJ-F1sHCt-Ct-Cs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {4,S} {5,S}
2   Ct  u0 p0 c0 {1,S} {3,T}
3   Ct  u0 p0 c0 {2,T} {6,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cs  u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 403,
    label = "CsJ-HF1sCt-Ct-Cs-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {5,S} {6,S}
2   Ct  u0 p0 c0 {1,S} {3,T}
3   Ct  u0 p0 c0 {2,T} {4,S}
4   Cs  u0 p0 c0 {3,S} {7,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 404,
    label = "CsJ-HCtF1s-Ct-Cs-HH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {4,S} {7,S} {8,S}
3   Ct  u0 p0 c0 {1,S} {4,T}
4   Ct  u0 p0 c0 {2,S} {3,T}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08996,-2.54552,-4.23445,-6.1227,-10.0201,-13.5013,-18.6906],'J/(mol*K)'),
        H298 = (371.769,'kJ/mol'),
        S298 = (3.58447,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 405,
    label = "CsJ-CsO2sO2s-F1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 406,
    label = "CsJ-O2sCsO2s-F1sH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S} {6,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 407,
    label = "CsJ-O2sO2sCs-HHF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S} {6,S}
4   O2s u0 p2 c0 {1,S} {7,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {3,S}
7   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 408,
    label = "CsJ-O2sO2sCs-F1sHHH",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   O2s u0 p2 c0 {1,S} {8,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.0228,-2.34549,-5.0335,-7.3768,-11.2451,-14.1956,-18.7339],'J/(mol*K)'),
        H298 = (397.909,'kJ/mol'),
        S298 = (4.58162,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "CsJ-F1sHCd",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.16317,0.719851,-2.04078,-4.95412,-9.31607,-12.6962,-18.5995],'J/(mol*K)'),
        H298 = (365.091,'kJ/mol'),
        S298 = (1.69827,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 410,
    label = "CsJ-CdF1sH-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.40471,0.459033,-3.05699,-6.02516,-10.0314,-13.182,-18.766],'J/(mol*K)'),
        H298 = (378.807,'kJ/mol'),
        S298 = (7.51281,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "CsJ-CdHF1s-CdH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47659,1.55346,-2.4229,-5.80418,-10.0908,-12.8786,-18.7288],'J/(mol*K)'),
        H298 = (371.886,'kJ/mol'),
        S298 = (3.9541,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 412,
    label = "CsJ-HF1sCd-CdH-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0860614,-0.937909,-3.19873,-5.85405,-10.2042,-13.2744,-18.7719],'J/(mol*K)'),
        H298 = (355.068,'kJ/mol'),
        S298 = (-1.60277,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 413,
    label = "CsJ-F1sHCs",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.791118,-2.52641,-6.09643,-8.79684,-11.559,-13.0193,-16.3534],'J/(mol*K)'),
        H298 = (414.439,'kJ/mol'),
        S298 = (-6.99707,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 414,
    label = "CsJ-HCsF1s-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.53174,-0.893619,-3.40642,-5.85912,-10.2072,-13.4205,-18.0522],'J/(mol*K)'),
        H298 = (415.583,'kJ/mol'),
        S298 = (6.56277,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 415,
    label = "CsJ-CsHF1s-O2sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.02516,0.172014,-2.87507,-5.49853,-9.87904,-13.2915,-18.5104],'J/(mol*K)'),
        H298 = (417.871,'kJ/mol'),
        S298 = (10.6012,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 416,
    label = "CsJ-F1sCsH-F1sHO2s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.37389,-0.385841,-3.37604,-5.94421,-10.2125,-13.4962,-18.5833],'J/(mol*K)'),
        H298 = (422.574,'kJ/mol'),
        S298 = (15.7798,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "CsJ-F1sHCO",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   CO  u0 p0 c0 {1,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.50145,-3.18195,-5.20129,-7.63743,-11.9826,-14.647,-18.9015],'J/(mol*K)'),
        H298 = (376.47,'kJ/mol'),
        S298 = (-5.17408,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "CsJ-COHF1s-O2s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   CO  u0 p0 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "CsJ-F1sHCO-O2dO2s",
    group = 
"""
multiplicity [2]
1   CO  u0 p0 c0 {2,S} {3,S} {4,D}
2 * Cs  u1 p0 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S}
4   O2d u0 p2 c0 {1,D}
5   H   u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.84507,-1.12215,-3.77683,-6.35776,-10.6191,-13.8621,-18.7789],'J/(mol*K)'),
        H298 = (388.488,'kJ/mol'),
        S298 = (4.25059,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 420,
    label = "CsJ-O2sF1sO2s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 421,
    label = "CsJ-O2sO2sF1s-H",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.10077,-2.85472,-5.36356,-7.93277,-12.0037,-14.4862,-18.8578],'J/(mol*K)'),
        H298 = (423.764,'kJ/mol'),
        S298 = (5.07747,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 422,
    label = "CsJ-F1sO2sF1s",
    group = 
"""
multiplicity [2]
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13734,-3.25283,-5.66397,-7.95644,-11.816,-14.4995,-18.8749],'J/(mol*K)'),
        H298 = (435.596,'kJ/mol'),
        S298 = (-0.907376,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 423,
    label = "CdsJ",
    group = 
"""
1 * [Cd,CO] u1
""",
    thermo = u'Cds_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 424,
    label = "CdsJO",
    group = 
"""
1 * CO  u1 {2,D}
2   O2d u0 {1,D}
""",
    thermo = u'CCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 425,
    label = "HCdsJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],'cal/(mol*K)'),
        H298 = (88.45,'kcal/mol'),
        S298 = (-0.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 426,
    label = "CCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
""",
    thermo = u'CsCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 427,
    label = "CC(C)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1,-5.8,-7.9,-9.9,-13.5,-16.2,-20.3],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 428,
    label = "CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7,-5,-7.4,-9.6,-13.1,-15.6,-19.9],'J/(mol*K)'),
        H298 = (373.3,'kJ/mol'),
        S298 = (7.5,'J/(mol*K)'),
    shotDesc = u"""\Derved fom CB-QB3 alcuationwith 1HR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3L
DOI: 10.1002
1   
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7,-4,-5.4,-7.2,-10.9,-13.9,-18.6],'J/(mol*K)'),
        H298 = (375.2,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 430,
    label = "C=CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.5,2.6,-2.4,-6.5,-12,-15.3,-19.7],'J/(mol*K)'),
        H298 = (373.6,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 431,
    label = "C=CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-4.2,-7,-9.3,-12.8,-15.4,-19.4],'J/(mol*K)'),
        H298 = (371.9,'kJ/mol'),
        S298 = (10.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 432,
    label = "CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9,-2.6,-5.6,-8.1,-12,-14.9,-19.6],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (6.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 433,
    label = "C=CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1,-4.5,-7.4,-9.7,-12.7,-15.1,-19.5],'J/(mol*K)'),
        H298 = (375.3,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 434,
    label = "CCCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {4,D}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-3.9,-7,-9.9,-14.5,-17.5,-21.4],'J/(mol*K)'),
        H298 = (378,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 435,
    label = "C=OCCJ=O",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * CO  u1 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,1.4,-2.8,-6.4,-12,-15.8,-20.4],'J/(mol*K)'),
        H298 = (379.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 436,
    label = "C=OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.2,-4.6,-4.4,-4.5,-4.9,-5.7,-7.8],'J/(mol*K)'),
        H298 = (330.2,'kJ/mol'),
        S298 = (-19.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 437,
    label = "C=C(C)CJ=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.8,-6.4,-8.8,-12.5,-15.3,-19.5],'J/(mol*K)'),
        H298 = (381.7,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 438,
    label = "CsCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 439,
    label = "COJ-O2dCs-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S}
2 * CO  u1 p0 c0 {1,S} {4,D}
3   F1s u0 p3 c0 {1,S}
4   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33176,-2.79586,-5.03525,-7.46101,-11.3575,-13.8111,-17.9402],'J/(mol*K)'),
        H298 = (380.179,'kJ/mol'),
        S298 = (-1.27551,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 440,
    label = "COJ-O2dCs-O2sF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO  u1 p0 c0 {1,S} {5,D}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 441,
    label = "COJ-O2dCs-O2sHF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 p0 c0 {1,S} {6,D}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12427,-2.3508,-5.26715,-7.66519,-11.6349,-14.6679,-19.2914],'J/(mol*K)'),
        H298 = (388.538,'kJ/mol'),
        Cpdata = ([5.3,2.5,-1.1,-4.5,-9.9,-13.7,-18.9],'J/(mol*K)'),
        H298 = (379.9,'kJ/mol'),
        S298 = (7.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 443,
    label = "OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
    themo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3,-4.7,-7,-9.5,-14,-17.2,-21.1],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (4.6,
    ),
ent
3   O2d u0 {1,D}
4   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],'cal/(mol*K)'),
        H298 = (100.75,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
)

entry(
    index = 446,
    label = "(O)CJOC",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,-0.2,-3.5,-6.5,-10.9,-13.6,-17],'J/(mol*K)'),
        H298 = (415.2,'kJ/mol'),
        S298 = (-4.3,'J/(mol*K)'),
    ),
    lone""  ,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    

""",
)

entry(
    index = 448,
    label = "(O)CJOCC",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],'cal/(mol*K)'),
        H298 = (99.49,'kcal/mol'),
        S298 = (0.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 449,
    label = "(O)CJOCC2",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 450,
    label = "(O)CJOCC3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],'cal/(mol*K)'),
        H298 = (97.98,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 451,
    label = "COJ-O2dO2s-Cs-F1s",
    group = 
"""
multiplicity [2]
1   O2s u0 p2 c0 {2,S} {3,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3 * CO  u1 p0 c0 {1,S} {5,D}
4   F1s u0 p3 c0 {2,S}
5   O2d u0 p2 c0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 452,
    label = "COJ-O2sO2d-Cs-HF1s",
    group = 
multipliu0 pd,2

entry(
    index = 453,
    label = "Cds-P-Cl",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   Cl u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.514,-1.16,-1.74,-2.238,-3.032,-3.631,-4.562],'cal/(mol*K)'),
        H298 = (109.865,'kcal/mol'),
        S298 = (1.542,'cal/(mol*K)'),
 
    longDesc = 
u"""

""",
)

entry(
    index = 454,
    label = "CJ(Cl)=CC",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D} {4,S}
3   Cl u0 {1,S}
u""",
    thermo = u'Cds-P-Cl',
    shortDesc = u"""""",
    longDesc = 
u"""

1 * 
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],'cal/(mol*K)'),
        H298 = (111.2,'kcal/mol'),
        S298 = (1.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 456,
    label = "C=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 457,
    label = "CdJ-HCdd-Cd-F1s",
    group = 
"""
multiplicity [2]
1   Cdd u0 p0 c0 {2,D} {3,D}
2   Cd  u0 p0 c0 {1,D} {4,S}
3 * Cd  u1 p0 c0 {1,D} {5,S}
4   F1s u0 p3 c0 {2,S}
5   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 458,
    label = "CdJ-CddH-Cdd-Cd-F1s",
    group = 
"""
multiplicity [2]
1   Cdd u0 p0 c0 {2,D} {3,D}
2   Cdd u0 p0 c0 {1,D} {4,D}
3   Cd  u0 p0 c0 {1,D} {5,S}
4 * Cd  u1 p0 c0 {2,D} {6,S}
5   F1s u0 p3 c0 {3,S}
6   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.0256,-0.544452,-3.65133,-6.34551,-10.7359,-14.0173,-18.8622],'J/(mol*K)'),
        H298 = (401.514,'kJ/mol'),
        S298 = (12.7244,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 459,
    label = "CdJ-HCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S}
2 * Cd  u1 p0 c0 {1,D} {4,S}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.177223,-2.67125,-5.43964,-7.79459,-11.1936,-13.8101,-18.2475],'J/(mol*K)'),
        H298 = (479.451,'kJ/mol'),
        S298 = (0.697379,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 460,
    label = "CdJ-CdH-F1sO2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * Cd  u1 p0 c0 {1,D} {5,S}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.924798,-2.13871,-4.865,-7.27185,-11.2394,-14.2525,-18.8043],'J/(mol*K)'),
        H298 = (484.462,'kJ/mol'),
        S298 = (0.495599,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 461,
    label = "CdJ-HCd-O2sF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3 * Cd  u1 p0 c0 {1,D} {6,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.199494,-2.67897,-5.30968,-7.58737,-11.357,-14.2439,-18.7183],'J/(mol*K)'),
        H298 = (484.219,'kJ/mol'),
        S298 = (6.52921,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 462,
    label = "CdJ-HCd-O2sCs-HF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd  u1 p0 c0 {1,D} {7,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 463,
    label = "CdJ-HCd-O2sCs-HF1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {7,S}
3 * Cd  u1 p0 c0 {2,D} {8,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   O2s u0 p2 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.43041,-3.39418,-5.71529,-7.94885,-11.647,-14.4826,-18.8861],'J/(mol*K)'),
        H298 = (476.556,'kJ/mol'),
        S298 = (4.15004,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 464,
    label = "CdJ-HCd-CsH-F1sH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd  u1 p0 c0 {1,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0852646,-2.17507,-4.70723,-6.96806,-10.7246,-13.7017,-18.4983],'J/(mol*K)'),
        H298 = (465.254,'kJ/mol'),
        S298 = (6.9363,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 465,
    label = "Cds_S",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 466,
    label = "C=CJC=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   CO  u0 {1,S} {4,D}
3   C   u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.4,-2.2,-4.8,-7.2,-11.6,-15.5,-22],'J/(mol*K)'),
        H298 = (462.3,'kJ/mol'),
        S298 = (9.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 467,
    label = "C=CJC=C",
    group = 
"""
1 * Cd      u1 {2,D} {3,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],'cal/(mol*K)'),
        H298 = (99.8,'kcal/mol'),
        S298 = (0.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 468,
    label = "cyclobutadiene-C1",
    group = 
"""
1 * Cd u1 {2,D} {4,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (104.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 469,
    label = "bicyclo[2.2.0]hexa-1(4),2,5-triene-C2",
    group = 
"""
1   Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (102.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 470,
    label = "1,3-cyclopentadiene-vinyl-2",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4 * Cd u1 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.2,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 471,
    label = "CdJ-CdCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   Cd  u0 p0 c0 {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 472,
    label = "CdJ-CdCd-HF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * Cd  u1 p0 c0 {1,D} {5,S}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   Cd  u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 473,
    label = "CdJ-CdCd-HHF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   Cd  u0 p0 c0 {2,S} {6,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 474,
    label = "CdJ-CdCd-F1sHCdH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cd  u0 p0 c0 {1,D}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 475,
    label = "CdJ-CdCd-HCdF1sH-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cd  u0 p0 c0 {1,D} {8,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65879,-1.53204,-4.31643,-6.6579,-10.5347,-13.5185,-18.2708],'J/(mol*K)'),
        H298 = (440.503,'kJ/mol'),
        S298 = (11.0254,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 476,
    label = "CdJ-CdCd-HHHCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cd  u0 p0 c0 {1,D} {8,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.28928,0.137854,-2.98774,-5.61349,-9.91563,-13.1663,-18.1202],'J/(mol*K)'),
        H298 = (428.168,'kJ/mol'),
        S298 = (10.2892,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 477,
    label = "cyclopropenyl-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
""",
r       Tdata = ([300,400500,60,8001000,500],K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDes
    
"""
1   C  u0 {2,S} {4,S}
2   C  u0 {1,S} {3,S}
3 * Cd u1 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (112.5,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Cds_S""",
    longDesc = 
u"""

e"
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   C  u0 {1,S} {2,S}
4 * Cd u1 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109.8,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 480,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 481,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (111.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "cyclopentene-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S} {4,S}
4 * Cd u1 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (113.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 483,
    label = "bicyclo[2.1.1]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (115.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 484,
e    grop = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {4,D}
3   Cd u0 {1,S} {5,D
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 485,
    label = "CCCJ=C=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   C   u0 {1,S} {4,S}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,S}
 """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6,-3,-4.9,-6.5,-9.4,-11.6,-15.1],'J/(mol*K)'),
        H298 = (420.
        S298 -311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
m130
entry(
    index = 486,
    label = "CC(C)CJ=C=O",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.8,-3.6,-6,-7.8,-10.6,-12.6,-15.8],'J/(mol*K)'),
        H298 = (424,'kJ/mol'),
        S298 = (1.7,'J/(mol*K)'),
lDO
entry(
    index = 487,
    label = "C=C(C)CJ=C=O",
    group = 
"""
1   
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,D}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.5,-13.7,-14.6,-15,-15.7,-16.3,-17.8],'J/(mol*K)'),
        H298 = (404,'kJ/mol'),
        S298 = (5.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 488,
    label = "OC=CJCb",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D} {4,S}
3   Cb  u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.047,0.607,0.374,-0.3,-1.28,-1.972,-3.196],'cal/(mol*K)'),
        H298 = (123.797,'kcal/mol'),
        S298 = (2.661,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations""",
    longDesc = 
u"""
Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations for OC=[C]c1ccccc1
""",
)

entry(
    index = 489,
    label = "CdJ-CsCd-CsF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u1 p0 c0 {1,S} {5,D}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   Cd  u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 490,
    label = "CdJ-CsCd-F1sHCs",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {2,D} {6,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 491,
    label = "CdJ-CdCs-CsF1sF1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 492,
    label = "CdJ-CsCd-F1sHF1sHCs",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 493,
    label = "CdJ-CdCs-HF1sF1sCsH-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S} {9,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 494,
    label = "CdJ-CdCs-F1sHHCsF1s-HF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {1,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {4,D} {9,S} {10,S}
4  * Cd  u1 p0 c0 {1,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    F1s u0 p3 c0 {3,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83282,-3.57369,-5.90441,-8.42711,-12.5441,-14.6196,-18.7337],'J/(mol*K)'),
        H298 = (472.786,'kJ/mol'),
        S298 = (18.5012,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 495,
    label = "CdJ-CdCs-F1sHCsH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
 6   H  u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""
    longDesc = 1sHHHCs",
u"""
""",
)

entry(
    index = 499,
e   groupr= 
 = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {6,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cd  u0 p0 c0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 501,
    label = "CdJ-CddCs-F1sCdHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {7,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   Cd  u0 p0 c0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 502,
    label = "CdJ-CddCs-HCdF1sH-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {4,D}
4   Cd  u0 p0 c0 {3,D} {8,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {1,S}
8   H   u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79187,-1.50603,-4.72258,-7.5888,-11.7155,-14.44,-19.009],'J/(mol*K)'),
        H298 = (376.131,'kJ/mol'),
        S298 = (16.3133,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    

""",
)

   index = 503,
   label   (005'
   C/'= 0 c0 {1,S} {4,S}
3   Cd  u0  
5   F1s u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11117,-4.29952,-7.01397,-9.0569,-11.8646,-14.3577,-18.8804],'J/(mol*K)'),
        H298 = (470.134,'kJ/mol'),
        S298 = (-6.14678,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

   index =]o 6,S} {7,S}
   0Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    F1sH298 = (469.738,'kJ/mol'),
        S298 = (13.252,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

)

entry(
    index = 510,
    label = "CdJ-CtCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   Ct  u0 p0 c0 {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 511,
    label = "CdJ-CdCt-F1sCt",
    group = 
"""
multiplicity [2]
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   Ct  u0 p0 c0 {1,S} {4,T}
4   Ct  u0 p0 c0 {3,T}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 512,
    label = "CdJ-CdCt-F1sHCt",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   Ct  u0 p0 c0 {2,S} {6,T}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Ct  u0 p0 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22749,-2.09554,-5.13675,-7.4954,-11.3396,-14.2264,-18.6174],'J/(mol*K)'),
        H298 = (446.426,'kJ/mol'),
        S298 = (15.0264,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 513,
    label = "CdJ-CddCs-O2dF1s",
    group = 
"""
multiplicity [2]
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   Cs  u0 p0 c0 {1,S} {4,S}
3   Cdd u0 p0 c0 {1,D} {5,D}
4   F1s u0 p3 c0 {2,S}
5   O2d u0 p2 c0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
u"""

entry(
    index = 514,
    label = "CdJ-CddCs-F1sHO2d",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {6,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2d u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.67428,-6.27527,-8.39582,-10.0294,-12.8592,-15.355,-19.1034],'J/(mol*K)'),
        H298 = (437.637,'kJ/mol'),
        S298 = (5.34821,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 515,
    label = "CdJ-CsCd-HHHCsH-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S} {9,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 516,
    label = "CdJ-CdCs-HHCsHH-F1sH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    Cs  u0 p0 c0 {1,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {4,D} {9,S} {10,S}
4  * Cd  u1 p0 c0 {1,S} {3,D}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19872,-1.58274,-4.63139,-7.43408,-11.3702,-13.7642,-18.585],'J/(mol*K)'),
        H298 = (449.411,'kJ/mol'),
        S298 = (10.1851,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 517,
    label = "CdJ-CsCd-F1sHHO2s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {4,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   O2s u0 p2 c0 {2,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 518,
    label = "CdJ-CsCd-HF1sO2sHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   O2s u0 p2 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.61384,-4.36556,-6.98197,-9.15038,-12.2038,-14.5206,-18.7343],'J/(mol*K)'),
        H298 = (463.423,'kJ/mol'),
        S298 = (10.0372,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 519,
    label = "CdJ-CsCdd-HHCdH-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {4,D}
4   Cd  u0 p0 c0 {3,D} {8,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {1,S}
8   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 520,
    label = "CdJ-CsCd-F1sHHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.529246,-2.4402,-4.89685,-7.14311,-11.1455,-14.1348,-18.4487],'J/(mol*K)'),
        H298 = (460.858,'kJ/mol'),
        S298 = (11.7574,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 521,
    label = "CdJ-CdCs-HHHCsH-HF1s",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2    Cd  u0 p0 c0 {3,S} {4,D} {8,S}
3    Cs  u0 p0 c0 {2,S} {9,S} {10,S}
4  * Cd  u1 p0 c0 {1,S} {2,D}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
s10   H  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-
        H298 
entry(
    index = 523,
    label = "C=CJO",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-11.8,-15.2,-17.2,-19.2,-20.3,-22],'J/(mol*K)'),
        H298 = (457.4,'kJ/mol'),
        S298 = (26.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
 = ([-3.42121,-4.83128,-6.57495,-8.75149,-12.9576,-15.7001,-19.0911],'J/(mol*K)'),
        H298 = (453.982,'kJ/mol'),
        S298 = (-3.99041,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 527,
    label = "CdJ-CdO2s-CsHF1s-HF1s",
    group = 
"""
multiplicity [2]
1   
3   O2s u0 p2 c0 {1,S} {4,S}
4 * Cd  u1 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
        Cpdata = ([-1.93972,-3.54028,-5.75846,-8.24453,-12.6448,-15.2555,-18.9802],'J/(mol*K)'),
        H298 = (465.304,'
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
e   label = "CdJ-O2sCdF
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(,'K'),
        Cpdata = ([-4.19264,-6.22992,-8.25926,-10.1195,-13.1869,-15.5311,-19.2091],'J/(mol*K)'),
        H298 = (459.704,'kJ/mol'),
        S298 = (2.56246,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
entry(
    index = 529,
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {3,S}
    themo = Thermot[,
    longDesc = 
u"""

""",

entry(
    index = 530,
    label = "CdJ-CddO2s-HCd-F1s",
    group = 
"""
multiplicity [2]
H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01815,-3.5278,-5.725,-7.78573,-11.674,-14.6419,-18.6975],'J/(mol*K)'),
        H298 = (461.419,'kJ/mol'),
        S298 = (3.87556,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 532,
    label = "CdJ-CdF1s",
    group = 
"""
multiplicity [2]
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   Cd  u0 p0 c0 {1,D}
3   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49865,-5.62628,-8.07074,-9.99562,-13.034,-15.3186,-19.0561],'J/(mol*K)'),
        H298 = (487.486,'kJ/mol'),
        S298 = (6.99096,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 533,
    label = "CdJ-F1sCd-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S}
2 * Cd  u1 p0 c0 {1,D} {4,S}
3   H   u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.49989,-4.15413,-6.68648,-8.93883,-12.5829,-15.2111,-18.9928],'J/(mol*K)'),
        H298 = (477.286,'kJ/mol'),
        S298 = (2.97737,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 534,
    label = "CdJ-F1sCd-HCs",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * Cd  u1 p0 c0 {1,D} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.29211,-3.86043,-6.4816,-8.73103,-12.1356,-14.4985,-18.8345],'J/(mol*K)'),
        H298 = (475.718,'kJ/mol'),
        S298 = (-2.24456,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 535,
    label = "CdJ-F1sCd-CsH-Cs",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3 * Cd  u1 p0 c0 {1,D} {6,S}
4   H   u0 p0 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 536,
    label = "CdJ-F1sCd-CsH-CsH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd  u1 p0 c0 {1,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 537,
    label = "CdJ-CdF1s-CsH-HCsH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {7,S}
3 * Cd  u1 p0 c0 {2,D} {8,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 538,
    label = "CdJ-F1sCd-CsH-CsHH-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3   Cs  u0 p0 c0 {1,S} {8,S}
4 * Cd  u1 p0 c0 {2,D} {9,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 539,
    label = "CdJ-F1sCd-CsH-HHCs-HH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2    Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {8,S} {9,S}
4  * Cd  u1 p0 c0 {2,D} {10,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {3,S}
9    H   u0 p0 c0 {3,S}
10   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94753,-4.25845,-6.68599,-8.95101,-12.4807,-15.0037,-19.0909],'J/(mol*K)'),
        H298 = (469.632,'kJ/mol'),
        S298 = (-3.83664,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 540,
    label = "CdJ-F1sCdd",
    group = 
"""
multiplicity [2]
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   Cdd u0 p0 c0 {1,D}
3   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41197,-4.16928,-6.78891,-8.9962,-12.4913,-15.1148,-19.1822],'J/(mol*K)'),
        H298 = (424.851,'kJ/mol'),
        S298 = (1.00396,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 541,
    label = "CdJ-F1sCdd-Cdd",
    group = 
"""
multiplicity [2]
1   Cdd u0 p0 c0 {2,D} {3,D}
2 * Cd  u1 p0 c0 {1,D} {4,S}
3   Cdd u0 p0 c0 {1,D}
4   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00488583,-3.53424,-6.30895,-8.6709,-12.2563,-14.8068,-19.1154],'J/(mol*K)'),
        H298 = (439.511,'kJ/mol'),
        S298 = (4.46501,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 542,
    label = "CtJ",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T}
""",
    thermo = u'Acetyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 543,
    label = "Acetyl",
    group = 
"""
1   Ct u0 {2,T} {3,S}
2 * Ct u1 {1,T}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],'cal/(mol*K)'),
        H298 = (132.7,'kcal/mol'),
        S298 = (2.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 544,
    label = "CtJ-Ct-Cd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,S}
2   Ct  u0 p0 c0 {1,S} {4,T}
3   F1s u0 p3 c0 {1,S}
4 * Ct  u1 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 545,
    label = "CtJ-Ct-Cd-F1sCd",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Ct  u0 p0 c0 {1,S} {5,T}
3   Cd  u0 p0 c0 {1,D}
4   F1s u0 p3 c0 {1,S}
5 * Ct  u1 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 546,
    label = "CtJ-Ct-Cd-CdF1s-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   Ct  u0 p0 c0 {1,S} {6,T}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6 * Ct  u1 p0 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.64431,-6.94426,-9.73992,-11.1116,-13.3047,-15.0535,-18.2794],'J/(mol*K)'),
        H298 = (558.89,'kJ/mol'),
        S298 = (11.7438,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 547,
    label = "CtJ-Ct-Cs-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S}
2   Ct  u0 p0 c0 {1,S} {4,T}
3   F1s u0 p3 c0 {1,S}
4 * Ct  u1 p0 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.92228,-8.21901,-9.48362,-10.6209,-12.7874,-14.8081,-18.0219],'J/(mol*K)'),
        H298 = (560.419,'kJ/mol'),
        S298 = (5.39474,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 548,
    label = "CtJ-Ct-Cs-O2sF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Ct  u0 p0 c0 {1,S} {5,T}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5 * Ct  u1 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 549,
    label = "CtJ-Ct-Cs-F1sHO2s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 p0 c0 {1,S} {6,T}
3   O2s u0 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * Ct  u1 p0 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.44455,-8.13718,-9.46677,-10.9407,-13.7766,-15.8681,-18.3498],'J/(mol*K)'),
        H298 = (553.688,'kJ/mol'),
        S298 = (16.3462,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 550,
    label = "CtJ-Ct-Cs-HCsH-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S}
3   Ct  u0 p0 c0 {1,S} {7,T}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7 * Ct  u1 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 551,
    label = "CtJ-Ct-Cs-HHCs-HF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   Ct  u0 p0 c0 {1,S} {8,T}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8 * Ct  u1 p0 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.28939,-7.97139,-9.41457,-10.4474,-12.3833,-14.6959,-18.1371],'J/(mol*K)'),
        H298 = (563.296,'kJ/mol'),
        S298 = (8.39156,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 552,
    label = "CtJ-Ct-O2s-Cs-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2   O2s u0 p2 c0 {1,S} {3,S}
3   Ct  u0 p0 c0 {2,S} {6,T}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * Ct  u1 p0 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.40149,-9.35254,-10.8779,-12.1794,-14.3349,-16.0137,-18.8866],'J/(mol*K)'),
        H298 = (531.433,'kJ/mol'),
        S298 = (-13.5806,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 553,
    label = "CbJ",
    group = 
"""
1 * Cb u1 {2,B} {3,B}
2   C  u0 {1,B}
3   C  u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],'cal/(mol*K)'),
        H298 = (113,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from TSANG, S and Cp from THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 554,
    label = "C=SJ",
    group = 
"""
1 * CS  u1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 555,
    label = "C=SJ-S2s",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   S2s u0 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 556,
    label = "C=SJ-H",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.88,-1.47,-1.99,-2.85,-3.49,-4.52],'cal/(mol*K)'),
        H298 = (92.39,'kcal/mol'),
        S298 = (-0.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 557,
    label = "C=SJ-C",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   C   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 558,
    label = "C=SJ-Cd",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cd  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21,-1.76,-2.24,-2.65,-3.3,-3.81,-4.67],'cal/(mol*K)'),
        H298 = (77.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 559,
    label = "C=SJ-Cs",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cs  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.8,-2.25,-2.63,-3.24,-3.74,-4.64],'cal/(mol*K)'),
        H298 = (91.94,'kcal/mol'),
        S298 = (0.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 560,
    label = "OJ",
    group = 
"""
1 * O u1
""",
    thermo = u'COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 561,
    label = "HOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],'cal/(mol*K)'),
        H298 = (119.22,'kcal/mol'),
        S298 = (-2.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O, OH and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 562,
    label = "FOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   F   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.28604,-6.2973,-7.34985,-8.35589,-10.1637,-11.7554,-14.7303],'J/(mol*K)'),
        H298 = (416.179,'kJ/mol'),
        S298 = (-15.1237,'J/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O, OH and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 563,
    label = "COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   C   u0 {1,S}
""",
    thermo = u'CsOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 564,
    label = "CCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.1,-12.2,-14.4,-15.1,-14.7,-14.5,-15.6],'J/(mol*K)'),
        H298 = (442.9,'kJ/mol'),
        S298 = (3.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 565,
    label = "CC(F)OJ",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   F1s u0 p3 c0 {1,S}
3 * O2s u1 p2 c0 {1,S}
4   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.98843,-6.77606,-8.33283,-9.80506,-12.3459,-14.4232,-18.098],'J/(mol*K)'),
        H298 = (457.059,'kJ/mol'),
        S298 = (-4.00076,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 566,
    label = "FCC(F)OJ",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   F1s u0 p3 c0 {1,S}
4 * O2s u1 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.16027,-5.19334,-6.28545,-7.70498,-11.2319,-13.7956,-17.4323],'J/(mol*K)'),
        H298 = (444.912,'kJ/mol'),
        S298 = (11.9355,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 567,
    label = "HOCC(F)OJ",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3   O   u0 p2 c0 {2,S} {6,S}
4   F1s u0 p3 c0 {1,S}
5 * O2s u1 p2 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.732542,-2.94369,-5.40419,-7.44028,-10.793,-13.3712,-17.5499],'J/(mol*K)'),
        H298 = (445.622,'kJ/mol'),
        S298 = (11.6102,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 568,
    label = "CC(F)(F)OJ",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 p3 c0 {1,S}
3 * O2s u1 p2 c0 {1,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23703,-7.04889,-8.57511,-10.0323,-12.5433,-14.5836,-18.1757],'J/(mol*K)'),
        H298 = (475.572,'kJ/mol'),
        S298 = (-6.48276,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 569,
    label = "C=OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-9.3,-11.5,-13.2,-15,-16,-17.5],'J/(mol*K)'),
        H298 = (461,'kJ/mol'),
        S298 = (2.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 570,
    label = "C=CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4 * O2s u1 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-11.3,-14.6,-16.2,-17.2,-17.4,-18.4],'J/(mol*K)'),
        H298 = (462.1,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 571,
    label = "CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.6,-13.9,-16.3,-17.5,-18.4,-18.8,-19.1],'J/(mol*K)'),
        H298 = (459.1,'kJ/mol'),
        S298 = (16.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 572,
    label = "C=OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3 * O2s u1 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1,-6.8,-10.1,-13,-17.5,-20.9,-25.9],'J/(mol*K)'),
        H298 = (479.5,'kJ/mol'),
        S298 = (16,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 573,
    label = "CC(C)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.3,-6.3,-7.3,-8.3,-9.8,-11.2,-14.2],'J/(mol*K)'),
        H298 = (447.6,'kJ/mol'),
        S298 = (-6.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 574,
    label = "CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-7.9,-9,-9.9,-10.7,-11.7,-14.6],'J/(mol*K)'),
        H298 = (446.1,'kJ/mol'),
        S298 = (-4.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 575,
    label = "C=CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-12.1,-12.9,-12.9,-12.6,-12.9,-14.8],'J/(mol*K)'),
        H298 = (445.9,'kJ/mol'),
        S298 = (2.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 576,
    label = "CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.8,-18.8,-22.1,-22.3,-19.5,-17.2,-16],'J/(mol*K)'),
        H298 = (449,'kJ/mol'),
        S298 = (8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 577,
    label = "C=CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.2,-12.5,-16.7,-19.1,-20.1,-19.4,-18.2],'J/(mol*K)'),
        H298 = (450.7,'kJ/mol'),
        S298 = (8.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 578,
    label = "O2sJ-Cs-CsCsH-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {6,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {3,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 579,
    label = "O2sJ-Cs-HCsCs-F1sF1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   Cs  u0 p0 c0 {1,S} {8,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 580,
    label = "O2sJ-Cs-HCsCs-HHF1sF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {8,S} {9,S}
3   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {3,S}
7   F1s u0 p3 c0 {3,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)
u0 p0 c0 {1,S} {9,S} {10,S}
4  * O2s u1 p2 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9   
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 582,
    label = "C=C(C)OJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.2,-13.1,-15.6,-17,-17.7,-17.6,-17.6],'J/(mol*K)'),
        H298 = (354.8,'kJ/mol'),
        S298 = (7.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 583,
    label = "O2sJ-Cd-CsCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   Cs  u0 p0 c0 {1,S}
4 * O2s u1 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 584,
    label = "O2sJ-Cd-CdCs-F1sH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S}
3   Cd  u0 p0 c0 {1,D} {6,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 585,
e   groupit}}
      """""",
    longDesc = 
u"""

""",
)

entry(
    index = 591,
    label = "O2sJ-Cs-HF1sCt",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 p0 c0 {1,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
""",
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.31373,-6.00632,-7.76458,-9.3213,-11.947,-14.0398,-17.6843],'J/(mol*K)'),
        H298 = (448.198,'kJ/mol'),
        S298 = (10.4974,'J/(mol*K)'),
    ),
[m" c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * O2s u1 p2 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 595,
    label = "O2sJ-Cs-HHCs-F1sHCs-H",
    group = 
"""
mult
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3   Cs  u0 p0 c0 {1,S} {9,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * O2s u1 p2 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
  label = "O2sJ-Cs-HHCs-F1sHCs-HH",
    group = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    Cs  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} 
5    H   u0 p0 c0 {1,S}
6  * O2s u1 p2 c0 {2,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    H   u0 p0 c0 {3,S}
10   H   u0 p0 c0 {3,S}
""",
r   shortl]  ([1.38665,-1.99842,-4.81984,-6.85689,-10.1885,-12.7401,-16.9571],'J/(mol*K)'),
        H298 = (
entry(
    index = 600,
    label = "O2sJ-Cs-O2sCsH-F1sHH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3   O2s u0 p2 c0 {1,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

    index = 601,
    label = "O2sJ-Cs-HCsH-CsHH-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3   Cs  u0 p0 c0 {1,S} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * O2s u1 p2 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
 = 
"""
multiplicity [2]
1    Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    Cs  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {9,S} {10,S}
4   
6  * O2s u1 p2 c0 {2,S}
7    H   u0 p0 c0 {2,S}
8    H   u0 p0 c0 {2,S}
9    F1s u0 p3 c0 {3,S}
10   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.35687,-5.52396,-7.31796,-8.62233,-10.5223,-13.2395,-17.4908],'J/(mol*K)'),
        H298 = (436.762,'kJ/mol'),
        S298 = (5.95494,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 603,
    label = "O2sJ-Cs-HHCd-F1sCd",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {6,D} {7,S}
3 * O2s u1 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cd  u0 p0 c0 {2,D}
7   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 604,
    label = "O2sJ-Cs-CdHH-CdF1s-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {7,S}
3   Cd  u0 p0 c0 {2,D} {8,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.87816,-4.6546,-6.56486,-8.09549,-10.7609,-13.0759,-17.363],'J/(mol*K)'),
        H298 = (440.376,'kJ/mol'),
        S298 = (2.80795,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 605,
    label = "O2sJ-Cs-CdHH-HCd-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {7,S}
3   Cd  u0 p0 c0 {2,D} {8,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.6559,-6.16723,-7.21179,-8.08267,-10.8233,-13.384,-17.3395],'J/(mol*K)'),
        H298 = (441.38,'kJ/mol'),
        S298 = (5.08247,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 606,
    label = "O2sJ-Cs-HO2sCs-HHF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {8,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 607,
    label = "CdsOJ",
    group = 
"""
1 * O2s     u1 {2,S}
2   [Cd,CO] u0 {1,S}
""",
    thermo = u'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 608,
    label = "RC=COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],'cal/(mol*K)'),
        H298 = (88,'kcal/mol'),
        S298 = (-1.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 609,
    label = "C=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.1,-13.5,-14.6,-14.6,-14.3,-14.5,-16],'J/(mol*K)'),
        H298 = (358.1,'kJ/mol'),
        S298 = (3.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 610,
    label = "O2sJ-Cd-CdH-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.78793,-8.20378,-10.1334,-11.5723,-13.8122,-15.4701,-18.1934],'J/(mol*K)'),
        H298 = (333.863,'kJ/mol'),
        S298 = (1.28416,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 611,
    label = "O2sJ-Cd-CdH-CsF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5 * O2s u1 p2 c0 {2,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 612,
    label = "O2sJ-Cd-HCd-CsF1s-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {7,S}
4   F1s u0 p3 c0 {1,S}
5 * O2s u1 p2 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 613,
    label = "O2sJ-Cd-HCd-F1sCs-HH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S} {8,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7 * O2s u1 p2 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.15968,-9.49679,-11.168,-12.1777,-13.2982,-15.1636,-18.4995],'J/(mol*K)'),
        H298 = (327.799,'kJ/mol'),
        S298 = (2.48238,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 614,
    label = "O2sJ-Cd-O2sCd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   O2s u0 p2 c0 {1,S}
4 * O2s u1 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 615,
    label = "O2sJ-Cd-CdO2s-HF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S}
4 * O2s u1 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.25834,-9.47199,-10.9515,-12.2268,-14.3271,-15.9534,-18.735],'J/(mol*K)'),
        H298 = (294.792,'kJ/mol'),
        S298 = (2.09187,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 616,
    label = "O2sJ-Cd-CdO2s-F1sH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   O2s u0 p2 c0 {1,S} {6,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   F1s u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.27049,-7.85013,-9.84738,-11.2755,-13.6398,-15.4785,-18.5892],'J/(mol*K)'),
        H298 = (320.435,'kJ/mol'),
        S298 = (1.91663,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 617,
    label = "O2sJ-Cd-HCd-CsH-F1sH",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,D} {7,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7 * O2s u1 p2 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.433,-12.2556,-13.488,-14.4273,-16.5145,-18.6738,-22.2075],'J/(mol*K)'),
        H298 = (349.795,'kJ/mol'),
        S298 = (-3.76196,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 718,
    label = "O2sJ-Cd-CdF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.11528,-7.00474,-9.1936,-10.609,-12.8364,-14.9487,-18.4359],'J/(mol*K)'),
        H298 = (295.397,'kJ/mol'),
        S298 = (6.08319,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),


entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 718,
    label = "O2sJ-Cd-CdF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.11528,-7.00474,-9.1936,-10.609,-12.8364,-14.9487,-18.4359],'J/(mol*K)'),
        H298 = (295.397,'kJ/mol'),
        S298 = (6.08319,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 684,
    label = "O2sJ-Cd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,S}
2 * O2s u1 p2 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 718,
    label = "O2sJ-Cd-CdF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.11528,-7.00474,-9.1936,-10.609,-12.8364,-14.9487,-18.4359],'J/(mol*K)'),
        H298 = (295.397,'kJ/mol'),
        S298 = (6.08319,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 718,
    label = "O2sJ-Cd-CdF1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.11528,-7.00474,-9.1936,-10.609,-12.8364,-14.9487,-18.4359],'J/(mol*K)'),
        H298 = (295.397,'kJ/mol'),
        S298 = (6.08319,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "O2sJ-Cd-CdF1s-O2s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3 * O2s u1 p2 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80255,-10.9917,-12.2922,-13.2987,-15.025,-16.4182,-18.9747],'J/(mol*K)'),
        H298 = (246.88,'kJ/mol'),
        S298 = (-0.589188,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 751,
    label = "OJC=O",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 752,
    label = "OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.5,-13.1,-16.3,-18.3,-20.4,-21.2,-21.4],'J/(mol*K)'),
        H298 = (460.9,'kJ/mol'),
        S298 = (6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 753,
    label = "OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.9,-17.5,-19.8,-19.3,-16.2,-14.3,-14.3],'J/(mol*K)'),
        H298 = (444.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 754,
    label = "O2sJ-Cs-HHO2s-Cs-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {2,S} {7,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 755,
    label = "O2sJ-Cs-HO2sH-Cs-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {3,S} {7,S} {8,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4 * O2s u1 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   F1s u0 p3 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.26187,-5.7871,-7.1952,-8.48149,-10.7581,-12.9316,-17.2327],'J/(mol*K)'),
        H298 = (432.431,'kJ/mol'),
        S298 = (2.32922,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 756,
    label = "CsOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],'cal/(mol*K)'),
        H298 = (104.06,'kcal/mol'),
        S298 = (-1.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI(ROJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 757,
    label = "H3COJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],'cal/(mol*K)'),
        H298 = (104.27,'kcal/mol'),
        S298 = (0.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 758,
    label = "O2sJ-Cs-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S}
2 * O2s u1 p2 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.20365,-8.27061,-9.83202,-11.1316,-13.4393,-15.2816,-18.4888],'J/(mol*K)'),
        H298 = (492.934,'kJ/mol'),
        S298 = (-8.83824,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 759,
    label = "O2sJ-Cs-HF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.34939,-6.27192,-7.47956,-8.87855,-11.51,-13.6268,-17.3354],'J/(mol*K)'),
        H298 = (455.881,'kJ/mol'),
        S298 = (0.164027,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 760,
    label = "CbOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = u'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 761,
    label = "O2sJ-Ct-Ct-F",
    group = 
"""
1   Ct  u0 p0 c0 {2,T} {3,S}
2   Ct  u0 p0 c0 {1,T} {4,S}
3   F   u0 p3 c0 {1,S}
4 * O2s u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.3327,-11.4723,-11.9878,-12.6312,-13.942,-15.2422,-18.1846],'J/(mol*K)'),
        H298 = (272.073,'kJ/mol'),
        S298 = (-0.371713,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 762,
    label = "O2sJ-Ct-Ct-Cs-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S}
2   Ct  u0 p0 c0 {1,S} {3,T}
3   Ct  u0 p0 c0 {2,T} {6,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * O2s u1 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.3132,-10.9707,-11.4932,-12.2423,-14.1436,-15.4764,-18.5071],'J/(mol*K)'),
        H298 = (297.361,'kJ/mol'),
        S298 = (-6.60568,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 763,
    label = "OOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   O2s u0 {1,S}
""",
    thermo = u'ROOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 764,
    label = "ROOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 765,
    label = "C(=O)OOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (98.33,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
u"""

""",
)

entry(
    index = 766,
    label = "C3COOJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S} {6,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6 * O2s u1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (85.3,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 767,
    label = "O2sJ-O2s-Cs-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   F1s u0 p3 c0 {1,S}
4 * O2s u1 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 768,
    label = "O2sJ-O2s-Cs-CsF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5 * O2s u1 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 769,
    label = "O2sJ-O2s-Cs-F1sCsF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 p2 c0 {1,S} {6,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6 * O2s u1 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 770,
    label = "O2sJ-O2s-Cs-F1sCsF1s-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7 * O2s u1 p2 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 771,
    label = "O2sJ-O2s-Cs-F1sF1sCs-HH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {8,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8 * O2s u1 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.53767,-9.61037,-10.967,-12.2195,-14.3202,-15.9838,-18.8791],'J/(mol*K)'),
        H298 = (377.024,'kJ/mol'),
        S298 = (-10.1408,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 772,
    label = "O2sJ-O2s-Cs-F1sCsH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 p2 c0 {1,S} {6,S}
3   Cs  u0 p0 c0 {1,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6 * O2s u1 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 773,
    label = "O2sJ-O2s-Cs-F1sHCs-H",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7 * O2s u1 p2 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 774,
    label = "O2sJ-O2s-Cs-F1sHCs-HH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {8,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8 * O2s u1 p2 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 775,
    label = "O2sJ-O2s-Cs-HF1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   F1s u0 p3 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5 * O2s u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.43251,-9.43891,-11.1015,-12.2823,-14.2778,-15.9698,-19.0636],'J/(mol*K)'),
        H298 = (380.546,'kJ/mol'),
        S298 = (1.371,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 776,
    label = "O2sJ-O2s-Cd-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   F1s u0 p3 c0 {1,S}
4 * O2s u1 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 777,
    label = "O2sJ-O2s-Cd-F1sCd",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   Cd  u0 p0 c0 {1,D}
4   F1s u0 p3 c0 {1,S}
5 * O2s u1 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 778,
    label = "O2sJ-O2s-Cd-F1sCd-H",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   O2s u0 p2 c0 {1,S} {6,S}
4   F1s u0 p3 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6 * O2s u1 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.4911,-10.2942,-11.0853,-12.3084,-14.4079,-16.0725,-18.9432],'J/(mol*K)'),
        H298 = (382.646,'kJ/mol'),
        S298 = (-3.686,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 779,
    label = "O2sJ-O2s-Cs-HCsH-F1s",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7 * O2s u1 p2 c0 {3,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 780,
    label = "O2sJ-O2s-Cs-HHCs-F1sH",
    group = 
"""
multiplicity [2]
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {6,S} {7,S}
3   O2s u0 p2 c0 {1,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   F1s u0 p3 c0 {2,S}
7   H   u0 p0 c0 {2,S}
8 * O2s u1 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.60691,-9.83685,-11.5667,-12.2273,-13.4714,-15.6949,-19.0469],'J/(mol*K)'),
        H298 = (356.09,'kJ/mol'),
        S298 = (7.0196,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 781,
    label = "O2sJ-O2s-Cd-CdH-F1s",
    group = 
"""
multiplicity [2]
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S}
3   O2s u0 p2 c0 {1,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
6 * O2s u1 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.1872,-10.7555,-11.2386,-12.3574,-14.6756,-16.3483,-18.9143],'J/(mol*K)'),
        H298 = (362.927,'kJ/mol'),
        S298 = (-4.31604,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 782,
    label = "HOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],'cal/(mol*K)'),
        H298 = (85.13,'kcal/mol'),
        S298 = (-0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 783,
    label = "SOJ",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S   ux c0 {1,S}
""",
    thermo = u'O2sJ-S2s',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 784,
    label = "O2sJ-S2s",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.621,-0.066,-0.612,-0.929,-1.545,-2.001,-2.488],'cal/(mol*K)'),
        H298 = (80.237,'kcal/mol'),
        S298 = (2.635,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value of 52.103 kcal/mol, 4/2017, Ryan Gillis
""",
)

entry(
    index = 785,
    label = "NJ",
    group = 
"""
1 * N u1
""",
    thermo = u'N3sJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 786,
    label = "N3sJ",
    group = 
"""
1 * N3s u1 p1
""",
    thermo = u'NHJ_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 787,
    label = "NH2J",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   H   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.43,-0.82,-1.27,-1.72,-2.48,-3.08,-4.1],'cal/(mol*K)'),
        H298 = (107.183,'kcal/mol'),
        S298 = (0.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to ammonia from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
u"""

""",
)

entry(
    index = 788,
    label = "NHJ_C",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-1.23,-1.64,-2.02,-2.66,-3.2,-4.16],'cal/(mol*K)'),
        H298 = (99.653,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to CH3NH2 from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
u"""

""",
)

entry(
    index = 789,
    label = "NHJ_O",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   O   u0 p2 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26,-1.89,-2.4,-2.79,-3.17,-3.37,-3.65],'cal/(mol*K)'),
        H298 = (85.023,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2OH and [NH]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 790,
    label = "NHJ_N",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N   u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77,-2.62,-3.28,-3.79,-4.57,-5.11,-5.85],'cal/(mol*K)'),
        H298 = (82.283,'kcal/mol'),
        S298 = (-0.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2NH2 and [NH]NH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 791,
    label = "NJ_CC",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.46,3.7,3.86,3.95,3.73,3.16,1.98],'cal/(mol*K)'),
        H298 = (120.063,'kcal/mol'),
        S298 = (10.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t CH3NHCH3 and CH3[N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 792,
    label = "N3dJ",
    group = 
"""
1 * N3d u1 p1
""",
    thermo = u'N3dJ_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 793,
    label = "N3dJ_C",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   C   u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2,-0.6,-1.07,-1.56,-2.44,-3.15,-4.26],'cal/(mol*K)'),
        H298 = (88.343,'kcal/mol'),
        S298 = (-0.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH=CH2 and [N]=CH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 794,
    label = "N3dJ_O",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12,-1.36,-1.67,-2,-2.62,-3.11,-3.89],'cal/(mol*K)'),
        H298 = (48.613,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t HN=O and [N]=O, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 795,
    label = "N3dJ_N",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14,-0.51,-0.97,-1.46,-2.33,-3.02,-4.16],'cal/(mol*K)'),
        H298 = (64.083,'kcal/mol'),
        S298 = (1.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t HN=NH and [N]=NH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 796,
    label = "SiJ",
    group = 
"""
1 * Si u1
""",
    thermo = u'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 797,
    label = "SJ",
    group = 
"""
1 * S u1
""",
    thermo = u'S2J',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 798,
    label = "S2J",
    group = 
"""
1 * S2s u1 p2
""",
    thermo = u'S2J-C',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 799,
    label = "S2J-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.52,-1.84,-2.17,-2.73,-3.2,-3.95],'cal/(mol*K)'),
        H298 = (91.82,'kcal/mol'),
        S298 = (-4.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 800,
    label = "S2J-C",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   C   u0 {1,S}
""",
    thermo = u'S2J-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 801,
    label = "S2J-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.94,-2.78,-2.72,-2.78,-3.07,-3.41,-4.04],'cal/(mol*K)'),
        H298 = (86.98,'kcal/mol'),
        S298 = (-2.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 802,
    label = "S2J-Ct",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18,-2.05,-2.66,-3.12,-3.76,-4.24,-4.99],'cal/(mol*K)'),
        H298 = (77.56,'kcal/mol'),
        S298 = (-4.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 803,
    label = "S2J-Cb",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92,-2.1,-2.3,-2.51,-2.93,-3.32,-3.96],'cal/(mol*K)'),
        H298 = (81.36,'kcal/mol'),
        S298 = (-3.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 804,
    label = "S2J-Cd",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * S2s u1 p2 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29,-2.56,-2.72,-2.87,-3.19,-3.52,-4.13],'cal/(mol*K)'),
        H298 = (79.29,'kcal/mol'),
        S298 = (-1.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 805,
    label = "S2J-C=S",
    group = 
"""
1   CS  u0 {2,S} {3,D}
2 * S2s u1 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93,-3.56,-3.88,-4.08,-4.41,-4.74,-5.25],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (-0.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 806,
    label = "S2J-CO",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * S2s u1 p2 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-2.82,-3.17,-3.44,-3.89,-4.29,-4.95],'cal/(mol*K)'),
        H298 = (89.6,'kcal/mol'),
        S298 = (-0.42,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 CAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 807,
    label = "S2J-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S}
""",
    thermo = u'S2J-S2s-H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 808,
    label = "S2J-S2s-H",
    group = 
"""
1   S2s u0 p2 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93,-2.7,-3.26,-3.67,-4.24,-4.59,-5],'cal/(mol*K)'),
        H298 = (73.97,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 809,
    label = "S2J-S2s-Cs",
    group = 
"""
1   S2s u0 p2 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95,-3.43,-3.78,-4.06,-4.47,-4.74,-5.03],'cal/(mol*K)'),
        H298 = (71.05,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 810,
    label = "S2J-S2s-S2s",
    group = 
"""
1   S2s u0 p2 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   S2s u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63,-4.32,-4.84,-5.26,-5.82,-6.07,-5.99],'cal/(mol*K)'),
        H298 = (72.74,'kcal/mol'),
        S298 = (0.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 811,
    label = "S2sJ-O",
    group = 
"""
1 * S2s u1 p2 c0 {2,S}
2   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.15904,-4.00975,-4.36187,-4.91092,-5.32059,-5.53025,-5.75797],'cal/(mol*K)'),
        H298 = (108.577,'kcal/mol'),
        S298 = (-7.47722,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 812,
    label = "S4sJ",
    group = 
"""
1 * S4s u1 p1
""",
    thermo = u'S4sJ-CCC',
    shortDesc = u"""Sulfur Oxygen Extension""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 813,
    label = "S4sJ-CCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.055,-3.801,4.696,-5.408,-6.524,-7.325,-8.52],'cal/(mol*K)'),
        H298 = (63.249,'kcal/mol'),
        S298 = (12.849,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
Calculated at CBS-QB3
""",
)

entry(
    index = 814,
    label = "S4dJ",
    group = 
"""
1 * S4d u1 p1
""",
    thermo = u'S4dJ-OdO',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 815,
    label = "S4dJ-OdH",
    group = 
"""
1 * S4d u1 p1 c0 {2,D} {3,S}
2   O2d u0 p2 c0 {1,D}
3   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.2,-1.93,-2.59,-3.6,-4.27,-5.1],'cal/(mol*K)'),
        H298 = (58,'kcal/mol'),
        S298 = (0.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 816,
    label = "S4dJ-OdO",
    group = 
"""
1 * S4d u1 p1 c0 {2,D} {3,S}
2   O2d u0 p2 c0 {1,D}
3   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-2.41,-3.09,-3.65,-4.42,-4.89,-5.45],'cal/(mol*K)'),
        H298 = (58.9,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 817,
    label = "S6sJ",
    group = 
"""
1 * S6s u1 p0
""",
    thermo = u'S6sJ-CCCCC',
    shortDesc = u"""Calculated at CBS-QB3""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 818,
    label = "S6sJ-CCCCC",
    group = 
"""
1 * S6s u1 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.815,3.48,2.34,1.364,-0.161,-1.233,-2.644],'cal/(mol*K)'),
        H298 = (60.164,'kcal/mol'),
        S298 = (9.723,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 819,
    label = "S6ddJ",
    group = 
"""
1 * S6dd u1 p0
""",
    thermo = u'S6ddJ-OdOdO',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
""",
)

entry(
    index = 820,
    label = "S6ddJ-OdOdH",
    group = 
"""
1 * S6dd u1 p0 c0 {2,D} {3,D} {4,S}
2   O2d  u0 p2 c0 {1,D}
3   O2d  u0 p2 c0 {1,D}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.977,0.64,-0.027,-0.741,-1.913,-2.873,-4.269],'cal/(mol*K)'),
        H298 = (75.948,'kcal/mol'),
        S298 = (3.331,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 821,
    label = "S6ddJ-OdOdO",
    group = 
"""
1 * S6dd u1 p0 c0 {2,D} {3,D} {4,S}
2   O2d  u0 p2 c0 {1,D}
3   O2d  u0 p2 c0 {1,D}
4   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539,-1.537,-2.332,-2.933,-4.01,-4.785,-5.701],'cal/(mol*K)'),
        H298 = (86.194,'kcal/mol'),
        S298 = (4.146,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
u"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 822,
    label = "RJ2_triplet",
    group = 
"""
1 * R!H u2
""",
    thermo = u'CJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 823,
    label = "CJ2_triplet",
    group = 
"""
1 * C u2
""",
    thermo = u'CsJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 824,
    label = "OsCsJ2H_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   O  u0 p2 {1,S} {4,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.444,-1.111,-1.988,-2.889,-4.529,-5.915,-8.422],'cal/(mol*K)'),
        H298 = (205.773,'kcal/mol'),
        S298 = (-2.011,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fittted to DFT_QCI_thermo library""",
    longDesc = 
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 825,
    label = "CsJ2_triplet",
    group = 
"""
1 * Cs u2
""",
    thermo = u'CH2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 826,
    label = "CH2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (214.44,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 827,
    label = "CsJ2_P_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = u'CsCsJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 828,
    label = "CsCsJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = u'CCJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 829,
    label = "CCJ2_triplet",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u2 {1,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],'cal/(mol*K)'),
        H298 = (211.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 830,
    label = "PhCH_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (195,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 831,
    label = "AllylJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (192.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 832,
    label = "CsJ2_S_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = u'CsJ2_P_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 833,
    label = "CdJ2_triplet",
    group = 
"""
1 * [Cd,CO] u2
""",
    thermo = u'CCdJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)



""",
)
entry(
    index = 835,
    label = "CdCdJ2_triplet",
    group = 
"""
1   Cd u0 {2,D} {3,S} {4,S}
2 * Cd u2 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904,-2.152,-3.433,-4.583,-6.214,-7.197,-9.27],'cal/(mol*K)'),
        H298 = (237.632,'kcal/mol'),
        S298 = (1.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fittted to DFT_QCI_thermo library""",
    longDesc = 
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 836,
    label = "(CO)CdJ2_triplet",
    group = 
"""
1   Cdd u0 {2,D} {3,D}
2 * Cd  u2 {1,D}
3   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.763,-2.732,-3.654,-4.473,-5.712,-6.563,-8.315],'cal/(mol*K)'),
        H298 = (206.595,'kcal/mol'),
        S298 = (-1.634,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fittted to DFT_QCI_thermo library""",
    longDesc = 
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 837,
    label = "CdJ2-Sd_triplet",
    group = 
"""
1 * CS  u2 {2,D}
2   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-2.3,-3.22,-4.04,-5.42,-6.5,-8.29],'cal/(mol*K)'),
        H298 = (238.75,'kcal/mol'),
        S298 = (-3.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 838,
    label = "NJ2_triplet",
    group = 
"""
1 * N u2
""",
    thermo = u'NJ2_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 839,
    label = "N3sJ2",
    group = 
"""
1 * N3s u2 p1
""",
    thermo = u'NJ2_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 840,
    label = "NHJ2",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.1,-2.78,-3.47,-4.75,-5.77,-7.61],'cal/(mol*K)'),
        H298 = (200.636,'kcal/mol'),
        S298 = (-2.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH3 and [N], both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 841,
    label = "NJ2_C",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36,-2.97,-3.51,-4,-5,-5.96,-7.75],'cal/(mol*K)'),
        H298 = (184.816,'kcal/mol'),
        S298 = (-3.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2CH3 and [N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 842,
    label = "NJ2_O",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   O   u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-3.22,-4.34,-5.36,-6.88,-7.91,-9.25],'cal/(mol*K)'),
        H298 = (166.156,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2OH and [N]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 843,
    label = "Oa_triplet",
    group = 
"""
1 * O u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (221.55,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 844,
    label = "SiJ2_triplet",
    group = 
"""
1 * Si u2
""",
    thermo = u'CJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 845,
    label = "SJ2_triplet",
    group = 
"""
1 * S u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19,-3.52,-3.89,-4.3,-5.12,-5.86,-7.14],'cal/(mol*K)'),
        H298 = (176.42,'kcal/mol'),
        S298 = (-12.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 846,
    label = "RJ3",
    group = 
"""
1 * R!H u3
""",
    thermo = u'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 847,
    label = "CJ3",
    group = 
"""
1 * Cs u3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],'cal/(mol*K)'),
        H298 = (316.19,'kcal/mol'),
        S298 = (-5.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 848,
    label = "SiJ3",
    group = 
"""
1 * Sis u3
""",
    thermo = u'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CH3
                L5: Cs_P_ClCl
                    L6: CsCsJ(Cl)(Cl)
                        L7: RCCJ(Cl)(Cl)
                L5: Cs_P_Cl
                    L6: CsCsJ(Cl)
                        L7: RCCJ(Cl)
                L5: Cs_P
                    L6: CJCO
                        L7: C=C(O)CJ
                        L7: CJCOOH
                        L7: CJC(C)OC
                        L7: CJC(C)2O
                            L8: C=CC(C)(O)CJ
                                L9: C=CC(O)(C=O)CJ
                            L8: CJC(C)(C=O)O
                        L7: CJC(O)2C
                            L8: C=CC(O)2CJ
                        L7: CsJ-HCsH-O2sHCs-HF1s
                            L8: CsJ-HHCs-HO2sCs-HHF1s
                    L6: CJCC=O
                        L7: CJC(C)2C=O
                            L8: CJC(C=O)2C
                                L9: C=CC(C=O)2CJ
                            L8: C=CC(C)(C=O)CJ
                        L7: CJC(C)C=O
                        L7: C=C(C=O)CJ
                    L6: CJCC=C=O
                        L7: CJC(C)C=C=O
                        L7: C=C(CJ)C=C=O
                    L6: CsCsJ
                        L7: CCJ
                        L7: RCCJ
                            L8: CsJ-CsHH-CsHH-F1s
                                L9: CsJ-CsHH-CsHH-F1sF1s
                                L9: CsJ-HCsH-HHCs-HF1sO2s
                            L8: CsJ-HHCs-HCdH-CdH-F1s
                        L7: Neopentyl
                        L7: Isobutyl
                        L7: CsJ-HHCs-F1s
                            L8: CsJ-CsHH-F1sF1s
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                        L7: CJC=C=O
                        L7: CsJ-HHCd-CdCs-F1sH
                            L8: CsJ-HHCd-CsCd-HHF1s
                                L9: CsJ-CdHH-CsCd-F1sHHH
                        L7: CsJ-HCdH-F1s
                            L8: CsJ-HCdH-F1sCd
                                L9: CsJ-CdHH-CdF1s-F1s
                        L7: CsJ-HHCd-CdH-F1s
                        L7: CsJ-HCdH-HCd-HCs-F1sH
                        L7: CsJ-HHCd-CddH-Cd-F1s
                    L6: Propargyl
                    L6: CJC=O
                        L7: C2JC=O
                            L8: CsJ-COHH-CsO2d-HF1s
                L5: Cs_S_Cl
                    L6: (Cs)2ClCsJ
                L5: Cs_S
                    L6: CCJCO
                        L7: C=CCJCO
                            L8: C=CCJC(O)C=C
                        L7: CCJCOOH
                        L7: CsJ-CsCsH-HF1sHHO2sH
                    L6: CCJCC=O
                    L6: CCJC(C)=C=O
                    L6: (Cs)2CsJ
                        L7: cyclopentene-4
                            L8: bicyclo[2.1.1]hex-2-ene-C5
                                L9: tricyclo[2.1.1.0(1,4)]hex-2-ene-C5
                            L8: bicyclo[2.1.0]pent-2-ene-C5
                        L7: bicyclo[1.1.1]pentane-C2
                            L8: tricyclo[1.1.1.0(1,3)]pentane-C2
                        L7: bicyclo[2.1.1]hexane-C5
                            L8: tricyclo[2.1.1.0(1,4)]hexane-C5
                        L7: cyclopropane
                            L8: spiro[2.2]pentane-secondary
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C7
                            L8: bicyclo[2.1.0]pentane-secondary-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C6
                            L8: bicyclo[1.1.0]butane-secondary
                            L8: bicyclo[3.1.0]hexane-C3
                            L8: bicyclo[4.1.0]heptane-C3-7
                            L8: bicyclo[4.1.0]heptane-C3-7
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C2
                        L7: bicyclo[3.1.1]heptane-C6
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C2
                        L7: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[2.2.2]octane-C2
                            L8: tricyclo[2.2.2.0(1,4)]octane-C2
                        L7: cyclobutane
                            L8: bicyclo[2.1.0]pentane-secondary-C4
                            L8: bicyclo[2.2.0]hexane-secondary
                            L8: bicyclo[3.2.0]heptane-C5-6
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C2
                            L8: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[3.1.1]heptane-C2
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C2
                        L7: bicyclo[3.1.0]hexane-C5-2
                        L7: bicyclo[3.1.0]hexane-C5-3
                        L7: bicyclo[2.1.1]hexane-C2
                        L7: 7-norbornyl
                        L7: 2-norbornyl
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: cycloheptane
                            L8: bicyclo[3.2.0]heptane-C5-2
                            L8: bicyclo[3.2.0]heptane-C5-3
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[3.1.1]heptane-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C3
                        L7: octahydro-pentalene-C5-2
                        L7: octahydro-pentalene-C5-3
                        L7: bicyclo[4.2.0]octane-C6-2
                        L7: bicyclo[4.2.0]octane-C6-3
                        L7: CCJC
                        L7: RCCJC
                            L8: CsJ-CsCsH-HHHHCsH-HF1s
                        L7: RCCJCC
                            L8: cyclopentane
                            L8: cyclohexane
                        L7: CsJ-CsHCs-F1sCsHH
                            L8: CsJ-CsHCs-HHCsF1sH
                                L9: CsJ-CsCsH-HHCsHHF1s
                                    L10: CsJ-CsHCs-HCsHF1sHH-H
                                        L11: CsJ-HCsCs-HF1sCsHHH-HH
                        L7: CsJ-CsHCs-F1s
                            L8: CsJ-HCsCs-F1sF1s
                                L9: CsJ-HCsCs-HF1sF1s
                                    L10: CsJ-HCsCs-F1sHHF1s
                                        L11: CsJ-CsCsH-HF1sHF1sH
                    L6: Benzyl_S
                        L7: Indenyl
                        L7: Benzyl_S_Fused5
                        L7: Benzyl_S_Fused6
                            L8: Benzyl_S_dihydronaphthalene
                        L7: Benzyl_S_Fused7
                    L6: Allyl_S
                        L7: Aromatic_pi_S_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_S_(fused5)_1_3
                                    L10: Aromatic_pi_S_(fused6)_1_3
                                    L10: Aromatic_pi_S_(fused7)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2
                            L8: Aromatic_pi_S_(CH3_CH3_Para)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Para)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Para)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_3
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_3
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3
                        L7: CJ-Cd-Benzene
                        L7: CJ-Cd-Benzene7
                        L7: cyclobutene-allyl
                        L7: cyclopentene-allyl
                        L7: cyclohexene-allyl
                        L7: CsJ-HCsCd-F1sHH
                            L8: CsJ-HCdCs-CdF1sHH
                                L9: CsJ-HCsCd-HHCdHF1s
                                    L10: CsJ-CsCdH-F1sHHCdH-F1s
                        L7: CsJ-HCdCs-F1sCdHH
                            L8: CsJ-CdCsH-F1sHCdHH
                                L9: CsJ-CdHCs-HCdF1sHH-H
                        L7: CsJ-CsHCd-HHHHCd-F1s
                    L6: C=CCJC=C
                        L7: Aromatic_pi_S_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4
                                    L10: Aromatic_pi_S_(fused5)_1_4
                                    L10: Aromatic_pi_S_(fused6)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_4
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_4
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4
                        L7: cyclopropenyl-allyl
                        L7: 1,3-cyclopentadiene-allyl
                        L7: C=CCJC=C=O
                    L6: Sec_Propargyl
                    L6: CCJC=O
                        L7: CCJCHO
                        L7: C=OCJC=O
                L5: Cs_T
                    L6: CCJ(C)CO
                        L7: C2CJCOOH
                    L6: Tertalkyl
                        L7: bicyclo[1.1.0]butane-tertiary
                        L7: bicyclo[2.1.0]pentane-tertiary
                        L7: bicyclo[1.1.1]pentane-C1
                        L7: bicyclo[3.1.0]hexane-tertiary
                        L7: bicyclo[2.2.0]hexane-tertiary
                        L7: bicyclo[2.1.1]hexane-C1
                        L7: bridgehead_norbornyl
                        L7: bicyclo[3.2.0]heptane-tertiary
                        L7: bicyclo[4.1.0]heptane-tertiary
                        L7: bicyclo[3.1.1]heptane-C1
                        L7: octahydro-pentalene-tertiary
                        L7: bicyclo[4.2.0]octane-tertiary
                        L7: bicyclo[2.2.2]octane-C1
                        L7: CsJ-CsCsCs-F1sHHHH
                            L8: CsJ-CsCsCs-HHF1sHHH
                                L9: CsJ-CsCsCs-HHHHHHF1s
                                    L10: CsJ-CsCsCs-HHHHF1sHF1sH
                    L6: Benzyl_T
                        L7: Benzyl_T_Fused5
                        L7: Benzyl_T_Fused6
                            L8: Benzyl_T_dihydronaphthalene
                    L6: CCJ(C)C=C=O
                        L7: C=CCJ(C)C=C=O
                            L8: C=CCJ(C=C=O)C=C
                    L6: Allyl_T
                        L7: Aromatic_pi_T_1_3
                            L8: Aromatic_pi_T_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_T_(fused5)_1_3
                                    L10: Aromatic_pi_T_(fused6)_1_3
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3
                        L7: Aromatic_pi_T_1_4
                            L8: Aromatic_pi_T_(CH3_CH3_Para)_1_4
                                L9: Aromatic_pi_T_(CH3_C2H5_Para)_1_4
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Para)_1_4
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4
                        L7: bicyclo[2.1.0]pent-2-ene-C1
                        L7: bicyclo[2.1.1]hex-2-ene-C1
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C1
                        L7: C=CCJ(C)C=O
                            L8: C=CCJ(C=O)C=C
                    L6: Tert_Propargyl
                    L6: C2CJCO
                        L7: C2CJCHO
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                            L8: CsOJCF
                                L9: CsOJCF2
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                            L8: C=COCJ
                                L9: CsJ-HO2sH-Cd-HCd-F1s
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                L5: CCsJO
                    L6: CCsJOC
                        L7: C=CCJ(O)C
                        L7: CCsJOCs
                            L8: CsJ-HCsO2s-CsHHH-F1sH
                            L8: CsJ-CsO2sH-F1sHF1sCs
                                L9: CsJ-HO2sCs-F1sCsHF1s-H
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: C=CCJO
                        L7: CsJ-CdO2sH-HCdH-F1s
                    L6: OCJC=O
                    L6: CCsJOH
                        L7: FCCsJOH
                        L7: CsJ-O2sCsH-HCsHH-F1s
                            L8: CsJ-CsO2sH-CsHHH-F1sH
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                L5: C2CsJO
                    L6: C2CsJOH
                        L7: CsJ-CsO2sCs-F1sHHHH
                            L8: CsJ-CsCsO2s-HHHF1sHF1s
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
                L5: CsJ-S
                    L6: CsJ-SsHH
                    L6: CsJ-CSH
                        L7: CsJ-CsSsH
                        L7: CsJ-CtSsH
                        L7: CsJ-CbSsH
                        L7: CsJ-CdSsH
                        L7: CsJ-C=SSsH
                    L6: CsJ-CCS
                        L7: CsJ-CsCsSs
                        L7: CsJ-CsCtSs
                        L7: CsJ-CsCbSs
                        L7: CsJ-CsCdSs
                        L7: CsJ-CsC=SSs
                    L6: CsJ-SS
                        L7: CsJ-SsSsH
                        L7: CsJ-CSS
                            L8: CsJ-CsSsSs
                            L8: CsJ-CtSsSs
                            L8: CsJ-CbSsSs
                            L8: CsJ-CdSsSs
                            L8: CsJ-C=SSsSs
                        L7: CsJ-SsSsSs
                    L6: CCsJOS
                        L7: CCsJOHSH
                    L6: CsJ-SsOsH
                L5: CsJN
                L5: CCsJN
                L5: C2CsJN
                L5: OCJO
                    L6: CsJ-HO2sO2s-CsH-F1sH
                L5: CsJ-CdF1sCs
                    L6: CsJ-CsF1sCd-H
                        L7: CsJ-CsF1sCd-HH
                            L8: CsJ-F1sCsCd-HHH
                                L9: CsJ-CsCdF1s-HHHH
                                    L10: CsJ-CdF1sCs-CdHHHH
                                        L11: CsJ-CsF1sCd-HHHHCd-H
                L5: CsJ-CsF1sO2s
                    L6: CsJ-F1sO2sCs-Cs
                        L7: CsJ-F1sO2sCs-CsF1s
                            L8: CsJ-F1sO2sCs-HCsF1s
                                L9: CsJ-O2sF1sCs-HHF1sCs
                                    L10: CsJ-CsF1sO2s-F1sCsHH-H
                                        L11: CsJ-CsF1sO2s-HF1sCsH-HH
                L5: CsJ-CsF1sF1s
                    L6: CsJ-CsF1sF1s-O2s
                        L7: CsJ-F1sCsF1s-O2sH
                            L8: CsJ-CsF1sF1s-O2sHH
                                L9: CsJ-F1sF1sCs-O2sHH-Cs
                                    L10: CsJ-CsF1sF1s-HHO2s-Cs-H
                                        L11: CsJ-F1sF1sCs-HHO2s-Cs-HH
                L5: CsJ-F1sF1sCd
                    L6: CsJ-F1sF1sCd-H
                        L7: CsJ-CdF1sF1s-CdH
                            L8: CsJ-CdF1sF1s-HCd-H
                                L9: CsJ-F1sF1sCd-CdH-HCs
                                    L10: CsJ-F1sF1sCd-CdH-CsH-H
                                        L11: CsJ-F1sCdF1s-CdH-CsH-HH
                L5: CsJ-F1sCsCs
                    L6: CsJ-F1sCsCs-H
                        L7: CsJ-CsCsF1s-F1sH
                            L8: CsJ-F1sCsCs-F1sHH
                                L9: CsJ-CsF1sCs-F1sHHF1s
                                    L10: CsJ-F1sCsCs-HF1sHHF1s
                L5: CsJ-CsCtF1s
                    L6: CsJ-CsCtF1s-H
                        L7: CsJ-F1sCtCs-HCt
                            L8: CsJ-CsCtF1s-CtHH
                                L9: CsJ-F1sCsCt-HCtHH
                L5: CsJ-HF1sO2s
                    L6: CsJ-F1sO2sH-Cd
                        L7: CsJ-HF1sO2s-Cd-F1s
                            L8: CsJ-HF1sO2s-Cd-F1sCd
                                L9: CsJ-F1sHO2s-Cd-F1sCd-H
                L5: CsJ-COF1sCs
                    L6: CsJ-F1sCsCO-H
                        L7: CsJ-COCsF1s-HO2d
                            L8: CsJ-COCsF1s-O2dHH
                                L9: CsJ-CsCOF1s-O2dHHH
                L5: CsJ-F1sF1sCt
                    L6: CsJ-F1sCtF1s-Ct
                        L7: CsJ-CtF1sF1s-Ct-Cs
                            L8: CsJ-CtF1sF1s-Ct-Cs-F1s
                                L9: CsJ-F1sCtF1s-Ct-Cs-F1sH
                L5: CsJ-CtHF1s
                    L6: CsJ-CtF1sH-Ct
                        L7: CsJ-F1sHCt-Ct-Cs
                            L8: CsJ-HF1sCt-Ct-Cs-H
                                L9: CsJ-HCtF1s-Ct-Cs-HH
                L5: CsJ-CsO2sO2s-F1s
                    L6: CsJ-O2sCsO2s-F1sH
                        L7: CsJ-O2sO2sCs-HHF1s
                            L8: CsJ-O2sO2sCs-F1sHHH
                L5: CsJ-F1sHCd
                    L6: CsJ-CdF1sH-H
                        L7: CsJ-CdHF1s-CdH
                            L8: CsJ-HF1sCd-CdH-H
                L5: CsJ-F1sHCs
                    L6: CsJ-HCsF1s-H
                        L7: CsJ-CsHF1s-O2sH
                            L8: CsJ-F1sCsH-F1sHO2s
                L5: CsJ-F1sHCO
                    L6: CsJ-COHF1s-O2s
                        L7: CsJ-F1sHCO-O2dO2s
                L5: CsJ-O2sF1sO2s
                    L6: CsJ-O2sO2sF1s-H
                L5: CsJ-F1sO2sF1s
            L4: CdsJ
                L5: CdsJO
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CC(C)CJ=O
                            L8: CC(C)2CJ=O
                                L9: CC(C)(C=O)CJ=O
                                    L10: C=CC(C)(C=O)CJ=O
                                L9: C=CC(C)2CJ=O
                            L8: CC(C)(O)CJ=O
                                L9: C=CC(C)(O)CJ=O
                        L7: CCCJ=O
                            L8: C=OCCJ=O
                                L9: C=OC=OCJ=O
                            L8: C=C(C)CJ=O
                        L7: CsCJ=O
                            L8: COJ-O2dCs-F1s
                                L9: COJ-O2dCs-O2sF1s
                                    L10: COJ-O2dCs-O2sHF1s
                        L7: C=CCJ=O
                        L7: OC=OCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                            L8: COJ-O2dO2s-Cs-F1s
                                L9: COJ-O2sO2d-Cs-HF1s
                L5: Cds-P-Cl
                    L6: CJ(Cl)=CC
                L5: Cds_P
                    L6: C=C=CJ
                        L7: CdJ-HCdd-Cd-F1s
                        L7: CdJ-CddH-Cdd-Cd-F1s
                    L6: CdJ-HCd-F1s
                        L7: CdJ-CdH-F1sO2s
                            L8: CdJ-HCd-O2sF1s-O2s
                    L6: CdJ-HCd-O2sCs-HF1s
                        L7: CdJ-HCd-O2sCs-HF1sH
                    L6: CdJ-HCd-CsH-F1sH
                L5: Cds_S
                    L6: C=CJC=O
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                            L8: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                        L7: 1,3-cyclopentadiene-vinyl-2
                        L7: CdJ-CdCd-F1s
                            L8: CdJ-CdCd-HF1s
                                L9: CdJ-CdCd-HHF1s
                                    L10: CdJ-CdCd-F1sHCdH
                                        L11: CdJ-CdCd-HCdF1sH-H
                        L7: CdJ-CdCd-HHHCd-F1s
                    L6: cyclopropenyl-vinyl
                    L6: cyclobutene-vinyl
                        L7: bicyclo[2.1.0]pent-2-ene-C2
                            L8: tricyclo[2.1.1.0(1,4)]hex-2-ene-C2
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C2
                    L6: cyclopentene-vinyl
                        L7: bicyclo[2.1.1]hex-2-ene-C2
                    L6: 1,3-cyclopentadiene-vinyl-1
                    L6: CCCJ=C=O
                        L7: CC(C)CJ=C=O
                        L7: C=C(C)CJ=C=O
                    L6: OC=CJCb
                    L6: CdJ-CsCd-CsF1s
                        L7: CdJ-CsCd-F1sHCs
                            L8: CdJ-CdCs-CsF1sF1sH
                                L9: CdJ-CsCd-F1sHF1sHCs
                                    L10: CdJ-CdCs-HF1sF1sCsH-H
                                        L11: CdJ-CdCs-F1sHHCsF1s-HF1s
                            L8: CdJ-CdCs-F1sHCsH
                                L9: CdJ-CsCd-F1sHHHCs
                                    L10: CdJ-CdCs-HCsHHF1s-H
                                        L11: CdJ-CdCs-HHHF1sCs-HH
                    L6: CdJ-CddCs-F1sCd
                        L7: CdJ-CsCdd-F1sHCd
                            L8: CdJ-CddCs-F1sCdHH
                                L9: CdJ-CddCs-HCdF1sH-H
                    L6: CdJ-CsCd-F1s
                        L7: CdJ-CsCd-F1sH
                            L8: CdJ-CdCs-F1sHF1s
                                L9: CdJ-CdCs-HF1sHF1s
                            L8: CdJ-CdCs-F1sHCsHH
                                L9: CdJ-CdCs-HCsF1sHH-H
                                    L10: CdJ-CdCs-HCsF1sHH-HF1s
                    L6: CdJ-CtCd-F1s
                        L7: CdJ-CdCt-F1sCt
                            L8: CdJ-CdCt-F1sHCt
                    L6: CdJ-CddCs-O2dF1s
                        L7: CdJ-CddCs-F1sHO2d
                    L6: CdJ-CsCd-HHHCsH-F1s
                        L7: CdJ-CdCs-HHCsHH-F1sH
                    L6: CdJ-CsCd-F1sHHO2s
                        L7: CdJ-CsCd-HF1sO2sHH
                    L6: CdJ-CsCdd-HHCdH-F1s
                    L6: CdJ-CsCd-F1sHHH
                    L6: CdJ-CdCs-HHHCsH-HF1s
                L5: CdsJ-S2s
                L5: C=CJO
                    L6: CdJ-CdO2s-F1sH
                        L7: CdJ-CdO2s-CsF1sH
                            L8: CdJ-O2sCd-CsF1sH-H
                                L9: CdJ-CdO2s-CsHF1s-HF1s
                    L6: CdJ-O2sCd-F1sF1s
                        L7: CdJ-CdO2s-F1sF1sCs
                    L6: CdJ-CddO2s-HCd-F1s
                    L6: CdJ-O2sCd-HHCs-F1sH
                L5: CdJ-CdF1s
                    L6: CdJ-F1sCd-H
                        L7: CdJ-F1sCd-HCs
                            L8: CdJ-F1sCd-CsH-Cs
                                L9: CdJ-F1sCd-CsH-CsH
                                    L10: CdJ-CdF1s-CsH-HCsH
                                        L11: CdJ-F1sCd-CsH-CsHH-H
                                            L12: CdJ-F1sCd-CsH-HHCs-HH
                L5: CdJ-F1sCdd
                    L6: CdJ-F1sCdd-Cdd
            L4: CtJ
                L5: Acetyl
                L5: CtJ-Ct-Cd-F1s
                    L6: CtJ-Ct-Cd-F1sCd
                        L7: CtJ-Ct-Cd-CdF1s-H
                L5: CtJ-Ct-Cs-F1s
                    L6: CtJ-Ct-Cs-O2sF1s
                        L7: CtJ-Ct-Cs-F1sHO2s
                L5: CtJ-Ct-Cs-HCsH-F1s
                    L6: CtJ-Ct-Cs-HHCs-HF1s
                L5: CtJ-Ct-O2s-Cs-F1sH
            L4: CbJ
            L4: C=SJ
                L5: C=SJ-S2s
                L5: C=SJ-H
                L5: C=SJ-C
                    L6: C=SJ-Cd
                    L6: C=SJ-Cs
        L3: OJ
            L4: HOJ
            L4: FOJ
            L4: COJ
                L5: CCOJ
                    L6: CC(F)OJ
                        L7: FCC(F)OJ
                        L7: HOCC(F)OJ
                        L7: CC(F)(F)OJ
                    L6: C=OCOJ
                        L7: C=CC(C)(C=O)OJ
                        L7: CC(C)(C=O)OJ
                        L7: C=OC=OOJ
                    L6: CC(C)OJ
                        L7: CC(C)2OJ
                            L8: C=CC(C)2OJ
                        L7: CC(C)(O)OJ
                            L8: C=CC(C)(O)OJ
                        L7: O2sJ-Cs-CsCsH-F1sH
                            L8: O2sJ-Cs-HCsCs-F1sF1sH
                                L9: O2sJ-Cs-HCsCs-HHF1sF1s
                                    L10: O2sJ-Cs-CsHCs-HHF1sHF1s
                    L6: C=C(C)OJ
                        L7: O2sJ-Cd-CsCd-F1s
                            L8: O2sJ-Cd-CdCs-F1sH
                                L9: O2sJ-Cd-CsCd-F1sHH
                                    L10: O2sJ-Cd-CdCs-HF1sHH
                        L7: O2sJ-Cd-CdCs-F1s
                            L8: O2sJ-Cd-CsCd-F1sH
                                L9: O2sJ-Cd-CdCs-HF1sF1s
                                    L10: O2sJ-Cd-CdCs-F1sHF1sF1s
                    L6: O2sJ-Cs-HF1sCt
                    L6: O2sJ-Cs-CsHH-F1s
                        L7: O2sJ-Cs-HCsH-HF1s
                            L8: O2sJ-Cs-HCsH-F1sCsH
                                L9: O2sJ-Cs-HHCs-F1sHCs-H
                                    L10: O2sJ-Cs-HHCs-F1sHCs-HH
                            L8: O2sJ-Cs-HCsH-F1sO2sH
                    L6: O2sJ-Cs-HO2sCs-F1s
                        L7: O2sJ-Cs-O2sHCs-HF1s
                            L8: O2sJ-Cs-O2sCsH-F1sHH
                    L6: O2sJ-Cs-HCsH-CsHH-F1s
                        L7: O2sJ-Cs-HCsH-CsHH-F1sH
                    L6: O2sJ-Cs-HHCd-F1sCd
                        L7: O2sJ-Cs-CdHH-CdF1s-H
                    L6: O2sJ-Cs-CdHH-HCd-F1s
                    L6: O2sJ-Cs-HO2sCs-HHF1s
                L5: CdsOJ
                    L6: RC=COJ
                        L7: C=COJ
                            L8: O2sJ-Cd-CdH-F1s
                                L9: O2sJ-Cd-CdH-CsF1s
                                    L10: O2sJ-Cd-HCd-CsF1s-H
                                        L11: O2sJ-Cd-HCd-F1sCs-HH
                            L8: O2sJ-Cd-O2sCd-F1s
                                L9: O2sJ-Cd-CdO2s-HF1s
                            L8: O2sJ-Cd-CdO2s-F1sH
                            L8: O2sJ-Cd-HCd-CsH-F1sH
                            L8: O2sJ-Cd-CdF1s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                            L8: O2sJ-Cd-CdF1s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                        L7: O2sJ-Cd-F1s
                            L8: O2sJ-Cd-CdF1s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                            L8: O2sJ-Cd-CdF1s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                                L9: O2sJ-Cd-CdF1s-O2s
                    L6: OJC=O
                        L7: OC=OOJ
                L5: OCOJ
                    L6: O2sJ-Cs-HHO2s-Cs-F1s
                        L7: O2sJ-Cs-HO2sH-Cs-F1sH
                L5: CsOJ
                    L6: H3COJ
                    L6: O2sJ-Cs-F1s
                        L7: O2sJ-Cs-HF1s
                L5: CbOJ
                L5: O2sJ-Ct-Ct-F
                L5: O2sJ-Ct-Ct-Cs-F1sH
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                    L6: O2sJ-O2s-Cs-F1s
                        L7: O2sJ-O2s-Cs-CsF1s
                            L8: O2sJ-O2s-Cs-F1sCsF1s
                                L9: O2sJ-O2s-Cs-F1sCsF1s-H
                                    L10: O2sJ-O2s-Cs-F1sF1sCs-HH
                            L8: O2sJ-O2s-Cs-F1sCsH
                                L9: O2sJ-O2s-Cs-F1sHCs-H
                                    L10: O2sJ-O2s-Cs-F1sHCs-HH
                        L7: O2sJ-O2s-Cs-HF1s
                    L6: O2sJ-O2s-Cd-F1s
                        L7: O2sJ-O2s-Cd-F1sCd
                            L8: O2sJ-O2s-Cd-F1sCd-H
                    L6: O2sJ-O2s-Cs-HCsH-F1s
                        L7: O2sJ-O2s-Cs-HHCs-F1sH
                    L6: O2sJ-O2s-Cd-CdH-F1s
                L5: HOOJ
            L4: SOJ
                L5: O2sJ-S2s
        L3: NJ
            L4: N3sJ
                L5: NH2J
                L5: NHJ_C
                L5: NHJ_O
                L5: NHJ_N
                L5: NJ_CC
            L4: N3dJ
                L5: N3dJ_C
                L5: N3dJ_O
                L5: N3dJ_N
        L3: SiJ
        L3: SJ
            L4: S2J
                L5: S2J-H
                L5: S2J-C
                    L6: S2J-Cs
                        L7: S2sJ-(CsHHH)
                        L7: S2J-(Cs-Cb)
                    L6: S2J-Ct
                    L6: S2J-Cb
                    L6: S2J-Cd
                    L6: S2J-C=S
                    L6: S2J-CO
                L5: S2J-S2s
                    L6: S2J-S2s-H
                    L6: S2J-S2s-Cs
                    L6: S2J-S2s-S2s
                L5: S2sJ-O
            L4: S4sJ
                L5: S4sJ-CCC
            L4: S4dJ
                L5: S4dJ-OdH
                L5: S4dJ-OdO
            L4: S6sJ
                L5: S6sJ-CCCCC
            L4: S6ddJ
                L5: S6ddJ-OdOdH
                L5: S6ddJ-OdOdO
    L2: RJ2_triplet
        L3: CJ2_triplet
            L4: OsCsJ2H_triplet
            L4: CsJ2_triplet
                L5: CH2_triplet
                L5: CsJ2_P_triplet
                    L6: CsCsJ2_triplet
                        L7: CCJ2_triplet
                    L6: PhCH_triplet
                    L6: AllylJ2_triplet
                L5: CsJ2_S_triplet
            L4: CdJ2_triplet
                L5: CCdJ2_triplet
                    L6: CdCdJ2_triplet
                    L6: (CO)CdJ2_triplet
            L4: CdJ2-Sd_triplet
        L3: NJ2_triplet
            L4: N3sJ2
                L5: NHJ2
                L5: NJ2_C
                L5: NJ2_O
        L3: Oa_triplet
        L3: SiJ2_triplet
        L3: SJ2_triplet
    L2: RJ3
        L3: CJ3
        L3: SiJ3
    L2: RJ4
        L3: CJ4
"""
)

