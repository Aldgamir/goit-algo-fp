import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_dice = die1 + die2
        sum_counts[sum_dice] += 1

    probabilities = {sum_val: count / num_rolls for sum_val, count in sum_counts.items()}
    return probabilities

def main():
    num_rolls = 1000000  # Дуже велика кількість кидків...
    probabilities = simulate_dice_rolls(num_rolls)
    
    analytical_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    
    # Виведення результатів
    print("Сума\tІмовірність (симуляція)\tІмовірність (аналітична)")
    for sum_val in range(2, 13):
        print(f"{sum_val}\t{probabilities[sum_val]:.4f}\t\t\t{analytical_probabilities[sum_val]:.4f}")
    
    # Побудова графіка
    sums = list(range(2, 13))
    sim_probs = [probabilities[sum_val] for sum_val in sums]
    ana_probs = [analytical_probabilities[sum_val] for sum_val in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_probs, alpha=0.6, label='Симуляція')
    plt.plot(sums, ana_probs, 'ro-', label='Аналітичні значення')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Імовірності сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
