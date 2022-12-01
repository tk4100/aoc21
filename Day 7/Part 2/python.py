import sys
import math
import statistics

with open(sys.argv[1], 'r') as inh:
    crabspots = [ int(x) for x in inh.read().split(',') ]
    
def fuelcost(distance):
    cost = 0
    while distance != 0:
        cost += distance
        distance -= 1
    return(cost)

# wow, off by one the first time.  This works with floor() in place of round()   
destination = math.floor(statistics.mean(crabspots))
cost = sum([ fuelcost(abs(x-destination)) for x in crabspots] )
print("Destination: {}, crabcost: {}".format(destination, cost))

''' leaving this because shame.  shame on me.
# bruteforce FTW
cost_per_position = []
for i in range(min(crabspots), max(crabspots)):
    print("Position {}".format(i))
    cost = sum([ fuelcost(abs(x-i)) for x in crabspots ])
    cost_per_position.append(cost)
    
cost = min(cost_per_position)
destination = cost_per_position.index(cost)

print("Destination: {}, crabcost: {}".format(destination, cost))
'''