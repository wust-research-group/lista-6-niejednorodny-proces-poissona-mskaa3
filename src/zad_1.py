import matplotlib.pyplot as plt
import numpy as np


def get_lam(t):
    return np.cos(t) + 1


def get_times(lam, T):
    times = []
    t, idx = 0, 0
    lam = 2
    T = 15
    while True:
        U_1 = np.random.uniform(0, 1)
        t = t - (1 / lam) * np.log(U_1)
        if t > T:
            break
        U_2 = np.random.uniform(0, 1)
        if U_2 <= get_lam(t) / lam:
            idx += 1
            times.append(t)
    times.sort()
    return times


lam = 2
times = get_times(2, 15)

# plt.step(times, np.arange(1, len(times) + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation (λ = {lam}, λ(t) = cos(t)+1 )\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')
