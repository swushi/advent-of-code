import sys
import re

def main():
    file = open(sys.argv[1])
    groups = list(map(lambda x: x.split('\n'), file.read().split('\n\n')))
    seeds = re.findall(r"\d+", groups[0][0])
    seed_maps = groups[1:]

    mappings = {}

    for seed_map in seed_maps:
        source, destination = re.search(r"(\w+)-to-(\w+) map:", seed_map[0]).groups()

        if source not in mappings:
            mappings[source] = {}

        def mapping_fn(value):
            


        # mappings[source][destination] = lambda seed: seed

        for mapping in seed_maps[1:]:
            pass
        

    print(mappings)



if __name__ == '__main__':
    main()