#!/usr/bin/env python
# encoding: utf-8

name = "acetal_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes hydrolysis of an acetal species (two esters), R1C(OR2)OR3.
The reaction is acid-catalyzed, the template here does not consider a pH effect.
R1C(OR2)OR3 + H2O <=> R1C(OR2)OH + R3OH

atom labels:

R1_C_(O_R2)_O[*1]_R3[*2] + H[*3]_O[*4]_H <=> R1_C_(O_R2)_O[*1]_H[*3] + R3[*2]_O[*4]_H

Some rate data is available here: https://doi.org/10.1021/ja00406a036
"""

template(reactants=["acetal", "H2O"], products=["hemiacetal", "alcohol"], ownReverse=False)

reverse = "alcohol_hemiacetal_condensation"

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index=0,
    label="acetal",
    group=
"""
1     Cs u0 p0 c0 {2,S} {3,S} {4,S}
2  *1 O  u0 p2 c0 {1,S} {5,S}
3     O  u0 p2 c0 {1,S} {6,S}
4     H  u0 p0 c0 {1,S}
5  *2 R!H ux px cx {2,S}
6     R!H ux px cx {3,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *4 O u0 p2 c0 {2,S} {3,S}
2 *3 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: acetal
L1: H2O
"""
)
