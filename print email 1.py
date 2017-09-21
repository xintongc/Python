fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = []
for line in fh:
    line = line.rstrip()
    if line.startswith('From'): 
        words = line.split()
       
        if words[1] not in lst:
            lst.append(words[1])
        #print words [1]
            count = count + 1
for element in lst:
    print element            
    
print "There were", count, "lines in the file with From as the first word"
