text = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

lines = [s.strip() for s in text.split("\n")]

lines = [s.strip() for s in open("p05.txt").readlines()]

# return (seeds[], ranges[tuples[]])
def parse(lines):
    seeds = [int(x.strip()) for x in lines[0].replace("seeds: ", "").split()]
    cur_map = []
    maps = [cur_map]
    
    for i in range(3, len(lines)):
        cur_line = lines[i]
        if cur_line == "":
            # finish map start new one
            cur_map = []
            maps.append(cur_map)
        elif ":" in cur_line: continue
        else:
            cur_map.append([int(x) for x in cur_line.split()])
    return (seeds, maps)

def map_seed(seed, maps):
    curr = seed
    for map in maps:
        # find applicable mapping
        for row in map:
            (dst_start, src_start, rlen) = row
            if curr >= src_start and curr <= src_start + rlen:
                # print(curr)
                curr = dst_start + (curr - src_start)
                break # break inner loop

    return curr

def map_range(sr, maps):
    mapped_ranges = [sr]
    for map in maps:
        # print(mapped_ranges)
        # take ranges from last iteration, and map them again
        ranges_to_map = mapped_ranges
        mapped_ranges = []
        while ranges_to_map: # treat like queue
            (st, ct) = ranges_to_map.pop(0)
            found = False
            for row in map:
                (dst_start, src_start, rlen) = row
                if st >= src_start and st + ct <= src_start + rlen:
                    # fully in range, map
                    
                    mapped_ranges.append((dst_start + (st - src_start), ct))
                    found = True
                    break
                elif st >= src_start and st < src_start + rlen: # partly in range, map starting at st
                    # for example st/ct = 10, 5 , src_start = 4,9 -- need to map 10,11,12 and leave 13,14 unmapped
                    leftover = (st+ct)-(src_start+rlen)  # 15-13=2
                    fit = ct - leftover # 5 - 2 = 3
                    
                    mapped_ranges.append((dst_start + (st - src_start), fit))
                    ranges_to_map.append((st + fit, leftover))
                    found = True
                    break
                elif st + ct > src_start and st + ct <= src_start + rlen:
                    # for example st/ct = 4,9 , src_start = 10,5 -- need to map 10,11,12 and leave 4,5,6,7,8,9 unmapped 
                    fit = st + ct - src_start # (4+9)-10 = 3
                    leftover = ct - fit # 9 - 3 = 6
                    mapped_ranges.append((dst_start, fit))
                    ranges_to_map.append((st, leftover))
                    found = True
                    break

            if not found:
                mapped_ranges.append((st, ct))

    return mapped_ranges
                            
(seeds, maps) = parse(lines)
# print(seeds)
# for m in maps: print(m)
# mapped_seeds = [map_seed(s, maps) for s in seeds]
# print(min(s) for s in mapped_seeds)

seed_ranges = [(seeds[j*2], seeds[j*2 + 1]) for j in range(0, len(seeds)//2)]
lowest = 9999999999999999
for sr in seed_ranges:
    mr = map_range(sr, maps)
    for loc in mr:
        if loc[0] < lowest:
            print(loc[0])
            lowest = loc[0]

# for sr in seed_ranges: print(sr)

