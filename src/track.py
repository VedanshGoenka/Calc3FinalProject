import numpy as np

from src.equationsAndVariables import pi

dR = 1
rA = [10, 20, 30, 20, 10]
tA = [pi / 4, pi / 3, pi / 5, pi / 2.5, pi / 3.75]

track1 = np.array([
    [(rA[0] + 2 * dR, tA[0]), (rA[1] + 2 * dR, tA[1]), (rA[2] + 2 * dR, tA[2]), (rA[3] + 2 * dR, tA[3]),
     (rA[4] + 2 * dR, tA[4])],
    [(rA[0] + dR, tA[0]), (rA[1] + dR, tA[1]), (rA[2] + dR, tA[2]), (rA[3] + dR, tA[3]), (rA[4] + dR, tA[4])],
    [(rA[0], tA[0]), (rA[1], tA[1]), (rA[2], tA[2]), (rA[3], tA[3]), (rA[4], tA[4])],
    [(rA[0] - dR, tA[0]), (rA[1] - dR, tA[1]), (rA[2] - dR, tA[2]), (rA[3] - dR, tA[3]), (rA[4] - dR, tA[4])],
    [(rA[0] - 2 * dR, tA[0]), (rA[1] - 2 * dR, tA[1]), (rA[2] - 2 * dR, tA[2]), (rA[3] - 2 * dR, tA[3]),
     (rA[4] - 2 * dR, tA[4])]
])

