t_estimate = int()


def nextT(t_est, f, f_prime, alpha, beta, gamma, delta, iterations, r, theta, V_x, mu_f, mu_a, mu_d, m, g):
    for x in range(iterations):
        t_est += f(t_est,
                   alpha(r, theta, V_x),
                   beta(r, mu_f, mu_a, mu_d, m),
                   gamma(r, theta, m, g, mu_a),
                   delta(r, theta, m, mu_d, mu_f, mu_a)) \
                 / f_prime(t_est,
                           alpha(r, theta, V_x),
                           beta(r, mu_f, mu_a, mu_d, m),
                           gamma(r, theta, m, g, mu_a),
                           delta(r, theta, m, mu_d, mu_f, mu_a))
    return t_est
