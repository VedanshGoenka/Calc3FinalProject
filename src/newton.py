t_estimate = int()


def nextT(t_est, f, f_prime, a, b, c, d, iterations, r, theta, V_x, mu_f, mu_a, mu_d, m, g):
    for x in range(iterations):
        t_est += f(t_est,
                   a(r, theta, V_x),
                   b(r, mu_f, mu_a, mu_d, m),
                   c(r, theta, m, g, mu_a),
                   d(r, theta, m, mu_d, mu_f, mu_a)) \
                 / f_prime(t_est,
                           a(r, theta, V_x),
                           b(r, mu_f, mu_a, mu_d, m),
                           c(r, theta, m, g, mu_a),
                           d(r, theta, m, mu_d, mu_f, mu_a))
    return t_est[0]
