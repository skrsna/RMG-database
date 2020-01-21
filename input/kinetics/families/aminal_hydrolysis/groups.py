#!/usr/bin/env python
# encoding: utf-8

name = "aminal_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of aminal groups:
C(OH)N(R1)R2 + H2O <=> C=O + HN(R1)R2 + H2O

atom labels:

C[*1]_(O[*2]_H[*3])_N[*4]_(R1)_R2 + H2O <=> C[*1]_=O[*2] + H[*3]_N[*4]_(R1)_R2 + H2O
"""

template(reactants=["aminal", "H2O"], products=["CdO", "NH2", "H2O"], ownReverse=False)

reverse = "condensation_to_amino_alcohol"

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['FORM_BOND', '*5', 1, '*6'],
])

entry(
    index=0,
    label="aminal",
    group=
"""
1 *2 O u0 p2 c0 {2,S} {4,S}
2 *1 C u0 p0 c0 {1,S} {3,S}
3 *4 N u0 p1 c0 {2,S} {5,S} {6,S}
4 *3 H u0 p0 c0 {1,S}
5    R ux px cx {3,S}
6    R ux px cx {3,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *5 O u0 p2 c0 {2,S} {3,S}
2 *6 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: aminal
L1: H2O
"""
)
