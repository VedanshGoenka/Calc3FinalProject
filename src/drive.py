import math

from src.equationsAndVariables import *
from src.newton import *
from src.track import *

xStartPos = int(len(track) / 2)
xPotential = list()
    [xStartPos - 1, xStartPos, xStartPos + 1]
ySegment = 0
V_l = 200
laptime = 0

def genXPot(xCenter):
    return [xCenter - 1, xCenter, xCenter + 1]


def calcsteptime(_track, x_init, x_fin, _ySegment, _V_l, iterVal):
    radius = (_track[x_init][_ySegment][0] + _track[x_fin][_ySegment][0]) / 2  # Average gives the r + dr/2
    theta = _track[x_init][_ySegment][1]
    timeGuess = (radius * theta) / _V_l  # if v = d/t, then t = d/v. time given no input
    tActual = nextT(timeGuess, func_t, func_dt, alpha, beta, gamma, delta, iterVal, radius, theta, _V_l, mu_f, mu_a,
                    mu_d, m, g)
    newSpeed = newfinalspeed(radius, theta, tActual)
    print(timeGuess - tActual)
    return tActual, newSpeed


def selectOptimalTime(_calcsteptime, x_init, x_pot, _ySegment, _V_l, iterVal, _track):
    timeCenter, newSpeed = _calcsteptime(_track, x_init, x_pot[1], _ySegment, _V_l, iterVal)
    if x_pot[0] >= 0:
        timeUp, newSpeed = _calcsteptime(_track, x_init, x_pot[0], _ySegment, _V_l, iterVal)
    if x_pot[2] < len(track):
        timeDown, newSpeed = _calcsteptime(_track, x_init, x_pot[2], _ySegment, _V_l, iterVal)
    if timeUp < timeCenter and timeUp < timeDown:
        return timeUp, x_init - 1
    elif timeCenter < timeUp and timeCenter < timeUp:
        return timeCenter, x_init, newSpeed
    elif timeDown < timeUp and timeDown < timeCenter:
        return timeDown, x_init + 1, newSpeed
    else:
        return timeCenter, x_init, newSpeed


def newfinalspeed(rad, theta, deltaT):
    return (rad * theta) / deltaT
