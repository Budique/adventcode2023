import sys

def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    row_size = len(lines)
    for i in range(row_size):
        lines[i] = lines[i].strip("\n")
    column_size = len(lines[0])

    return lines, row_size, column_size

def shoelace(points):
    area = 0

    X = [point[0] for point in points] + [points[0][0]]
    Y = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += X[i] * Y[i + 1] - Y[i] * X[i + 1]

    return abs(area) / 2

# pipe and entering_from is [x, y]
def move_next(pipe_char, pipe, entering_from):
    # Where is the entrance relative to the pipe
    above = entering_from[0] < pipe[0]
    right = entering_from[1] > pipe[1]

    if pipe_char == "|":
        if above:
            return [pipe[0]+1, pipe[1]]
        else:
            return [pipe[0]-1, pipe[1]]
    if pipe_char == "-":
        if right:
            return [pipe[0], pipe[1]-1]
        else:
            return [pipe[0], pipe[1]+1]
    if pipe_char == "L":
        if above:
            return [pipe[0], pipe[1]+1]
        else:
            return [pipe[0]-1, pipe[1]]
    if pipe_char == "J":
        if above:
            return [pipe[0], pipe[1]-1]
        else:
            return [pipe[0]-1, pipe[1]]
    if pipe_char == "7":
        if entering_from[1] < pipe[1]: # Entering from left
            return [pipe[0]+1, pipe[1]]
        else:
            return [pipe[0], pipe[1]-1]
    if pipe_char == "F":
        if right:
            return [pipe[0]+1, pipe[1]]
        else:
            return [pipe[0], pipe[1]+1]

def solve_loop(lines, row_size, column_size):
    start = [0, 0]

    for i in range(row_size):
        for j in range(column_size):
            # S will be J
            if (lines[i][j] == "S"):
                start = [i, j]

    points = [start]

    cur1 = [start[0], start[1]-1]
    cur1_entering_from = start

    while cur1 != start:
        points.append(cur1)

        cur1_tmp = cur1
        cur1 = move_next(lines[cur1[0]][cur1[1]], cur1, cur1_entering_from)
        cur1_entering_from = cur1_tmp
    
    return len(points), shoelace(points) 

def main():
    input_path = sys.argv[1]

    lines, row_size, column_size = read_input(input_path)
    result, area = solve_loop(lines, row_size, column_size)

    print(area + 1 - result / 2) # Pick's Theorem

if __name__ == "__main__":
    main()