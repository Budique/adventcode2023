import sys
import math

def read_file(path):
    lines = open(path, "r").readlines()

    time = ""
    distance = ""

    for i in lines[0]:
        if i.isdigit():
            time += i

    for i in lines[1]:
        if i.isdigit():
            distance += i

    return int(time), int(distance)


def main():
    input_path = sys.argv[1]

    time, distance = read_file(input_path)

    tmp = math.sqrt(time*time/4 - distance)

    print(2*int(tmp)+1)


if __name__ == "__main__":
    main()