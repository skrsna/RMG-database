#!/usr/bin/env python
# encoding: utf-8

name = "2_amine_ketone/groups"
shortDesc = u""
longDesc = u"""
This family describes a reaction between a secondary amine and a ketone/aldehyde, producing a tertiary amine.
R1NHR2 + C=O <=> R1N(R2)COH

atom labels:

R1_N[*1]_H[*2]_R2 + C[*3]_=O[*4] <=> R1_N[*1]_(R2)_C[*3]_O[*4]_H[*2]
"""

template(reactants=["acetal", "H2O"], products=["hemiacetal", "alcohol"], ownReverse=False)

reverse = "3_amine_C_OH_to_2_amine_ketone"

reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*4', 1, '*2'],
])

entry(
    index=0,
    label="2_amine",
    group=
"""
1    R!H u0 p2 c0 {2,S}
2 *1 N   u0 p1 c0 {1,S} {3,S} {4,S}
3    R!H u0 p2 c0 {2,S}
4 *2 H   u0 p0 c0 {2,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="ketone",
    group=
"""
1 *3 C u0 p0 c0 {2,D}
2 *4 O u0 p2 c0 {1,D}
""",
    kinetics=None,
)

entry(
    index=2,
    label="formaldehyde",
    group=
"""
1 *3 C u0 p0 c0 {2,D} {3,S} {4,S}
2 *4 O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}

""",
    kinetics=None,
)

tree(
"""
L1: 2_amine
L1: ketone
  L2: formaldehyde
"""
)
