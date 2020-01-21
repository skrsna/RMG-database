#!/usr/bin/env python
# encoding: utf-8

name = "api_small_rads"
shortDesc = ""
longDesc = """
Various small radical reactions relevant to API oxidation
"""

entry(
    index=0,
    label="AIBN <=> N2 + cyanoisopropyl + cyanoisopropyl",
    kinetics=Arrhenius(A=(5.40379e+15, 's^-1'), n=0, Ea=(132.417, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(363.6, 'K'), Tmax=(380.2, 'K')),
    shortDesc=u"""Juang 1992""",
    longDesc=
    u"""
Measured
Fig 4, k
R-S Juang, J-F Lianf, J. Chem. Tech. Biotechnol. 1992, 55, 379-383, doi: 10.1002/jctb.280550413

Another source:
    kinetics=Arrhenius(A=(2.14e+17, 's^-1'), n=0, Ea=(143, 'kJ/mol'), T0=(1, 'K')),
P.S. Eagel, Mechanism of the thermal and photochemical decomposition of azoalkanes
Chem. Rev. 1980, 80, 99-150

Juang is ~x2 faster than Eagel at the relevant temperatures
""",
)

entry(
    index=1,
    label="cyanoisopropyl + O2 <=> cyanoisopropylOO",
    kinetics=Arrhenius(A=(5.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc=u"""R_Recombination (RMG-Py rate rules)""",
    longDesc=
    u"""
""",
)

entry(
    index=2,
    label="cyanoisopropylOO + CH3OH <=> cyanoisopropylOOH + CH2OH",
    kinetics=Arrhenius(A=(0.234766, 'cm^3/(mol*s)'), n=3.50344, Ea=(25.4103, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
                       Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.05474, dn = +|- 0.00777691, 
                       dEa = +|- 0.0221566 kJ/mol"""),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
    CO[O] + CH3OH <=> COOH + CH2OH
    NOx2018 has a different value Arrhenius(A=(4.0e+13, 'cm^3/(mol*s)'), n=0, Ea=(19.40, 'kcal/mol'), T0=(1, 'K'))
""",
)

entry(
    index=3,
    label="cyanoisopropylOO + CH3OH <=> cyanoisopropylOOH + CH3O",
    kinetics=Arrhenius(A=(1.89162e-06, 'cm^3/(mol*s)'), n=5.47458, Ea=(64.6665, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
                       Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.14859, dn = +|- 0.0202144, dEa 
                       = +|- 0.0575912 kJ/mol"""),
    shortDesc=u"""H_abstraction""",
    longDesc=
    u"""
    CO[O] + CH3OH <=> COOH + CH3[O]
    H_abstraction has a different value Arrhenius(A=(1.17e-2, 'cm^3/(mol*s)'), n=4.29, Ea=(32.92, 'kcal/mol'),
    T0=(1, 'K'))
""",
)

entry(
    index=4,
    label="CH3OH + HO2 <=> CH2OH + H2O2",
    kinetics=Arrhenius(A=(3.5e-4, 'cm^3/(mol*s)'), n=4.85, Ea=(10.35, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=5,
    label="CH3OH + HO2 <=> CH3O + H2O2",
    kinetics=Arrhenius(A=(1.5e-3, 'cm^3/(mol*s)'), n=4.61, Ea=(15.93, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=6,
    label="CH3OH + OH <=> CH2OH + H2O",
    kinetics=Arrhenius(A=(1.5e+8, 'cm^3/(mol*s)'), n=1.44, Ea=(0.11, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""Klippenstein_Glarborg2016""",
    longDesc=
    u"""
""",
)

entry(
    index=7,
    label="CH3OH + OH <=> CH3O + H2O",
    kinetics=Arrhenius(A=(2.7e+7, 'cm^3/(mol*s)'), n=1.44, Ea=(0.11, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=8,
    label="CH3OH + CH3O <=> CH2OH + CH3OH",
    kinetics=Arrhenius(A=(3.0e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.07, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
    longDesc=
    u"""
""",
)

entry(
    index=9,
    label="CH3O + O2 <=> CH2O + HO2",
    kinetics=Arrhenius(A=(0.48, 'cm^3/(mol*s)'), n=3.57, Ea=(1.05, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=10,
    label="CH2OH + O2 <=> CH2O + HO2",
    kinetics=MultiArrhenius(
        arrhenius=[
            Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(3736, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+16, 'cm^3/(mol*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K'))]),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index = 11,
    label = "OOCH2OH <=> CH2OH + O2",
    kinetics = Arrhenius(A=(2.0e+15,'s^-1'), n=0, Ea=(35.8,'kcal/mol'), T0=(1,'K')),
    longDesc =
u"""
We get the following sequence of reactions because of the high CH3OH concentration:
1. CH3OO + CH3OH = CH3OOH + CH2OH
2. CH2OH + O2 = OOCH2OH
3.  OOCH2OH + API = HOOCH2OH + API_rad

We have a bad rate estimate for reaction 2, this entry tries to fix it.
Taken from: T.S. Dibble, Mechanism and dynamics of the CH2OH + O2 reaction, Chem. Phys. Lett. 2002, 355, 193-200
doi: 10.1016/S0009-2614(02)00211-7
""",
)

entry(
    index=12,
    label="CH3OO + O <=> CH3O + O2",
    kinetics=Arrhenius(A=(2.9e+10, 'cm^3/(mol*s)'), n=1.0, Ea=(0.72, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=13,
    label="OHCH2OO <=> OCH2OOH",
    kinetics=Arrhenius(A=(3.0e+11, 's^-1'), n=0, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
    longDesc=
    u"""
""",
)

entry(
    index=14,
    label="OHCH2OO <=> CH2O + HO2",
    kinetics=Arrhenius(A=(6.38e+12, 's^-1'), n=0, Ea=(29.45, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u""" """,
    longDesc=
    u"""
Hermans et al. 2005 (doi:10.1021/jp044080v) G2M calculations
Training reaction in HO2_Elimination_from_PeroxyRadical 
""",
)

entry(
    index=15,
    label="OHCH2OOH <=> CH2O + H2O2",
    kinetics=Arrhenius(A=(3.16e+11, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc=u""" """,
    longDesc=
    u"""
Used an estimated rate for the reverse of 1e+13 cm^3/(mol*s)
reversed using DFT_QCI_thermo thermo
""",
)

entry(
    index=16,
    label="cyanoisopropyl + CH3OH <=> cyanoisopropane + CH2OH",
    kinetics=Arrhenius(A=(1.20521e-20, 'cm^3/(mol*s)'), n=9.67402, Ea=(28.0373, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
                       Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.79835, dn = +|- 0.0856346, 
                       dEa = +|- 0.243975 kJ/mol"""),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
    C[C](C#N)C + CO <=> CC(C#N)C + [CH2]O
""",
)

entry(
    index=17,
    label="cyanoisopropyl + CH3OH <=> cyanoisopropane + CH3O",
    kinetics=Arrhenius(A=(0.109341, 'cm^3/(mol*s)'), n=3.92562, Ea=(66.4122, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
                       Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.01558, dn = +|- 0.00225605, 
                       dEa = +|- 0.00642752 kJ/mol"""),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
    C[C](C#N)C + CO <=> CC(C#N)C + C[O]
""",
)

entry(
    index=18,
    label="cyanoisopropylOO <=> cyclic_cyanoisopropylOO",
    kinetics=Arrhenius(A=(1e-30, 's^-1'), n=0, Ea=(1000, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
forbidding this reaction in Intra_R_Add_Endocyclic didn't work, assigning here a low rate instead
""",
)

entry(
    index=19,
    label="iC3H6CNOO <=> cyclic_cyanoisopropylOO",
    kinetics=Arrhenius(A=(1e-20, 's^-1'), n=0, Ea=(100, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
""",
)

entry(
    index=20,
    label="CH2O + H2O <=> OHCH2OH",
    kinetics=Arrhenius(A=(3.67e+06, 'cm^3/(mol*s)'), n=0, Ea=(5.83, 'kcal/mol'), T0=(1, 'K'), Tmin=(285, 'K'), Tmax=(345, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
J.G.M. Winkelman, O.K. Voorwinde, M. Ottens, A.A.C.M. Beenackers, L.P.B.M. Janssen
Chemical Engineering Science, Volume 57, Issue 19, October 2002, Pages 4067-4076
https://doi.org/10.1016/S0009-2509(02)00358-5
The original rate was multiplied by 18 cm3/mol to convert units into a second order reaction.
""",
)
