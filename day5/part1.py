import sys
import re

def main():
    input_path = sys.argv[1]

    with open(input_path, "r") as f:
        lines = f.readlines()

        seeds = [int(num) for num in re.findall("(\d+)", lines[0])]
        seeds_size = len(seeds)
        changed = [False for i in range(seeds_size)]

        for line in lines:
            if line[0] == "\n":
                continue

            if line[0].isalpha():
                for i in range(seeds_size):
                    changed[i] = False
                continue
            
            destination_start, source_start, range_len = [int(s) for s in re.findall("(\d+)", line)]

            for i in range(seeds_size):
                val = seeds[i]
                if not changed[i] and (val >= source_start and val < source_start + range_len):
                    seeds[i] = destination_start + val - source_start
                    changed[i] = True
        
        print(min(seeds))


if __name__ == "__main__":
    main()