from src.equationsAndVariables import *
from src.newton import *
from src.track import *

# xStartPos = int(len(track1) / 2)

xStartPos = 0
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
    if type(_V_l) is list:
        timeGuess = (radius * theta) / _V_l[_ySegment]  # if v = d/t, then t = d/v. time given no input
        tActual = nextT(timeGuess, func_t, func_dt, alpha, beta, gamma, delta, iterVal, radius, theta, _V_l[0], mu_f,
                        mu_a,
                        mu_d, m, g)
    else:
        timeGuess = (radius * theta) / _V_l
        tActual = nextT(timeGuess, func_t, func_dt, alpha, beta, gamma, delta, iterVal, radius, theta, _V_l, mu_f, mu_a,
                        mu_d, m, g)
    newSpeed = newfinalspeed(radius, theta, tActual)
    return tActual, newSpeed, radius


def selectOptimalTime(_calcsteptime, x_init, x_pot, _ySegment, _V_l, iterVal, _track):
    timeUp, timeDown, timeCenter = float('inf'), float('inf'), float('inf')
    newSpeedD, newSpeedC, newSpeedU = float('inf'), float('inf'), float('inf')
    timeCenter, newSpeedC, rad1 = _calcsteptime(_track, x_init, x_pot[1], _ySegment, _V_l, iterVal)
    timeCenter, newSpeedC, rad1 = _calcsteptime(_track, x_init, x_pot[1], _ySegment, maxSpeed(rad1), iterVal)
    if x_pot[0] >= 0:
        timeUp, newSpeedU, rad2 = _calcsteptime(_track, x_init, x_pot[0], _ySegment, _V_l, iterVal)
        timeUp, newSpeedU, rad2 = _calcsteptime(_track, x_init, x_pot[0], _ySegment, maxSpeed(rad2), iterVal)
    if x_pot[2] < len(track1):
        timeDown, newSpeedD, rad3 = _calcsteptime(_track, x_init, x_pot[2], _ySegment, _V_l, iterVal)
        timeDown, newSpeedD, rad3 = _calcsteptime(_track, x_init, x_pot[2], _ySegment, maxSpeed(rad3), iterVal)
    print(timeUp, timeCenter, timeDown)
    if timeUp < timeCenter and timeUp < timeDown:
        return timeUp, x_init - 1, newSpeedU
    elif timeCenter < timeUp and timeCenter < timeDown:
        return timeCenter, x_init, newSpeedC
    elif timeDown < timeUp and timeDown < timeCenter:
        return timeDown, x_init + 1, newSpeedD
    else:
        return timeCenter, x_init, newSpeedC


def newfinalspeed(rad, theta, deltaT):
    return (rad * theta) / deltaT


def maxSpeed(r):
    speed = ((mu_f * m * g) / ((m / r) - (mu_f * mu_a))) ** 0.5
    print("Max Speed: " + str(speed))
    return speed


def flipTrack(_yIndex, _xIndex):
    if _yIndex == 21:
        return abs(_xIndex - 8)
    return _xIndex


def increment(_xHistory, _xStartPos, _V_list, _v_temp, _laptime, dt, _y_seg):
    if _y_seg < 21:
        _xHistory.append(_xStartPos)
    else:
        _xHistory.append(abs(8 - _xStartPos))
    _V_list.append(_v_temp)
    return _laptime + dt, _y_seg + 1
