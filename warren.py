# %%
import numpy as np
import matplotlib.pyplot as plt

COMP_ROUND = 10
OUT_ROUND = 2

# Dimensions
X_LENGTH = 10
Y_LENGTH = 10
ANGLE = np.radians(45)

# Define CONSTANTS
F_DL = 20
X_DL = 3 * X_LENGTH
X_LL = 4 * X_LENGTH
# F_EL


def drawLine(m, c, header, ylabel, xlabel):  # y = mx + c
    x = np.arange(50)
    y = m * x + c
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set(title=header, ylabel=ylabel, xlabel=xlabel)

    plt.savefig('')
    plt.show()


# Definition of Members and Forces [m,c]
RA = np.array([F_DL * X_DL, X_LL]) / (X_LENGTH*8)
print("RA", RA)

RI = np.array([F_DL, 1])
RI = RI - RA
print("RI", RI)

# Member Definition
AJ = -RA / np.sin(ANGLE)
AB = RA

BJ = 0
BC = RA

JC = RA / np.sin(ANGLE)
JK = -2*RA

KC = np.zeros((1, 2))
KL = -2 * RA

CL = -RA / np.sin(ANGLE)
CD = 3 * RA

DL = np.array([20, 0])
DE = 3 * RA

LE = (RA - np.array([20, 0])) / np.sin(ANGLE)
LM = -4 * RA + np.array([20, 0])

ME = np.zeros((1, 2))
MN = -4 * RA + np.array([20, 0])

EN = (-RA + np.array([20, 1])) / np.sin(ANGLE)
EF = 5 * RA - np.array([40, 1])

FN = np.zeros((1, 2))
FG = 5 * RA - np.array([40, 1])

NG = (RA - np.array([20, 0])) / np.sin(ANGLE)
NO = -6 * RA + np.array([60, 2])

OG = np.zeros((1, 2))
OP = -6 * RA + np.array([60, 2])

GP = (-RA + np.array([20, 1])) / np.sin(ANGLE)
GH = 7 * RA - np.array([80, 3])

HP = np.zeros((1, 2))
HI = 7 * RA - np.array([80, 3])

PI_1 = (RA - np.array([20, 0])) / np.sin(ANGLE)
PI_2 = (-7 * RA + np.array([80, 3])) / np.cos(ANGLE)

memberName = ["AJ", 'AB', 'BJ', 'BC', 'JC', 'JK', 'KC', 'KL', 'CL', 'CD', 'DL', 'DE', 'LE',
              'LM', 'ME', 'MN', 'EN', 'FN', 'FG', 'NG', 'NO', 'OG', 'OP', 'GP', 'GH', 'HP', 'HI', 'PI']
# %%

