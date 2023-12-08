import sys
import re

def read_input(path):
    lines = open(path, "r").readlines()

    instructions = lines[0].strip("\n")
    nodes = {}

    for i in range(2, len(lines)):
        tmp = re.findall(r"[A-Z]+", lines[i])
        nodes[tmp[0]] = tmp[1:]

    return instructions, nodes

def main():
    input_path = sys.argv[1]

    instructions, nodes = read_input(input_path)

    instructions_length = len(instructions)
    steps = 0
    current_node = "AAA"

    while current_node != "ZZZ":
        left = instructions[steps % instructions_length] == "L"
        current_node = nodes[current_node][0 if left else 1]
        steps += 1
    
    print(steps)




if __name__ == "__main__":
    main()