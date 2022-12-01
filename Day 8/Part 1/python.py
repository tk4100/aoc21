import sys

with open(sys.argv[1], 'r') as inh:
    raw = inh.readlines()

total_count = 0
for line in raw:
    rando, output = line.split(' | ')
    random_bits = rando.split()
    output_bits = output.split()
    
    count = 0
    for bit in output_bits:
        if len(bit) == 2 or len(bit) == 3 or len(bit) == 4 or len(bit) == 7:
            count += 1
            
    print("Line {}".format(count))
    total_count += count

print("Total: {}".format(total_count))