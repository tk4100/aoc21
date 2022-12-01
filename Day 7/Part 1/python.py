import sys
import statistics

with open(sys.argv[1], 'r') as inh:
    crabspots = [ int(x) for x in inh.read().split(',') ]
    
destination = statistics.median(crabspots)

cost = sum([ abs(x-destination) for x in crabspots])

print("Destination: {}, crabcost: {}".format(destination, cost))