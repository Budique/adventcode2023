import sys

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def main():
    input_path = sys.argv[1]

    sum = 0

    first = -1
    last = 0

    index = 0

    with open(input_path, "r") as f:
        for line in f:
            size = len(line)
            while index < size:
                if line[index] in numbers:
                    if first == -1:
                        first = int(line[index])
                    last = int(line[index])
                index += 1

            sum += 10*first + last
            
            index = 0
            first = -1

    print(sum)


if __name__ == "__main__":
    main()