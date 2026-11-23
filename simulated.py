
import random
import math

def calculate_cost(state):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def simulated_annealing():
    current = random.sample(range(8), 8)

    temperature = 1000
    cooling_rate = 0.99

    while temperature > 0.1:

        if calculate_cost(current) == 0:
            return current

        next_state = current.copy()

        i, j = random.sample(range(8), 2)

        next_state[i], next_state[j] = (
            next_state[j], next_state[i]
        )

        delta = calculate_cost(current) - calculate_cost(next_state)

        if delta > 0:
            current = next_state

        else:
            probability = math.exp(delta / temperature)

            if random.random() < probability:
                current = next_state

        temperature *= cooling_rate

    if calculate_cost(current) == 0:
        return current

    return None


# Main program
solution = simulated_annealing()

if solution:
    print("Solution found:", solution)

    print("\nChess Board:")

    for row in range(8):
        for col in range(8):
            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("\nCost:", calculate_cost(solution))

else:
    print("No solution found. Run again.")
