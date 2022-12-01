import sys
from statistics import multimode

def getMode(input, digit):
    return(max(multimode([ x[digit] for x in input])))

def getMatches(input, digit=0, invert=False):
    output = []
    mode = getMode(input, digit)
    for datum in input:
        if datum[digit] == mode and invert == False:
            output.append(datum)
        elif datum[digit] != mode and invert == True:
            output.append(datum)
            
    return(output)
    
with open(sys.argv[1], "r") as inh:
    inputs = inh.readlines()
    inputs = [ x.strip() for x in inputs ]
    bitlength = len(inputs[0])
	
o2 = [ x for x in inputs ]
for digit in range(0,bitlength):
    o2 = getMatches(o2, digit)
    if len(o2) <= 1:
        o2=o2[0]
        break

co2 = [ x for x in inputs ]
for digit in range(0,bitlength):
    co2 = getMatches(co2, digit, True)
    if len(co2) <= 1:
        co2 = co2[0]
        break
        
lifesupport = int(co2,2)*int(o2,2)
print(lifesupport)