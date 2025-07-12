#the goal is to compute the minimum number of button presses needed to go from a starting station to a destination station, using a circular track system and a keypad with limited working digits, along with:

   # F to move forward by 1 station.

   # B to move backward by 1 station.

   # E (Enter) to go to a directly typed station.
#Collider Pod (Min Button Presses)

# Difficulty: Medium
# Concept: Graph/BFS traversal with custom transition rules
#Skills: BFS, shortest path search, handling typed input constraints

    #The state space is N stations and possible transitions via F/B or digit typing.

   # You model station movement as a graph problem with BFS to find the shortest button press sequence.

    #Common in company coding rounds (like Amazon, Flipkart, etc.) as a practical BFS + constraints scenario.



from collections import deque

def can_type(number, working_digits):
    for digit in str(number):
        if digit not in working_digits:
            return False
    return True

def min_button_presses(n, working_digits, start, dest):
    visited = [False] * (n + 1)  # stations are 1-indexed
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        station, presses = queue.popleft()

        if station == dest:
            return presses

        # Try moving forward (F)
        forward = station + 1 if station + 1 <= n else 1
        if not visited[forward]:
            visited[forward] = True
            queue.append((forward, presses + 1))

        # Try moving backward (B)
        backward = station - 1 if station - 1 >= 1 else n
        if not visited[backward]:
            visited[backward] = True
            queue.append((backward, presses + 1))

        # Try direct jump using working digits
        for target in range(1, n + 1):
            if not visited[target] and can_type(target, working_digits):
                visited[target] = True
                digit_presses = len(str(target)) + 1  # digits + 'Enter'
                queue.append((target, presses + digit_presses))

    return -1  # if not reachable

# ---------------------------
# Sample Input/Output Runner

def main():
    sample_input = """650
4
1 8 0 4
475
485"""
    print("Sample Input:")
    print(sample_input)

    lines = sample_input.strip().split("\n")
    n = int(lines[0])
    count_digits = int(lines[1])
    working_digits = set(lines[2].split())
    start = int(lines[3])
    dest = int(lines[4])

    result = min_button_presses(n, working_digits, start, dest)

    print("\nExpected Output:")
    print("5")
    print("\nYour Output:")
    print(result)

main()
