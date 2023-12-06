import sys
import re

def read_file(path):
    lines = open(path, "r").readlines()

    times = [int(num) for num in re.findall("\d+", lines[0])]
    distances = [int(num) for num in re.findall("\d+", lines[1])]

    return times, distances

def calculate(time, distance):
    mid = time // 2
    i = mid

    while i > 0 and i*(time-i) > distance:
        i -= 1
    
    while mid < time and mid*(time-mid) > distance:
        mid += 1

    return mid - i - 1


def main():
    input_path = sys.argv[1]

    times, distances = read_file(input_path)

    result = 1

    for time, distance in zip(times, distances):
        result *= calculate(time, distance)

    print(result)

if __name__ == "__main__":
    main()