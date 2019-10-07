#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 0,
    label = "CH3F + H <=> CH3_p1 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.73e+08,'cm^3/(mol*s)'), n=1.77, Ea=(31000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 1,
    label = "CH2F2 + H <=> CH2F_p1 + HF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.9e+08,'cm^3/(mol*s)'), n=1.73, Ea=(35370,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 2,
    label = "CHF3 + H <=> CHF2_p1 + HF",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.11e+08,'cm^3/(mol*s)'), n=1.77, Ea=(39800,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 3,
    label = "CF4 + H <=> CF3_p1 + HF",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(3.07e+09,'cm^3/(mol*s)'), n=1.58, Ea=(41330,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 4,
    label = "CF4 + CH3 <=> CH3F_p23 + CF3_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(96400,'cm^3/(mol*s)'), n=2.41, Ea=(26130,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

# entry(
#     index = 5,
#     label = "CF2O + H <=> CFO + HF",
#     degeneracy = 1.0,
#     duplicate = True,
#     kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(2.4e+07,'cm^3/(mol*s)'), n=1.88, Ea=(35900,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.2e+10,'cm^3/(mol*s)'), n=0.83, Ea=(22300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.2e+09,'cm^3/(mol*s)'), n=1.42, Ea=(18900,'cal/mol'), T0=(1,'K'))]),
#     rank = 10,
#     shortDesc = u"""From NIST CH2F2 model""",
# )

entry(
    index = 6,
    label = "CF3-CF3 + H <=> CF3-CF2_p1 + HF",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(1e+15,'cm^3/(mol*s)'), n=0, Ea=(30000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 7,
    label = "CF3-CF3 + CF3 <=> CF4_p23 + CF3-CF2_p1",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(3e+12,'cm^3/(mol*s)'), n=0, Ea=(11300,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 8,
    label = "CF3COF + H <=> CF3CO_p1 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(3000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 9,
    label = "CF3COF + CF3 <=> CF3CO_p1 + CF4_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(9000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 10,
    label = "CF3COF + CF3-CF2 <=> CF3CO_p1 + CF3-CF3_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+11,'cm^3/(mol*s)'), n=0, Ea=(14000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 11,
    label = "F2 + H <=> F_p1 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9e+09,'cm^3/(mol*s)'), n=1.4, Ea=(1330,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 12,
    label = "F2 + CF3 <=> CF4_p23 + F_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.65e+12,'cm^3/(mol*s)'), n=0, Ea=(2500,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 13,
    label = "CH3 + F2 <=> CH3F_p23 + F_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(1100,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 14,
    label = "CFO + F2 <=> CF2O + F_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)