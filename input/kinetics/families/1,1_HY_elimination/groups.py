#!/usr/bin/env python
#encoding: utf-8

name = "1,1_HY_elimination/groups"
shortDesc = u""
longDesc = u"""
Example:

Y = F,Cl,Br

     [H,Y]*2
     |                  ..
 R--C*1--[H,Y]*3 -> R--C*1--Y (S) + Y*2--H*3
     |
     Y

"""

template(reactants=["RCY_HY/HY"], products=["RCY", "HY-HY"], ownReverse=False)

reversible = True
reverse = "1,1_HY_addition"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_PAIR','*1',1],
])

entry(
    index = 1,
    label = "RCY_HY/HY",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 [H,Val7]  u0 px c0 {1,S}
3 *3 [H,Val7]  u0 px c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "RCY_H/H",
    group =
"""
1 *1 Cs u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "RCY_Y/HY",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Val7  u0 p3 c0 {1,S}
3 *3 [H,Val7]  u0 px c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "RCY_Y/H",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Val7  u0 p3 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 4,
    label = "RCY_Y/Y",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Val7  u0 p3 c0 {1,S}
3 *3 Val7 u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "RCY_F/Y",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 Val7 u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "RCY_F/F",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 F u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "RCY_F/Cl",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 Cl u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "RCY_F/Br",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 Br u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "RCY_Cl/Y",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Cl  u0 p3 c0 {1,S}
3 *3 Val7 u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "RCY_Cl/Cl",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Cl  u0 p3 c0 {1,S}
3 *3 Cl u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "RCY_Cl/Br",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Cl  u0 p3 c0 {1,S}
3 *3 Br u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "RCY_Br/Br",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 Br  u0 p3 c0 {1,S}
3 *3 Br u0 p3 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "RCF_F/F",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 F u0 p3 c0 {1,S}
4    F u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CF4",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 F u0 p3 c0 {1,S}
4    F u0 p3 c0 {1,S}
5    F u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CHF3",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 F u0 p3 c0 {1,S}
4    F u0 p3 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "RCY_F/H",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    Val7 u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "RCF_F/H",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    F u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "FCF_F/H",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    F u0 p3 c0 {1,S}
5    F u0 p3 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "HCF_F/H",
    group =
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 F  u0 p3 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    F u0 p3 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: RCY_HY/HY
    L2: RCY_Y/HY
        L3: RCY_Y/H
            L4: RCY_F/H
                L5: RCF_F/H
                    L6: FCF_F/H
                    L6: HCF_F/H
        L3: RCY_Y/Y
            L4: RCY_F/Y
                L5: RCY_F/F
                    L6: RCF_F/F
                        L7: CF4
                        L7: CHF3
                L5: RCY_F/Cl
                L5: RCY_F/Br
            L4: RCY_Cl/Y
                L5: RCY_Cl/Br
                L5: RCY_Cl/Cl
            L4: RCY_Br/Br
"""
)
