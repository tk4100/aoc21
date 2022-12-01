import sys

increase_count = 0

with open(sys.argv[1], 'r') as inh:
    lines = inh.readlines()
    
i = 0
windows = []
while i < len(lines) - 2:
    windows.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
    i += 1

previous = False
for window in windows:
    if previous:
        if window > previous:
            increase_count += 1
    previous = int(window)
			
print(increase_count)