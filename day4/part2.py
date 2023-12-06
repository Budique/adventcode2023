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

    return result


def main():
    input_path = sys.argv[1]

    cards_numbers = []
    cards_instances = []
    with open(input_path, "r") as f:

        for line in f:
            cards_instances.append(1)
            cards_numbers.append(processLine(line))

        for i in range(len(cards_numbers)):
            for j in range(1, cards_numbers[i] + 1):
                cards_instances[i+j] += cards_instances[i]

        
        print(sum(cards_instances))


if __name__ == "__main__":
    main()