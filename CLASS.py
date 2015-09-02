import DPlib

#text to be analized
text = 'Soledad_OBrien Soledad- As an HR influencer, we look forward to your thoughts on our social recruiting White Paper: http://t.co/C9lvr6zL17'

#loading NAME class
NAMES, vNAMES = DPlib.getNames()

print ''
#print original text
print text

#print analized text
print DPlib.textClass(text, NAMES)

