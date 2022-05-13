import numpy as np

from src.equationsAndVariables import pi

# First corner from Saudi Arabia GP

dR = 1.722
dRTotal = 9
rA = [20.41800] * 20
tA = [0.080372412] * len(rA)


def track(_dR, _dRTotal, _rA, _tA):
    trackA = [[(0, 0) for i in range(len(_rA))] for i in range(_dRTotal)]
    middleRow = int(_dRTotal / 2)
    for r in range(len(trackA)):
        for c in range(len(trackA[0])):
            trackA[r][c] = (_rA[c] + ((middleRow - r) * _dR), _tA[c])
    return trackA


track1 = track(dR, dRTotal, rA, tA)

# deprecated
# trackRandom = np.array([
#     [(rA[0] + 2 * dR, tA[0]), (rA[1] + 2 * dR, tA[1]), (rA[2] + 2 * dR, tA[2]), (rA[3] + 2 * dR, tA[3]),
#      (rA[4] + 2 * dR, tA[4])],
#     [(rA[0] + dR, tA[0]), (rA[1] + dR, tA[1]), (rA[2] + dR, tA[2]), (rA[3] + dR, tA[3]), (rA[4] + dR, tA[4])],
#     [(rA[0], tA[0]), (rA[1], tA[1]), (rA[2], tA[2]), (rA[3], tA[3]), (rA[4], tA[4])],
#     [(rA[0] - dR, tA[0]), (rA[1] - dR, tA[1]), (rA[2] - dR, tA[2]), (rA[3] - dR, tA[3]), (rA[4] - dR, tA[4])],
#     [(rA[0] - 2 * dR, tA[0]), (rA[1] - 2 * dR, tA[1]), (rA[2] - 2 * dR, tA[2]), (rA[3] - 2 * dR, tA[3]),
#      (rA[4] - 2 * dR, tA[4])]
# ])
