import sys
import re
import math

def read_input(path):
    lines = open(path, "r").readlines()

    instructions = lines[0].strip("\n")
    nodes = {}
    starting_nodes = []

    for i in range(2, len(lines)):
        tmp = re.findall(r"[1-9A-Z]+", lines[i])
        nodes[tmp[0]] = tmp[1:]
        if tmp[0][-1] == 'A':
            starting_nodes.append(tmp[0])

    return instructions, nodes, starting_nodes

def solve_steps(start_node):
    current_node = start_node
    steps = 0

    while current_node[-1] != 'Z':
        left = instructions[steps % (len(instructions))] == "L"
        current_node = nodes[current_node][0 if left else 1]
        steps += 1
    
    return steps

def main():
    input_path = sys.argv[1]
    
    global instructions
    global nodes
    instructions, nodes, start_nodes = read_input(input_path)
    result = 1

    for start_node in start_nodes:
        result = math.lcm(result, solve_steps(start_node))
    
    print(result)

if __name__ == "__main__":
    main()