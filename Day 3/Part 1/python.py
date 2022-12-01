import sys

with open(sys.argv[1], "r") as inh:
    inputs = inh.readlines()
	
bitlength = 12
gamma = 0
epsilon = 0

# 5 bits
bitcounts = [ 0 for x in range(0,bitlength) ]

for input in inputs:
    i = 0
    while i < bitlength:
        bitcounts[i] += int(input[i])
        i += 1
        
gamma_str = ""
epsilon_str = ""
threshold = len(inputs) / 2
for count in bitcounts:
    if count >= threshold:
        gamma_str += "1"
        epsilon_str += "0"
    else:
        gamma_str += "0"
        epsilon_str += "1"
        
gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)

print("Gamma: {}, Epsilon: {}, Power: {}".format(gamma, epsilon, gamma * epsilon))