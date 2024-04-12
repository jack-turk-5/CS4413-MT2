import numpy as np
import matplotlib.pyplot as plt

def generate_points(N):
    points = np.random.rand(N, 2)
    return points

def plot_points(points):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], marker='.')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('ui')
    plt.ylabel('vi')
    plt.title('N-pairs uniformly distributed in the unit square')
    plt.grid(True)
    plt.show()

def main():
    N = 10**3  # Number of pairs
    points = generate_points(N)
    plot_points(points)

if __name__ == "__main__":
    main()
