import numpy as np
import matplotlib.pyplot as plt

def catalan(n):
    if n == 0:
        return 1
    else:
        catalan_nums = np.zeros(n+1)
        catalan_nums[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                catalan_nums[i] += catalan_nums[j] * catalan_nums[i-j-1]
        return catalan_nums[n-1]

def parenthesizing_count(n):
    return catalan(n-1)

n_values = np.arange(2, 21)
parenthesizing_counts = [parenthesizing_count(n) for n in n_values]

plt.plot(n_values, parenthesizing_counts, marker='o')
plt.xlabel('n')
plt.ylabel('P(n)')
plt.title('Number of Ways of Parenthesizing vs Number of Atoms')
plt.grid(True)
plt.show()
