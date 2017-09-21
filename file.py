# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    number = line.find(':')
    f1 = line[number+1:]
    f = float(f1)
    s = s + f
aver = s / count
print "Average spam confidence:", aver