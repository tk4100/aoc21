import sys

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
              
    def print(self):
        print("({},{})".format(self.x, self.y))

class Line():
    def __init__(self, start, end, value=1):
        if start.x == end.x:
            self.direction = "vertical"
        elif start.y == end.y:
            self.direction = "horizontal"
        else:
            print("This is not a valid line, it's a diagonal!!! ({},{}) -> ({},{})".format(start.x, start.y, end.x, end.y))
            self.direction = "diagonal"
        self.start = start
        self.end = end
        self.value = value

    def getPoints(self):
        if self.direction == "vertical":
            start = min([self.start.y, self.end.y])
            end = max([self.start.y, self.end.y])
            points = [ Point(self.start.x, x) for x in range(start, end+1) ]
        if self.direction == "horizontal":
            start = min([self.start.x, self.end.x])
            end = max([self.start.x, self.end.x])
            points = [ Point(x, self.start.y) for x in range(start, end+1) ]
            
        return(points)
        
        
            
    def print(self):
        print("({},{}) -> ({},{})".format(self.start.x, self.start.y, self.end.x, self.end.y))

class Map():
    def __init__(self, input_string):
        self.mapInitFromString(input_string)
        
        self.renderLines()
        
    def unpackLine(self, line):
        start, end = line.split(" -> ")
        start = Point(int(start.split(',')[0]), int(start.split(',')[1]))
        end = Point(int(end.split(',')[0]), int(end.split(',')[1]))
        
        line = Line(start, end)
        return(line)
        
    # won't tolerate extra newlines at the end of the input.
    def mapInitFromString(self, input):
        self.map = []
        
        # suck in all lines
        self.lines = []
        for line in input:
            unpacked = self.unpackLine(line.strip())
            if unpacked.direction == "horizontal" or unpacked.direction == "vertical":
                self.lines.append(unpacked)
            
        # get map dims
        max_startx = max([ x.start.x for x in self.lines ])
        max_endx = max([ x.end.x for x in self.lines ])
        self.dim_x = max([max_startx, max_endx]) + 1
        
        max_starty = max([ x.start.y for x in self.lines ])
        max_endy = max([ x.end.y for x in self.lines ])
        self.dim_y = max([max_starty, max_endy]) + 1
        
        # generate map
        self.map = []
        for x in range(0,self.dim_x):
            self.map.append([ Point(x,y) for y in range(0,self.dim_y) ])
        
    def renderLines(self):
        for line in self.lines:
            for point in line.getPoints():
                self.map[point.x][point.y].value += 1
            
    def getPoint(self, point):
        return(self.map[point.x][point.y].value)
        
    def countOverlaps(self):
        score = 0
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                if self.map[x][y].value > 1:
                    score += 1
        return(score)
        
    def print(self):
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                sys.stdout.write("{: <2}".format(self.map[x][y].value))
            sys.stdout.write("\n")
       
with open(sys.argv[1], 'r') as inh:
    data = inh.readlines()
    
worldmap = Map(data)
if "demo" in sys.argv[1]:
    worldmap.print()
print("Overlap points: {}".format(worldmap.countOverlaps()))