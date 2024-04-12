import matplotlib.pyplot as plt

def leader_rounds(n):
    if n == 1:
        return 1
    else:
        return 1 + (1 - 1/n) * leader_rounds(n-1)

n_values = list(range(1, 101))
l_values = [leader_rounds(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, l_values, marker='o', linestyle='-', color='b')
plt.title('Average number of rounds needed to elect a leader')
plt.xlabel('Number of people n')
plt.ylabel('Average number of rounds L(n)')
plt.grid(True)
plt.show()
