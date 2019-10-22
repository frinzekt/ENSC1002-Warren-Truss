# %%[markdown]
"""# Reaction Equivalence From RA to LL and DL
# By Frinze
"""

# %%
import scipy as sci
import sympy as sp
import math
from IPython.display import display


LL, DL, ANGLE = sp.symbols('F_{L} F_{D} 45')
# ANGLE = math.radians(45)

RI = (DL*30+LL*40)/(80)
RA = DL + LL - RI

display(sp.Eq(sp.S("F_RA"), RA))
display(sp.Eq(sp.S("F_RI"), RI))

# %%
# Member Definition
AJ = -RA / sp.sin(ANGLE)
AB = RA

display(sp.Eq(sp.S("F_AJ"), AJ))
display(sp.Eq(sp.S("F_AB"), AB))

BJ = 0
BC = RA

display(sp.Eq(sp.S("F_BJ"), BJ))
display(sp.Eq(sp.S("F_BC"), BC))

JC = RA / sp.sin(ANGLE)
JK = -2 * RA

display(sp.Eq(sp.S("F_JC"), JC))
display(sp.Eq(sp.S("F_JK"), JK))

KC = 0
KL = -2 * RA

display(sp.Eq(sp.S("F_KC"), KC))
display(sp.Eq(sp.S("F_KL"), KL))

CL = -RA / sp.sin(ANGLE)
CD = 3 * RA

display(sp.Eq(sp.S("F_CL"), CL))
display(sp.Eq(sp.S("F_CD"), CD))

# Dj = DL
DE = 3 * RA

# display(sp.Eq(sp.S("F_DL"), DL))
display(sp.Eq(sp.S("F_DE"), DE))

LE = (RA - DL) / sp.sin(ANGLE)
LM = -4 * RA + DL

display(sp.Eq(sp.S("F_LE"), LE))
display(sp.Eq(sp.S("F_LM"), LM))

ME = 0
MN = -4 * RA + DL

display(sp.Eq(sp.S("F_ME"), ME))
display(sp.Eq(sp.S("F_MN"), MN))

EN = (-RA + DL) / sp.sin(ANGLE)
EF = 5 * RA - (LL + 2 * DL)

display(sp.Eq(sp.S("F_EN"), EN))
display(sp.Eq(sp.S("F_EF"), EF))

FN = 0
FG = 5 * RA - (LL + 2 * DL)

display(sp.Eq(sp.S("F_FN"), FN))
display(sp.Eq(sp.S("F_FG"), FG))

NG = (RA - (LL+DL)) / sp.sin(ANGLE)
NO = -6 * RA + (2 * LL + 3 * DL)

display(sp.Eq(sp.S("F_NG"), NG))
display(sp.Eq(sp.S("F_NO"), NO))

OG = 0
OP = -6 * RA + (2 * LL + 3 * DL)

display(sp.Eq(sp.S("F_OG"), OG))
display(sp.Eq(sp.S("F_OP"), OP))

GP = (-RA + (LL+DL)) / sp.sin(ANGLE)
GH = 7 * RA - (3 * LL + 4 * DL)

display(sp.Eq(sp.S("F_GP"), GP))
display(sp.Eq(sp.S("F_GH"), GH))

HP = 0
HI = 7 * RA - (3 * LL + 4 * DL)

display(sp.Eq(sp.S("F_HP"), HP))
display(sp.Eq(sp.S("F_HI"), HI))

PI = (RA - (LL + DL)) / sp.sin(ANGLE)

display(sp.Eq(sp.S("F_PI"), PI))

# %%
