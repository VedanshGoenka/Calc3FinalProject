from src.equationsAndVariables import *
from src.newton import *
from src.track import *

xStartPos = int(len(track1) / 2)
ySegment = 0
lapTime = 0

xPotential = list()
V_temp = 0
T_temp = 0

xHistory = [xStartPos]
V_list = [V_o]


def genXPot(xCenter):
    return [xCenter - 1, xCenter, xCenter + 1]


def calcsteptime(_track, x_init, x_fin, _ySegment, _V_l, iterVal):
    radius = (_track[x_init][_ySegment][0] + _track[x_fin][_ySegment][0]) / 2  # Average gives the r + dr/2
    theta = _track[x_init][_ySegment][1]
    timeGuess = (radius * theta) / _V_l[_ySegment]  # if v = d/t, then t = d/v. time given no input
    tActual = nextT(timeGuess, func_t, func_dt, alpha, beta, gamma, delta, iterVal, radius, theta, _V_l, mu_f, mu_a,
                    mu_d, m, g)
    newSpeed = newfinalspeed(radius, theta, tActual)
    print(timeGuess - tActual)
    return tActual, newSpeed


def selectOptimalTime(_calcsteptime, x_init, x_pot, _ySegment, _V_l, iterVal, _track):
    timeUp, timeDown, timeCenter = float('inf'), float('inf'), float('inf')
    timeCenter, newSpeed = _calcsteptime(_track, x_init, x_pot[1], _ySegment, _V_l, iterVal)
    if x_pot[0] >= 0:
        timeUp, newSpeed = _calcsteptime(_track, x_init, x_pot[0], _ySegment, _V_l, iterVal)
    if x_pot[2] < len(track1):
        timeDown, newSpeed = _calcsteptime(_track, x_init, x_pot[2], _ySegment, _V_l, iterVal)
    if timeUp < timeCenter and timeUp < timeDown:
        return timeUp, x_init - 1, newSpeed
    elif timeCenter < timeUp and timeCenter < timeUp:
        return timeCenter, x_init, newSpeed
    elif timeDown < timeUp and timeDown < timeCenter:
        return timeDown, x_init + 1, newSpeed
    else:
        return timeCenter, x_init, newSpeed


def newfinalspeed(rad, theta, deltaT):
    return (rad * theta) / deltaT


def increment(_xHistory, _xStartPos, _V_list, _v_temp, _laptime, dt, _y_seg):
    _xHistory.append(_xStartPos)
    _V_list.append(_v_temp)
    return _laptime + dt, _y_seg + 1
