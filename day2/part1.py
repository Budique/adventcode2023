import sys
import re

def processLine(string):
    reds = [int(s) for s in re.findall(r"(\d+) red", string)]
    blues = [int(s) for s in re.findall(r"(\d+) blue", string)]
    greens = [int(s) for s in re.findall(r"(\d+) green", string)]

    global red, blue, green

    for i in reds:
        if i > red:
            return False
        
    for i in blues:
        if i > blue:
            return False
        
    for i in greens:
        if i > green:
            return False

    return True



def main():
    input_path = sys.argv[1]

    global red, blue, green
    red, blue, green = [12, 14, 13]

    gameId = 1
    sum = 0

    with open(input_path, "r") as f:
        for line in f:
            if processLine(line):
                sum += gameId
            gameId += 1

    print(sum)

if __name__ == "__main__":
    main()