
import random

# Calculate the number of attacking queen pairs
def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            # Check diagonal attacks
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Generate neighbors by swapping two queens
def get_neighbors(state):
    neighbors = []
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            neighbor = state[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors


# Hill Climbing Algorithm
def hill_climbing(n):

    # Random initial state
    current = list(range(n))
    random.shuffle(current)

    while True:
        current_cost = calculate_cost(current)

        # Goal reached
        if current_cost == 0:
            return current

        best_neighbor = current
        best_cost = current_cost

        # Find the best neighbor
        for neighbor in get_neighbors(current):
            neighbor_cost = calculate_cost(neighbor)

            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost

        # Stop if no better neighbor exists
        if best_cost >= current_cost:
            return None

        current = best_neighbor


# Print the chessboard
def print_board(state):
    n = len(state)

    for row in range(n):
        for col in range(n):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()


# Solve using random restarts
def solve_n_queens(n):
    while True:
        solution = hill_climbing(n)

        if solution is not None:
            return solution


# Main program
for n in [4, 8]:

    print("\n", n, "- Queens Solution:")

    solution = solve_n_queens(n)

    print("State:", solution)
    print("Cost:", calculate_cost(solution))

    print_board(solution)
