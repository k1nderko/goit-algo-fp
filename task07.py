import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(n_trials=1000000):
    """ Моделює кидки двох кубиків та обчислює ймовірності сум """
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(n_trials):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[dice_sum] += 1

    probabilities = {s: count / n_trials for s, count in sum_counts.items()}
    return probabilities

def theoretical_probabilities():
    """ Обчислює аналітичні ймовірності сум при киданні двох кубиків """
    outcomes = {i: 0 for i in range(2, 13)}

    for d1 in range(1, 7):
        for d2 in range(1, 7):
            outcomes[d1 + d2] += 1

    total_combinations = 6 * 6
    return {s: count / total_combinations for s, count in outcomes.items()}

monte_carlo_results = monte_carlo_simulation()
theoretical_results = theoretical_probabilities()

print("Сума | Монте-Карло | Теоретична")
print("-------------------------------")
for s in range(2, 13):
    print(f"{s:4} | {monte_carlo_results[s]:.4f}   | {theoretical_results[s]:.4f}")

# Візуалізація результатів
plt.figure(figsize=(10, 5))
plt.bar(monte_carlo_results.keys(), monte_carlo_results.values(), alpha=0.6, label="Монте-Карло", color='blue')
plt.plot(theoretical_results.keys(), theoretical_results.values(), "ro-", label="Теоретична", markersize=8)
plt.xlabel("Сума на двох кубиках ")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло vs Теоретична)")
plt.legend()
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle="--", alpha=0.6)
plt.show()