#!/usr/bin/env python
# encoding: utf-8

name = "imine_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
C=NR + H2O <=> C=O + RNH2

atom labels:

C[*1]_=N[*2]_R + H[*4]_O[*3]_H[*5] <=> C[*1]_=O[*3] + R_N[*2]_H[*4]_H[*5]
"""

template(reactants=["CdN", "H2O"], products=["CdO", "NH2"], ownReverse=False)

reverse = "condensation_to_imine"

reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*5'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*5'],
])

entry(
    index=0,
    label="CdN",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {3,S}
2 *2 N u0 p1 c0 {1,D}
3    R ux px cx {1,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *3 O u0 p2 c0 {2,S} {3,S}
2 *4 H u0 p0 c0 {1,S}
3 *5 H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: CdN
L1: H2O
"""
)
