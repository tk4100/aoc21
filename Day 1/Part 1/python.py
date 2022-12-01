import sys

increase_count = 0

with open(sys.argv[1], 'r') as inh:
    previous = False
    for line in inh.readlines():
        if previous:
            if int(line) > previous:
                increase_count += 1
        previous = int(line)
			
print(increase_count)