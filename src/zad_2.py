from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def m_t(t):
    return t / 5


def calculate_integral(t, m_t: Callable[[float], float]):
    # Integrate m(t) from 0 to T
    return integrate.quad(m_t, 0, t)[0]


def generate_times(T, m_t: Callable[[float], float]):
    m_T = calculate_integral(T, m_t)
    N_T = np.random.poisson(m_T)
    event_times = []
    num = 0
    while num < N_T:
        t = T * np.random.rand()
        u = np.random.rand()
        acceptance_prob = calculate_integral(t, m_t) / m_T
        if u < acceptance_prob:
            event_times.append(t)
            num += 1
    event_times.sort()
    return event_times


T = 15
event_times = generate_times(T, m_t=m_t)

# plt.step(event_times, np.arange(1, len(event_times) + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation (λ(t) = t/5)\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')


def plot_await(times, T, m_t):
    waiting_times = np.diff(times)
    times = np.linspace(0, T, 1000)
    acceptance_probs = [
        calculate_integral(t, m_t) / calculate_integral(T, m_t) for t in times
    ]

    plt.hist(
        waiting_times, bins=40, density=True, alpha=0.6, color="g", label="Await times"
    )
    plt.plot(times, acceptance_probs, "r-", lw=2, label="Acceptance dist")
    plt.xlabel("Await Time")
    plt.ylabel("Density")
    plt.legend()
    plt.show()


# plot_await(event_times, T, m_t)
