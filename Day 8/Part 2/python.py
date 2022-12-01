import sys

class SevenSegFigurer():
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None
        self.g = None
        
        self.seen_one = False
        self.seen_four = False
        self.seen_seven = False
    
    def feed(self, digit):
        # one
        if len(digit) == 2 and not self.seen_one:
            self.c = [ x for x in digit ]
            self.f = [ x for x in digit ]
        # four
        if len(digit) == 4 and not self.seen_four:
            self.b = [ x for x in digit ]
            self.c = [ x for x in digit ]
            self.d = [ x for x in digit ]
            self.f = [ x for x in digit ]
        # seven
        if len(digit) == 3 and not self.seen_seven:
            self.a = [ x for x in digit ]
            self.c = [ x for x in digit ]
            self.f = [ x for x in digit ]
            
        # zero, six, or nine, a, b, f, and g are always present
        if len(digit) == 6:
            # solidify segments c and f
            for seg in self.f:
                if seg in digit:
                    self.f = seg
                    self.c.remove(seg)

            
        # two, three, or five
        if len(digit) == 5:
            pass
 
            
        
    def decode(self, digit):
        pass

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