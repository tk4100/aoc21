import sys

class LanternFish():
    def __init__(self, timer=8):
        self.timer = timer
        
    def age(self):
        if self.timer == 0:
            self.timer = 7
            result = LanternFish()
        else:
            result = False
            
        self.timer -= 1
        return(result)
            
            
with open(sys.argv[1], 'r') as inh:
    raw = inh.read().strip()
    
# create initial fish
fish = [ LanternFish(int(x)) for x in raw.split(',') ]

# the dawn of time....
i = 1
while i <= 80:
    new_births = []
    for a_fish in fish:
        birth = a_fish.age()
        if birth:
            new_births.append(birth)
            
    fish = fish + new_births
    if "demo" in sys.argv[1]:
        sys.stdout.write("After {: <2} day(s): {} fish: {}\n".format(i, len(fish), ','.join([str(x.timer) for x in fish ])))
    else:
        sys.stdout.write("Day {: <2}: {} fish.\n".format(i, len(fish)))
    
    
    i += 1