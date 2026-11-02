
import heapq

# Initial and goal states
start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Heuristic 1: Tiles out of place
def tiles_out_of_place(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


# Heuristic 2: Manhattan distance
def manhattan(state):
    total = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal_index = GOAL.index(tile)

            row, col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3)

            total += abs(row - goal_row)
            total += abs(col - goal_col)

    return total


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)

    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            new_state = list(state)

            new_state[blank], new_state[new_pos] = (
                new_state[new_pos], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search
def a_star(start, heuristic):
    OPEN = []
    CLOSED = set()

    g = {start: 0}
    parent = {start: None}

    f = heuristic(start)

    heapq.heappush(OPEN, (f, 0, start))

    while OPEN:
        f, cost, state = heapq.heappop(OPEN)

        if state in CLOSED:
            continue

        if state == GOAL:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        CLOSED.add(state)

        for neighbor in get_neighbors(state):

            if neighbor in CLOSED:
                continue

            new_g = g[state] + 1

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = state

                h = heuristic(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    OPEN, (new_f, new_g, neighbor)
                )

    return None


# Display the board
def print_board(state):
    for i in range(0, 9, 3):
        print(*state[i:i+3])


# Main program
print("A* Search using Tiles Out of Place")

solution = a_star(start, tiles_out_of_place)

if solution:
    for step, state in enumerate(solution):
        print("\nStep", step)
        print_board(state)

    print("\nTotal Moves:", len(solution) - 1)

else:
    print("No solution")


print("\nA* Search using Manhattan Distance")

solution = a_star(start, manhattan)

if solution:
    for step, state in enumerate(solution):
        print("\nStep", step)
        print_board(state)

    print("\nTotal Moves:", len(solution) - 1)

else:
    print("No solution")
