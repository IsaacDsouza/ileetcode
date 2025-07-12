#Smallest Square Finder

# Difficulty: Easy to Medium
# Concept: Brute force + geometry
# Skills: 2D geometry, set lookup optimization, nested loops

 #   You loop through all pairs of points and check if they can form the diagonal of a square.

#    It requires basic understanding of point manipulation and set-based optimization.

 #   Intro to geometry + brute force in interviews or early rounds of coding contests


def find_smallest_square(points):
    point_set = set(points)
    n = len(points)
    min_side = float('inf')

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            # Skip if aligned horizontally or vertically
            if x1 == x2 or y1 == y2:
                continue

            # Check if they can form diagonal corners of a square
            if abs(x1 - x2) != abs(y1 - y2):
                continue

            # The other two points needed to form a square
            p3 = (x1, y2)
            p4 = (x2, y1)

            if p3 in point_set and p4 in point_set:
                side = abs(x1 - x2)
                min_side = min(min_side, side)

    return 0 if min_side == float('inf') else min_side

# Sample input/output runner
def main():
    sample_input = """8
3 3
2 5
1 1
5 2
2 2
1 3
5 5
"""  # Duplicate point

    print("Sample Input:")
    print(sample_input)

    lines = sample_input.strip().split('\n')
    n = int(lines[0])
    # Deduplicate points here
    points = list(set(tuple(map(int, line.split())) for line in lines[1:]))

    expected_output = 2
    actual_output = find_smallest_square(points)

    print("\nExpected Output:")
    print(expected_output)
    print("\nYour Output:")
    print(actual_output)

main()

