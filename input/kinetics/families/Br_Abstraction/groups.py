#!/usr/bin/env python
# encoding: utf-8

name = "Br_Abstraction/groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 needs a lone pair in order to react. It cannot be 2S or 4S.
"""

template(reactants=["X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br", "Y_rad_birad_trirad_quadrad"], products=["X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br", "Y_rad_birad_trirad_quadrad"], ownReverse=True)

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br",
    group = "OR{Xtrirad_Br, Xbirad_Br, Xrad_Br, X_Br}",
    kinetics = None,
)

entry(
    index = 1,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_rad, Y_1centerbirad, Y_1centertrirad, Y_1centerquadrad}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Xtrirad_Br",
    group = "OR{C_quartet_Br, C_doublet_Br}",
    kinetics = None,
)

entry(
    index = 3,
    label = "C_quartet_Br",
    group = 
"""
1 *1 C u3 p0 {2,S}
2 *2 Br u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C_doublet_Br",
    group = 
"""
1 *1 C u1 p1 {2,S}
2 *2 Br u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Xbirad_Br",
    group = "OR{NH_triplet_Br, NH_singlet_Br, C/H_or_Val7/2_triplet_/H_or_Val7/, C/H_or_Val7/2_singlet_/H_or_Val7/}",
    kinetics = None,
)

entry(
    index = 6,
    label = "C/H_or_Val7/2_triplet_/H_or_Val7/",
    group = 
"""
1 *1 Cs       u2 {2,S} {3,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CH2_triplet_Br",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CH2_triplet_Br-F",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CH2_triplet_Br-Cl",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CH2_triplet_Br-Br",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "C/H_or_Val7/2_singlet_/H_or_Val7/",
    group = 
"""
1 *1 C        u0 p1 {2,S} {3,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CH2_singlet_Br",
    group = 
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CH2_singlet_Br-F",
    group = 
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CH2_singlet_Br-Cl",
    group = 
"""
1 *1 C  u0 p1 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CH2_singlet_Br-Br",
    group = 
"""
1 *1 C  u0 p1 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "NH_triplet_Br",
    group = 
"""
1 *1 N u2 p1 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "NH_singlet_Br",
    group = 
"""
1 *1 N u0 p2 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Xrad_Br",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 Br   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "C_rad_Br",
    group = 
"""
1 *1 C u1 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C/H_or_Val7/3_rad_/H_or_Val7/",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S} {4,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "CH3_rad_Br",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CH3_rad_Br-HF",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CH3_rad_Br-HCl",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CH3_rad_Br-HBr",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CH3_rad_Br-FF",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CH3_rad_Br-FCl",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CH3_rad_Br-FBr",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CH3_rad_Br-ClCl",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CH3_rad_Br-ClBr",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CH3_rad_Br-BrBr",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cs/H_or_Val7/2/OneDeN",
    group = 
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    [H,Val7]   u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cs/H2/OneDeN",
    group = 
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    H          u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cs/H2/OneDeN-F",
    group = 
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    F          u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Cs/H2/OneDeN-Cl",
    group = 
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    Cl         u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Cs/H2/OneDeN-Br",
    group = 
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    Br         u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "OH_rad_Br",
    group = 
"""
1 *1 O u1 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Srad_Br",
    group = 
"""
1 *1 S u1 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "N3s_rad_Br",
    group = 
"""
1 *1 N3s u1 {2,S}
2 *2 Br   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "N/H_or_Val7/2_rad_/H_or_Val7/",
    group = 
"""
1 *1 N3s      u1 {2,S} {3,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "NH2_rad_Br",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "NH2_rad_Br-F",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "NH2_rad_Br-Cl",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "NH2_rad_Br-Br",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "N3s_rad_Br_pri",
    group = 
"""
1 *1 N3s     u1 {2,S} {3,S}
2 *2 Br       u0 {1,S}
3    [C,N,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "N3s_rad_Br/H/NonDeN",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "N5sc_radH",
    group = 
"""
1 *1 N5sc u1 {2,S}
2 *2 Br    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "X_Br",
    group = 
"""
1 *1 R u0 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "H2",
    group = 
"""
1 *1 H u0 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Ct_Br",
    group = 
"""
1 *1 Ct    u0 {2,S} {3,T}
2 *2 Br     u0 {1,S}
3    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Ct/H/NonDeC",
    group = 
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 Br  u0 {1,S}
3    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Ct/H/NonDeN",
    group = 
"""
1 *1 Ct  u0 {2,S} {3,T}
2 *2 Br   u0 {1,S}
3    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "O_Br",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "O_pri-H_or_Val7-1",
    group = 
"""
1 *1 O        u0 {2,S} {3,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "O_pri",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "O_pri-F",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "O_pri-Cl",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "O_pri-Br",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "O_sec",
    group = 
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "O/H/NonDeC",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 Br  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "O/H/NonDeO",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "/H_or_Val7/2O2",
    group = 
"""
1 *1 O        u0 {2,S} {3,S}
2    O        u0 {1,S} {4,S}
3 *2 Br        u0 {1,S}
4    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "H2O2",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2    O u0 {1,S} {4,S}
3 *2 Br u0 {1,S}
4    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "H2O2-F",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2    O u0 {1,S} {4,S}
3 *2 Br u0 {1,S}
4    F u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "H2O2-Cl",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2    O  u0 {1,S} {4,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "H2O2-Br",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2    O  u0 {1,S} {4,S}
3 *2 Br  u0 {1,S}
4    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "ROO/H_or_Val7/_pri",
    group = 
"""
1    C        u0 {2,S} {4,S} {5,S} {6,S}
2    O        u0 {1,S} {3,S}
3 *1 O        u0 {2,S} {7,S}
4    Cs       u0 {1,S}
5    [H,Val7] u0 {1,S}
6    [H,Val7] u0 {1,S}
7 *2 Br        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "ROOH_pri",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "ROOH_pri-HF",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "ROOH_pri-HCl",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "ROOH_pri-HBr",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "ROOH_pri-FF",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "ROOH_pri-FCl",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "ROOH_pri-FBr",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "ROOH_pri-ClCl",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "ROOH_pri-ClBr",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "ROOH_pri-BrBr",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "ROO/H_or_Val7/_sec",
    group = 
"""
1    C        u0 {2,S} {4,S} {5,S} {6,S}
2    O        u0 {1,S} {3,S}
3 *1 O        u0 {2,S} {7,S}
4    Cs       u0 {1,S}
5    Cs       u0 {1,S}
6    [H,Val7] u0 {1,S}
7 *2 Br        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "ROOH_sec",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    H  u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "ROOH_sec-F",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    F  u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "ROOH_sec-Cl",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cl u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "ROOH_sec-Br",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Br u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "ROOH_ter",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {1,S}
7 *2 Br  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "O/H/NonDeN",
    group = 
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "O/H/OneDe",
    group = 
"""
1 *1 O                         u0 {2,S} {3,S}
2 *2 Br                         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "O/H/OneDeC",
    group = 
"""
1 *1 O                u0 {2,S} {3,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "O/H/OneDeN",
    group = 
"""
1 *1 O          u0 {2,S} {3,S}
2 *2 Br          u0 {1,S}
3    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "OSrad_O_Br",
    group = 
"""
1 *1 O     u0 {2,S} {3,S}
2 *2 Br     u0 {1,S}
3    [O,S] u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Orad_O_Br",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Srad_O_Br",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 Br u0 {1,S}
3    S u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "S_Br",
    group = 
"""
1 *1 S u0 {2,S}
2 *2 Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "S_pri-H_or_Val7-1",
    group = 
"""
1 *1 S2s      u0 {2,S} {3,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "S_pri",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "S_pri-F",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "S_pri-Cl",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "S_pri-Br",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "S/H/single",
    group = 
"""
1 *1 S   u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "S/H/NonDeC",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "S/H/NonDeS",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "S/H/NonDeN",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "S/H/NonDeO",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "S/H/OneDe",
    group = 
"""
1 *1 S2s              u0 {2,S} {3,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "S/H/Ct",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "S/H/Cb",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "S/H/CO",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "S/H/Cd",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D}
3 *2 Br   u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "S/H/CS",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2    CS  u0 {1,S} {4,D}
3 *2 Br   u0 {1,S}
4    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "S/H/Rad",
    group = 
"""
1 *1 S   u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    R!H u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "S/H/CRad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    Cs  u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "S/H/SRad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    S   u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "S/H/NRad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    N   u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "S/H/ORad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    O   u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "S/H/MulBondRad",
    group = 
"""
1 *1 S2s        u0 {2,S} {3,S}
2 *2 Br          u0 {1,S}
3    [Cd,CO,CS] u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "S/H/CORad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 Br   u0 {1,S}
3    CO  u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "S/H/CdRad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2    Cd  u1 {1,S} {4,D}
3 *2 Br   u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "S/H/CSRad",
    group = 
"""
1 *1 S2s u0 {2,S} {3,S}
2    CS  u1 {1,S} {4,D}
3 *2 Br   u0 {1,S}
4    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "S/H/double",
    group = 
"""
1 *1 S   u0 p[0,1] {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    R!H ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "S/H/double_val4",
    group = 
"""
1 *1 S   u0 p1 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    R!H ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "S/H/double_val4C",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 Br u0 {1,S}
3    C ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "S/H/double_val4N",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 Br u0 {1,S}
3    N ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "S/H/double_val4S",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 Br u0 {1,S}
3    S ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "S/H/double_val4O",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 Br u0 {1,S}
3    O ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "S/H/double_val6",
    group = 
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    R!H ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "S/H/double_val6C",
    group = 
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    C   ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "S/H/double_val6N",
    group = 
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    N   ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "S/H/double_val6S",
    group = 
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    S   ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "S/H/double_val6O",
    group = 
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    O   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "S/H/twoDoubles",
    group = 
"""
1 *1 S6dd u0 p0 {2,S} {3,D} {4,D}
2 *2 Br    u0 {1,S}
3    R!H  ux {1,D}
4    R!H  ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "S/H/twoDoublesOO",
    group = 
"""
1 *1 S6dd u0 p0 {2,S} {3,D} {4,D}
2 *2 Br    u0 {1,S}
3    O    u0 {1,D}
4    O    u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "S/H/triple",
    group = 
"""
1 *1 S   u0 p[0,1] {2,S} {3,T}
2 *2 Br   u0 {1,S}
3    R!H ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "S/H/triple_val4",
    group = 
"""
1 *1 S   u0 p1 {2,S} {3,T}
2 *2 Br   u0 {1,S}
3    R!H ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "S/H/triple_val4C",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,T}
2 *2 Br u0 {1,S}
3    C ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "S/H/triple_val4N",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,T}
2 *2 Br u0 {1,S}
3    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "S/H/triple_val4S",
    group = 
"""
1 *1 S u0 p1 {2,S} {3,T}
2 *2 Br u0 {1,S}
3    S ux p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "S/H/triple_val6",
    group = 
"""
1 *1 S   u0 p0 {2,S} {3,T}
2 *2 Br   u0 {1,S}
3    R!H ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "S/H/triple_val6C",
    group = 
"""
1 *1 S u0 p0 {2,S} {3,T}
2 *2 Br u0 {1,S}
3    C ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "S/H/triple_val6N",
    group = 
"""
1 *1 S u0 p0 {2,S} {3,T}
2 *2 Br u0 {1,S}
3    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "S/H/triple_val6S",
    group = 
"""
1 *1 S u0 p0 {2,S} {3,T}
2 *2 Br u0 {1,S}
3    S ux p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Cd_Br",
    group = 
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    [C,N] u0 {1,D}
3 *2 Br     u0 {1,S}
4    R     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Cd_pri-H_or_Val7-1",
    group = 
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    [Cd,N]   u0 {1,D} {5,S}
3 *2 Br        u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Cd_pri",
    group = 
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 Br      u0 {1,S}
4    H      u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Cd/H2/NonDeC",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Cd/H2/NonDeN",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D} {5,S}
3 *2 Br   u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Cd_pri-F",
    group = 
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 Br      u0 {1,S}
4    F      u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Cd/H2/NonDeC-F",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Cd/H2/NonDeN-F",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D} {5,S}
3 *2 Br   u0 {1,S}
4    F   u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Cd_pri-Cl",
    group = 
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 Br      u0 {1,S}
4    Cl     u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Cd/H2/NonDeC-Cl",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Cd/H2/NonDeN-Cl",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D} {5,S}
3 *2 Br   u0 {1,S}
4    Cl  u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Cd_pri-Br",
    group = 
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 Br      u0 {1,S}
4    Br     u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Cd/H2/NonDeC-Br",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Cd/H2/NonDeN-Br",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D} {5,S}
3 *2 Br   u0 {1,S}
4    Br  u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Cd_sec",
    group = 
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 Br      u0 {1,S}
4    R!H    u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    O  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Cd/H/NonDeS",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    S  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Cd/H/NonDeN",
    group = 
"""
1 *1 C          u0 {2,D} {3,S} {4,S}
2    Cd         u0 {1,D} {5,S}
3 *2 Br          u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
5    R          u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Cd/H/OneDe",
    group = 
"""
1 *1 C                                                u0 {2,D} {3,S} {4,S}
2    Cd                                               u0 {1,D} {5,S}
3 *2 Br                                                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N3t,N3b,N5dc,N5ddc,N5tc,N5b] u0 {1,S}
5    R                                                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Cd/H/Ct",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    Ct u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Cd/H/Cb",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    Cb u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Cd/H/CO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Cd/H/Cd",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {6,S}
3    Cd u0 {1,S} {5,D}
4 *2 Br  u0 {1,S}
5    C  u0 {3,D}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Cd/H/CS",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br  u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Cd/H/DeN",
    group = 
"""
1 *1 C                                 u0 {2,D} {3,S} {4,S}
2    Cd                                u0 {1,D} {5,S}
3 *2 Br                                 u0 {1,S}
4    [N3d,N3t,N3b,N5dc,N5ddc,N5tc,N5b] u0 {1,S}
5    R                                 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Cd_allenic",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 Br   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Cd_Cdd/H_or_Val7/2",
    group = 
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    Cdd      u0 {1,D}
3 *2 Br        u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Cd_Cdd/H2",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 Br   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Cd_Cdd/H2-F",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 Br   u0 {1,S}
4    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Cd_Cdd/H2-Cl",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 Br   u0 {1,S}
4    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Cd_Cdd/H2-Br",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 Br   u0 {1,S}
4    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Cb_Br",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,B} {4,S}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
4 *2 Br        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "CO_Br",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 Br u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "CO_pri-H_or_Val7-1",
    group = 
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    O        u0 {1,D}
3 *2 Br        u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "CO_pri",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 Br u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "CO_pri-F",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 Br u0 {1,S}
4    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "CO_pri-Cl",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    O  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "CO_pri-Br",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    O  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "CO_sec",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    O   u0 {1,D}
3 *2 Br   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "CO/H/NonDe",
    group = 
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    O        u0 {1,D}
3 *2 Br        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "CO/H/Cs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    O  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "CO/H/Cs\Cs|Cs",
    group = 
"""
1 *1 C  u0 {2,S} {4,D} {5,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {6,S}
4    O  u0 {1,D}
5 *2 Br  u0 {1,S}
6    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "CO/H/OneDe",
    group = 
"""
1 *1 C                u0 {2,D} {3,S} {4,S}
2    O                u0 {1,D}
3 *2 Br                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "CS_Br",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 Br u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "CS_pri-H_or_Val7-1",
    group = 
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    S        u0 {1,D}
3 *2 Br        u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "CS_pri",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 Br u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "CS_pri-F",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 Br u0 {1,S}
4    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "CS_pri-Cl",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "CS_pri-Br",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "CS_sec",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    S   u0 {1,D}
3 *2 Br   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "CS/H/NonDeC",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "CS/H/NonDeO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 Br u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "CS/H/NonDeS",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 Br u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "CS/H/OneDe",
    group = 
"""
1 *1 C                u0 {2,D} {3,S} {4,S}
2    S                u0 {1,D}
3 *2 Br                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "CS/H/Ct",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "CS/H/Cb",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 Br  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "CS/H/CO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 Br  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "CS/H/Cd",
    group = 
"""
1 *1 C  u0 {2,S} {3,D} {4,S}
2    Cd u0 {1,S} {5,D}
3    S  u0 {1,D}
4 *2 Br  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "CS/H/CS",
    group = 
"""
1 *1 C  u0 {2,S} {3,D} {4,S}
2    CS u0 {1,S} {5,D}
3    S  u0 {1,D}
4 *2 Br  u0 {1,S}
5    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Cs_Br",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "C_methane-H_or_Val7-3",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "C_methane",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "C_methane-HHF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "C_methane-HHCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "C_methane-HHBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "C_methane-HFF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    F u0 {1,S}
5    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "C_methane-HFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "C_methane-HFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "C_methane-HClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "C_methane-HClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "C_methane-HBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "C_methane-FFF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    F u0 {1,S}
4    F u0 {1,S}
5    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "C_methane-FFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "C_methane-FFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "C_methane-FClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "C_methane-FClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "C_methane-FBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "C_methane-ClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "C_methane-ClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "C_methane-ClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "C_methane-BrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "C_pri-H_or_Val7-2",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R!H      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "C_pri",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "C/H3/Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "C/H3/Cs\H3",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "C/H3/Cs\H3-HHHHF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "C/H3/Cs\H3-HHHHCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "C/H3/Cs\H3-HHHHBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "C/H3/Cs\H3-HHHFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "C/H3/Cs\H3-HHHFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "C/H3/Cs\H3-HHHFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "C/H3/Cs\H3-HHHClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "C/H3/Cs\H3-HHHClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "C/H3/Cs\H3-HHHBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "C/H3/Cs\H3-HHFFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "C/H3/Cs\H3-HHFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "C/H3/Cs\H3-HHFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "C/H3/Cs\H3-HHFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "C/H3/Cs\H3-HHFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "C/H3/Cs\H3-HHFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "C/H3/Cs\H3-HHClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "C/H3/Cs\H3-HHClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "C/H3/Cs\H3-HHClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "C/H3/Cs\H3-HHBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "C/H3/Cs\OneNonDe",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "C/H3/Cs\H2\Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "C/H3/Cs\H2\Cs|O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "C/H3/Cs\H2\O",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "C/H3/Cs\OneNonDe-HHHF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    H        u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "C/H3/Cs\H2\Cs-HHHF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "C/H3/Cs\H2\O-HHHF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    H     u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "C/H3/Cs\OneNonDe-HHHCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    H        u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "C/H3/Cs\H2\Cs-HHHCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "C/H3/Cs\H2\O-HHHCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    H     u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "C/H3/Cs\OneNonDe-HHHBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    H        u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "C/H3/Cs\H2\Cs-HHHBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "C/H3/Cs\H2\O-HHHBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    H     u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "C/H3/Cs\OneNonDe-HHFF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "C/H3/Cs\H2\Cs-HHFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "C/H3/Cs\H2\O-HHFF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "C/H3/Cs\OneNonDe-HHFCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "C/H3/Cs\H2\Cs-HHFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "C/H3/Cs\H2\O-HHFCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "C/H3/Cs\OneNonDe-HHFBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "C/H3/Cs\H2\Cs-HHFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "C/H3/Cs\H2\O-HHFBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "C/H3/Cs\OneNonDe-HHClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "C/H3/Cs\H2\Cs-HHClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "C/H3/Cs\H2\O-HHClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "C/H3/Cs\OneNonDe-HHClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "C/H3/Cs\H2\Cs-HHClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "C/H3/Cs\H2\O-HHClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "C/H3/Cs\OneNonDe-HHBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "C/H3/Cs\H2\Cs-HHBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "C/H3/Cs\H2\O-HHBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "C/H3/Cs\TwoNonDe",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "C/H3/Cs\H\Cs\O",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "C/H3/Cs\H\Cs\Cs|O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "C/H3/Cs\TwoNonDe-HHF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "C/H3/Cs\H\Cs\O-HHF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "C/H3/Cs\H\Cs\Cs|O-HHF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "C/H3/Cs\TwoNonDe-HHCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "C/H3/Cs\H\Cs\O-HHCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "C/H3/Cs\H\Cs\Cs|O-HHCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "C/H3/Cs\TwoNonDe-HHBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "C/H3/Cs\H\Cs\O-HHBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "C/H3/Cs\H\Cs\Cs|O-HHBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "C/H3/Cs\TwoDe",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    H             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    H             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "1_methyl_CPD",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     H  u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "C/H3/Cs\TwoDe-HHF",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    H             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    F             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "1_methyl_CPD-HHF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     F  u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "C/H3/Cs\TwoDe-HHCl",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    H             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Cl            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "1_methyl_CPD-HHCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Cl u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "C/H3/Cs\TwoDe-HHBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    H             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "1_methyl_CPD-HHBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "C/H3/O",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "C/H3/S",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "C/H3/OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "C/H3/Ct",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "C/H3/Cb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "C/H3/CO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "C/H3/CS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "C/H3/Cd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "2_methyl_CPD",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "3_methyl_CPD",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "C/H3/Cd\H_Cd\H2",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "C/H3/Cd\H_Cd\H2-HHHHF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "C/H3/Cd\H_Cd\H2-HHHHCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "C/H3/Cd\H_Cd\H2-HHHHBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "C/H3/Cd\H_Cd\H2-HHHFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "C/H3/Cd\H_Cd\H2-HHHFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "C/H3/Cd\H_Cd\H2-HHHFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "C/H3/Cd\H_Cd\H2-HHHClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "C/H3/Cd\H_Cd\H2-HHHClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "C/H3/Cd\H_Cd\H2-HHHBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "C/H3/Cd\H_Cd\H2-HHFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "C/H3/Cd\H_Cd\H2-HHFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "C/H3/Cd\H_Cd\H2-HHFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "C/H3/Cd\H_Cd\H2-HHFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "C/H3/Cd\H_Cd\H2-HHFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "C/H3/Cd\H_Cd\H2-HHFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "C/H3/Cd\H_Cd\H2-HHClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "C/H3/Cd\H_Cd\H2-HHClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "C/H3/Cd\H_Cd\H2-HHClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "C/H3/Cd\H_Cd\H2-HHBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "C/H3/Cd\H_Cd\H\Cs",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cs u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "C/H3/Cd\H_Cd\H\Cs-HHHF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cs u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "C/H3/Cd\H_Cd\H\Cs-HHHCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "C/H3/Cd\H_Cd\H\Cs-HHHBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "C/H3/Cd\H_Cd\H\Cs-HHFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "C/H3/Cd\H_Cd\H\Cs-HHFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "C/H3/Cd\H_Cd\H\Cs-HHFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "C/H3/Cd\H_Cd\H\Cs-HHClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "C/H3/Cd\H_Cd\H\Cs-HHClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "C/H3/Cd\H_Cd\H\Cs-HHBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "C/H3/Cd\Cs_Cd\H2",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "C/H3/Cd\Cs_Cd\H2-HHHF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "C/H3/Cd\Cs_Cd\H2-HHHCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "C/H3/Cd\Cs_Cd\H2-HHHBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "C/H3/Cd\Cs_Cd\H2-HHFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "C/H3/Cd\Cs_Cd\H2-HHFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "C/H3/Cd\Cs_Cd\H2-HHFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "C/H3/Cd\Cs_Cd\H2-HHClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "C/H3/Cd\Cs_Cd\H2-HHClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "C/H3/Cd\Cs_Cd\H2-HHBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "Cs/H3/NonDeN",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "Cs/H3/OneDeN",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    H          u0 {1,S}
5    H          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "C_pri-HF",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    F   u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "C/H3/Cs-HF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "C/H3/Cs\H3-HFFFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "C/H3/Cs\H3-HFFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "C/H3/Cs\H3-HFFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "C/H3/Cs\H3-HFFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "C/H3/Cs\H3-HFFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "C/H3/Cs\H3-HFFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "C/H3/Cs\H3-HFClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "C/H3/Cs\H3-HFClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "C/H3/Cs\H3-HFClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "C/H3/Cs\H3-HFBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "C/H3/Cs\OneNonDe-HFFF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "C/H3/Cs\H2\Cs-HFFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "C/H3/Cs\H2\O-HFFF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "C/H3/Cs\OneNonDe-HFFCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "C/H3/Cs\H2\Cs-HFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "C/H3/Cs\H2\O-HFFCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "C/H3/Cs\OneNonDe-HFFBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "C/H3/Cs\H2\Cs-HFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "C/H3/Cs\H2\O-HFFBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "C/H3/Cs\OneNonDe-HFClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "C/H3/Cs\H2\Cs-HFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "C/H3/Cs\H2\O-HFClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "C/H3/Cs\OneNonDe-HFClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "C/H3/Cs\H2\Cs-HFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "C/H3/Cs\H2\O-HFClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "C/H3/Cs\OneNonDe-HFBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "C/H3/Cs\H2\Cs-HFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "C/H3/Cs\H2\O-HFBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "C/H3/Cs\TwoNonDe-HFF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "C/H3/Cs\H\Cs\O-HFF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "C/H3/Cs\H\Cs\Cs|O-HFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "C/H3/Cs\TwoNonDe-HFCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "C/H3/Cs\H\Cs\O-HFCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "C/H3/Cs\H\Cs\Cs|O-HFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "C/H3/Cs\TwoNonDe-HFBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "C/H3/Cs\H\Cs\O-HFBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "C/H3/Cs\H\Cs\Cs|O-HFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 385,
    label = "C/H3/Cs\TwoDe-HFF",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    F             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    F             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 386,
    label = "1_methyl_CPD-HFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     F  u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 387,
    label = "C/H3/Cs\TwoDe-HFCl",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    F             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Cl            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 388,
    label = "1_methyl_CPD-HFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Cl u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 389,
    label = "C/H3/Cs\TwoDe-HFBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    F             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 390,
    label = "1_methyl_CPD-HFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 391,
    label = "C/H3/Cs\H2\Cs|O-HHHF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 392,
    label = "C/H3/O-HF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    F u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 393,
    label = "C/H3/S-HF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    F u0 {1,S}
5    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 394,
    label = "C/H3/OneDe-HF",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    F                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 395,
    label = "C/H3/Ct-HF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 396,
    label = "C/H3/Cb-HF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 397,
    label = "C/H3/CO-HF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 398,
    label = "C/H3/CS-HF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 399,
    label = "C/H3/Cd-HF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "2_methyl_CPD-HF",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "3_methyl_CPD-HF",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "C/H3/Cd\H_Cd\H2-HFFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "C/H3/Cd\H_Cd\H2-HFFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "C/H3/Cd\H_Cd\H2-HFFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "C/H3/Cd\H_Cd\H2-HFFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "C/H3/Cd\H_Cd\H2-HFFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "C/H3/Cd\H_Cd\H2-HFFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 408,
    label = "C/H3/Cd\H_Cd\H2-HFClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 409,
    label = "C/H3/Cd\H_Cd\H2-HFClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 410,
    label = "C/H3/Cd\H_Cd\H2-HFClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 411,
    label = "C/H3/Cd\H_Cd\H2-HFBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 412,
    label = "C/H3/Cd\H_Cd\H\Cs-HFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 413,
    label = "C/H3/Cd\H_Cd\H\Cs-HFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 414,
    label = "C/H3/Cd\H_Cd\H\Cs-HFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 415,
    label = "C/H3/Cd\H_Cd\H\Cs-HFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 416,
    label = "C/H3/Cd\H_Cd\H\Cs-HFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 417,
    label = "C/H3/Cd\H_Cd\H\Cs-HFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 418,
    label = "C/H3/Cd\Cs_Cd\H2-HFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 419,
    label = "C/H3/Cd\Cs_Cd\H2-HFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 420,
    label = "C/H3/Cd\Cs_Cd\H2-HFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 421,
    label = "C/H3/Cd\Cs_Cd\H2-HFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 422,
    label = "C/H3/Cd\Cs_Cd\H2-HFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 423,
    label = "C/H3/Cd\Cs_Cd\H2-HFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 424,
    label = "Cs/H3/NonDeN-HF",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    H   u0 {1,S}
5    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 425,
    label = "Cs/H3/OneDeN-HF",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    H          u0 {1,S}
5    F          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 426,
    label = "C_pri-HCl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    Cl  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 427,
    label = "C/H3/Cs-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 428,
    label = "C/H3/Cs\H3-HClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 429,
    label = "C/H3/Cs\H3-HClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 430,
    label = "C/H3/Cs\H3-HClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 431,
    label = "C/H3/Cs\H3-HClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 432,
    label = "C/H3/Cs\OneNonDe-HClClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 433,
    label = "C/H3/Cs\H2\Cs-HClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 434,
    label = "C/H3/Cs\H2\O-HClClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 435,
    label = "C/H3/Cs\OneNonDe-HClClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 436,
    label = "C/H3/Cs\H2\Cs-HClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 437,
    label = "C/H3/Cs\H2\O-HClClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 438,
    label = "C/H3/Cs\OneNonDe-HClBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 439,
    label = "C/H3/Cs\H2\Cs-HClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 440,
    label = "C/H3/Cs\H2\O-HClBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 441,
    label = "C/H3/Cs\TwoNonDe-HClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 442,
    label = "C/H3/Cs\H\Cs\O-HClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 443,
    label = "C/H3/Cs\H\Cs\Cs|O-HClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 444,
    label = "C/H3/Cs\TwoNonDe-HClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 445,
    label = "C/H3/Cs\H\Cs\O-HClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 446,
    label = "C/H3/Cs\H\Cs\Cs|O-HClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 447,
    label = "C/H3/Cs\TwoDe-HClCl",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    Cl            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Cl            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 448,
    label = "1_methyl_CPD-HClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Cl u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 449,
    label = "C/H3/Cs\TwoDe-HClBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    Cl            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 450,
    label = "1_methyl_CPD-HClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 451,
    label = "C/H3/Cs\H2\Cs|O-HHHCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 452,
    label = "C/H3/O-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 453,
    label = "C/H3/S-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 454,
    label = "C/H3/OneDe-HCl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    Cl               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 455,
    label = "C/H3/Ct-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 456,
    label = "C/H3/Cb-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 457,
    label = "C/H3/CO-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 458,
    label = "C/H3/CS-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 459,
    label = "C/H3/Cd-HCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 460,
    label = "2_methyl_CPD-HCl",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 461,
    label = "3_methyl_CPD-HCl",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 462,
    label = "C/H3/Cd\H_Cd\H2-HClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 463,
    label = "C/H3/Cd\H_Cd\H2-HClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 464,
    label = "C/H3/Cd\H_Cd\H2-HClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 465,
    label = "C/H3/Cd\H_Cd\H2-HClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 466,
    label = "C/H3/Cd\H_Cd\H\Cs-HClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 467,
    label = "C/H3/Cd\H_Cd\H\Cs-HClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 468,
    label = "C/H3/Cd\H_Cd\H\Cs-HClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 469,
    label = "C/H3/Cd\Cs_Cd\H2-HClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 470,
    label = "C/H3/Cd\Cs_Cd\H2-HClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 471,
    label = "C/H3/Cd\Cs_Cd\H2-HClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 472,
    label = "Cs/H3/NonDeN-HCl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    H   u0 {1,S}
5    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 473,
    label = "Cs/H3/OneDeN-HCl",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    H          u0 {1,S}
5    Cl         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 474,
    label = "C_pri-HBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    Br  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 475,
    label = "C/H3/Cs-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 476,
    label = "C/H3/Cs\H3-HBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 477,
    label = "C/H3/Cs\OneNonDe-HBrBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 478,
    label = "C/H3/Cs\H2\Cs-HBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Br u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 479,
    label = "C/H3/Cs\H2\O-HBrBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Br    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 480,
    label = "C/H3/Cs\TwoNonDe-HBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    H        u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 481,
    label = "C/H3/Cs\H\Cs\O-HBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Br    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 482,
    label = "C/H3/Cs\H\Cs\Cs|O-HBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 483,
    label = "C/H3/Cs\TwoDe-HBrBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    H             u0 {1,S}
5    Br            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 484,
    label = "1_methyl_CPD-HBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     H  u0 {2,S}
10    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 485,
    label = "C/H3/Cs\H2\Cs|O-HHHBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    H     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 486,
    label = "C/H3/O-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 487,
    label = "C/H3/S-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 488,
    label = "C/H3/OneDe-HBr",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    Br               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 489,
    label = "C/H3/Ct-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 490,
    label = "C/H3/Cb-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 491,
    label = "C/H3/CO-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 492,
    label = "C/H3/CS-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 493,
    label = "C/H3/Cd-HBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Br u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 494,
    label = "2_methyl_CPD-HBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 495,
    label = "3_methyl_CPD-HBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    H  u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 496,
    label = "C/H3/Cd\H_Cd\H2-HBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 497,
    label = "C/H3/Cd\H_Cd\H\Cs-HBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 498,
    label = "C/H3/Cd\Cs_Cd\H2-HBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 499,
    label = "Cs/H3/NonDeN-HBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    H   u0 {1,S}
5    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 500,
    label = "Cs/H3/OneDeN-HBr",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    H          u0 {1,S}
5    Br         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 501,
    label = "C_pri-FF",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    F   u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 502,
    label = "C/H3/Cs-FF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 503,
    label = "C/H3/Cs\H3-FFFFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 504,
    label = "C/H3/Cs\H3-FFFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 505,
    label = "C/H3/Cs\H3-FFFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 506,
    label = "C/H3/Cs\H3-FFFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 507,
    label = "C/H3/Cs\H3-FFFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 508,
    label = "C/H3/Cs\H3-FFFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 509,
    label = "C/H3/Cs\H3-FFClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 510,
    label = "C/H3/Cs\H3-FFClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 511,
    label = "C/H3/Cs\H3-FFClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 512,
    label = "C/H3/Cs\H3-FFBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 513,
    label = "C/H3/Cs\OneNonDe-FFFF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 514,
    label = "C/H3/Cs\H2\Cs-FFFF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 515,
    label = "C/H3/Cs\H2\Cs|O-FFFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 516,
    label = "C/H3/Cs\H2\O-FFFF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 517,
    label = "C/H3/Cs\OneNonDe-FFFCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 518,
    label = "C/H3/Cs\H2\Cs-FFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 519,
    label = "C/H3/Cs\H2\O-FFFCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 520,
    label = "C/H3/Cs\OneNonDe-FFFBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    F        u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 521,
    label = "C/H3/Cs\H2\Cs-FFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    F  u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 522,
    label = "C/H3/Cs\H2\O-FFFBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 523,
    label = "C/H3/Cs\OneNonDe-FFClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 524,
    label = "C/H3/Cs\H2\Cs-FFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 525,
    label = "C/H3/Cs\H2\O-FFClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 526,
    label = "C/H3/Cs\OneNonDe-FFClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 527,
    label = "C/H3/Cs\H2\Cs-FFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 528,
    label = "C/H3/Cs\H2\O-FFClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 529,
    label = "C/H3/Cs\OneNonDe-FFBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 530,
    label = "C/H3/Cs\H2\Cs-FFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 531,
    label = "C/H3/Cs\H2\O-FFBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 532,
    label = "C/H3/Cs\TwoNonDe-FFF",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    F        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 533,
    label = "C/H3/Cs\H\Cs\O-FFF",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 534,
    label = "C/H3/Cs\H\Cs\Cs|O-FFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 535,
    label = "C/H3/Cs\TwoNonDe-FFCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 536,
    label = "C/H3/Cs\H\Cs\O-FFCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 537,
    label = "C/H3/Cs\H\Cs\Cs|O-FFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 538,
    label = "C/H3/Cs\TwoNonDe-FFBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    F        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 539,
    label = "C/H3/Cs\H\Cs\O-FFBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 540,
    label = "C/H3/Cs\H\Cs\Cs|O-FFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 541,
    label = "C/H3/Cs\TwoDe-FFF",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    F             u0 {1,S}
5    F             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    F             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 542,
    label = "1_methyl_CPD-FFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     F  u0 {1,S}
8  *2 Br  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 543,
    label = "C/H3/Cs\TwoDe-FFCl",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    F             u0 {1,S}
5    F             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Cl            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 544,
    label = "1_methyl_CPD-FFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Cl u0 {1,S}
8  *2 Br  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 545,
    label = "C/H3/Cs\TwoDe-FFBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    F             u0 {1,S}
5    F             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 546,
    label = "1_methyl_CPD-FFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 547,
    label = "C/H3/Cs\H2\Cs|O-HHFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 548,
    label = "C/H3/Cs\H2\Cs|O-HFFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 549,
    label = "C/H3/O-FF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    F u0 {1,S}
4    F u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 550,
    label = "C/H3/S-FF",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    F u0 {1,S}
4    F u0 {1,S}
5    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 551,
    label = "C/H3/OneDe-FF",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    F                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 552,
    label = "C/H3/Ct-FF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 553,
    label = "C/H3/Cb-FF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 554,
    label = "C/H3/CO-FF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 555,
    label = "C/H3/CS-FF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 556,
    label = "C/H3/Cd-FF",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 557,
    label = "2_methyl_CPD-FF",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    F  u0 {1,S}
9    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 558,
    label = "3_methyl_CPD-FF",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    F  u0 {1,S}
9    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 559,
    label = "C/H3/Cd\H_Cd\H2-FFFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 560,
    label = "C/H3/Cd\H_Cd\H2-FFFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 561,
    label = "C/H3/Cd\H_Cd\H2-FFFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 562,
    label = "C/H3/Cd\H_Cd\H2-FFFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 563,
    label = "C/H3/Cd\H_Cd\H2-FFFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 564,
    label = "C/H3/Cd\H_Cd\H2-FFFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 565,
    label = "C/H3/Cd\H_Cd\H2-FFClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 566,
    label = "C/H3/Cd\H_Cd\H2-FFClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 567,
    label = "C/H3/Cd\H_Cd\H2-FFClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 568,
    label = "C/H3/Cd\H_Cd\H2-FFBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 569,
    label = "C/H3/Cd\H_Cd\H\Cs-FFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 570,
    label = "C/H3/Cd\H_Cd\H\Cs-FFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 571,
    label = "C/H3/Cd\H_Cd\H\Cs-FFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 572,
    label = "C/H3/Cd\H_Cd\H\Cs-FFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 573,
    label = "C/H3/Cd\H_Cd\H\Cs-FFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 574,
    label = "C/H3/Cd\H_Cd\H\Cs-FFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 575,
    label = "C/H3/Cd\Cs_Cd\H2-FFFF",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 576,
    label = "C/H3/Cd\Cs_Cd\H2-FFFCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 577,
    label = "C/H3/Cd\Cs_Cd\H2-FFFBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 578,
    label = "C/H3/Cd\Cs_Cd\H2-FFClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 579,
    label = "C/H3/Cd\Cs_Cd\H2-FFClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 580,
    label = "C/H3/Cd\Cs_Cd\H2-FFBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 581,
    label = "Cs/H3/NonDeN-FF",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    F   u0 {1,S}
5    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 582,
    label = "Cs/H3/OneDeN-FF",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    F          u0 {1,S}
5    F          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 583,
    label = "C_pri-FCl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    Cl  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 584,
    label = "C/H3/Cs-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 585,
    label = "C/H3/Cs\H3-FClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 586,
    label = "C/H3/Cs\H3-FClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 587,
    label = "C/H3/Cs\H3-FClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 588,
    label = "C/H3/Cs\H3-FClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 589,
    label = "C/H3/Cs\OneNonDe-FClClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 590,
    label = "C/H3/Cs\H2\Cs-FClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 591,
    label = "C/H3/Cs\H2\O-FClClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 592,
    label = "C/H3/Cs\OneNonDe-FClClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 593,
    label = "C/H3/Cs\H2\Cs-FClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 594,
    label = "C/H3/Cs\H2\O-FClClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 595,
    label = "C/H3/Cs\OneNonDe-FClBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 596,
    label = "C/H3/Cs\H2\Cs-FClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 597,
    label = "C/H3/Cs\H2\O-FClBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 598,
    label = "C/H3/Cs\TwoNonDe-FClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 599,
    label = "C/H3/Cs\H\Cs\O-FClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 600,
    label = "C/H3/Cs\H\Cs\Cs|O-FClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 601,
    label = "C/H3/Cs\TwoNonDe-FClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 602,
    label = "C/H3/Cs\H\Cs\O-FClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 603,
    label = "C/H3/Cs\H\Cs\Cs|O-FClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 604,
    label = "C/H3/Cs\TwoDe-FClCl",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    F             u0 {1,S}
5    Cl            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Cl            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 605,
    label = "1_methyl_CPD-FClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Cl u0 {1,S}
8  *2 Br  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 606,
    label = "C/H3/Cs\TwoDe-FClBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    F             u0 {1,S}
5    Cl            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 607,
    label = "1_methyl_CPD-FClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 608,
    label = "C/H3/Cs\H2\Cs|O-HHFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 609,
    label = "C/H3/Cs\H2\Cs|O-HFFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "C/H3/Cs\H2\Cs|O-FFFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "C/H3/O-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "C/H3/S-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 613,
    label = "C/H3/OneDe-FCl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    Cl               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 614,
    label = "C/H3/Ct-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 615,
    label = "C/H3/Cb-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 616,
    label = "C/H3/CO-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 617,
    label = "C/H3/CS-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 618,
    label = "C/H3/Cd-FCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 619,
    label = "2_methyl_CPD-FCl",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    F  u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 620,
    label = "3_methyl_CPD-FCl",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    F  u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 621,
    label = "C/H3/Cd\H_Cd\H2-FClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 622,
    label = "C/H3/Cd\H_Cd\H2-FClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 623,
    label = "C/H3/Cd\H_Cd\H2-FClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 624,
    label = "C/H3/Cd\H_Cd\H2-FClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 625,
    label = "C/H3/Cd\H_Cd\H\Cs-FClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 626,
    label = "C/H3/Cd\H_Cd\H\Cs-FClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 627,
    label = "C/H3/Cd\H_Cd\H\Cs-FClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 628,
    label = "C/H3/Cd\Cs_Cd\H2-FClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 629,
    label = "C/H3/Cd\Cs_Cd\H2-FClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 630,
    label = "C/H3/Cd\Cs_Cd\H2-FClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 631,
    label = "Cs/H3/NonDeN-FCl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    F   u0 {1,S}
5    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 632,
    label = "Cs/H3/OneDeN-FCl",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    F          u0 {1,S}
5    Cl         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 633,
    label = "C_pri-FBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    Br  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 634,
    label = "C/H3/Cs-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 635,
    label = "C/H3/Cs\H3-FBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 636,
    label = "C/H3/Cs\OneNonDe-FBrBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 637,
    label = "C/H3/Cs\H2\Cs-FBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 638,
    label = "C/H3/Cs\H2\O-FBrBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Br    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 639,
    label = "C/H3/Cs\TwoNonDe-FBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    F        u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 640,
    label = "C/H3/Cs\H\Cs\O-FBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Br    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 641,
    label = "C/H3/Cs\H\Cs\Cs|O-FBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 642,
    label = "C/H3/Cs\TwoDe-FBrBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    F             u0 {1,S}
5    Br            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 643,
    label = "1_methyl_CPD-FBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 644,
    label = "C/H3/Cs\H2\Cs|O-HHFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 645,
    label = "C/H3/Cs\H2\Cs|O-HFFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 646,
    label = "C/H3/Cs\H2\Cs|O-FFFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 647,
    label = "C/H3/O-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 648,
    label = "C/H3/S-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 649,
    label = "C/H3/OneDe-FBr",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    Br               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 650,
    label = "C/H3/Ct-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 651,
    label = "C/H3/Cb-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 652,
    label = "C/H3/CO-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 653,
    label = "C/H3/CS-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 654,
    label = "C/H3/Cd-FBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 655,
    label = "2_methyl_CPD-FBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    F  u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 656,
    label = "3_methyl_CPD-FBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    F  u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 657,
    label = "C/H3/Cd\H_Cd\H2-FBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 658,
    label = "C/H3/Cd\H_Cd\H\Cs-FBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 659,
    label = "C/H3/Cd\Cs_Cd\H2-FBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 660,
    label = "Cs/H3/NonDeN-FBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    F   u0 {1,S}
5    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 661,
    label = "Cs/H3/OneDeN-FBr",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    F          u0 {1,S}
5    Br         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 662,
    label = "C_pri-ClCl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    Cl  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 663,
    label = "C/H3/Cs-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 664,
    label = "C/H3/Cs\H3-ClClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 665,
    label = "C/H3/Cs\H3-ClClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 666,
    label = "C/H3/Cs\H3-ClClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 667,
    label = "C/H3/Cs\H3-ClClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 668,
    label = "C/H3/Cs\OneNonDe-ClClClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 669,
    label = "C/H3/Cs\H2\Cs-ClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 670,
    label = "C/H3/Cs\H2\Cs|O-ClClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 671,
    label = "C/H3/Cs\H2\O-ClClClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 672,
    label = "C/H3/Cs\OneNonDe-ClClClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Cl       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 673,
    label = "C/H3/Cs\H2\Cs-ClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Cl u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 674,
    label = "C/H3/Cs\H2\O-ClClClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 675,
    label = "C/H3/Cs\OneNonDe-ClClBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 676,
    label = "C/H3/Cs\H2\Cs-ClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 677,
    label = "C/H3/Cs\H2\O-ClClBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 678,
    label = "C/H3/Cs\TwoNonDe-ClClCl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Cl       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 679,
    label = "C/H3/Cs\H\Cs\O-ClClCl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 680,
    label = "C/H3/Cs\H\Cs\Cs|O-ClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 681,
    label = "C/H3/Cs\TwoNonDe-ClClBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Cl       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 682,
    label = "C/H3/Cs\H\Cs\O-ClClBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 683,
    label = "C/H3/Cs\H\Cs\Cs|O-ClClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 684,
    label = "C/H3/Cs\TwoDe-ClClCl",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    Cl            u0 {1,S}
5    Cl            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Cl            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 685,
    label = "1_methyl_CPD-ClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Cl u0 {1,S}
8  *2 Br  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 686,
    label = "C/H3/Cs\TwoDe-ClClBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    Cl            u0 {1,S}
5    Cl            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 687,
    label = "1_methyl_CPD-ClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 688,
    label = "C/H3/Cs\H2\Cs|O-HHClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 689,
    label = "C/H3/Cs\H2\Cs|O-HFClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 690,
    label = "C/H3/Cs\H2\Cs|O-HClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 691,
    label = "C/H3/Cs\H2\Cs|O-FFClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 692,
    label = "C/H3/Cs\H2\Cs|O-FClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 693,
    label = "C/H3/O-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 694,
    label = "C/H3/S-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 695,
    label = "C/H3/OneDe-ClCl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    Cl               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 696,
    label = "C/H3/Ct-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 697,
    label = "C/H3/Cb-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 698,
    label = "C/H3/CO-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 699,
    label = "C/H3/CS-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 700,
    label = "C/H3/Cd-ClCl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 701,
    label = "2_methyl_CPD-ClCl",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    Cl u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 702,
    label = "3_methyl_CPD-ClCl",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    Cl u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 703,
    label = "C/H3/Cd\H_Cd\H2-ClClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 704,
    label = "C/H3/Cd\H_Cd\H2-ClClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 705,
    label = "C/H3/Cd\H_Cd\H2-ClClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 706,
    label = "C/H3/Cd\H_Cd\H2-ClClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 707,
    label = "C/H3/Cd\H_Cd\H\Cs-ClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 708,
    label = "C/H3/Cd\H_Cd\H\Cs-ClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 709,
    label = "C/H3/Cd\H_Cd\H\Cs-ClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 710,
    label = "C/H3/Cd\Cs_Cd\H2-ClClClCl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 711,
    label = "C/H3/Cd\Cs_Cd\H2-ClClClBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 712,
    label = "C/H3/Cd\Cs_Cd\H2-ClClBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 713,
    label = "Cs/H3/NonDeN-ClCl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    Cl  u0 {1,S}
5    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 714,
    label = "Cs/H3/OneDeN-ClCl",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    Cl         u0 {1,S}
5    Cl         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 715,
    label = "C_pri-ClBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    Br  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 716,
    label = "C/H3/Cs-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 717,
    label = "C/H3/Cs\H3-ClBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 718,
    label = "C/H3/Cs\OneNonDe-ClBrBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 719,
    label = "C/H3/Cs\H2\Cs-ClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 720,
    label = "C/H3/Cs\H2\O-ClBrBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Br    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 721,
    label = "C/H3/Cs\TwoNonDe-ClBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Cl       u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 722,
    label = "C/H3/Cs\H\Cs\O-ClBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Br    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 723,
    label = "C/H3/Cs\H\Cs\Cs|O-ClBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 724,
    label = "C/H3/Cs\TwoDe-ClBrBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    Cl            u0 {1,S}
5    Br            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 725,
    label = "1_methyl_CPD-ClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 726,
    label = "C/H3/Cs\H2\Cs|O-HHClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 727,
    label = "C/H3/Cs\H2\Cs|O-HFClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 728,
    label = "C/H3/Cs\H2\Cs|O-HClClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 729,
    label = "C/H3/Cs\H2\Cs|O-FFClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 730,
    label = "C/H3/Cs\H2\Cs|O-FClClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 731,
    label = "C/H3/Cs\H2\Cs|O-ClClClBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Cl    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 732,
    label = "C/H3/O-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 733,
    label = "C/H3/S-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 734,
    label = "C/H3/OneDe-ClBr",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    Br               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 735,
    label = "C/H3/Ct-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 736,
    label = "C/H3/Cb-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 737,
    label = "C/H3/CO-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 738,
    label = "C/H3/CS-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 739,
    label = "C/H3/Cd-ClBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 740,
    label = "2_methyl_CPD-ClBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    Cl u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 741,
    label = "3_methyl_CPD-ClBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    Cl u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 742,
    label = "C/H3/Cd\H_Cd\H2-ClBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 743,
    label = "C/H3/Cd\H_Cd\H\Cs-ClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 744,
    label = "C/H3/Cd\Cs_Cd\H2-ClBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 745,
    label = "Cs/H3/NonDeN-ClBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    Cl  u0 {1,S}
5    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 746,
    label = "Cs/H3/OneDeN-ClBr",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    Cl         u0 {1,S}
5    Br         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 747,
    label = "C_pri-BrBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    Br  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 748,
    label = "C/H3/Cs-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 749,
    label = "C/H3/Cs\H3-BrBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 750,
    label = "C/H3/Cs\OneNonDe-BrBrBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Br       u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br       u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 751,
    label = "C/H3/Cs\H2\Cs-BrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
6    Cs u0 {2,S}
7    Br u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 752,
    label = "C/H3/Cs\H2\Cs|O-BrBrBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Br    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 753,
    label = "C/H3/Cs\H2\O-BrBrBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Br    u0 {1,S}
5    Br    u0 {1,S}
6    [O,S] u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 754,
    label = "C/H3/Cs\TwoNonDe-BrBrBr",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br        u0 {1,S}
4    Br       u0 {1,S}
5    Br       u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 755,
    label = "C/H3/Cs\H\Cs\O-BrBrBr",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br     u0 {1,S}
4    Br    u0 {1,S}
5    Br    u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 756,
    label = "C/H3/Cs\H\Cs\Cs|O-BrBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 757,
    label = "C/H3/Cs\TwoDe-BrBrBr",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Br             u0 {1,S}
4    Br            u0 {1,S}
5    Br            u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 758,
    label = "1_methyl_CPD-BrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     Br u0 {1,S}
8  *2 Br  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 759,
    label = "C/H3/Cs\H2\Cs|O-HHBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 760,
    label = "C/H3/Cs\H2\Cs|O-HFBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 761,
    label = "C/H3/Cs\H2\Cs|O-HClBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 762,
    label = "C/H3/Cs\H2\Cs|O-HBrBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 763,
    label = "C/H3/Cs\H2\Cs|O-FFBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 764,
    label = "C/H3/Cs\H2\Cs|O-FClBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 765,
    label = "C/H3/Cs\H2\Cs|O-FBrBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F     u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 766,
    label = "C/H3/Cs\H2\Cs|O-ClClBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 767,
    label = "C/H3/Cs\H2\Cs|O-ClBrBrBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cl    u0 {1,S}
5    Br    u0 {1,S}
6 *2 Br     u0 {2,S}
7    Br    u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 768,
    label = "C/H3/O-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 769,
    label = "C/H3/S-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 770,
    label = "C/H3/OneDe-BrBr",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Br               u0 {1,S}
4    Br               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 771,
    label = "C/H3/Ct-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 772,
    label = "C/H3/Cb-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 773,
    label = "C/H3/CO-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 774,
    label = "C/H3/CS-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 775,
    label = "C/H3/Cd-BrBr",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 776,
    label = "2_methyl_CPD-BrBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 Br  u0 {1,S}
8    Br u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 777,
    label = "3_methyl_CPD-BrBr",
    group = 
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 Br  u0 {1,S}
8    Br u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 778,
    label = "C/H3/Cd\H_Cd\H2-BrBrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 779,
    label = "C/H3/Cd\H_Cd\H\Cs-BrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Cs u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 780,
    label = "C/H3/Cd\Cs_Cd\H2-BrBrBrBr",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 Br  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {3,S}
9    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 781,
    label = "Cs/H3/NonDeN-BrBr",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 Br   u0 {1,S}
4    Br  u0 {1,S}
5    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 782,
    label = "Cs/H3/OneDeN-BrBr",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 Br          u0 {1,S}
4    Br         u0 {1,S}
5    Br         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 783,
    label = "C_sec-H_or_Val7-1",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H      u0 {1,S}
5    R!H      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 784,
    label = "C_sec",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 785,
    label = "C/H2/NonDeC",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 786,
    label = "C/H2/Cs/Cs\O",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S}
3 *2 Br     u0 {1,S}
4    H     u0 {1,S}
5    Cs    u0 {1,S}
6    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 787,
    label = "C/H2/Cs/Cs\Cs|O",
    group = 
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2    Cs    u0 {1,S} {3,S}
3    Cs    u0 {2,S} {7,S}
4 *2 Br     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {1,S}
7    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 788,
    label = "C/H2/NonDeC_5ring",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 Br  u0 {1,S}
7    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 789,
    label = "C/H2/NonDeC_5ring_fused6_1",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {8,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {4,S} {5,S} {7,S}
4    Cs u0 {1,S} {3,S}
5    Cs u0 {2,S} {3,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 790,
    label = "C/H2/NonDeC_5ring_fused6_2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {8,S} {9,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 791,
    label = "C/H2/NonDeC_5ring_alpha6ring",
    group = 
"""
1  *1 C  u0 {2,S} {4,S} {10,S} {11,S}
2     Cs u0 {1,S} {3,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {5,S}
5     Cs u0 {3,S} {4,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 792,
    label = "C/H2/NonDeC_5ring_beta6ring",
    group = 
"""
1  *1 C  u0 {4,S} {5,S} {10,S} {11,S}
2     Cs u0 {3,S} {4,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {2,S}
5     Cs u0 {1,S} {3,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 793,
    label = "C/H2/Cs\H3/Cs\H3",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 794,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHHF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 795,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHHCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 796,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHHBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 797,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 798,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 799,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 800,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 801,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 802,
    label = "C/H2/Cs\H3/Cs\H3-HHHHHBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 803,
    label = "C/H2/Cs\H3/Cs\H3-HHHHFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 804,
    label = "C/H2/Cs\H3/Cs\H3-HHHHFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 805,
    label = "C/H2/Cs\H3/Cs\H3-HHHHFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 806,
    label = "C/H2/Cs\H3/Cs\H3-HHHHFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 807,
    label = "C/H2/Cs\H3/Cs\H3-HHHHFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 808,
    label = "C/H2/Cs\H3/Cs\H3-HHHHFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 809,
    label = "C/H2/Cs\H3/Cs\H3-HHHHClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 810,
    label = "C/H2/Cs\H3/Cs\H3-HHHHClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 811,
    label = "C/H2/Cs\H3/Cs\H3-HHHHClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 812,
    label = "C/H2/Cs\H3/Cs\H3-HHHHBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 813,
    label = "C/H2/Cs\H3/Cs\H3-HHHFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 814,
    label = "C/H2/Cs\H3/Cs\H3-HHHFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 815,
    label = "C/H2/Cs\H3/Cs\H3-HHHFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 816,
    label = "C/H2/Cs\H3/Cs\H3-HHHFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 817,
    label = "C/H2/Cs\H3/Cs\H3-HHHFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 818,
    label = "C/H2/Cs\H3/Cs\H3-HHHFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 819,
    label = "C/H2/Cs\H3/Cs\H3-HHHFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 820,
    label = "C/H2/Cs\H3/Cs\H3-HHHFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 821,
    label = "C/H2/Cs\H3/Cs\H3-HHHFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 822,
    label = "C/H2/Cs\H3/Cs\H3-HHHFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 823,
    label = "C/H2/Cs\H3/Cs\H3-HHHClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 824,
    label = "C/H2/Cs\H3/Cs\H3-HHHClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 825,
    label = "C/H2/Cs\H3/Cs\H3-HHHClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 826,
    label = "C/H2/Cs\H3/Cs\H3-HHHClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 827,
    label = "C/H2/Cs\H3/Cs\H3-HHHBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 828,
    label = "C/H2/Cs\H3/Cs\H3-HHFFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 829,
    label = "C/H2/Cs\H3/Cs\H3-HHFFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 830,
    label = "C/H2/Cs\H3/Cs\H3-HHFFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 831,
    label = "C/H2/Cs\H3/Cs\H3-HHFFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 832,
    label = "C/H2/Cs\H3/Cs\H3-HHFFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 833,
    label = "C/H2/Cs\H3/Cs\H3-HHFFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 834,
    label = "C/H2/Cs\H3/Cs\H3-HHFFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 835,
    label = "C/H2/Cs\H3/Cs\H3-HHFFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 836,
    label = "C/H2/Cs\H3/Cs\H3-HHFFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 837,
    label = "C/H2/Cs\H3/Cs\H3-HHFFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 838,
    label = "C/H2/Cs\H3/Cs\H3-HHFClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 839,
    label = "C/H2/Cs\H3/Cs\H3-HHFClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 840,
    label = "C/H2/Cs\H3/Cs\H3-HHFClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 841,
    label = "C/H2/Cs\H3/Cs\H3-HHFClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 842,
    label = "C/H2/Cs\H3/Cs\H3-HHFBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 843,
    label = "C/H2/Cs\H3/Cs\H3-HHClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 844,
    label = "C/H2/Cs\H3/Cs\H3-HHClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 845,
    label = "C/H2/Cs\H3/Cs\H3-HHClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 846,
    label = "C/H2/Cs\H3/Cs\H3-HHClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 847,
    label = "C/H2/Cs\H3/Cs\H3-HHClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 848,
    label = "C/H2/Cs\H3/Cs\H3-HHBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 849,
    label = "C/H2/Cs\H3/Cs\H3-HFFFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 850,
    label = "C/H2/Cs\H3/Cs\H3-HFFFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 851,
    label = "C/H2/Cs\H3/Cs\H3-HFFFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 852,
    label = "C/H2/Cs\H3/Cs\H3-HFFFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 853,
    label = "C/H2/Cs\H3/Cs\H3-HFFFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 854,
    label = "C/H2/Cs\H3/Cs\H3-HFFFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 855,
    label = "C/H2/Cs\H3/Cs\H3-HFFFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 856,
    label = "C/H2/Cs\H3/Cs\H3-HFFFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 857,
    label = "C/H2/Cs\H3/Cs\H3-HFFFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 858,
    label = "C/H2/Cs\H3/Cs\H3-HFFFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 859,
    label = "C/H2/Cs\H3/Cs\H3-HFFClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 860,
    label = "C/H2/Cs\H3/Cs\H3-HFFClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 861,
    label = "C/H2/Cs\H3/Cs\H3-HFFClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 862,
    label = "C/H2/Cs\H3/Cs\H3-HFFClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 863,
    label = "C/H2/Cs\H3/Cs\H3-HFFBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 864,
    label = "C/H2/Cs\H3/Cs\H3-HFClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 865,
    label = "C/H2/Cs\H3/Cs\H3-HFClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 866,
    label = "C/H2/Cs\H3/Cs\H3-HFClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 867,
    label = "C/H2/Cs\H3/Cs\H3-HFClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 868,
    label = "C/H2/Cs\H3/Cs\H3-HFClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 869,
    label = "C/H2/Cs\H3/Cs\H3-HFBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 870,
    label = "C/H2/Cs\H3/Cs\H3-HClClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 871,
    label = "C/H2/Cs\H3/Cs\H3-HClClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 872,
    label = "C/H2/Cs\H3/Cs\H3-HClClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 873,
    label = "C/H2/Cs\H3/Cs\H3-HClClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 874,
    label = "C/H2/Cs\H3/Cs\H3-HClClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 875,
    label = "C/H2/Cs\H3/Cs\H3-HClBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 876,
    label = "C/H2/Cs\H3/Cs\H3-HBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 877,
    label = "C/H2/NonDeO",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    H        u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 878,
    label = "C/H2/CsO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 879,
    label = "C/H2/Cs\Cs2/O",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
15    H  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 880,
    label = "C/H2/Cs\Cs2/O-HHHHHHHHF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 881,
    label = "C/H2/Cs\Cs2/O-HHHHHHHHCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 882,
    label = "C/H2/Cs\Cs2/O-HHHHHHHHBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 883,
    label = "C/H2/Cs\Cs2/O-HHHHHHHFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 884,
    label = "C/H2/Cs\Cs2/O-HHHHHHHFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 885,
    label = "C/H2/Cs\Cs2/O-HHHHHHHFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 886,
    label = "C/H2/Cs\Cs2/O-HHHHHHHClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 887,
    label = "C/H2/Cs\Cs2/O-HHHHHHHClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 888,
    label = "C/H2/Cs\Cs2/O-HHHHHHHBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 889,
    label = "C/H2/Cs\Cs2/O-HHHHHHFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 890,
    label = "C/H2/Cs\Cs2/O-HHHHHHFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 891,
    label = "C/H2/Cs\Cs2/O-HHHHHHFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 892,
    label = "C/H2/Cs\Cs2/O-HHHHHHFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 893,
    label = "C/H2/Cs\Cs2/O-HHHHHHFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 894,
    label = "C/H2/Cs\Cs2/O-HHHHHHFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 895,
    label = "C/H2/Cs\Cs2/O-HHHHHHClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 896,
    label = "C/H2/Cs\Cs2/O-HHHHHHClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 897,
    label = "C/H2/Cs\Cs2/O-HHHHHHClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 898,
    label = "C/H2/Cs\Cs2/O-HHHHHHBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 899,
    label = "C/H2/Cs\Cs2/O-HHHHHFFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 900,
    label = "C/H2/Cs\Cs2/O-HHHHHFFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 901,
    label = "C/H2/Cs\Cs2/O-HHHHHFFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 902,
    label = "C/H2/Cs\Cs2/O-HHHHHFFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 903,
    label = "C/H2/Cs\Cs2/O-HHHHHFFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 904,
    label = "C/H2/Cs\Cs2/O-HHHHHFFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 905,
    label = "C/H2/Cs\Cs2/O-HHHHHFClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 906,
    label = "C/H2/Cs\Cs2/O-HHHHHFClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 907,
    label = "C/H2/Cs\Cs2/O-HHHHHFClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 908,
    label = "C/H2/Cs\Cs2/O-HHHHHFBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 909,
    label = "C/H2/Cs\Cs2/O-HHHHHClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 910,
    label = "C/H2/Cs\Cs2/O-HHHHHClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 911,
    label = "C/H2/Cs\Cs2/O-HHHHHClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 912,
    label = "C/H2/Cs\Cs2/O-HHHHHClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 913,
    label = "C/H2/Cs\Cs2/O-HHHHHBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 914,
    label = "C/H2/Cs\Cs2/O-HHHHFFFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 915,
    label = "C/H2/Cs\Cs2/O-HHHHFFFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 916,
    label = "C/H2/Cs\Cs2/O-HHHHFFFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 917,
    label = "C/H2/Cs\Cs2/O-HHHHFFFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 918,
    label = "C/H2/Cs\Cs2/O-HHHHFFFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 919,
    label = "C/H2/Cs\Cs2/O-HHHHFFFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 920,
    label = "C/H2/Cs\Cs2/O-HHHHFFClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 921,
    label = "C/H2/Cs\Cs2/O-HHHHFFClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 922,
    label = "C/H2/Cs\Cs2/O-HHHHFFClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 923,
    label = "C/H2/Cs\Cs2/O-HHHHFFBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 924,
    label = "C/H2/Cs\Cs2/O-HHHHFClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 925,
    label = "C/H2/Cs\Cs2/O-HHHHFClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 926,
    label = "C/H2/Cs\Cs2/O-HHHHFClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 927,
    label = "C/H2/Cs\Cs2/O-HHHHFClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 928,
    label = "C/H2/Cs\Cs2/O-HHHHFBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 929,
    label = "C/H2/Cs\Cs2/O-HHHHClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 930,
    label = "C/H2/Cs\Cs2/O-HHHHClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 931,
    label = "C/H2/Cs\Cs2/O-HHHHClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 932,
    label = "C/H2/Cs\Cs2/O-HHHHClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 933,
    label = "C/H2/Cs\Cs2/O-HHHHClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 934,
    label = "C/H2/Cs\Cs2/O-HHHHBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 935,
    label = "C/H2/Cs\Cs2/O-HHHFFFFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 936,
    label = "C/H2/Cs\Cs2/O-HHHFFFFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 937,
    label = "C/H2/Cs\Cs2/O-HHHFFFFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 938,
    label = "C/H2/Cs\Cs2/O-HHHFFFFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 939,
    label = "C/H2/Cs\Cs2/O-HHHFFFFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 940,
    label = "C/H2/Cs\Cs2/O-HHHFFFFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 941,
    label = "C/H2/Cs\Cs2/O-HHHFFFClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 942,
    label = "C/H2/Cs\Cs2/O-HHHFFFClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 943,
    label = "C/H2/Cs\Cs2/O-HHHFFFClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 944,
    label = "C/H2/Cs\Cs2/O-HHHFFFBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 945,
    label = "C/H2/Cs\Cs2/O-HHHFFClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 946,
    label = "C/H2/Cs\Cs2/O-HHHFFClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 947,
    label = "C/H2/Cs\Cs2/O-HHHFFClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 948,
    label = "C/H2/Cs\Cs2/O-HHHFFClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 949,
    label = "C/H2/Cs\Cs2/O-HHHFFBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 950,
    label = "C/H2/Cs\Cs2/O-HHHFClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 951,
    label = "C/H2/Cs\Cs2/O-HHHFClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 952,
    label = "C/H2/Cs\Cs2/O-HHHFClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 953,
    label = "C/H2/Cs\Cs2/O-HHHFClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 954,
    label = "C/H2/Cs\Cs2/O-HHHFClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 955,
    label = "C/H2/Cs\Cs2/O-HHHFBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 956,
    label = "C/H2/Cs\Cs2/O-HHHClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 957,
    label = "C/H2/Cs\Cs2/O-HHHClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 958,
    label = "C/H2/Cs\Cs2/O-HHHClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 959,
    label = "C/H2/Cs\Cs2/O-HHHClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 960,
    label = "C/H2/Cs\Cs2/O-HHHClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 961,
    label = "C/H2/Cs\Cs2/O-HHHClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 962,
    label = "C/H2/Cs\Cs2/O-HHHBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 963,
    label = "C/H2/Cs\Cs2/O-HHFFFFFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 964,
    label = "C/H2/Cs\Cs2/O-HHFFFFFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 965,
    label = "C/H2/Cs\Cs2/O-HHFFFFFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 966,
    label = "C/H2/Cs\Cs2/O-HHFFFFFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 967,
    label = "C/H2/Cs\Cs2/O-HHFFFFFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 968,
    label = "C/H2/Cs\Cs2/O-HHFFFFFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 969,
    label = "C/H2/Cs\Cs2/O-HHFFFFClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 970,
    label = "C/H2/Cs\Cs2/O-HHFFFFClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 971,
    label = "C/H2/Cs\Cs2/O-HHFFFFClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 972,
    label = "C/H2/Cs\Cs2/O-HHFFFFBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 973,
    label = "C/H2/Cs\Cs2/O-HHFFFClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 974,
    label = "C/H2/Cs\Cs2/O-HHFFFClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 975,
    label = "C/H2/Cs\Cs2/O-HHFFFClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 976,
    label = "C/H2/Cs\Cs2/O-HHFFFClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 977,
    label = "C/H2/Cs\Cs2/O-HHFFFBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 978,
    label = "C/H2/Cs\Cs2/O-HHFFClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 979,
    label = "C/H2/Cs\Cs2/O-HHFFClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 980,
    label = "C/H2/Cs\Cs2/O-HHFFClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 981,
    label = "C/H2/Cs\Cs2/O-HHFFClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 982,
    label = "C/H2/Cs\Cs2/O-HHFFClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 983,
    label = "C/H2/Cs\Cs2/O-HHFFBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 984,
    label = "C/H2/Cs\Cs2/O-HHFClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 985,
    label = "C/H2/Cs\Cs2/O-HHFClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 986,
    label = "C/H2/Cs\Cs2/O-HHFClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 987,
    label = "C/H2/Cs\Cs2/O-HHFClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 988,
    label = "C/H2/Cs\Cs2/O-HHFClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 989,
    label = "C/H2/Cs\Cs2/O-HHFClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 990,
    label = "C/H2/Cs\Cs2/O-HHFBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 991,
    label = "C/H2/Cs\Cs2/O-HHClClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 992,
    label = "C/H2/Cs\Cs2/O-HHClClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 993,
    label = "C/H2/Cs\Cs2/O-HHClClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 994,
    label = "C/H2/Cs\Cs2/O-HHClClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 995,
    label = "C/H2/Cs\Cs2/O-HHClClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 996,
    label = "C/H2/Cs\Cs2/O-HHClClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 997,
    label = "C/H2/Cs\Cs2/O-HHClBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 998,
    label = "C/H2/Cs\Cs2/O-HHBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     H  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 999,
    label = "C/H2/O2",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1000,
    label = "C/H2/NonDeS",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    H        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1001,
    label = "C/H2/CsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1002,
    label = "C/H2/NonDeN",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br          u0 {1,S}
3    H          u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1003,
    label = "C/H2/OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1004,
    label = "C/H2/OneDeC",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1005,
    label = "C/H2/CtCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1006,
    label = "C/H2/CbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1007,
    label = "C/H2/COCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1008,
    label = "C/H2/CO\H/Cs\H3",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     O  u0 {3,D}
10    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1009,
    label = "C/H2/CO\H/Cs\H3-HHHHF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     O  u0 {3,D}
10    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1010,
    label = "C/H2/CO\H/Cs\H3-HHHHCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1011,
    label = "C/H2/CO\H/Cs\H3-HHHHBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1012,
    label = "C/H2/CO\H/Cs\H3-HHHFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1013,
    label = "C/H2/CO\H/Cs\H3-HHHFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1014,
    label = "C/H2/CO\H/Cs\H3-HHHFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1015,
    label = "C/H2/CO\H/Cs\H3-HHHClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1016,
    label = "C/H2/CO\H/Cs\H3-HHHClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1017,
    label = "C/H2/CO\H/Cs\H3-HHHBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1018,
    label = "C/H2/CO\H/Cs\H3-HHFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1019,
    label = "C/H2/CO\H/Cs\H3-HHFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1020,
    label = "C/H2/CO\H/Cs\H3-HHFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1021,
    label = "C/H2/CO\H/Cs\H3-HHFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1022,
    label = "C/H2/CO\H/Cs\H3-HHFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1023,
    label = "C/H2/CO\H/Cs\H3-HHFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1024,
    label = "C/H2/CO\H/Cs\H3-HHClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1025,
    label = "C/H2/CO\H/Cs\H3-HHClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1026,
    label = "C/H2/CO\H/Cs\H3-HHClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1027,
    label = "C/H2/CO\H/Cs\H3-HHBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1028,
    label = "C/H2/CO\H/Cs\H3-HFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1029,
    label = "C/H2/CO\H/Cs\H3-HFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1030,
    label = "C/H2/CO\H/Cs\H3-HFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1031,
    label = "C/H2/CO\H/Cs\H3-HFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1032,
    label = "C/H2/CO\H/Cs\H3-HFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1033,
    label = "C/H2/CO\H/Cs\H3-HFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1034,
    label = "C/H2/CO\H/Cs\H3-HFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1035,
    label = "C/H2/CO\H/Cs\H3-HFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1036,
    label = "C/H2/CO\H/Cs\H3-HFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1037,
    label = "C/H2/CO\H/Cs\H3-HFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     F  u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1038,
    label = "C/H2/CO\H/Cs\H3-HClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1039,
    label = "C/H2/CO\H/Cs\H3-HClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1040,
    label = "C/H2/CO\H/Cs\H3-HClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1041,
    label = "C/H2/CO\H/Cs\H3-HClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Cl u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1042,
    label = "C/H2/CO\H/Cs\H3-HBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     H  u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1043,
    label = "C/H2/CdCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    Cd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1044,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {4,S}
12    H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1045,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHHF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1046,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHHCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1047,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHHBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1048,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1049,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1050,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1051,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1052,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1053,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHHBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1054,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1055,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1056,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1057,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1058,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1059,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1060,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1061,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1062,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1063,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHHBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1064,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1065,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1066,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1067,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1068,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1069,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1070,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1071,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1072,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1073,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1074,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1075,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1076,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1077,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1078,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHHBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1079,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1080,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1081,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1082,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1083,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1084,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1085,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1086,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1087,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1088,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1089,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1090,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1091,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1092,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1093,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHFBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1094,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1095,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1096,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1097,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1098,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1099,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HHBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1100,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1101,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1102,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1103,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1104,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1105,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1106,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1107,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1108,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1109,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1110,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1111,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1112,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1113,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1114,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFFBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1115,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1116,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1117,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1118,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1119,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1120,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HFBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1121,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HClClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1122,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HClClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1123,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HClClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1124,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HClClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1125,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HClClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1126,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HClBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1127,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-HBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     H  u0 {1,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1128,
    label = "C/H2/CSCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1129,
    label = "C/H2/OneDeO",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1130,
    label = "C/H2/OneDeS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1131,
    label = "C/H2/CbS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1132,
    label = "C/H2/CtS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1133,
    label = "C/H2/CdS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    S  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1134,
    label = "C/H2/CSS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    S  u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1135,
    label = "C/H2/TwoDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1136,
    label = "C/H2/CtCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1137,
    label = "C/H2/CtCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1138,
    label = "C/H2/CtCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1139,
    label = "C/H2/CbCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1140,
    label = "C/H2/CbCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1141,
    label = "C/H2/COCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1142,
    label = "C/H2/CdCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1143,
    label = "C/H2/CtCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1144,
    label = "C/H2/CdCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1145,
    label = "C/H2/CbCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1146,
    label = "C/H2/CdCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1147,
    label = "C/H2/COCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1148,
    label = "C/H2/CdCd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1149,
    label = "C/H2/CdCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1150,
    label = "C/H2/CSCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    H  u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1151,
    label = "C_sec-F",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1152,
    label = "C/H2/NonDeC-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1153,
    label = "C/H2/Cs/Cs\O-F",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S}
3 *2 Br     u0 {1,S}
4    F     u0 {1,S}
5    Cs    u0 {1,S}
6    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1154,
    label = "C/H2/Cs/Cs\Cs|O-F",
    group = 
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2    Cs    u0 {1,S} {3,S}
3    Cs    u0 {2,S} {7,S}
4 *2 Br     u0 {1,S}
5    F     u0 {1,S}
6    Cs    u0 {1,S}
7    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1155,
    label = "C/H2/NonDeC_5ring-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 Br  u0 {1,S}
7    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1156,
    label = "C/H2/NonDeC_5ring_fused6_1-F",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {8,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {4,S} {5,S} {7,S}
4    Cs u0 {1,S} {3,S}
5    Cs u0 {2,S} {3,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1157,
    label = "C/H2/NonDeC_5ring_fused6_2-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {8,S} {9,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1158,
    label = "C/H2/NonDeC_5ring_alpha6ring-F",
    group = 
"""
1  *1 C  u0 {2,S} {4,S} {10,S} {11,S}
2     Cs u0 {1,S} {3,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {5,S}
5     Cs u0 {3,S} {4,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1159,
    label = "C/H2/NonDeC_5ring_beta6ring-F",
    group = 
"""
1  *1 C  u0 {4,S} {5,S} {10,S} {11,S}
2     Cs u0 {3,S} {4,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {2,S}
5     Cs u0 {1,S} {3,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1160,
    label = "C/H2/Cs\H3/Cs\H3-FFFFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1161,
    label = "C/H2/Cs\H3/Cs\H3-FFFFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1162,
    label = "C/H2/Cs\H3/Cs\H3-FFFFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1163,
    label = "C/H2/Cs\H3/Cs\H3-FFFFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1164,
    label = "C/H2/Cs\H3/Cs\H3-FFFFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1165,
    label = "C/H2/Cs\H3/Cs\H3-FFFFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1166,
    label = "C/H2/Cs\H3/Cs\H3-FFFFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1167,
    label = "C/H2/Cs\H3/Cs\H3-FFFFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1168,
    label = "C/H2/Cs\H3/Cs\H3-FFFFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1169,
    label = "C/H2/Cs\H3/Cs\H3-FFFFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1170,
    label = "C/H2/Cs\H3/Cs\H3-FFFClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1171,
    label = "C/H2/Cs\H3/Cs\H3-FFFClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1172,
    label = "C/H2/Cs\H3/Cs\H3-FFFClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1173,
    label = "C/H2/Cs\H3/Cs\H3-FFFClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1174,
    label = "C/H2/Cs\H3/Cs\H3-FFFBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1175,
    label = "C/H2/Cs\H3/Cs\H3-FFClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1176,
    label = "C/H2/Cs\H3/Cs\H3-FFClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1177,
    label = "C/H2/Cs\H3/Cs\H3-FFClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1178,
    label = "C/H2/Cs\H3/Cs\H3-FFClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1179,
    label = "C/H2/Cs\H3/Cs\H3-FFClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1180,
    label = "C/H2/Cs\H3/Cs\H3-FFBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1181,
    label = "C/H2/Cs\H3/Cs\H3-FClClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1182,
    label = "C/H2/Cs\H3/Cs\H3-FClClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1183,
    label = "C/H2/Cs\H3/Cs\H3-FClClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1184,
    label = "C/H2/Cs\H3/Cs\H3-FClClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1185,
    label = "C/H2/Cs\H3/Cs\H3-FClClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1186,
    label = "C/H2/Cs\H3/Cs\H3-FClBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1187,
    label = "C/H2/Cs\H3/Cs\H3-FBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1188,
    label = "C/H2/NonDeO-F",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    F        u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1189,
    label = "C/H2/CsO-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1190,
    label = "C/H2/Cs\Cs2/O-HFFFFFFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1191,
    label = "C/H2/Cs\Cs2/O-HFFFFFFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1192,
    label = "C/H2/Cs\Cs2/O-HFFFFFFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1193,
    label = "C/H2/Cs\Cs2/O-HFFFFFFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1194,
    label = "C/H2/Cs\Cs2/O-HFFFFFFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1195,
    label = "C/H2/Cs\Cs2/O-HFFFFFFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1196,
    label = "C/H2/Cs\Cs2/O-HFFFFFClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1197,
    label = "C/H2/Cs\Cs2/O-HFFFFFClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1198,
    label = "C/H2/Cs\Cs2/O-HFFFFFClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1199,
    label = "C/H2/Cs\Cs2/O-HFFFFFBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1200,
    label = "C/H2/Cs\Cs2/O-HFFFFClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1201,
    label = "C/H2/Cs\Cs2/O-HFFFFClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1202,
    label = "C/H2/Cs\Cs2/O-HFFFFClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1203,
    label = "C/H2/Cs\Cs2/O-HFFFFClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1204,
    label = "C/H2/Cs\Cs2/O-HFFFFBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1205,
    label = "C/H2/Cs\Cs2/O-HFFFClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1206,
    label = "C/H2/Cs\Cs2/O-HFFFClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1207,
    label = "C/H2/Cs\Cs2/O-HFFFClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1208,
    label = "C/H2/Cs\Cs2/O-HFFFClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1209,
    label = "C/H2/Cs\Cs2/O-HFFFClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1210,
    label = "C/H2/Cs\Cs2/O-HFFFBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1211,
    label = "C/H2/Cs\Cs2/O-HFFClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1212,
    label = "C/H2/Cs\Cs2/O-HFFClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1213,
    label = "C/H2/Cs\Cs2/O-HFFClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1214,
    label = "C/H2/Cs\Cs2/O-HFFClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1215,
    label = "C/H2/Cs\Cs2/O-HFFClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1216,
    label = "C/H2/Cs\Cs2/O-HFFClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1217,
    label = "C/H2/Cs\Cs2/O-HFFBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1218,
    label = "C/H2/Cs\Cs2/O-HFClClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1219,
    label = "C/H2/Cs\Cs2/O-HFClClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1220,
    label = "C/H2/Cs\Cs2/O-HFClClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1221,
    label = "C/H2/Cs\Cs2/O-HFClClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1222,
    label = "C/H2/Cs\Cs2/O-HFClClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1223,
    label = "C/H2/Cs\Cs2/O-HFClClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1224,
    label = "C/H2/Cs\Cs2/O-HFClBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1225,
    label = "C/H2/Cs\Cs2/O-HFBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1226,
    label = "C/H2/Cs\Cs2/O-FFFFFFFFF",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    F  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1227,
    label = "C/H2/Cs\Cs2/O-FFFFFFFFCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1228,
    label = "C/H2/Cs\Cs2/O-FFFFFFFFBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1229,
    label = "C/H2/Cs\Cs2/O-FFFFFFFClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1230,
    label = "C/H2/Cs\Cs2/O-FFFFFFFClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1231,
    label = "C/H2/Cs\Cs2/O-FFFFFFFBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1232,
    label = "C/H2/Cs\Cs2/O-FFFFFFClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1233,
    label = "C/H2/Cs\Cs2/O-FFFFFFClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1234,
    label = "C/H2/Cs\Cs2/O-FFFFFFClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1235,
    label = "C/H2/Cs\Cs2/O-FFFFFFBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1236,
    label = "C/H2/Cs\Cs2/O-FFFFFClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1237,
    label = "C/H2/Cs\Cs2/O-FFFFFClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1238,
    label = "C/H2/Cs\Cs2/O-FFFFFClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1239,
    label = "C/H2/Cs\Cs2/O-FFFFFClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1240,
    label = "C/H2/Cs\Cs2/O-FFFFFBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1241,
    label = "C/H2/Cs\Cs2/O-FFFFClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1242,
    label = "C/H2/Cs\Cs2/O-FFFFClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1243,
    label = "C/H2/Cs\Cs2/O-FFFFClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1244,
    label = "C/H2/Cs\Cs2/O-FFFFClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1245,
    label = "C/H2/Cs\Cs2/O-FFFFClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1246,
    label = "C/H2/Cs\Cs2/O-FFFFBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1247,
    label = "C/H2/Cs\Cs2/O-FFFClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1248,
    label = "C/H2/Cs\Cs2/O-FFFClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1249,
    label = "C/H2/Cs\Cs2/O-FFFClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1250,
    label = "C/H2/Cs\Cs2/O-FFFClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1251,
    label = "C/H2/Cs\Cs2/O-FFFClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1252,
    label = "C/H2/Cs\Cs2/O-FFFClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1253,
    label = "C/H2/Cs\Cs2/O-FFFBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1254,
    label = "C/H2/Cs\Cs2/O-FFClClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1255,
    label = "C/H2/Cs\Cs2/O-FFClClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1256,
    label = "C/H2/Cs\Cs2/O-FFClClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1257,
    label = "C/H2/Cs\Cs2/O-FFClClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1258,
    label = "C/H2/Cs\Cs2/O-FFClClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1259,
    label = "C/H2/Cs\Cs2/O-FFClClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1260,
    label = "C/H2/Cs\Cs2/O-FFClBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1261,
    label = "C/H2/Cs\Cs2/O-FFBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1262,
    label = "C/H2/O2-F",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    F u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1263,
    label = "C/H2/NonDeS-F",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    F        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1264,
    label = "C/H2/CsS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1265,
    label = "C/H2/NonDeN-F",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br          u0 {1,S}
3    F          u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1266,
    label = "C/H2/OneDe-F",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1267,
    label = "C/H2/OneDeC-F",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1268,
    label = "C/H2/CtCs-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1269,
    label = "C/H2/CbCs-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1270,
    label = "C/H2/COCs-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1271,
    label = "C/H2/CO\H/Cs\H3-FFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1272,
    label = "C/H2/CO\H/Cs\H3-FFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1273,
    label = "C/H2/CO\H/Cs\H3-FFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1274,
    label = "C/H2/CO\H/Cs\H3-FFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1275,
    label = "C/H2/CO\H/Cs\H3-FFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1276,
    label = "C/H2/CO\H/Cs\H3-FFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1277,
    label = "C/H2/CO\H/Cs\H3-FFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1278,
    label = "C/H2/CO\H/Cs\H3-FFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1279,
    label = "C/H2/CO\H/Cs\H3-FFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1280,
    label = "C/H2/CO\H/Cs\H3-FFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     F  u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1281,
    label = "C/H2/CO\H/Cs\H3-FClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1282,
    label = "C/H2/CO\H/Cs\H3-FClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1283,
    label = "C/H2/CO\H/Cs\H3-FClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1284,
    label = "C/H2/CO\H/Cs\H3-FClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Cl u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1285,
    label = "C/H2/CO\H/Cs\H3-FBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     F  u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1286,
    label = "C/H2/CdCs-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cs u0 {1,S}
6    Cd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1287,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFFFF",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1288,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFFFCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1289,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFFFBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1290,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFFClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1291,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFFClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1292,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFFBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1293,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1294,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1295,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1296,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFFBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1297,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1298,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1299,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1300,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1301,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFFBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1302,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1303,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1304,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1305,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1306,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1307,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FFBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1308,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FClClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1309,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FClClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1310,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FClClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1311,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FClClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1312,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FClClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1313,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FClBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1314,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-FBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     F  u0 {1,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1315,
    label = "C/H2/CSCs-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1316,
    label = "C/H2/OneDeO-F",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1317,
    label = "C/H2/OneDeS-F",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1318,
    label = "C/H2/CbS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1319,
    label = "C/H2/CtS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1320,
    label = "C/H2/CdS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    S  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1321,
    label = "C/H2/CSS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    S  u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1322,
    label = "C/H2/TwoDe-F",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    F                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1323,
    label = "C/H2/CtCt-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1324,
    label = "C/H2/CtCb-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1325,
    label = "C/H2/CtCO-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1326,
    label = "C/H2/CbCb-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1327,
    label = "C/H2/CbCO-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    Cb u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1328,
    label = "C/H2/COCO-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    F  u0 {1,S}
4    CO u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1329,
    label = "C/H2/CdCt-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Ct u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1330,
    label = "C/H2/CtCS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Ct u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1331,
    label = "C/H2/CdCb-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cb u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1332,
    label = "C/H2/CbCS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    Cb u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1333,
    label = "C/H2/CdCO-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    CO u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1334,
    label = "C/H2/COCS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    F  u0 {1,S}
5    CO u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1335,
    label = "C/H2/CdCd-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1336,
    label = "C/H2/CdCS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1337,
    label = "C/H2/CSCS-F",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    F  u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1338,
    label = "C_sec-Cl",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1339,
    label = "C/H2/NonDeC-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1340,
    label = "C/H2/Cs/Cs\O-Cl",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S}
3 *2 Br     u0 {1,S}
4    Cl    u0 {1,S}
5    Cs    u0 {1,S}
6    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1341,
    label = "C/H2/Cs/Cs\Cs|O-Cl",
    group = 
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2    Cs    u0 {1,S} {3,S}
3    Cs    u0 {2,S} {7,S}
4 *2 Br     u0 {1,S}
5    Cl    u0 {1,S}
6    Cs    u0 {1,S}
7    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1342,
    label = "C/H2/NonDeC_5ring-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 Br  u0 {1,S}
7    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1343,
    label = "C/H2/NonDeC_5ring_fused6_1-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {8,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {4,S} {5,S} {7,S}
4    Cs u0 {1,S} {3,S}
5    Cs u0 {2,S} {3,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1344,
    label = "C/H2/NonDeC_5ring_fused6_2-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {8,S} {9,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1345,
    label = "C/H2/NonDeC_5ring_alpha6ring-Cl",
    group = 
"""
1  *1 C  u0 {2,S} {4,S} {10,S} {11,S}
2     Cs u0 {1,S} {3,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {5,S}
5     Cs u0 {3,S} {4,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1346,
    label = "C/H2/NonDeC_5ring_beta6ring-Cl",
    group = 
"""
1  *1 C  u0 {4,S} {5,S} {10,S} {11,S}
2     Cs u0 {3,S} {4,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {2,S}
5     Cs u0 {1,S} {3,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1347,
    label = "C/H2/Cs\H3/Cs\H3-ClClClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1348,
    label = "C/H2/Cs\H3/Cs\H3-ClClClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1349,
    label = "C/H2/Cs\H3/Cs\H3-ClClClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1350,
    label = "C/H2/Cs\H3/Cs\H3-ClClClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1351,
    label = "C/H2/Cs\H3/Cs\H3-ClClClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1352,
    label = "C/H2/Cs\H3/Cs\H3-ClClBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1353,
    label = "C/H2/Cs\H3/Cs\H3-ClBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1354,
    label = "C/H2/NonDeO-Cl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    Cl       u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1355,
    label = "C/H2/CsO-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1356,
    label = "C/H2/Cs\Cs2/O-HClClClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1357,
    label = "C/H2/Cs\Cs2/O-HClClClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1358,
    label = "C/H2/Cs\Cs2/O-HClClClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1359,
    label = "C/H2/Cs\Cs2/O-HClClClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1360,
    label = "C/H2/Cs\Cs2/O-HClClClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1361,
    label = "C/H2/Cs\Cs2/O-HClClClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1362,
    label = "C/H2/Cs\Cs2/O-HClClBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1363,
    label = "C/H2/Cs\Cs2/O-HClBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1364,
    label = "C/H2/Cs\Cs2/O-FClClClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1365,
    label = "C/H2/Cs\Cs2/O-FClClClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1366,
    label = "C/H2/Cs\Cs2/O-FClClClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1367,
    label = "C/H2/Cs\Cs2/O-FClClClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1368,
    label = "C/H2/Cs\Cs2/O-FClClClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1369,
    label = "C/H2/Cs\Cs2/O-FClClClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1370,
    label = "C/H2/Cs\Cs2/O-FClClBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1371,
    label = "C/H2/Cs\Cs2/O-FClBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1372,
    label = "C/H2/Cs\Cs2/O-ClClClClClClClClCl",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Cl u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1373,
    label = "C/H2/Cs\Cs2/O-ClClClClClClClClBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1374,
    label = "C/H2/Cs\Cs2/O-ClClClClClClClBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1375,
    label = "C/H2/Cs\Cs2/O-ClClClClClClBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1376,
    label = "C/H2/Cs\Cs2/O-ClClClClClBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1377,
    label = "C/H2/Cs\Cs2/O-ClClClClBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1378,
    label = "C/H2/Cs\Cs2/O-ClClClBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1379,
    label = "C/H2/Cs\Cs2/O-ClClBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1380,
    label = "C/H2/O2-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    O  u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1381,
    label = "C/H2/NonDeS-Cl",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    Cl       u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1382,
    label = "C/H2/CsS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1383,
    label = "C/H2/NonDeN-Cl",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br          u0 {1,S}
3    Cl         u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1384,
    label = "C/H2/OneDe-Cl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1385,
    label = "C/H2/OneDeC-Cl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1386,
    label = "C/H2/CtCs-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1387,
    label = "C/H2/CbCs-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1388,
    label = "C/H2/COCs-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1389,
    label = "C/H2/CO\H/Cs\H3-ClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1390,
    label = "C/H2/CO\H/Cs\H3-ClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1391,
    label = "C/H2/CO\H/Cs\H3-ClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1392,
    label = "C/H2/CO\H/Cs\H3-ClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Cl u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1393,
    label = "C/H2/CO\H/Cs\H3-ClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     Cl u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1394,
    label = "C/H2/CdCs-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {1,S}
6    Cd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1395,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClClClClClClCl",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1396,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClClClClClClBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1397,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClClClClClBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1398,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClClClClBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1399,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClClClBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1400,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClClBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1401,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-ClBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Cl u0 {1,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1402,
    label = "C/H2/CSCs-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1403,
    label = "C/H2/OneDeO-Cl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1404,
    label = "C/H2/OneDeS-Cl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1405,
    label = "C/H2/CbS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1406,
    label = "C/H2/CtS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1407,
    label = "C/H2/CdS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    S  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1408,
    label = "C/H2/CSS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    S  u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1409,
    label = "C/H2/TwoDe-Cl",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Cl               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1410,
    label = "C/H2/CtCt-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1411,
    label = "C/H2/CtCb-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1412,
    label = "C/H2/CtCO-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1413,
    label = "C/H2/CbCb-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1414,
    label = "C/H2/CbCO-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1415,
    label = "C/H2/COCO-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cl u0 {1,S}
4    CO u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1416,
    label = "C/H2/CdCt-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Ct u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1417,
    label = "C/H2/CtCS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Ct u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1418,
    label = "C/H2/CdCb-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cb u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1419,
    label = "C/H2/CbCS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    Cb u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1420,
    label = "C/H2/CdCO-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    CO u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1421,
    label = "C/H2/COCS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cl u0 {1,S}
5    CO u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1422,
    label = "C/H2/CdCd-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1423,
    label = "C/H2/CdCS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1424,
    label = "C/H2/CSCS-Cl",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Cl u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1425,
    label = "C_sec-Br",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1426,
    label = "C/H2/NonDeC-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1427,
    label = "C/H2/Cs/Cs\O-Br",
    group = 
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S}
3 *2 Br     u0 {1,S}
4    Br    u0 {1,S}
5    Cs    u0 {1,S}
6    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1428,
    label = "C/H2/Cs/Cs\Cs|O-Br",
    group = 
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2    Cs    u0 {1,S} {3,S}
3    Cs    u0 {2,S} {7,S}
4 *2 Br     u0 {1,S}
5    Br    u0 {1,S}
6    Cs    u0 {1,S}
7    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1429,
    label = "C/H2/NonDeC_5ring-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 Br  u0 {1,S}
7    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1430,
    label = "C/H2/NonDeC_5ring_fused6_1-Br",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {8,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {4,S} {5,S} {7,S}
4    Cs u0 {1,S} {3,S}
5    Cs u0 {2,S} {3,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1431,
    label = "C/H2/NonDeC_5ring_fused6_2-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {8,S} {9,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 Br  u0 {1,S}
9    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1432,
    label = "C/H2/NonDeC_5ring_alpha6ring-Br",
    group = 
"""
1  *1 C  u0 {2,S} {4,S} {10,S} {11,S}
2     Cs u0 {1,S} {3,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {5,S}
5     Cs u0 {3,S} {4,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1433,
    label = "C/H2/NonDeC_5ring_beta6ring-Br",
    group = 
"""
1  *1 C  u0 {4,S} {5,S} {10,S} {11,S}
2     Cs u0 {3,S} {4,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {2,S}
5     Cs u0 {1,S} {3,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 Br  u0 {1,S}
11    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1434,
    label = "C/H2/Cs\H3/Cs\H3-BrBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Br  u0 {1,S}
5     Br u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1435,
    label = "C/H2/NonDeO-Br",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    Br       u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1436,
    label = "C/H2/CsO-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1437,
    label = "C/H2/Cs\Cs2/O-HBrBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1438,
    label = "C/H2/Cs\Cs2/O-FBrBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     F  u0 {1,S}
7  *2 Br  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1439,
    label = "C/H2/Cs\Cs2/O-ClBrBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Cl u0 {1,S}
7  *2 Br  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1440,
    label = "C/H2/Cs\Cs2/O-BrBrBrBrBrBrBrBrBr",
    group = 
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     Br u0 {1,S}
7  *2 Br  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {3,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
15    Br u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1441,
    label = "C/H2/O2-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    O  u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1442,
    label = "C/H2/NonDeS-Br",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    Br       u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1443,
    label = "C/H2/CsS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1444,
    label = "C/H2/NonDeN-Br",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br          u0 {1,S}
3    Br         u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1445,
    label = "C/H2/OneDe-Br",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Br               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1446,
    label = "C/H2/OneDeC-Br",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Br               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1447,
    label = "C/H2/CtCs-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1448,
    label = "C/H2/CbCs-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1449,
    label = "C/H2/COCs-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1450,
    label = "C/H2/CO\H/Cs\H3-BrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 Br  u0 {1,S}
5     Br u0 {1,S}
6     Br u0 {2,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     O  u0 {3,D}
10    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1451,
    label = "C/H2/CdCs-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {1,S}
6    Cd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1452,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-BrBrBrBrBrBrBr",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 Br  u0 {1,S}
6     Br u0 {1,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {4,S}
12    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1453,
    label = "C/H2/CSCs-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1454,
    label = "C/H2/OneDeO-Br",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Br               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1455,
    label = "C/H2/OneDeS-Br",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Br               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1456,
    label = "C/H2/CbS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1457,
    label = "C/H2/CtS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1458,
    label = "C/H2/CdS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    S  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1459,
    label = "C/H2/CSS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    S  u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1460,
    label = "C/H2/TwoDe-Br",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    Br               u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1461,
    label = "C/H2/CtCt-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1462,
    label = "C/H2/CtCb-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1463,
    label = "C/H2/CtCO-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1464,
    label = "C/H2/CbCb-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1465,
    label = "C/H2/CbCO-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    Cb u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1466,
    label = "C/H2/COCO-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Br u0 {1,S}
4    CO u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1467,
    label = "C/H2/CdCt-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Ct u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1468,
    label = "C/H2/CtCS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Ct u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1469,
    label = "C/H2/CdCb-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Cb u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1470,
    label = "C/H2/CbCS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    Cb u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1471,
    label = "C/H2/CdCO-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    CO u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1472,
    label = "C/H2/COCS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Br u0 {1,S}
5    CO u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1473,
    label = "C/H2/CdCd-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Br u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1474,
    label = "C/H2/CdCS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Br u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1475,
    label = "C/H2/CSCS-Br",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Br u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1476,
    label = "C_ter",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1477,
    label = "C/H/NonDe",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br          u0 {1,S}
3    [Cs,O,S,N] u0 {1,S}
4    [Cs,O,S,N] u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1478,
    label = "C/H/Cs3",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1479,
    label = "C/H_or_Val7/Cs2/Cs\O",
    group = 
"""
1  *1 C        u0 {2,S} {3,S} {4,S} {6,S}
2     Cs       u0 {1,S} {5,S} {7,S} {8,S}
3     Cs       u0 {1,S} {9,S} {10,S} {11,S}
4     Cs       u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S]    u0 {2,S} {15,S}
6  *2 Br        u0 {1,S}
7     [H,Val7] u0 {2,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {3,S}
10    [H,Val7] u0 {3,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {4,S}
13    [H,Val7] u0 {4,S}
14    [H,Val7] u0 {4,S}
15    [H,Val7] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1480,
    label = "C/H/Cs2/Cs\O",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1481,
    label = "C/H/Cs2/Cs\O-HHHHHHHHF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1482,
    label = "C/H/Cs2/Cs\O-HHHHHHHHCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1483,
    label = "C/H/Cs2/Cs\O-HHHHHHHHBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1484,
    label = "C/H/Cs2/Cs\O-HHHHHHHFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1485,
    label = "C/H/Cs2/Cs\O-HHHHHHHFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1486,
    label = "C/H/Cs2/Cs\O-HHHHHHHFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1487,
    label = "C/H/Cs2/Cs\O-HHHHHHHClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1488,
    label = "C/H/Cs2/Cs\O-HHHHHHHClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1489,
    label = "C/H/Cs2/Cs\O-HHHHHHHBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1490,
    label = "C/H/Cs2/Cs\O-HHHHHHFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1491,
    label = "C/H/Cs2/Cs\O-HHHHHHFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1492,
    label = "C/H/Cs2/Cs\O-HHHHHHFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1493,
    label = "C/H/Cs2/Cs\O-HHHHHHFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1494,
    label = "C/H/Cs2/Cs\O-HHHHHHFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1495,
    label = "C/H/Cs2/Cs\O-HHHHHHFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1496,
    label = "C/H/Cs2/Cs\O-HHHHHHClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1497,
    label = "C/H/Cs2/Cs\O-HHHHHHClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1498,
    label = "C/H/Cs2/Cs\O-HHHHHHClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1499,
    label = "C/H/Cs2/Cs\O-HHHHHHBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1500,
    label = "C/H/Cs2/Cs\O-HHHHHFFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1501,
    label = "C/H/Cs2/Cs\O-HHHHHFFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1502,
    label = "C/H/Cs2/Cs\O-HHHHHFFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1503,
    label = "C/H/Cs2/Cs\O-HHHHHFFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1504,
    label = "C/H/Cs2/Cs\O-HHHHHFFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1505,
    label = "C/H/Cs2/Cs\O-HHHHHFFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1506,
    label = "C/H/Cs2/Cs\O-HHHHHFClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1507,
    label = "C/H/Cs2/Cs\O-HHHHHFClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1508,
    label = "C/H/Cs2/Cs\O-HHHHHFClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1509,
    label = "C/H/Cs2/Cs\O-HHHHHFBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1510,
    label = "C/H/Cs2/Cs\O-HHHHHClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1511,
    label = "C/H/Cs2/Cs\O-HHHHHClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1512,
    label = "C/H/Cs2/Cs\O-HHHHHClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1513,
    label = "C/H/Cs2/Cs\O-HHHHHClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1514,
    label = "C/H/Cs2/Cs\O-HHHHHBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1515,
    label = "C/H/Cs2/Cs\O-HHHHFFFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1516,
    label = "C/H/Cs2/Cs\O-HHHHFFFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1517,
    label = "C/H/Cs2/Cs\O-HHHHFFFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1518,
    label = "C/H/Cs2/Cs\O-HHHHFFFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1519,
    label = "C/H/Cs2/Cs\O-HHHHFFFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1520,
    label = "C/H/Cs2/Cs\O-HHHHFFFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1521,
    label = "C/H/Cs2/Cs\O-HHHHFFClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1522,
    label = "C/H/Cs2/Cs\O-HHHHFFClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1523,
    label = "C/H/Cs2/Cs\O-HHHHFFClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1524,
    label = "C/H/Cs2/Cs\O-HHHHFFBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1525,
    label = "C/H/Cs2/Cs\O-HHHHFClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1526,
    label = "C/H/Cs2/Cs\O-HHHHFClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1527,
    label = "C/H/Cs2/Cs\O-HHHHFClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1528,
    label = "C/H/Cs2/Cs\O-HHHHFClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1529,
    label = "C/H/Cs2/Cs\O-HHHHFBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1530,
    label = "C/H/Cs2/Cs\O-HHHHClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1531,
    label = "C/H/Cs2/Cs\O-HHHHClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1532,
    label = "C/H/Cs2/Cs\O-HHHHClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1533,
    label = "C/H/Cs2/Cs\O-HHHHClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1534,
    label = "C/H/Cs2/Cs\O-HHHHClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1535,
    label = "C/H/Cs2/Cs\O-HHHHBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1536,
    label = "C/H/Cs2/Cs\O-HHHFFFFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1537,
    label = "C/H/Cs2/Cs\O-HHHFFFFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1538,
    label = "C/H/Cs2/Cs\O-HHHFFFFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1539,
    label = "C/H/Cs2/Cs\O-HHHFFFFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1540,
    label = "C/H/Cs2/Cs\O-HHHFFFFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1541,
    label = "C/H/Cs2/Cs\O-HHHFFFFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1542,
    label = "C/H/Cs2/Cs\O-HHHFFFClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1543,
    label = "C/H/Cs2/Cs\O-HHHFFFClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1544,
    label = "C/H/Cs2/Cs\O-HHHFFFClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1545,
    label = "C/H/Cs2/Cs\O-HHHFFFBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1546,
    label = "C/H/Cs2/Cs\O-HHHFFClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1547,
    label = "C/H/Cs2/Cs\O-HHHFFClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1548,
    label = "C/H/Cs2/Cs\O-HHHFFClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1549,
    label = "C/H/Cs2/Cs\O-HHHFFClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1550,
    label = "C/H/Cs2/Cs\O-HHHFFBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1551,
    label = "C/H/Cs2/Cs\O-HHHFClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1552,
    label = "C/H/Cs2/Cs\O-HHHFClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1553,
    label = "C/H/Cs2/Cs\O-HHHFClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1554,
    label = "C/H/Cs2/Cs\O-HHHFClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1555,
    label = "C/H/Cs2/Cs\O-HHHFClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1556,
    label = "C/H/Cs2/Cs\O-HHHFBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1557,
    label = "C/H/Cs2/Cs\O-HHHClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1558,
    label = "C/H/Cs2/Cs\O-HHHClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1559,
    label = "C/H/Cs2/Cs\O-HHHClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1560,
    label = "C/H/Cs2/Cs\O-HHHClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1561,
    label = "C/H/Cs2/Cs\O-HHHClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1562,
    label = "C/H/Cs2/Cs\O-HHHClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1563,
    label = "C/H/Cs2/Cs\O-HHHBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1564,
    label = "C/H/Cs2/Cs\O-HHFFFFFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1565,
    label = "C/H/Cs2/Cs\O-HHFFFFFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1566,
    label = "C/H/Cs2/Cs\O-HHFFFFFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1567,
    label = "C/H/Cs2/Cs\O-HHFFFFFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1568,
    label = "C/H/Cs2/Cs\O-HHFFFFFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1569,
    label = "C/H/Cs2/Cs\O-HHFFFFFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1570,
    label = "C/H/Cs2/Cs\O-HHFFFFClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1571,
    label = "C/H/Cs2/Cs\O-HHFFFFClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1572,
    label = "C/H/Cs2/Cs\O-HHFFFFClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1573,
    label = "C/H/Cs2/Cs\O-HHFFFFBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1574,
    label = "C/H/Cs2/Cs\O-HHFFFClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1575,
    label = "C/H/Cs2/Cs\O-HHFFFClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1576,
    label = "C/H/Cs2/Cs\O-HHFFFClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1577,
    label = "C/H/Cs2/Cs\O-HHFFFClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1578,
    label = "C/H/Cs2/Cs\O-HHFFFBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1579,
    label = "C/H/Cs2/Cs\O-HHFFClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1580,
    label = "C/H/Cs2/Cs\O-HHFFClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1581,
    label = "C/H/Cs2/Cs\O-HHFFClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1582,
    label = "C/H/Cs2/Cs\O-HHFFClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1583,
    label = "C/H/Cs2/Cs\O-HHFFClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1584,
    label = "C/H/Cs2/Cs\O-HHFFBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1585,
    label = "C/H/Cs2/Cs\O-HHFClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1586,
    label = "C/H/Cs2/Cs\O-HHFClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1587,
    label = "C/H/Cs2/Cs\O-HHFClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1588,
    label = "C/H/Cs2/Cs\O-HHFClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1589,
    label = "C/H/Cs2/Cs\O-HHFClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1590,
    label = "C/H/Cs2/Cs\O-HHFClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1591,
    label = "C/H/Cs2/Cs\O-HHFBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1592,
    label = "C/H/Cs2/Cs\O-HHClClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1593,
    label = "C/H/Cs2/Cs\O-HHClClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1594,
    label = "C/H/Cs2/Cs\O-HHClClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1595,
    label = "C/H/Cs2/Cs\O-HHClClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1596,
    label = "C/H/Cs2/Cs\O-HHClClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1597,
    label = "C/H/Cs2/Cs\O-HHClClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1598,
    label = "C/H/Cs2/Cs\O-HHClBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1599,
    label = "C/H/Cs2/Cs\O-HHBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1600,
    label = "C/H/Cs2/Cs\O-HFFFFFFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1601,
    label = "C/H/Cs2/Cs\O-HFFFFFFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1602,
    label = "C/H/Cs2/Cs\O-HFFFFFFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1603,
    label = "C/H/Cs2/Cs\O-HFFFFFFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1604,
    label = "C/H/Cs2/Cs\O-HFFFFFFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1605,
    label = "C/H/Cs2/Cs\O-HFFFFFFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1606,
    label = "C/H/Cs2/Cs\O-HFFFFFClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1607,
    label = "C/H/Cs2/Cs\O-HFFFFFClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1608,
    label = "C/H/Cs2/Cs\O-HFFFFFClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1609,
    label = "C/H/Cs2/Cs\O-HFFFFFBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1610,
    label = "C/H/Cs2/Cs\O-HFFFFClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1611,
    label = "C/H/Cs2/Cs\O-HFFFFClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1612,
    label = "C/H/Cs2/Cs\O-HFFFFClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1613,
    label = "C/H/Cs2/Cs\O-HFFFFClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1614,
    label = "C/H/Cs2/Cs\O-HFFFFBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1615,
    label = "C/H/Cs2/Cs\O-HFFFClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1616,
    label = "C/H/Cs2/Cs\O-HFFFClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1617,
    label = "C/H/Cs2/Cs\O-HFFFClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1618,
    label = "C/H/Cs2/Cs\O-HFFFClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1619,
    label = "C/H/Cs2/Cs\O-HFFFClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1620,
    label = "C/H/Cs2/Cs\O-HFFFBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1621,
    label = "C/H/Cs2/Cs\O-HFFClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1622,
    label = "C/H/Cs2/Cs\O-HFFClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1623,
    label = "C/H/Cs2/Cs\O-HFFClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1624,
    label = "C/H/Cs2/Cs\O-HFFClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1625,
    label = "C/H/Cs2/Cs\O-HFFClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1626,
    label = "C/H/Cs2/Cs\O-HFFClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1627,
    label = "C/H/Cs2/Cs\O-HFFBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1628,
    label = "C/H/Cs2/Cs\O-HFClClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1629,
    label = "C/H/Cs2/Cs\O-HFClClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1630,
    label = "C/H/Cs2/Cs\O-HFClClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1631,
    label = "C/H/Cs2/Cs\O-HFClClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1632,
    label = "C/H/Cs2/Cs\O-HFClClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1633,
    label = "C/H/Cs2/Cs\O-HFClClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1634,
    label = "C/H/Cs2/Cs\O-HFClBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1635,
    label = "C/H/Cs2/Cs\O-HFBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1636,
    label = "C/H/Cs2/Cs\O-HClClClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1637,
    label = "C/H/Cs2/Cs\O-HClClClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1638,
    label = "C/H/Cs2/Cs\O-HClClClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1639,
    label = "C/H/Cs2/Cs\O-HClClClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1640,
    label = "C/H/Cs2/Cs\O-HClClClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1641,
    label = "C/H/Cs2/Cs\O-HClClClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1642,
    label = "C/H/Cs2/Cs\O-HClClBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1643,
    label = "C/H/Cs2/Cs\O-HClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1644,
    label = "C/H/Cs2/Cs\O-HBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1645,
    label = "C/H/Cs2/Cs\O-FFFFFFFFF",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1646,
    label = "C/H/Cs2/Cs\O-FFFFFFFFCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1647,
    label = "C/H/Cs2/Cs\O-FFFFFFFFBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1648,
    label = "C/H/Cs2/Cs\O-FFFFFFFClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1649,
    label = "C/H/Cs2/Cs\O-FFFFFFFClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1650,
    label = "C/H/Cs2/Cs\O-FFFFFFFBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1651,
    label = "C/H/Cs2/Cs\O-FFFFFFClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1652,
    label = "C/H/Cs2/Cs\O-FFFFFFClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1653,
    label = "C/H/Cs2/Cs\O-FFFFFFClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1654,
    label = "C/H/Cs2/Cs\O-FFFFFFBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1655,
    label = "C/H/Cs2/Cs\O-FFFFFClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1656,
    label = "C/H/Cs2/Cs\O-FFFFFClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1657,
    label = "C/H/Cs2/Cs\O-FFFFFClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1658,
    label = "C/H/Cs2/Cs\O-FFFFFClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1659,
    label = "C/H/Cs2/Cs\O-FFFFFBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1660,
    label = "C/H/Cs2/Cs\O-FFFFClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1661,
    label = "C/H/Cs2/Cs\O-FFFFClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1662,
    label = "C/H/Cs2/Cs\O-FFFFClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1663,
    label = "C/H/Cs2/Cs\O-FFFFClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1664,
    label = "C/H/Cs2/Cs\O-FFFFClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1665,
    label = "C/H/Cs2/Cs\O-FFFFBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1666,
    label = "C/H/Cs2/Cs\O-FFFClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1667,
    label = "C/H/Cs2/Cs\O-FFFClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1668,
    label = "C/H/Cs2/Cs\O-FFFClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1669,
    label = "C/H/Cs2/Cs\O-FFFClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1670,
    label = "C/H/Cs2/Cs\O-FFFClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1671,
    label = "C/H/Cs2/Cs\O-FFFClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1672,
    label = "C/H/Cs2/Cs\O-FFFBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1673,
    label = "C/H/Cs2/Cs\O-FFClClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1674,
    label = "C/H/Cs2/Cs\O-FFClClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1675,
    label = "C/H/Cs2/Cs\O-FFClClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1676,
    label = "C/H/Cs2/Cs\O-FFClClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1677,
    label = "C/H/Cs2/Cs\O-FFClClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1678,
    label = "C/H/Cs2/Cs\O-FFClClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1679,
    label = "C/H/Cs2/Cs\O-FFClBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1680,
    label = "C/H/Cs2/Cs\O-FFBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1681,
    label = "C/H/Cs2/Cs\O-FClClClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1682,
    label = "C/H/Cs2/Cs\O-FClClClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1683,
    label = "C/H/Cs2/Cs\O-FClClClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1684,
    label = "C/H/Cs2/Cs\O-FClClClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1685,
    label = "C/H/Cs2/Cs\O-FClClClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1686,
    label = "C/H/Cs2/Cs\O-FClClClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1687,
    label = "C/H/Cs2/Cs\O-FClClBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1688,
    label = "C/H/Cs2/Cs\O-FClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1689,
    label = "C/H/Cs2/Cs\O-FBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1690,
    label = "C/H/Cs2/Cs\O-ClClClClClClClClCl",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1691,
    label = "C/H/Cs2/Cs\O-ClClClClClClClClBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1692,
    label = "C/H/Cs2/Cs\O-ClClClClClClClBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1693,
    label = "C/H/Cs2/Cs\O-ClClClClClClBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1694,
    label = "C/H/Cs2/Cs\O-ClClClClClBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1695,
    label = "C/H/Cs2/Cs\O-ClClClClBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1696,
    label = "C/H/Cs2/Cs\O-ClClClBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1697,
    label = "C/H/Cs2/Cs\O-ClClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1698,
    label = "C/H/Cs2/Cs\O-ClBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1699,
    label = "C/H/Cs2/Cs\O-BrBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 Br     u0 {1,S}
7     Br    u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {4,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1700,
    label = "C/H_or_Val7/Cs2/Cs\Cs|O",
    group = 
"""
1  *1 Cs       u0 {2,S} {3,S} {4,S} {6,S}
2     Cs       u0 {1,S} {5,S} {7,S} {8,S}
3     Cs       u0 {1,S} {9,S} {10,S} {11,S}
4     Cs       u0 {1,S} {13,S} {14,S} {15,S}
5     Cs       u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br        u0 {1,S}
7     [H,Val7] u0 {2,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {3,S}
10    [H,Val7] u0 {3,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {5,S}
13    [H,Val7] u0 {4,S}
14    [H,Val7] u0 {4,S}
15    [H,Val7] u0 {4,S}
16    [H,Val7] u0 {5,S}
17    [O,S]    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1701,
    label = "C/H/Cs2/Cs\Cs|O",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {4,S}
16    H     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1702,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHHF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1703,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHHCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1704,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHHBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1705,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1706,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1707,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1708,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1709,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1710,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHHBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1711,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1712,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1713,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1714,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1715,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1716,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1717,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1718,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1719,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1720,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHHBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1721,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1722,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1723,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1724,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1725,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1726,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1727,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1728,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1729,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1730,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1731,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1732,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1733,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1734,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1735,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHHBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1736,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1737,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1738,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1739,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1740,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1741,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1742,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1743,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1744,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1745,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1746,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1747,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1748,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1749,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1750,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHFBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    F     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1751,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1752,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1753,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1754,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1755,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1756,
    label = "C/H/Cs2/Cs\Cs|O-HHHHHBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1757,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1758,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1759,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1760,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1761,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1762,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1763,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1764,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1765,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1766,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1767,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1768,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1769,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1770,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1771,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFFBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1772,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1773,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1774,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1775,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1776,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1777,
    label = "C/H/Cs2/Cs\Cs|O-HHHHFBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1778,
    label = "C/H/Cs2/Cs\Cs|O-HHHHClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1779,
    label = "C/H/Cs2/Cs\Cs|O-HHHHClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1780,
    label = "C/H/Cs2/Cs\Cs|O-HHHHClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1781,
    label = "C/H/Cs2/Cs\Cs|O-HHHHClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1782,
    label = "C/H/Cs2/Cs\Cs|O-HHHHClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1783,
    label = "C/H/Cs2/Cs\Cs|O-HHHHClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1784,
    label = "C/H/Cs2/Cs\Cs|O-HHHHBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1785,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1786,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1787,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1788,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1789,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1790,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1791,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1792,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1793,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1794,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1795,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1796,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1797,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1798,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1799,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFFBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1800,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1801,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1802,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1803,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1804,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1805,
    label = "C/H/Cs2/Cs\Cs|O-HHHFFBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1806,
    label = "C/H/Cs2/Cs\Cs|O-HHHFClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1807,
    label = "C/H/Cs2/Cs\Cs|O-HHHFClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1808,
    label = "C/H/Cs2/Cs\Cs|O-HHHFClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1809,
    label = "C/H/Cs2/Cs\Cs|O-HHHFClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1810,
    label = "C/H/Cs2/Cs\Cs|O-HHHFClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1811,
    label = "C/H/Cs2/Cs\Cs|O-HHHFClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1812,
    label = "C/H/Cs2/Cs\Cs|O-HHHFBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1813,
    label = "C/H/Cs2/Cs\Cs|O-HHHClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1814,
    label = "C/H/Cs2/Cs\Cs|O-HHHClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1815,
    label = "C/H/Cs2/Cs\Cs|O-HHHClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1816,
    label = "C/H/Cs2/Cs\Cs|O-HHHClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1817,
    label = "C/H/Cs2/Cs\Cs|O-HHHClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1818,
    label = "C/H/Cs2/Cs\Cs|O-HHHClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1819,
    label = "C/H/Cs2/Cs\Cs|O-HHHClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1820,
    label = "C/H/Cs2/Cs\Cs|O-HHHBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1821,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1822,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1823,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1824,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1825,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1826,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1827,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1828,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1829,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1830,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1831,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1832,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1833,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1834,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1835,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFFBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1836,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1837,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1838,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1839,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1840,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1841,
    label = "C/H/Cs2/Cs\Cs|O-HHFFFBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1842,
    label = "C/H/Cs2/Cs\Cs|O-HHFFClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1843,
    label = "C/H/Cs2/Cs\Cs|O-HHFFClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1844,
    label = "C/H/Cs2/Cs\Cs|O-HHFFClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1845,
    label = "C/H/Cs2/Cs\Cs|O-HHFFClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1846,
    label = "C/H/Cs2/Cs\Cs|O-HHFFClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1847,
    label = "C/H/Cs2/Cs\Cs|O-HHFFClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1848,
    label = "C/H/Cs2/Cs\Cs|O-HHFFBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1849,
    label = "C/H/Cs2/Cs\Cs|O-HHFClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1850,
    label = "C/H/Cs2/Cs\Cs|O-HHFClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1851,
    label = "C/H/Cs2/Cs\Cs|O-HHFClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1852,
    label = "C/H/Cs2/Cs\Cs|O-HHFClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1853,
    label = "C/H/Cs2/Cs\Cs|O-HHFClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1854,
    label = "C/H/Cs2/Cs\Cs|O-HHFClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1855,
    label = "C/H/Cs2/Cs\Cs|O-HHFClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1856,
    label = "C/H/Cs2/Cs\Cs|O-HHFBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     F     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1857,
    label = "C/H/Cs2/Cs\Cs|O-HHClClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1858,
    label = "C/H/Cs2/Cs\Cs|O-HHClClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1859,
    label = "C/H/Cs2/Cs\Cs|O-HHClClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1860,
    label = "C/H/Cs2/Cs\Cs|O-HHClClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1861,
    label = "C/H/Cs2/Cs\Cs|O-HHClClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1862,
    label = "C/H/Cs2/Cs\Cs|O-HHClClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1863,
    label = "C/H/Cs2/Cs\Cs|O-HHClClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1864,
    label = "C/H/Cs2/Cs\Cs|O-HHClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1865,
    label = "C/H/Cs2/Cs\Cs|O-HHBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1866,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1867,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1868,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1869,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1870,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1871,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1872,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1873,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1874,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1875,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1876,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1877,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1878,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1879,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1880,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFFBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1881,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1882,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1883,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1884,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1885,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1886,
    label = "C/H/Cs2/Cs\Cs|O-HFFFFBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1887,
    label = "C/H/Cs2/Cs\Cs|O-HFFFClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1888,
    label = "C/H/Cs2/Cs\Cs|O-HFFFClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1889,
    label = "C/H/Cs2/Cs\Cs|O-HFFFClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1890,
    label = "C/H/Cs2/Cs\Cs|O-HFFFClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1891,
    label = "C/H/Cs2/Cs\Cs|O-HFFFClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1892,
    label = "C/H/Cs2/Cs\Cs|O-HFFFClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1893,
    label = "C/H/Cs2/Cs\Cs|O-HFFFBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1894,
    label = "C/H/Cs2/Cs\Cs|O-HFFClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1895,
    label = "C/H/Cs2/Cs\Cs|O-HFFClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1896,
    label = "C/H/Cs2/Cs\Cs|O-HFFClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1897,
    label = "C/H/Cs2/Cs\Cs|O-HFFClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1898,
    label = "C/H/Cs2/Cs\Cs|O-HFFClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1899,
    label = "C/H/Cs2/Cs\Cs|O-HFFClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1900,
    label = "C/H/Cs2/Cs\Cs|O-HFFClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1901,
    label = "C/H/Cs2/Cs\Cs|O-HFFBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1902,
    label = "C/H/Cs2/Cs\Cs|O-HFClClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1903,
    label = "C/H/Cs2/Cs\Cs|O-HFClClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1904,
    label = "C/H/Cs2/Cs\Cs|O-HFClClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1905,
    label = "C/H/Cs2/Cs\Cs|O-HFClClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1906,
    label = "C/H/Cs2/Cs\Cs|O-HFClClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1907,
    label = "C/H/Cs2/Cs\Cs|O-HFClClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1908,
    label = "C/H/Cs2/Cs\Cs|O-HFClClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1909,
    label = "C/H/Cs2/Cs\Cs|O-HFClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1910,
    label = "C/H/Cs2/Cs\Cs|O-HFBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     F     u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1911,
    label = "C/H/Cs2/Cs\Cs|O-HClClClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1912,
    label = "C/H/Cs2/Cs\Cs|O-HClClClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1913,
    label = "C/H/Cs2/Cs\Cs|O-HClClClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1914,
    label = "C/H/Cs2/Cs\Cs|O-HClClClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1915,
    label = "C/H/Cs2/Cs\Cs|O-HClClClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1916,
    label = "C/H/Cs2/Cs\Cs|O-HClClClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1917,
    label = "C/H/Cs2/Cs\Cs|O-HClClClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1918,
    label = "C/H/Cs2/Cs\Cs|O-HClClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1919,
    label = "C/H/Cs2/Cs\Cs|O-HClBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Cl    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1920,
    label = "C/H/Cs2/Cs\Cs|O-HBrBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     H     u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1921,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFFFF",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    F     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1922,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFFFCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1923,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFFFBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    F     u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1924,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFFClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1925,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFFClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1926,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFFBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    F     u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1927,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1928,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1929,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1930,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFFBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    F     u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1931,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1932,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1933,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1934,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1935,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFFBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    F     u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1936,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1937,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1938,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1939,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1940,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1941,
    label = "C/H/Cs2/Cs\Cs|O-FFFFFBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    F     u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1942,
    label = "C/H/Cs2/Cs\Cs|O-FFFFClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1943,
    label = "C/H/Cs2/Cs\Cs|O-FFFFClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1944,
    label = "C/H/Cs2/Cs\Cs|O-FFFFClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1945,
    label = "C/H/Cs2/Cs\Cs|O-FFFFClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1946,
    label = "C/H/Cs2/Cs\Cs|O-FFFFClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1947,
    label = "C/H/Cs2/Cs\Cs|O-FFFFClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1948,
    label = "C/H/Cs2/Cs\Cs|O-FFFFBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    F     u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1949,
    label = "C/H/Cs2/Cs\Cs|O-FFFClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1950,
    label = "C/H/Cs2/Cs\Cs|O-FFFClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1951,
    label = "C/H/Cs2/Cs\Cs|O-FFFClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1952,
    label = "C/H/Cs2/Cs\Cs|O-FFFClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1953,
    label = "C/H/Cs2/Cs\Cs|O-FFFClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1954,
    label = "C/H/Cs2/Cs\Cs|O-FFFClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1955,
    label = "C/H/Cs2/Cs\Cs|O-FFFClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1956,
    label = "C/H/Cs2/Cs\Cs|O-FFFBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     F     u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1957,
    label = "C/H/Cs2/Cs\Cs|O-FFClClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1958,
    label = "C/H/Cs2/Cs\Cs|O-FFClClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1959,
    label = "C/H/Cs2/Cs\Cs|O-FFClClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1960,
    label = "C/H/Cs2/Cs\Cs|O-FFClClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1961,
    label = "C/H/Cs2/Cs\Cs|O-FFClClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1962,
    label = "C/H/Cs2/Cs\Cs|O-FFClClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1963,
    label = "C/H/Cs2/Cs\Cs|O-FFClClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1964,
    label = "C/H/Cs2/Cs\Cs|O-FFClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1965,
    label = "C/H/Cs2/Cs\Cs|O-FFBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     F     u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1966,
    label = "C/H/Cs2/Cs\Cs|O-FClClClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1967,
    label = "C/H/Cs2/Cs\Cs|O-FClClClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1968,
    label = "C/H/Cs2/Cs\Cs|O-FClClClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1969,
    label = "C/H/Cs2/Cs\Cs|O-FClClClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1970,
    label = "C/H/Cs2/Cs\Cs|O-FClClClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1971,
    label = "C/H/Cs2/Cs\Cs|O-FClClClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1972,
    label = "C/H/Cs2/Cs\Cs|O-FClClClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1973,
    label = "C/H/Cs2/Cs\Cs|O-FClClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1974,
    label = "C/H/Cs2/Cs\Cs|O-FClBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Cl    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1975,
    label = "C/H/Cs2/Cs\Cs|O-FBrBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     F     u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1976,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClClClClClClCl",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Cl    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1977,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClClClClClClBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Cl    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1978,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClClClClClBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Cl    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1979,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClClClClBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Cl    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1980,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClClClBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Cl    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1981,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClClBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Cl    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1982,
    label = "C/H/Cs2/Cs\Cs|O-ClClClClBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Cl    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1983,
    label = "C/H/Cs2/Cs\Cs|O-ClClClBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Cl    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1984,
    label = "C/H/Cs2/Cs\Cs|O-ClClBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Cl    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1985,
    label = "C/H/Cs2/Cs\Cs|O-ClBrBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Cl    u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1986,
    label = "C/H/Cs2/Cs\Cs|O-BrBrBrBrBrBrBrBrBrBr",
    group = 
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 Br     u0 {1,S}
7     Br    u0 {2,S}
8     Br    u0 {2,S}
9     Br    u0 {3,S}
10    Br    u0 {3,S}
11    Br    u0 {3,S}
12    Br    u0 {5,S}
13    Br    u0 {4,S}
14    Br    u0 {4,S}
15    Br    u0 {4,S}
16    Br    u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1987,
    label = "C/H/Cs3_5ring",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 Br  u0 {1,S}
7    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1988,
    label = "C/H/Cs3_5ring_fused6",
    group = 
"""
1 *1 C  u0 {3,S} {4,S} {5,S} {8,S}
2    Cs u0 {3,S} {6,S} {7,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {1,S} {7,S}
6    Cs u0 {2,S} {4,S}
7    Cs u0 {2,S} {5,S}
8 *2 Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1989,
    label = "C/H/Cs3_5ring_adj5",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {7,S}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {2,S} {7,S}
6    Cs u0 {2,S} {8,S}
7    Cs u0 {3,S} {5,S}
8    Cs u0 {4,S} {6,S}
9 *2 Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1990,
    label = "C/H/Cs2N",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    N  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1991,
    label = "C/H/NDMustO",
    group = 
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1992,
    label = "C/H/Cs2O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    O  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1993,
    label = "C/H/CsO2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    O  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1994,
    label = "C/H/O3",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1995,
    label = "C/H/NDMustS",
    group = 
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br      u0 {1,S}
3    S      u0 {1,S}
4    [Cs,S] u0 {1,S}
5    [Cs,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1996,
    label = "C/H/Cs2S",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1997,
    label = "C/H/CsS2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    S  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1998,
    label = "C/H/S3",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
5    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1999,
    label = "C/H/NDMustOS",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br        u0 {1,S}
3    O        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2000,
    label = "C/H/CsOS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    O  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2001,
    label = "C/H/OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2002,
    label = "C/H/Cs2",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2003,
    label = "C/H/Cs2Ct",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2004,
    label = "C/H/Cs2Cb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2005,
    label = "C/H/Cs2CO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2006,
    label = "C/H/Cs2Cd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2007,
    label = "C/H/Cs2CS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2008,
    label = "C/H/CsO",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2009,
    label = "C/H/CsS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2010,
    label = "C/H/CbCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cb u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2011,
    label = "C/H/CtCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Ct u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2012,
    label = "C/H/CdCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2013,
    label = "C/H/CSCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2014,
    label = "C/H/OO",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2015,
    label = "C/H/OS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2016,
    label = "C/H/SS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2017,
    label = "C/H/TwoDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2018,
    label = "C/H/Cs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2019,
    label = "C/H/CtCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2020,
    label = "C/H/CtCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2021,
    label = "C/H/CtCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2022,
    label = "C/H/CbCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2023,
    label = "C/H/CbCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2024,
    label = "C/H/COCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2025,
    label = "C/H/CdCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2026,
    label = "C/H/CtCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2027,
    label = "C/H/CdCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2028,
    label = "C/H/CbCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br  u0 {1,S}
3    Cb u0 {1,S}
4    CS u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2029,
    label = "C/H/CdCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2030,
    label = "C/H/COCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 Br  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2031,
    label = "C/H/CdCd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2032,
    label = "C/H/CdCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2033,
    label = "C/H/CSCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 Br  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2034,
    label = "C/H/TDMustO",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2035,
    label = "C/H/TDMustS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2036,
    label = "C/H/ThreeDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2037,
    label = "N3_Br",
    group = 
"""
1 *1 [N3s,N3d] u0 {2,S}
2 *2 Br         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2038,
    label = "N3s_Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2039,
    label = "N/H_or_Val7/3",
    group = 
"""
1 *1 N3s      u0 {2,S} {3,S} {4,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2040,
    label = "NH3",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2041,
    label = "NH3-HF",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2042,
    label = "NH3-HCl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2043,
    label = "NH3-HBr",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2044,
    label = "NH3-FF",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2045,
    label = "NH3-FCl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2046,
    label = "NH3-FBr",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2047,
    label = "NH3-ClCl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2048,
    label = "NH3-ClBr",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2049,
    label = "NH3-BrBr",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2050,
    label = "N3s_pri_/H_or_Val7/",
    group = 
"""
1 *1 N3s      u0 {2,S} {3,S} {4,S}
2 *2 Br        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2051,
    label = "N3s_pri_Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2052,
    label = "N3s/H2/NonDe",
    group = 
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 Br            u0 {1,S}
3    H            u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2053,
    label = "N3s/H2/NonDeC",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2054,
    label = "N3s/H2/NonDeO",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2055,
    label = "N3s/H2/NonDeN",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    H   u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2056,
    label = "N3s/H2/OneDe",
    group = 
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 Br                          u0 {1,S}
3    H                          u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2057,
    label = "N3s/H2/OneDeN",
    group = 
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    H          u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2058,
    label = "N3s_pri_Br-F",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2059,
    label = "N3s/H2/NonDe-F",
    group = 
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 Br            u0 {1,S}
3    F            u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2060,
    label = "N3s/H2/NonDeC-F",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2061,
    label = "N3s/H2/NonDeO-F",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2062,
    label = "N3s/H2/NonDeN-F",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    F   u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2063,
    label = "N3s/H2/OneDe-F",
    group = 
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 Br                          u0 {1,S}
3    F                          u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2064,
    label = "N3s/H2/OneDeN-F",
    group = 
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    F          u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2065,
    label = "N3s_pri_Br-Cl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2066,
    label = "N3s/H2/NonDe-Cl",
    group = 
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 Br            u0 {1,S}
3    Cl           u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2067,
    label = "N3s/H2/NonDeC-Cl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2068,
    label = "N3s/H2/NonDeO-Cl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2069,
    label = "N3s/H2/NonDeN-Cl",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Cl  u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2070,
    label = "N3s/H2/OneDe-Cl",
    group = 
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 Br                          u0 {1,S}
3    Cl                         u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2071,
    label = "N3s/H2/OneDeN-Cl",
    group = 
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    Cl         u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2072,
    label = "N3s_pri_Br-Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2073,
    label = "N3s/H2/NonDe-Br",
    group = 
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 Br            u0 {1,S}
3    Br           u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2074,
    label = "N3s/H2/NonDeC-Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2075,
    label = "N3s/H2/NonDeO-Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2076,
    label = "N3s/H2/NonDeN-Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    Br  u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2077,
    label = "N3s/H2/OneDe-Br",
    group = 
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 Br                          u0 {1,S}
3    Br                         u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2078,
    label = "N3s/H2/OneDeN-Br",
    group = 
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 Br          u0 {1,S}
3    Br         u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2079,
    label = "N3s_sec_Br",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 Br   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2080,
    label = "N3d_Br",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2081,
    label = "N3d/H/NonDe",
    group = 
"""
1 *1 N3d          u0 {2,S} {3,D}
2 *2 Br            u0 {1,S}
3    [N3d,O2d,Cd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2082,
    label = "N3d/H/NonDeC",
    group = 
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5 *2 Br   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2083,
    label = "N3d/H/NonDeO",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2084,
    label = "N3d/H/NonDeN",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 Br   u0 {1,S}
3    N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2085,
    label = "N3d/H/OneDe",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2    Cdd u0 {1,D} {4,D}
3 *2 Br   u0 {1,S}
4    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2086,
    label = "N3d/H/CddO",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2    Cdd u0 {1,D} {4,D}
3 *2 Br   u0 {1,S}
4    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2087,
    label = "N5_Br",
    group = 
"""
1 *1 [N5sc,N5dc,N5ddc,N5tc,N5b] u0 p0 c+1 {2,S}
2 *2 Br                          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2088,
    label = "N5dc_Br",
    group = 
"""
1 *1 N5dc u0 p0 c+1 {2,S}
2 *2 Br    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2089,
    label = "N5dc/H/NonDeOO",
    group = 
"""
1 *1 N5dc u0 p0 c+1 {2,S} {3,S} {4,D}
2 *2 Br    u0 {1,S}
3    O2s  u0 {1,S}
4    O2d  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2090,
    label = "HCl",
    group = 
"""
1 *1 Cl1s u0 {2,S}
2 *2 Br    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2091,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    kinetics = None,
)

entry(
    index = 2092,
    label = "C_quintet",
    group = 
"""
1 *3 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 2093,
    label = "C_triplet",
    group = 
"""
1 *3 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 2094,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, C/H_or_Val7/quartet, C/H_or_Val7/doublet}",
    kinetics = None,
)

entry(
    index = 2095,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N u3 p1
""",
    kinetics = None,
)

entry(
    index = 2096,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N u1 p2
""",
    kinetics = None,
)

entry(
    index = 2097,
    label = "C/H_or_Val7/quartet",
    group = 
"""
1 *3 C        u3 p0 {2,S}
2    [H,Val7] u0 px {1,S}
""",
    kinetics = None,
)

entry(
    index = 2098,
    label = "CH_quartet",
    group = 
"""
1 *3 C u3 p0 {2,S}
2    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2099,
    label = "CH_quartet-F",
    group = 
"""
1 *3 C u3 p0 {2,S}
2    F u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2100,
    label = "CH_quartet-Cl",
    group = 
"""
1 *3 C  u3 p0 {2,S}
2    Cl u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2101,
    label = "CH_quartet-Br",
    group = 
"""
1 *3 C  u3 p0 {2,S}
2    Br u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2102,
    label = "C/H_or_Val7/doublet",
    group = 
"""
1 *3 C        u1 p1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2103,
    label = "CH_doublet",
    group = 
"""
1 *3 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2104,
    label = "CH_doublet-F",
    group = 
"""
1 *3 C u1 p1 {2,S}
2    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2105,
    label = "CH_doublet-Cl",
    group = 
"""
1 *3 C  u1 p1 {2,S}
2    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2106,
    label = "CH_doublet-Br",
    group = 
"""
1 *3 C  u1 p1 {2,S}
2    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2107,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 [Cs,Cd,CO,CS,O,S,N] u2
""",
    kinetics = None,
)

entry(
    index = 2108,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 2109,
    label = "S_atom_triplet",
    group = 
"""
1 *3 S u2
""",
    kinetics = None,
)

entry(
    index = 2110,
    label = "C/H_or_Val7/2_triplet",
    group = 
"""
1 *3 Cs       u2 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2111,
    label = "CH2_triplet",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2112,
    label = "CH2_triplet-HF",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2113,
    label = "CH2_triplet-HCl",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2114,
    label = "CH2_triplet-HBr",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2115,
    label = "CH2_triplet-FF",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2116,
    label = "CH2_triplet-FCl",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2117,
    label = "CH2_triplet-FBr",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2118,
    label = "CH2_triplet-ClCl",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2119,
    label = "CH2_triplet-ClBr",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    Cl u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2120,
    label = "CH2_triplet-BrBr",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    Br u0 {1,S}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2121,
    label = "N/H_or_Val7/_triplet",
    group = 
"""
1 *3 N3s      u2 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2122,
    label = "NH_triplet",
    group = 
"""
1 *3 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2123,
    label = "NH_triplet-F",
    group = 
"""
1 *3 N3s u2 {2,S}
2    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2124,
    label = "NH_triplet-Cl",
    group = 
"""
1 *3 N3s u2 {2,S}
2    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2125,
    label = "NH_triplet-Br",
    group = 
"""
1 *3 N3s u2 {2,S}
2    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2126,
    label = "Y_rad",
    group = 
"""
1 *3 R u1
""",
    kinetics = None,
)

entry(
    index = 2127,
    label = "H_rad",
    group = 
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 2128,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 [Ct,O2s,S2s] u1 {2,[S,T]}
2    [Ct,O2s,S2s] u1 {1,[S,T]}
""",
    kinetics = None,
)

entry(
    index = 2129,
    label = "O2b",
    group = 
"""
1 *3 O2s u1 {2,S}
2    O2s u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2130,
    label = "S2b",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    S2s u1 p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2131,
    label = "C2b",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2132,
    label = "Ct_rad",
    group = 
"""
1 *3 C     u1 {2,T}
2    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2133,
    label = "Ct_rad/Ct",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2134,
    label = "Ct_rad/N",
    group = 
"""
1 *3 Ct         u1 {2,T}
2    [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2135,
    label = "O_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2136,
    label = "O_pri_rad-H_or_Val7-1",
    group = 
"""
1 *3 O        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2137,
    label = "O_pri_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2138,
    label = "O_pri_rad-F",
    group = 
"""
1 *3 O u1 {2,S}
2    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2139,
    label = "O_pri_rad-Cl",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2140,
    label = "O_pri_rad-Br",
    group = 
"""
1 *3 O  u1 {2,S}
2    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2141,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2142,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2143,
    label = "O_rad/Cs\/H_or_Val7/2\Cs|/H_or_Val7/|Cs2",
    group = 
"""
1     C        u0 {2,S} {3,S} {4,S} {5,S}
2     C        u0 {1,S} {7,S} {8,S} {9,S}
3     Cs       u0 {1,S} {6,S} {10,S} {11,S}
4     C        u0 {1,S} {12,S} {13,S} {14,S}
5     [H,Val7] u0 {1,S}
6  *3 O        u1 {3,S}
7     [H,Val7] u0 {2,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {2,S}
10    [H,Val7] u0 {3,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {4,S}
13    [H,Val7] u0 {4,S}
14    [H,Val7] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2144,
    label = "O_rad/Cs\H2\Cs|H|Cs2",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2145,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHHF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2146,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHHCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2147,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHHBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2148,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2149,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2150,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2151,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2152,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2153,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHHBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2154,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2155,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2156,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2157,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2158,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2159,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2160,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2161,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2162,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2163,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHHBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2164,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2165,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2166,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2167,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2168,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2169,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2170,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2171,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2172,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2173,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHFBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2174,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2175,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2176,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2177,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2178,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHHBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2179,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2180,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2181,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2182,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2183,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2184,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2185,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2186,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2187,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2188,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFFBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2189,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2190,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2191,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2192,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2193,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHFBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2194,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2195,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2196,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2197,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2198,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2199,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHHBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2200,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2201,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2202,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2203,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2204,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2205,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2206,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2207,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2208,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2209,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFFBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2210,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2211,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2212,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2213,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2214,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFFBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2215,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2216,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2217,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2218,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2219,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2220,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHFBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2221,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2222,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2223,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2224,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2225,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2226,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2227,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHHBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2228,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2229,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2230,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2231,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2232,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2233,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2234,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2235,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2236,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2237,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFFBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2238,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2239,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2240,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2241,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2242,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFFBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2243,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2244,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2245,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2246,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2247,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2248,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFFBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2249,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2250,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2251,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2252,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2253,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2254,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2255,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHFBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2256,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2257,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2258,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2259,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2260,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2261,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2262,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHClBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2263,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HHBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2264,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2265,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2266,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2267,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2268,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2269,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2270,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2271,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2272,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2273,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFFBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2274,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2275,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2276,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2277,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2278,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFFBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2279,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2280,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2281,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2282,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2283,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2284,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFFBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2285,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2286,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2287,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2288,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2289,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2290,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2291,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFFBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2292,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2293,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2294,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2295,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2296,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2297,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2298,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFClBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2299,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HFBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2300,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2301,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2302,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2303,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2304,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2305,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2306,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClClBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2307,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HClBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2308,
    label = "O_rad/Cs\H2\Cs|H|Cs2-HBrBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2309,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFFFF",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    F  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2310,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFFFCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2311,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFFFBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    F  u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2312,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFFClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2313,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFFClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2314,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFFBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    F  u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2315,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2316,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2317,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2318,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFFBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    F  u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2319,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2320,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2321,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2322,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2323,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFFBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    F  u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2324,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2325,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2326,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2327,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2328,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2329,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFFBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     F  u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2330,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2331,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2332,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2333,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2334,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2335,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2336,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFFBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     F  u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2337,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2338,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2339,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2340,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2341,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2342,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2343,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFClBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2344,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FFBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     F  u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2345,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2346,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2347,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2348,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2349,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2350,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2351,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClClBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2352,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FClBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2353,
    label = "O_rad/Cs\H2\Cs|H|Cs2-FBrBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     F  u0 {1,S}
6  *3 O  u1 {3,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2354,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2355,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClClClClClClBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Cl u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2356,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClClClClClBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Cl u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2357,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClClClClBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Cl u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2358,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClClClBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Cl u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2359,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClClBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Cl u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2360,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClClBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Cl u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2361,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClClBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Cl u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2362,
    label = "O_rad/Cs\H2\Cs|H|Cs2-ClBrBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Cl u0 {1,S}
6  *3 O  u1 {3,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2363,
    label = "O_rad/Cs\H2\Cs|H|Cs2-BrBrBrBrBrBrBrBrBr",
    group = 
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     Br u0 {1,S}
6  *3 O  u1 {3,S}
7     Br u0 {2,S}
8     Br u0 {2,S}
9     Br u0 {2,S}
10    Br u0 {3,S}
11    Br u0 {3,S}
12    Br u0 {4,S}
13    Br u0 {4,S}
14    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2364,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O u1 {2,S}
2    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2365,
    label = "OOC",
    group = 
"""
1    O u0 {2,S} {3,S}
2 *3 O u1 {1,S}
3    C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2366,
    label = "O_rad/NonDeN",
    group = 
"""
1 *3 O   u1 {2,S}
2    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2367,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                             u1 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N3t,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2368,
    label = "O_rad/OneDeC",
    group = 
"""
1 *3 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2369,
    label = "O_rad/Cd",
    group = 
"""
1    Cd       u0 {2,S} {3,D}
2 *3 O        u1 {1,S}
3    [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2370,
    label = "O_rad/Cd\/H_or_Val7/_Cd\/H_or_Val7/2",
    group = 
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2    Cd       u0 {1,D} {5,S} {6,S}
3 *3 O        u1 {1,S}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2371,
    label = "O_rad/Cd\H_Cd\H2",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2372,
    label = "O_rad/Cd\H_Cd\H2-HHF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2373,
    label = "O_rad/Cd\H_Cd\H2-HHCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2374,
    label = "O_rad/Cd\H_Cd\H2-HHBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2375,
    label = "O_rad/Cd\H_Cd\H2-HFF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    F  u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2376,
    label = "O_rad/Cd\H_Cd\H2-HFCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    F  u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2377,
    label = "O_rad/Cd\H_Cd\H2-HFBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    F  u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2378,
    label = "O_rad/Cd\H_Cd\H2-HClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cl u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2379,
    label = "O_rad/Cd\H_Cd\H2-HClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cl u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2380,
    label = "O_rad/Cd\H_Cd\H2-HBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Br u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2381,
    label = "O_rad/Cd\H_Cd\H2-FFF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    F  u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2382,
    label = "O_rad/Cd\H_Cd\H2-FFCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    F  u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2383,
    label = "O_rad/Cd\H_Cd\H2-FFBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    F  u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2384,
    label = "O_rad/Cd\H_Cd\H2-FClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Cl u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2385,
    label = "O_rad/Cd\H_Cd\H2-FClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Cl u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2386,
    label = "O_rad/Cd\H_Cd\H2-FBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Br u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2387,
    label = "O_rad/Cd\H_Cd\H2-ClClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2388,
    label = "O_rad/Cd\H_Cd\H2-ClClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2389,
    label = "O_rad/Cd\H_Cd\H2-ClBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cl u0 {1,S}
5    Br u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2390,
    label = "O_rad/Cd\H_Cd\H2-BrBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Br u0 {1,S}
5    Br u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2391,
    label = "O_rad/Cd\/H_or_Val7/_Cd\/H_or_Val7/\Cs",
    group = 
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2    Cd       u0 {1,D} {5,S} {6,S}
3 *3 O        u1 {1,S}
4    [H,Val7] u0 {1,S}
5    Cs       u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2392,
    label = "O_rad/Cd\H_Cd\H\Cs",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2393,
    label = "O_rad/Cd\H_Cd\H\Cs-HF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2394,
    label = "O_rad/Cd\H_Cd\H\Cs-HCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2395,
    label = "O_rad/Cd\H_Cd\H\Cs-HBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2396,
    label = "O_rad/Cd\H_Cd\H\Cs-FF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Cs u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2397,
    label = "O_rad/Cd\H_Cd\H\Cs-FCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Cs u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2398,
    label = "O_rad/Cd\H_Cd\H\Cs-FBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Cs u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2399,
    label = "O_rad/Cd\H_Cd\H\Cs-ClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2400,
    label = "O_rad/Cd\H_Cd\H\Cs-ClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2401,
    label = "O_rad/Cd\H_Cd\H\Cs-BrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Br u0 {1,S}
5    Cs u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2402,
    label = "O_rad/Cd\/H_or_Val7/_Cd\Cs2",
    group = 
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2    Cd       u0 {1,D} {5,S} {6,S}
3 *3 O        u1 {1,S}
4    [H,Val7] u0 {1,S}
5    Cs       u0 {2,S}
6    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2403,
    label = "O_rad/Cd\H_Cd\Cs2",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2404,
    label = "O_rad/Cd\H_Cd\Cs2-F",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    F  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2405,
    label = "O_rad/Cd\H_Cd\Cs2-Cl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2406,
    label = "O_rad/Cd\H_Cd\Cs2-Br",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Br u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2407,
    label = "O_rad/Cd\Cs_Cd\/H_or_Val7/2",
    group = 
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2    Cd       u0 {1,D} {5,S} {6,S}
3 *3 O        u1 {1,S}
4    Cs       u0 {1,S}
5    [H,Val7] u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2408,
    label = "O_rad/Cd\Cs_Cd\H2",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2409,
    label = "O_rad/Cd\Cs_Cd\H2-HF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2410,
    label = "O_rad/Cd\Cs_Cd\H2-HCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2411,
    label = "O_rad/Cd\Cs_Cd\H2-HBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2412,
    label = "O_rad/Cd\Cs_Cd\H2-FF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    F  u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2413,
    label = "O_rad/Cd\Cs_Cd\H2-FCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    F  u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2414,
    label = "O_rad/Cd\Cs_Cd\H2-FBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    F  u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2415,
    label = "O_rad/Cd\Cs_Cd\H2-ClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cl u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2416,
    label = "O_rad/Cd\Cs_Cd\H2-ClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cl u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2417,
    label = "O_rad/Cd\Cs_Cd\H2-BrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Br u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2418,
    label = "O_rad/Cd\Cs_Cd\/H_or_Val7/\Cs",
    group = 
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2    Cd       u0 {1,D} {5,S} {6,S}
3 *3 O        u1 {1,S}
4    Cs       u0 {1,S}
5    Cs       u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2419,
    label = "O_rad/Cd\Cs_Cd\H\Cs",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2420,
    label = "O_rad/Cd\Cs_Cd\H\Cs-F",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2421,
    label = "O_rad/Cd\Cs_Cd\H\Cs-Cl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2422,
    label = "O_rad/Cd\Cs_Cd\H\Cs-Br",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2423,
    label = "O_rad/Cd\Cs_Cd\Cs2",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2424,
    label = "O_rad/OneDeN",
    group = 
"""
1 *3 O              u1 {2,S}
2    [N3d,N3t,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2425,
    label = "InChI=1S/NO3/c2-1(3)4",
    group = 
"""
1    N5dc u0 {2,S} {3,D} {4,S}
2 *3 O2s  u1 {1,S}
3    O2d  u0 {1,D}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2426,
    label = "S_rad",
    group = 
"""
1 *3 S u1
""",
    kinetics = None,
)

entry(
    index = 2427,
    label = "S_pri_rad-H_or_Val7-1",
    group = 
"""
1 *3 S2s      u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2428,
    label = "S_pri_rad",
    group = 
"""
1 *3 S2s u1 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2429,
    label = "S_pri_rad-F",
    group = 
"""
1 *3 S2s u1 {2,S}
2    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2430,
    label = "S_pri_rad-Cl",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2431,
    label = "S_pri_rad-Br",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2432,
    label = "S_rad/single",
    group = 
"""
1 *3 S   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2433,
    label = "S_rad/NonDeC",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2434,
    label = "S_rad/NonDeS",
    group = 
"""
1 *3 S2s u1 {2,S}
2    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2435,
    label = "S_rad/NonDeN",
    group = 
"""
1 *3 S2s u1 {2,S}
2    N   u0 p1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2436,
    label = "S_rad/NonDeO",
    group = 
"""
1 *3 S2s u1 {2,S}
2    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2437,
    label = "S_rad/OneDe",
    group = 
"""
1 *3 S2s              u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2438,
    label = "S_rad/Ct",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2439,
    label = "S_rad/Cb",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2440,
    label = "S_rad/CO",
    group = 
"""
1 *3 S2s u1 {2,S}
2    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2441,
    label = "S_rad/Cd",
    group = 
"""
1    Cd  u0 {2,S} {3,D}
2 *3 S2s u1 {1,S}
3    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2442,
    label = "S_rad/CS",
    group = 
"""
1    CS  u0 {2,S} {3,D}
2 *3 S2s u1 {1,S}
3    S   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2443,
    label = "S_rad/double",
    group = 
"""
1 *3 S   u1 p[0,1] {2,D}
2    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2444,
    label = "S_rad/double_val4",
    group = 
"""
1 *3 S   u1 p1 {2,D}
2    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2445,
    label = "S_rad/double_val4C",
    group = 
"""
1 *3 S u1 p1 {2,D}
2    C u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2446,
    label = "S_rad/double_val4N",
    group = 
"""
1 *3 S u1 p1 {2,D}
2    N u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2447,
    label = "S_rad/double_val4S",
    group = 
"""
1 *3 S u1 p1 {2,D}
2    S u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2448,
    label = "S_rad/double_val4O",
    group = 
"""
1 *3 S u1 p1 {2,D}
2    O u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2449,
    label = "S_rad/double_val6",
    group = 
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    R!H        u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2450,
    label = "S_rad/double_val6C",
    group = 
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    C          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2451,
    label = "S_rad/double_val6N",
    group = 
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    N          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2452,
    label = "S_rad/double_val6S",
    group = 
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    S          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2453,
    label = "S_rad/double_val6O",
    group = 
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    O          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2454,
    label = "S_rad/twoDoubles",
    group = 
"""
1 *3 [S6dd,S6dc] u1 p0 {2,D} {3,D}
2    R!H         u0 {1,D}
3    R!H         u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2455,
    label = "S_rad/twoDoublesOO",
    group = 
"""
1 *3 [S6dd,S6dc] u1 p0 {2,D} {3,D}
2    O           u0 {1,D}
3    O           u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2456,
    label = "S_rad/triple",
    group = 
"""
1 *3 S   u1 p[0,1] {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2457,
    label = "S_rad/triple_val4",
    group = 
"""
1 *3 S   u1 p1 {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2458,
    label = "S_rad/triple_val4C",
    group = 
"""
1 *3 S u1 p1 {2,T}
2    C u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2459,
    label = "S_rad/triple_val4N",
    group = 
"""
1 *3 S u1 p1 {2,T}
2    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2460,
    label = "S_rad/triple_val4S",
    group = 
"""
1 *3 S u1 p1 {2,T}
2    S u0 p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 2461,
    label = "S_rad/triple_val6",
    group = 
"""
1 *3 S   u1 p0 {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2462,
    label = "S_rad/triple_val6C",
    group = 
"""
1 *3 S u1 p0 {2,T}
2    C u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2463,
    label = "S_rad/triple_val6N",
    group = 
"""
1 *3 S u1 p0 {2,T}
2    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2464,
    label = "S_rad/triple_val6S",
    group = 
"""
1 *3 S u1 p0 {2,T}
2    S u0 p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 2465,
    label = "Cd_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2466,
    label = "Cd_pri_rad-H_or_Val7-1",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    Cd       u0 {1,D} {4,S}
3    [H,Val7] u0 {1,S}
4    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2467,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    H  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2468,
    label = "Cd_Cd\H2_pri_rad",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2469,
    label = "Cd_Cd\H\Cs_pri_rad",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2470,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2471,
    label = "Cd_Cd\Cs2_pri_rad",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2472,
    label = "Cd_pri_rad-F",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    F  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2473,
    label = "Cd_Cd\H2_pri_rad-HHF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2474,
    label = "Cd_Cd\H2_pri_rad-HFF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2475,
    label = "Cd_Cd\H2_pri_rad-FFF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2476,
    label = "Cd_Cd\H\Cs_pri_rad-HF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2477,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHF",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2478,
    label = "Cd_Cd\H\Cs_pri_rad-FF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2479,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFF",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2480,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFF",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2481,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFF",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    F  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2482,
    label = "Cd_Cd\Cs2_pri_rad-F",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2483,
    label = "Cd_pri_rad-Cl",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Cl u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2484,
    label = "Cd_Cd\H2_pri_rad-HHCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2485,
    label = "Cd_Cd\H2_pri_rad-HFCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2486,
    label = "Cd_Cd\H2_pri_rad-HClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2487,
    label = "Cd_Cd\H2_pri_rad-FFCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2488,
    label = "Cd_Cd\H2_pri_rad-FClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2489,
    label = "Cd_Cd\H2_pri_rad-ClClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2490,
    label = "Cd_Cd\H\Cs_pri_rad-HCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2491,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2492,
    label = "Cd_Cd\H\Cs_pri_rad-FCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2493,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2494,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2495,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2496,
    label = "Cd_Cd\H\Cs_pri_rad-ClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2497,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHClCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2498,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFClCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2499,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HClClCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2500,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFClCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2501,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FClClCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2502,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-ClClClCl",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Cl u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2503,
    label = "Cd_Cd\Cs2_pri_rad-Cl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2504,
    label = "Cd_pri_rad-Br",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Br u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2505,
    label = "Cd_Cd\H2_pri_rad-HHBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2506,
    label = "Cd_Cd\H2_pri_rad-HFBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2507,
    label = "Cd_Cd\H2_pri_rad-HClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2508,
    label = "Cd_Cd\H2_pri_rad-HBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2509,
    label = "Cd_Cd\H2_pri_rad-FFBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2510,
    label = "Cd_Cd\H2_pri_rad-FClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2511,
    label = "Cd_Cd\H2_pri_rad-FBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2512,
    label = "Cd_Cd\H2_pri_rad-ClClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2513,
    label = "Cd_Cd\H2_pri_rad-ClBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2514,
    label = "Cd_Cd\H2_pri_rad-BrBrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2515,
    label = "Cd_Cd\H\Cs_pri_rad-HBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2516,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2517,
    label = "Cd_Cd\H\Cs_pri_rad-FBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    F  u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2518,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    F  u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2519,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2520,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    F  u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2521,
    label = "Cd_Cd\H\Cs_pri_rad-ClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cl u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2522,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHClBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2523,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFClBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2524,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HClClBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2525,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFClBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2526,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FClClBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2527,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-ClClClBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cl u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2528,
    label = "Cd_Cd\H\Cs_pri_rad-BrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Br u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2529,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2530,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2531,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HClBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2532,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HBrBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2533,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2534,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FClBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2535,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FBrBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2536,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-ClClBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2537,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-ClBrBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2538,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-BrBrBrBr",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Br u0 {2,S}
8    Br u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2539,
    label = "Cd_Cd\Cs2_pri_rad-Br",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2540,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cd  u0 {1,D} {4,S}
3    R!H u0 {1,S}
4    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2541,
    label = "Cd_rad/NonDeC",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Cs u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2542,
    label = "Cd_Cd\/H_or_Val7/2_rad/Cs",
    group = 
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2 *3 Cd       u1 {1,D} {5,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2543,
    label = "Cd_Cd\H2_rad/Cs",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2544,
    label = "Cd_Cd\H2_rad/Cs-HF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2545,
    label = "Cd_Cd\H2_rad/Cs-HCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2546,
    label = "Cd_Cd\H2_rad/Cs-HBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2547,
    label = "Cd_Cd\H2_rad/Cs-FF",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2548,
    label = "Cd_Cd\H2_rad/Cs-FCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2549,
    label = "Cd_Cd\H2_rad/Cs-FBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2550,
    label = "Cd_Cd\H2_rad/Cs-ClCl",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2551,
    label = "Cd_Cd\H2_rad/Cs-ClBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2552,
    label = "Cd_Cd\H2_rad/Cs-BrBr",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2553,
    label = "Cd_Cd\/H_or_Val7/\Cs_rad/Cs",
    group = 
"""
1    Cs       u0 {3,S} {4,S} {5,S} {6,S}
2    Cd       u0 {3,D} {7,S} {8,S}
3 *3 Cd       u1 {1,S} {2,D}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {1,S}
6    [H,Val7] u0 {1,S}
7    Cs       u0 {2,S}
8    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2554,
    label = "Cd_Cd\H\Cs_rad/Cs",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2555,
    label = "Cd_Cd\H\Cs_rad/Cs-HHHF",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2556,
    label = "Cd_Cd\H\Cs_rad/Cs-HHHCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2557,
    label = "Cd_Cd\H\Cs_rad/Cs-HHHBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2558,
    label = "Cd_Cd\H\Cs_rad/Cs-HHFF",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2559,
    label = "Cd_Cd\H\Cs_rad/Cs-HHFCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2560,
    label = "Cd_Cd\H\Cs_rad/Cs-HHFBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2561,
    label = "Cd_Cd\H\Cs_rad/Cs-HHClCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2562,
    label = "Cd_Cd\H\Cs_rad/Cs-HHClBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2563,
    label = "Cd_Cd\H\Cs_rad/Cs-HHBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2564,
    label = "Cd_Cd\H\Cs_rad/Cs-HFFF",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2565,
    label = "Cd_Cd\H\Cs_rad/Cs-HFFCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2566,
    label = "Cd_Cd\H\Cs_rad/Cs-HFFBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2567,
    label = "Cd_Cd\H\Cs_rad/Cs-HFClCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2568,
    label = "Cd_Cd\H\Cs_rad/Cs-HFClBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2569,
    label = "Cd_Cd\H\Cs_rad/Cs-HFBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2570,
    label = "Cd_Cd\H\Cs_rad/Cs-HClClCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2571,
    label = "Cd_Cd\H\Cs_rad/Cs-HClClBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2572,
    label = "Cd_Cd\H\Cs_rad/Cs-HClBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2573,
    label = "Cd_Cd\H\Cs_rad/Cs-HBrBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2574,
    label = "Cd_Cd\H\Cs_rad/Cs-FFFF",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2575,
    label = "Cd_Cd\H\Cs_rad/Cs-FFFCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2576,
    label = "Cd_Cd\H\Cs_rad/Cs-FFFBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2577,
    label = "Cd_Cd\H\Cs_rad/Cs-FFClCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2578,
    label = "Cd_Cd\H\Cs_rad/Cs-FFClBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2579,
    label = "Cd_Cd\H\Cs_rad/Cs-FFBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2580,
    label = "Cd_Cd\H\Cs_rad/Cs-FClClCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2581,
    label = "Cd_Cd\H\Cs_rad/Cs-FClClBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2582,
    label = "Cd_Cd\H\Cs_rad/Cs-FClBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2583,
    label = "Cd_Cd\H\Cs_rad/Cs-FBrBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    F  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2584,
    label = "Cd_Cd\H\Cs_rad/Cs-ClClClCl",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2585,
    label = "Cd_Cd\H\Cs_rad/Cs-ClClClBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2586,
    label = "Cd_Cd\H\Cs_rad/Cs-ClClBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2587,
    label = "Cd_Cd\H\Cs_rad/Cs-ClBrBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    Cl u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2588,
    label = "Cd_Cd\H\Cs_rad/Cs-BrBrBrBr",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    Br u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {1,S}
7    Cs u0 {2,S}
8    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2589,
    label = "Cd_rad/NonDeO",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    O  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2590,
    label = "Cd_rad/NonDeS",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    S  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2591,
    label = "Cd_rad/NonDeN",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    N  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2592,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 Cd               u1 {2,D} {3,S}
2    Cd               u0 {1,D} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    R                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2593,
    label = "Cd_rad/Ct",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Ct u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2594,
    label = "Cd_rad/Cb",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Cb u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2595,
    label = "Cd_rad/CO",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    CO u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2596,
    label = "Cd_rad/Cd",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {5,S}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2597,
    label = "Cd_rad/CS",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {5,S}
3    CS u0 {1,S} {4,D}
4    S  u0 {3,D}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2598,
    label = "Cd_allenic_rad",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2599,
    label = "Cd_Cdd_rad/H_or_Val7/",
    group = 
"""
1 *3 Cd       u1 {2,D} {3,S}
2    Cdd      u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2600,
    label = "Cd_Cdd_rad/H",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2601,
    label = "Cd_Cdd_rad/H-F",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    F   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2602,
    label = "Cd_Cdd_rad/H-Cl",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cl  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2603,
    label = "Cd_Cdd_rad/H-Br",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Br  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2604,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       u1 {2,B} {3,B}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 2605,
    label = "CO_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2606,
    label = "CO_pri_rad-H_or_Val7-1",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2607,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2608,
    label = "CO_pri_rad-F",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2609,
    label = "CO_pri_rad-Cl",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2610,
    label = "CO_pri_rad-Br",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2611,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2612,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2613,
    label = "CO_rad/Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2614,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C                u1 {2,D} {3,S}
2    O                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2615,
    label = "CS_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2616,
    label = "CS_pri_rad-H_or_Val7-1",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2617,
    label = "CS_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2618,
    label = "CS_pri_rad-F",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2619,
    label = "CS_pri_rad-Cl",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2620,
    label = "CS_pri_rad-Br",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2621,
    label = "CS_sec_rad",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    S   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2622,
    label = "CS_rad/NonDe",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2623,
    label = "CS_rad/Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2624,
    label = "CS_rad/O",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2625,
    label = "CS_rad/S",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2626,
    label = "CS_rad/OneDe",
    group = 
"""
1 *3 C                u1 {2,D} {3,S}
2    S                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2627,
    label = "CS_rad/Ct",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2628,
    label = "CS_rad/Cb",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2629,
    label = "CS_rad/CO",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2630,
    label = "CS_rad/Cd",
    group = 
"""
1 *3 C  u1 {2,S} {3,D}
2    Cd u0 {1,S} {4,D}
3    S  u0 {1,D}
4    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2631,
    label = "CS_rad/CS",
    group = 
"""
1 *3 C  u1 {2,S} {3,D}
2    CS u0 {1,S} {4,D}
3    S  u0 {1,D}
4    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2632,
    label = "Cs_rad",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2633,
    label = "C_methyl-H_or_Val7-3",
    group = 
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2634,
    label = "C_methyl",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2635,
    label = "C_methyl-HHF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2636,
    label = "C_methyl-HHCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2637,
    label = "C_methyl-HHBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2638,
    label = "C_methyl-HFF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    F u0 {1,S}
4    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2639,
    label = "C_methyl-HFCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2640,
    label = "C_methyl-HFBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2641,
    label = "C_methyl-HClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2642,
    label = "C_methyl-HClBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2643,
    label = "C_methyl-HBrBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2644,
    label = "C_methyl-FFF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    F u0 {1,S}
3    F u0 {1,S}
4    F u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2645,
    label = "C_methyl-FFCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2646,
    label = "C_methyl-FFBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2647,
    label = "C_methyl-FClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2648,
    label = "C_methyl-FClBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2649,
    label = "C_methyl-FBrBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2650,
    label = "C_methyl-ClClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2651,
    label = "C_methyl-ClClBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2652,
    label = "C_methyl-ClBrBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2653,
    label = "C_methyl-BrBrBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Br u0 {1,S}
3    Br u0 {1,S}
4    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2654,
    label = "C_pri_rad-H_or_Val7-2",
    group = 
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2655,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2656,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2657,
    label = "C_rad/H2/Cs\H3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2658,
    label = "C_rad/H2/Cs\Cs2\O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    H     u0 {2,S}
7    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2659,
    label = "C_rad/H2/Cs\H\Cs\Cs|O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    H     u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2660,
    label = "C_rad/H2/Cs\H\Cs|Cs\O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    H     u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2661,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    H     u0 {2,S}
9    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2662,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2663,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2664,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2665,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2666,
    label = "C_rad/H2/CS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2667,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2668,
    label = "C_rad/H2/S",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2669,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,D}
3    H u0 {1,S}
4    H u0 {1,S}
5    C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2670,
    label = "C_rad/H2/Cd\H_Cd\H2",
    group = 
"""
1 *3 C u1 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,D} {6,S}
3    C u0 {2,D}
4    H u0 {1,S}
5    H u0 {1,S}
6    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2671,
    label = "C_rad/H2/Cd\H_Cd\H2-HHF",
    group = 
"""
1 *3 C u1 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,D} {6,S}
3    C u0 {2,D}
4    H u0 {1,S}
5    H u0 {1,S}
6    F u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2672,
    label = "C_rad/H2/Cd\H_Cd\H2-HHCl",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2673,
    label = "C_rad/H2/Cd\H_Cd\H2-HHBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2674,
    label = "C_rad/H2/Cd\Cs_Cd\H2",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {1,S}
8     H u0 {3,S}
9     H u0 {3,S}
10    H u0 {4,S}
11    H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2675,
    label = "C_rad/H2/N",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2676,
    label = "C_pri_rad-HF",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2677,
    label = "C_rad/H2/Cs-HF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2678,
    label = "C_rad/H2/Cs\H3-HHHHF",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2679,
    label = "C_rad/H2/Cs\Cs2\O-HF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    H     u0 {2,S}
7    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2680,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HHF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    F     u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2681,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HHF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    F     u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2682,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHHF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    H     u0 {2,S}
9    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2683,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHHF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    H     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2684,
    label = "C_rad/H2/Ct-HF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2685,
    label = "C_rad/H2/Cb-HF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2686,
    label = "C_rad/H2/CO-HF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2687,
    label = "C_rad/H2/CS-HF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    F  u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2688,
    label = "C_rad/H2/O-HF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    F u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2689,
    label = "C_rad/H2/S-HF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    F u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2690,
    label = "C_rad/H2/Cd-HF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,D}
3    H u0 {1,S}
4    F u0 {1,S}
5    C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2691,
    label = "C_rad/H2/Cd\H_Cd\H2-HFF",
    group = 
"""
1 *3 C u1 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,D} {6,S}
3    C u0 {2,D}
4    H u0 {1,S}
5    F u0 {1,S}
6    F u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2692,
    label = "C_rad/H2/Cd\H_Cd\H2-HFCl",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2693,
    label = "C_rad/H2/Cd\H_Cd\H2-HFBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2694,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHHF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {1,S}
8     H u0 {3,S}
9     H u0 {3,S}
10    H u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2695,
    label = "C_rad/H2/N-HF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    F u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2696,
    label = "C_pri_rad-HCl",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    Cl  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2697,
    label = "C_rad/H2/Cs-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2698,
    label = "C_rad/H2/Cs\H3-HHHHCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2699,
    label = "C_rad/H2/Cs\Cs2\O-HCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    H     u0 {2,S}
7    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2700,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HHCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    Cl    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2701,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HHCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    Cl    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2702,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHHCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    H     u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2703,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHHCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    H     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2704,
    label = "C_rad/H2/Ct-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2705,
    label = "C_rad/H2/Cb-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2706,
    label = "C_rad/H2/CO-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2707,
    label = "C_rad/H2/CS-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2708,
    label = "C_rad/H2/O-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2709,
    label = "C_rad/H2/S-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2710,
    label = "C_rad/H2/Cd-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    C  u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2711,
    label = "C_rad/H2/Cd\H_Cd\H2-HClCl",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2712,
    label = "C_rad/H2/Cd\H_Cd\H2-HClBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2713,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHHCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     H  u0 {3,S}
10    H  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2714,
    label = "C_rad/H2/N-HCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cl u0 {1,S}
4    N  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2715,
    label = "C_pri_rad-HBr",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    Br  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2716,
    label = "C_rad/H2/Cs-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2717,
    label = "C_rad/H2/Cs\H3-HHHHBr",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2718,
    label = "C_rad/H2/Cs\Cs2\O-HBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    H     u0 {2,S}
7    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2719,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HHBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    Br    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2720,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HHBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    Br    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2721,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHHBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    H     u0 {2,S}
9    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2722,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHHBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    H     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2723,
    label = "C_rad/H2/Ct-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2724,
    label = "C_rad/H2/Cb-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2725,
    label = "C_rad/H2/CO-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2726,
    label = "C_rad/H2/CS-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2727,
    label = "C_rad/H2/O-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2728,
    label = "C_rad/H2/S-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2729,
    label = "C_rad/H2/Cd-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    C  u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Br u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2730,
    label = "C_rad/H2/Cd\H_Cd\H2-HBrBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    H  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2731,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHHBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     H  u0 {3,S}
10    H  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2732,
    label = "C_rad/H2/N-HBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Br u0 {1,S}
4    N  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2733,
    label = "C_pri_rad-FF",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F   u0 {1,S}
3    F   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2734,
    label = "C_rad/H2/Cs-FF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2735,
    label = "C_rad/H2/Cs\H3-HHHFF",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2736,
    label = "C_rad/H2/Cs\H3-HHFFF",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2737,
    label = "C_rad/H2/Cs\H3-HFFFF",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2738,
    label = "C_rad/H2/Cs\H3-FFFFF",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    F  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2739,
    label = "C_rad/H2/Cs\Cs2\O-FF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    F     u0 {2,S}
7    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2740,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    F     u0 {2,S}
7    F     u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2741,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-FFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    F     u0 {1,S}
6    F     u0 {2,S}
7    F     u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2742,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    F     u0 {2,S}
7    F     u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2743,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-FFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    F     u0 {1,S}
6    F     u0 {2,S}
7    F     u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2744,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2745,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HFFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2746,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-FFFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    F     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2747,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2748,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HFFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    F     u0 {1,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2749,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-FFFF",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    F     u0 {1,S}
6    F     u0 {1,S}
7    F     u0 {2,S}
8    F     u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2750,
    label = "C_rad/H2/Ct-FF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2751,
    label = "C_rad/H2/Cb-FF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2752,
    label = "C_rad/H2/CO-FF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2753,
    label = "C_rad/H2/CS-FF",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    F  u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2754,
    label = "C_rad/H2/O-FF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    F u0 {1,S}
3    F u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2755,
    label = "C_rad/H2/S-FF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    F u0 {1,S}
3    F u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2756,
    label = "C_rad/H2/Cd-FF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,D}
3    F u0 {1,S}
4    F u0 {1,S}
5    C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2757,
    label = "C_rad/H2/Cd\H_Cd\H2-FFF",
    group = 
"""
1 *3 C u1 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,D} {6,S}
3    C u0 {2,D}
4    F u0 {1,S}
5    F u0 {1,S}
6    F u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2758,
    label = "C_rad/H2/Cd\H_Cd\H2-FFCl",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2759,
    label = "C_rad/H2/Cd\H_Cd\H2-FFBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2760,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHFF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {1,S}
8     H u0 {3,S}
9     H u0 {3,S}
10    F u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2761,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHFFF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {1,S}
8     H u0 {3,S}
9     F u0 {3,S}
10    F u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2762,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHFFFF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {1,S}
8     F u0 {3,S}
9     F u0 {3,S}
10    F u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2763,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHFFFFF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     F u0 {1,S}
8     F u0 {3,S}
9     F u0 {3,S}
10    F u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2764,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFFFFFF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     F u0 {1,S}
7     F u0 {1,S}
8     F u0 {3,S}
9     F u0 {3,S}
10    F u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2765,
    label = "C_rad/H2/Cd\Cs_Cd\H2-FFFFFFF",
    group = 
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     F u0 {1,S}
6     F u0 {1,S}
7     F u0 {1,S}
8     F u0 {3,S}
9     F u0 {3,S}
10    F u0 {4,S}
11    F u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2766,
    label = "C_rad/H2/N-FF",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    F u0 {1,S}
3    F u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2767,
    label = "C_pri_rad-FCl",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F   u0 {1,S}
3    Cl  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2768,
    label = "C_rad/H2/Cs-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2769,
    label = "C_rad/H2/Cs\H3-HHHFCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2770,
    label = "C_rad/H2/Cs\H3-HHFFCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2771,
    label = "C_rad/H2/Cs\H3-HFFFCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2772,
    label = "C_rad/H2/Cs\H3-FFFFCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2773,
    label = "C_rad/H2/Cs\Cs2\O-FCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    F     u0 {2,S}
7    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2774,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    F     u0 {2,S}
7    Cl    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2775,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-FFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    F     u0 {1,S}
6    F     u0 {2,S}
7    Cl    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2776,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    F     u0 {2,S}
7    Cl    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2777,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-FFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    F     u0 {1,S}
6    F     u0 {2,S}
7    Cl    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2778,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2779,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HFFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2780,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-FFFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2781,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2782,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HFFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    F     u0 {1,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2783,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-FFFCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    F     u0 {1,S}
6    F     u0 {1,S}
7    F     u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2784,
    label = "C_rad/H2/Ct-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2785,
    label = "C_rad/H2/Cb-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2786,
    label = "C_rad/H2/CO-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2787,
    label = "C_rad/H2/CS-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2788,
    label = "C_rad/H2/O-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2789,
    label = "C_rad/H2/S-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2790,
    label = "C_rad/H2/Cd-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    C  u0 {1,S} {5,D}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2791,
    label = "C_rad/H2/Cd\H_Cd\H2-FClCl",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2792,
    label = "C_rad/H2/Cd\H_Cd\H2-FClBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2793,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHFCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     H  u0 {3,S}
10    F  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2794,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHFFCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2795,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHFFFCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2796,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHFFFFCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2797,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFFFFFCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2798,
    label = "C_rad/H2/Cd\Cs_Cd\H2-FFFFFFCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     F  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2799,
    label = "C_rad/H2/N-FCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Cl u0 {1,S}
4    N  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2800,
    label = "C_pri_rad-FBr",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F   u0 {1,S}
3    Br  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2801,
    label = "C_rad/H2/Cs-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2802,
    label = "C_rad/H2/Cs\H3-HHHFBr",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2803,
    label = "C_rad/H2/Cs\H3-HHFFBr",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2804,
    label = "C_rad/H2/Cs\H3-HFFFBr",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2805,
    label = "C_rad/H2/Cs\H3-FFFFBr",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    F  u0 {2,S}
7    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2806,
    label = "C_rad/H2/Cs\Cs2\O-FBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    F     u0 {2,S}
7    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2807,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    F     u0 {2,S}
7    Br    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2808,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-FFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    F     u0 {1,S}
6    F     u0 {2,S}
7    Br    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2809,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    F     u0 {2,S}
7    Br    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2810,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-FFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    F     u0 {1,S}
6    F     u0 {2,S}
7    Br    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2811,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2812,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HFFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2813,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-FFFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    F     u0 {2,S}
9    Br    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2814,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2815,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HFFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    F     u0 {1,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2816,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-FFFBr",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    F     u0 {1,S}
6    F     u0 {1,S}
7    F     u0 {2,S}
8    Br    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2817,
    label = "C_rad/H2/Ct-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2818,
    label = "C_rad/H2/Cb-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2819,
    label = "C_rad/H2/CO-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2820,
    label = "C_rad/H2/CS-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2821,
    label = "C_rad/H2/O-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2822,
    label = "C_rad/H2/S-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2823,
    label = "C_rad/H2/Cd-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    C  u0 {1,S} {5,D}
3    F  u0 {1,S}
4    Br u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2824,
    label = "C_rad/H2/Cd\H_Cd\H2-FBrBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    F  u0 {1,S}
5    Br u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2825,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHFBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     H  u0 {3,S}
10    F  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2826,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHFFBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2827,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHFFFBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2828,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHFFFFBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2829,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFFFFFBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2830,
    label = "C_rad/H2/Cd\Cs_Cd\H2-FFFFFFBr",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     F  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    F  u0 {4,S}
11    Br u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2831,
    label = "C_rad/H2/N-FBr",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    F  u0 {1,S}
3    Br u0 {1,S}
4    N  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2832,
    label = "C_pri_rad-ClCl",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    Cl  u0 {1,S}
3    Cl  u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2833,
    label = "C_rad/H2/Cs-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2834,
    label = "C_rad/H2/Cs\H3-HHHClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2835,
    label = "C_rad/H2/Cs\H3-HHFClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2836,
    label = "C_rad/H2/Cs\H3-HHClClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2837,
    label = "C_rad/H2/Cs\H3-HFFClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2838,
    label = "C_rad/H2/Cs\H3-HFClClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2839,
    label = "C_rad/H2/Cs\H3-HClClClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2840,
    label = "C_rad/H2/Cs\H3-FFFClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    F  u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2841,
    label = "C_rad/H2/Cs\H3-FFClClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    F  u0 {1,S}
4    F  u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2842,
    label = "C_rad/H2/Cs\H3-FClClClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    F  u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2843,
    label = "C_rad/H2/Cs\H3-ClClClClCl",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
7    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2844,
    label = "C_rad/H2/Cs\Cs2\O-ClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2845,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-HClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2846,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-FClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    F     u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2847,
    label = "C_rad/H2/Cs\H\Cs\Cs|O-ClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    Cl    u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2848,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-HClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2849,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-FClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    F     u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2850,
    label = "C_rad/H2/Cs\H\Cs|Cs\O-ClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    Cl    u0 {1,S}
6    Cl    u0 {2,S}
7    Cl    u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2851,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HHClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    Cl    u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2852,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HFClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    Cl    u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2853,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-HClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    Cl    u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    Cl    u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2854,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-FFClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    F     u0 {1,S}
5    F     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    Cl    u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2855,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-FClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    F     u0 {1,S}
5    Cl    u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    Cl    u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2856,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O-ClClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    Cl    u0 {1,S}
5    Cl    u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    Cl    u0 {2,S}
9    Cl    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2857,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HHClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2858,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HFClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    F     u0 {1,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2859,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-HClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    Cl    u0 {1,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2860,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-FFClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    F     u0 {1,S}
6    F     u0 {1,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2861,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-FClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    F     u0 {1,S}
6    Cl    u0 {1,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2862,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O-ClClClCl",
    group = 
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    Cl    u0 {1,S}
6    Cl    u0 {1,S}
7    Cl    u0 {2,S}
8    Cl    u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2863,
    label = "C_rad/H2/Ct-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2864,
    label = "C_rad/H2/Cb-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2865,
    label = "C_rad/H2/CO-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2866,
    label = "C_rad/H2/CS-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2867,
    label = "C_rad/H2/O-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2868,
    label = "C_rad/H2/S-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cl u0 {1,S}
3    Cl u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2869,
    label = "C_rad/H2/Cd-ClCl",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    C  u0 {1,S} {5,D}
3    Cl u0 {1,S}
4    Cl u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2870,
    label = "C_rad/H2/Cd\H_Cd\H2-ClClCl",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Cl u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2871,
    label = "C_rad/H2/Cd\H_Cd\H2-ClClBr",
    group = 
"""
1 *3 C  u1 {2,S} {4,S} {5,S}
2    C  u0 {1,S} {3,D} {6,S}
3    C  u0 {2,D}
4    Cl u0 {1,S}
5    Cl u0 {1,S}
6    Br u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2872,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     H  u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2873,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHFClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     F  u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2874,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2875,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHFFClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2876,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHFClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     F  u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2877,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2878,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHFFFClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2879,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHFFClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2880,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHFClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     F  u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2881,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHClClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     Cl u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2882,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFFFFClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2883,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFFFClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2884,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFFClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2885,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HFClClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     F  u0 {1,S}
7     Cl u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2886,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HClClClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     H  u0 {1,S}
6     Cl u0 {1,S}
7     Cl u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2887,
    label = "C_rad/H2/Cd\Cs_Cd\H2-FFFFFClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     F  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     F  u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2888,
    label = "C_rad/H2/Cd\Cs_Cd\H2-FFFFClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     F  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     F  u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2889,
    label = "C_rad/H2/Cd\Cs_Cd\H2-FFFClClClCl",
    group = 
"""
1     C  u0 {2,S} {5,S} {6,S} {7,S}
2     C  u0 {1,S} {3,D} {4,S}
3     C  u0 {2,D} {8,S} {9,S}
4  *3 C  u1 {2,S} {10,S} {11,S}
5     F  u0 {1,S}
6     F  u0 {1,S}
7     F  u0 {1,S}
8     Cl u0 {3,S}
9     Cl u0 {3,S}
10    Cl u0 {4,S}
11    Cl u0 {4,S}
)
