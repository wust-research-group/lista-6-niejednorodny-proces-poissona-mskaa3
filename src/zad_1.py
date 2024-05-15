import matplotlib.pyplot as plt
import numpy as np


def get_lam(t: float):
    return np.cos(t) + 1


def get_times(lam: float, T: int):
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
    return times


lam = 2
T = 15
times = get_times(lam, T)

# plt.step(times, np.arange(1, len(times) + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation (λ = {lam}, λ(t) = cos(t)+1 )\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')


# check
def plot_await(times, lam):
    interarrival_times = np.diff(times)
    plt.hist(
        interarrival_times,
        bins=40,
        density=True,
        alpha=0.6,
        color="g",
        label="Await times",
    )

    x = np.linspace(0, np.max(interarrival_times), 100)
    y = lam * np.exp(-lam * x)
    plt.plot(x, y, "r-", lw=2, label=f"Poisson (λ={lam})")

    plt.xlabel("Await time")
    plt.ylabel("Density")
    plt.legend()
    plt.show()


# plot_await(times, lam)
