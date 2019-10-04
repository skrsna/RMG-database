#!/usr/bin/env python
# encoding: utf-8

name = "XY-Addition_DoubleBond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

# entry(
#     index = 0,
#     label = "CH3-CH2F <=> C2H4 + HF",
#     degeneracy = 1.0,
#     kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.83e+13,'s^-1'), n=0, Ea=(59900,'cal/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(8.7e+68,'cm^3/(mol*s)'), n=-14.94, Ea=(75710,'cal/mol'), T0=(1,'K')), alpha=0.652, T3=(10,'K'), T1=(1496,'K'), efficiencies={'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C-]#[O+]': 1.5, '[Ar]': 0.7}),
#     rank = 10,
#     shortDesc = u"""From NIST CH2F2 model""",
# )

entry(
    index = 1,
    label = "CH3-CHF2 <=> CH2CHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+13,'s^-1'), n=0, Ea=(61900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 2,
    label = "CH3-CF3 <=> CH2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'s^-1'), n=0, Ea=(68700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 3,
    label = "CH2F-CH2F <=> CH2CHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(62900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 4,
    label = "CH2F-CHF2 <=> CHFCHF[Z] + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+14,'s^-1'), n=0, Ea=(69100,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 5,
    label = "CH2F-CHF2 <=> CH2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(65400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 6,
    label = "CH2F-CF3 <=> CHFCF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.63e+13,'s^-1'), n=0, Ea=(70700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 7,
    label = "CHF2-CHF2 <=> CHFCF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(69400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)

entry(
    index = 8,
    label = "CHF2-CF3 <=> CF2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(71600,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = u"""From NIST CH2F2 model""",
)