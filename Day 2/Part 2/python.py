import sys

with open(sys.argv[1], "r") as inh:
    inputs = inh.readlines()
	
aim = 0
coords = [0, 0]

for input in inputs:
    cmd, count = input.split()
    count = int(count)

    if cmd == "up":
        aim -= count
    if cmd == "down":
        aim += count
    if cmd == "forward":
        coords[0] += count
        coords[1] += count * aim    
        
print("Coords are {},{}, giving a puzzle answer of {}.".format(coords[0], coords[1], coords[0] * coords[1]))