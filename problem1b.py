import numpy as np
import matplotlib.pyplot as plt

def generate_points(N):
    points = np.random.rand(N, 2)
    return points

def estimate_pi_4(N):
    points = generate_points(N)
    inside = 0

    for point in points:
        if point[0] ** 2 + point[1] ** 2 <= 1:
            inside += 1

    return inside / N

samples = [10**3, 10**4, 10**5, 10**6]
pi_4_estimates = [estimate_pi_4(N) for N in samples]
plt.plot(samples, pi_4_estimates, marker='o')
plt.xlabel('N')
plt.ylabel('Pi/4 Estimate')
plt.title('Pi/4 Estimates vs N')
plt.xscale('log')
plt.show()