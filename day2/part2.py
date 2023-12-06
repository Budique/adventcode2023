import sys
import re

def processLine(string):
    reds = [int(s) for s in re.findall(r"(\d+) red", string)]
    blues = [int(s) for s in re.findall(r"(\d+) blue", string)]
    greens = [int(s) for s in re.findall(r"(\d+) green", string)]

    red = max(reds)
    blue = max(blues)
    green = max(greens)

    return red*blue*green



def main():
    input_path = sys.argv[1]

    sum = 0

    with open(input_path, "r") as f:
        for line in f:
            sum += processLine(line)

    print(sum)

if __name__ == "__main__":
    main()