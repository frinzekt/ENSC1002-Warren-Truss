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
# F_EL


class Line:
    def __init__(self, name, m, c):
        self.name = name
        self.m = m
        self.c = c

    def addLine(self, otherline):
        self.m = otherline.m
        self.c = otherline.c

    def printLine(self):
        print(self.name, " m:", str(self.m), "c:", str(self.c))

    def multiply(self, x):
        self.m = np.round


def drawLine(m, c, header, ylabel, xlabel):  # y = mx + c
    x = np.arange(50)
    y = m * x + c
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set(title=header, ylabel=ylabel, xlabel=xlabel)

    plt.savefig('')
    plt.show()


# Definition of Reaction Forces
RA = Line("Reaction Force at A", 15 / 2, 1 / 2)
RA.printLine()

RI = Line("Reaction Force At I", 25 / 2, 1 / 2)
RI.printLine()

#Line Definitions of Members


# %%
