items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Створюємо таблицю для динамічного програмування
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [item]

    max_calories = max(dp)
    selected_items = item_selection[dp.index(max_calories)]

    return selected_items, max_calories, sum(items[item]['cost'] for item in selected_items)

# Приклад використання функцій
budget = 100
print("Жадібний алгоритм:")
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Обрані найменування: {selected_items}")
print(f"Всього калорій: {total_calories}")
print(f"Загальна ціна: {total_cost}")

print("\nАлгоритм динамічного програмування:")
selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print(f"Обрані найменування: {selected_items}")
print(f"Всього калорій: {total_calories}")
print(f"Загальна ціна: {total_cost}")
