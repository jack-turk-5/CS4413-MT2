import math
import matplotlib.pyplot as plt

def stirling_approximation(n):
    return math.sqrt(2 * math.pi * n) * ((n / math.e) ** n)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n_values = list(range(2, 21))

errors = [factorial(n) - stirling_approximation(n) for n in n_values]
relative_errors = [errors[i] / factorial(n_values[i]) for i in range(len(n_values))]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(n_values, errors, marker='o')
plt.xlabel('n')
plt.ylabel('Error (e(n))')
plt.title('Error in Stirling\'s Approximation')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(n_values, relative_errors, marker='o', color='r')
plt.xlabel('n')
plt.ylabel('Relative Error (re(n))')
plt.title('Relative Error in Stirling\'s Approximation')
plt.grid(True)

plt.tight_layout()
plt.show()

# Comments on observations
print("Observations:")
print("- As n increases, the error in Stirling's approximation generally increases as well. This is expected because Stirling's approximation becomes less accurate for larger values of n.")
print("- The relative error decreases as n increases. This indicates that although the absolute error might be increasing, it is increasing at a slower rate compared to n!, resulting in a smaller relative error.")
print("- Overall, Stirling's approximation provides a good approximation for factorials, especially for larger values of n, but it's not perfect and the error increases as n gets larger.")

