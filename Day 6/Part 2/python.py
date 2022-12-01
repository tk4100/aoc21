import sys

class LanternFish():
    def __init__(self, timer, count):
        self.timer = timer
        self.count = count
        
    def age(self):
        if self.timer == 0:
            self.timer = 7
            result = True
        else:
            result = False
            
        self.timer -= 1
        return(result)
            
            
with open(sys.argv[1], 'r') as inh:
    raw = inh.read().strip()
    
# create initial fish
counts = {}
for x in raw.split(','):
    fish = int(x)
    if fish in counts.keys():
        counts[fish] += 1
    else:
        counts[fish] = 1
        
fish = []
for count in counts.keys():
    fish.append(LanternFish(count, counts[count]))

# the dawn of time....
i = 1
while i <= 256:
    # age
    birth_count = 0
    new_births = []
    for a_fish in fish:
        birth = a_fish.age()
        if birth:
            birth_count += a_fish.count
    if birth_count > 0:
        new_births.append(LanternFish(8, birth_count))
    
    #give deets
    fish = fish + new_births
    
    number_of_fishies = sum([x.count for x in fish])
    sys.stdout.write("Day {: <2}: {} fish.\n".format(i, number_of_fishies))
    
    
    i += 1