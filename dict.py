name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From:'): 
        words = line.split()
        
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1
a = 0
for key in counts:
    if counts[key] > a:
        a = counts [key]
        b = key
print b, a              