import matplotlib.pyplot as plt
import numpy as np

from zad_2 import generate_times


def f_1(t: float):
    return t**2


def f_2(t: float):
    return t / 10


def comb(t: float):
    return f_1(t) + f_2(t)


T = 15
times_1 = generate_times(T, f_1)
times_2 = generate_times(T, f_2)
times_combined = generate_times(T, comb)

times = times_1 + times_2
times.sort()

# plt.step(times, np.arange(1, len(times) + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')


# fig, axs = plt.subplots(2, 1, figsize=(8, 10))
# time_diffs=np.diff(times)
# axs[0].hist(time_diffs, bins=50, density=True, alpha=0.6, color='b')
# axs[0].set_title('Combination of two processes')
# axs[0].set_xlabel('await time')
# axs[0].set_ylabel('Density')
# time_diffs_combined=np.diff(times_combined)
# axs[1].hist(time_diffs_combined, bins=50, density=True, alpha=0.6, color='g')
# axs[1].set_title('Process with combined lambda functions')
# axs[1].set_xlabel('await time')
# axs[1].set_ylabel('Density')

# plt.tight_layout()
# plt.show()
