from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def get_lam(t: int):
    return np.cos(t) + 1


def get_dist(t: int):
    return np.sin(t) + t


def get_times(T: int, get_dist: Callable[[float], float]):
    times = []
    t, idx = 0, 0
    T = 15
    while True:
        U_1 = np.random.uniform(0, 1)
        tau = get_dist(U_1)
        t = t + tau
        if t > T:
            break
        idx += 1
        times.append(t)
    return times


T = 15
times = get_times(T=T, get_dist=get_dist)

# plt.step(times, np.arange(1, len(times) + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation (λ(t) = cos(t)+1)\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')
