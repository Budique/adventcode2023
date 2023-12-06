import sys
import re

def main():
    input_path = sys.argv[1]

    lines = open(input_path, "r").readlines()

    rng = 1000000

    seeds = []
    for pair in re.findall("(\d+) (\d+)", lines[0]):
        seed_start = int(pair[0])
        seed_range = int(pair[1])
        for i in range(0, seed_range, rng):
            seeds.append(seed_start + i)

    while rng > 0:
        seeds_size = len(seeds)
        seeds_copy = seeds.copy()
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
        
        if rng == 1:
            break

        winner_seed = seeds_copy[seeds.index(min(seeds))]

        seeds = []
        
        for i in range(0, rng, rng//10):
            seeds.append(winner_seed - i)
            seeds.append(winner_seed + i)
        rng //= 10

    print(min(seeds))

if __name__ == "__main__":
    main()