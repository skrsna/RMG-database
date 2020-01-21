#!/usr/bin/env python
# encoding: utf-8

name = "hydroperoxide_to_alcohol/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="ROOH;H2O",
    kinetics=ArrheniusEP(A=(3e+12, 'cm^3/(mol*s)'), n=0, alpha=0, E0=(0, 'kcal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)
