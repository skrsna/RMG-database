#!/usr/bin/env python
# encoding: utf-8

name = "hemiacetal_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=0,
    label="CH2O + H2O <=> OHCH2OH",
    degeneracy=2,
    rank=1,
    kinetics=Arrhenius(A=(3.67e+06, 'cm^3/(mol*s)'), n=0, Ea=(5.83, 'kcal/mol'), T0=(1, 'K'),
                       Tmin=(285, 'K'), Tmax=(345, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
J.G.M. Winkelman, O.K. Voorwinde, M. Ottens, A.A.C.M. Beenackers, L.P.B.M. Janssen
Chemical Engineering Science, Volume 57, Issue 19, October 2002, Pages 4067-4076
https://doi.org/10.1016/S0009-2509(02)00358-5
The original rate was multiplied by 18 cm3/mol to convert units into a second order reaction.
""",
)
