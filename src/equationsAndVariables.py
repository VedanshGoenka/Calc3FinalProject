import math

mu_f = 1.7
mu_d = 0.128311639  # Averaged val calc from https://commons.erau.edu/cgi/viewcontent.cgi?article=1003&context=aiaar2sc
mu_a = 0.150358519  # Averaged val calc from https://commons.erau.edu/cgi/viewcontent.cgi?article=1003&context=aiaar2sc
m = 905 * 1000  # 905kg https://www.autoweek.com/racing/formula-1/a38695541/why-f1-cars-2022-heaviest-hybrid-era/
g = 9.8067  # 9.8067 m/s

pi = math.pi
e = math.e

V_o = 100 / 3.6  # 100 km/h --> m/s


def alpha(r, theta, V_x):
    return V_x / (r * theta)


def beta(r, _mu_f, _mu_a, _mu_d, m):
    return (_mu_f * _mu_a * _mu_d * r) / (m ** 2)


def gamma(r, theta, m, g, _mu_a):
    return (-1 * m * g) / (_mu_a * r * theta)


def delta(r, theta, m, _mu_d, _mu_f, _mu_a):
    return ((m * r * theta * _mu_d) + (m ** 2)) / (_mu_f * _mu_a * _mu_d * r)


def func_t(t, a, b, c, d):
    return a * (t ** 2) * (e ** (-b * t)) + ((1 - (e ** (-b * t))) * ((c * t ** 2) + d)) - t


def func_dt(t, a, b, c, d):
    return (e ** (-b * t)) * ((((2 * c) - 1) * e ** (b * t)) + (((c - a) * ((b * t) - 2) * t) + b * d))
