text = "X-DSPAM-Confidence:    0.8475";
number = text.find(':')
f1 = text[number+1:]
f = float(f1)
print f