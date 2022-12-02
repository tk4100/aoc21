class Digit():
    def __init__(self):
        pass

    def AND(self, target, scope):
        out = [ x for x in target ]
        for segment in target:
            if segment not in scope:
                del(out[out.index(segment)])
        return(out)

    def getSig(self, signal):
        sig = 0
        sig += (100 * len(self.AND(self.one, signal)))
        sig += (10 * len(self.AND(self.four, signal)))
        sig += len(self.AND(self.seven, signal))
        return(sig)

    # takes a string, like "dab"
    def learn(self, signal):
        # One
        if len(signal) == 2:
            self.one = [ x for x in signal ]
        # Four
        elif len(signal) == 4:
            self.four = [ x for x in signal ]
        # Seven
        elif len(signal) == 3:
            self.seven = [ x for x in signal ]
        # Eight doesn't help us, since it lights all segments

    def match(self, signal):
        # count how many matches there are between our known numbers and this
        # signal. With that and the count of segments lit we can uniquely ID
        # the number
        sig = self.getSig(signal)

        # One, Four, Seven and Eight
        if len(signal) == 2:
            return(1)
        elif len(signal) == 4:
            return(4)
        elif len(signal) == 3:
            return(7)
        elif len(signal) == 7:
            return(8)

        # Two, Three, and Five
        if len(signal) == 5:
            if sig == 122:
                return(2)
            elif sig == 233:
                return(3)
            elif sig == 132:
                return(5)
            
        # Zero, Six and Nine
        elif len(signal) == 6:
            if sig == 233:
                return(0)
            elif sig == 132:
                return(6)
            elif sig == 243:
                return(9)


#####

with open("tk_input.txt") as fh:
    total = 0
    for line in fh:
        bits = line.split("|")
        signals = bits[0].split()
        code = bits[1].split()

        decoder = Digit()
        for signal in signals:
            decoder.learn(signal)

        digit_string = ''
        for digit in code:
            digit_string += str(decoder.match(digit))
        total += int(digit_string)

print("Total is: {}".format(total))
