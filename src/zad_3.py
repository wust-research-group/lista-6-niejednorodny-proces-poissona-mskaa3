import matplotlib.pyplot as plt
import numpy as np

from zad_2 import get_times


# lambda t = cos(t) + 1
def dist_1(t: float):
    return np.sin(t) + t


# lambda t = 1/2t + 1
def dist_2(t: float):
    return 0.25 * t**2 + t


T = 15
times_1 = get_times(T, dist_1)
times_2 = get_times(T, dist_2)

times = times_1 + times_2
times.sort()

# plt.step(times, np.arange(1, len(times) + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation (λ_1(t) = cos(t)+1, λ_2(t) = 0.5*t+1)\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')
