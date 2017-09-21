name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From'): 
        words = line.split()
        if words[0] == 'From':
            s = words[5]
            h = s.split(':')
            
            if h[0] not in counts:
                counts[h[0]] = 1
            else:
                counts[h[0]] += 1
            
t = counts.items()
t.sort()
for key, val in t:
    print key, val
