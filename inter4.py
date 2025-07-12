#Geeta needs to jump on slippery logs across a river:

 #   She starts at the bank (before log 0).

  #  She can jump right up to Y positions or left up to X positions.

   # She must land only on the right edge of a log.

   # If stuck, she returns to the starting bank.

    #You need to return the minimum number of jumps to reach the opposite bank or back.

# Difficulty: Medium to Hard
# Concept: BFS traversal with directional constraints
# Skills: Custom BFS, careful edge-case handling, state tracking

 #   The challenge lies in understanding directional constraints: left jump (X), right jump (Y), and bank entry/exit.

  #  Also, understanding how the logs behave as platforms makes this conceptually deeper.

from collections import deque

class State:
    def __init__(self, index, jumps):
        self.index = index
        self.jumps = jumps

def min_jumps(N, X, Y, logs):
    visited = [False] * N
    queue = deque()

    # Start from bank before first log
    queue.append(State(-1, 0))  # index -1 means bank

    while queue:
        current = queue.popleft()
        pos = current.index
        jumps = current.jumps

        for i in range(N):
            if visited[i]:
                continue

            if pos == -1:
                # First jump from bank to log i
                visited[i] = True
                queue.append(State(i, jumps + 1))
            else:
                jump_distance = abs(logs[i] - logs[pos])
                if i > pos and jump_distance <= Y:
                    visited[i] = True
                    queue.append(State(i, jumps + 1))
                elif i < pos and jump_distance <= X:
                    visited[i] = True
                    queue.append(State(i, jumps + 1))

        # Check if we can jump from current log to the opposite bank
        if pos != -1:
            # Java version assumed opposite bank reachable if distance from log to end ≤ Y
            # We'll simulate that via position
            if abs(N - pos - 1) <= Y:
                return jumps + 1

    return 0  # If unable to reach

# ---------- Sample runner ----------
def main():
    sample_input = """5 1 5
1 6 5 4 1"""
    print("Sample Input:")
    print(sample_input)

    lines = sample_input.strip().split('\n')
    N, X, Y = map(int, lines[0].split())
    logs = list(map(int, lines[1].split()))

    result = min_jumps(N, X, Y, logs)

    print("\nExpected Output:")
    print("6")
    print("\nYour Output:")
    print(result)

main()




