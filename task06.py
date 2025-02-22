def greedy_algorithm(items, budget):
    """ Жадібний алгоритм: вибирає страви з найкращим співвідношенням калорій/вартість """
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    """ Алгоритм динамічного програмування для вибору страв з максимальною калорійністю """
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    selected_items.reverse()
    return selected_items, dp[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 80  

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

# Вивід результатів
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Сумарна калорійність:", greedy_result[1])

print("\nДинамічне програмування:")
print("Вибрані страви:", dp_result[0])
print("Сумарна калорійність:", dp_result[1])