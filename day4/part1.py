import sys
import re

def processLine(line):
    line = line.split(":")[1]
    line = line.split("|")

    winning_numbers = [int(s) for s in re.findall("(\d+)", line[0])]
    picked_numbers = [int(s) for s in re.findall("(\d+)", line[1])]
    
    result = 0
    for winning_number in winning_numbers:
        for picked_number in picked_numbers:
            if winning_number == picked_number:
                result += 1

    if result:
        return 2**(result-1)
    
    return 0


def main():
    input_path = sys.argv[1]

    sum = 0
    with open(input_path, "r") as f:
        for line in f:
            sum += processLine(line)
            
    print(sum)


if __name__ == "__main__":
    main()