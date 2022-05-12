import math

mu_f = 1
mu_d = 1
mu_a = 1
m = 1
g = 1

pi = math.pi
e = math.e


def alpha(r, theta, V_x):
    return V_x / (r * theta)


def beta(r, mu_f, mu_a, mu_d, m):
    return (mu_f * mu_a * mu_d * r) / (m ** 2)


def gamma(r, theta, m, g, mu_a):
    return (-1 * m * g) / (mu_a * r * theta)


def delta(r, theta, m, mu_d, mu_f, mu_a):
    return ((m * r * theta * mu_d) + (m ** 2)) / (mu_f * mu_a * mu_d * r)


def func_t(t, a, b, c, d):
    return a * (t ** 2) * (e ** (-b * t)) + ((1 - (e ** (-b * t))) * ((c * t ** 2) + d)) - t


def func_dt(t, a, b, c, d):
    return (e ** (-b * t)) * ((((2 * c) - 1) * e ** (b * t)) + (((c - a) * ((b * t) - 2) * t) + b * d))
