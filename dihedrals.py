import re
print "We're going to make a dihedral. How many sides would you like it to have?"
n = int(raw_input("Type an integer and press enter "))
print "Apply group actions. Type an 'f' for flip  and an 'r' for rotate right. You can type as many as you want."
grpact=raw_input("Type a grpact and press enter.\n")
#from here to the end make it a function, excluding the print
while re.search('[^rf]', grpact) is not None: #while the input has letters other than r and f
	grpact = raw_input("Try again. Type a string with only the letter 'f' and the letter 'r'. Then press enter.\n")
#print grpact #for testing the io 
bucket= [] 
fsleft=0
for i in grpact:
	if i=='r':
		bucket.append(fsleft) #keeps track of f's to the left of the current r
	if i=='f':
		fsleft=fsleft+1 #change to +=format 
grpact=grpact.replace('f','') #remove all the f's from the grpact 
grpact=list(grpact)
for i in range(0,len(bucket)):
	if int(bucket[i])%2==1: #if we flipped the r an odd number of times, change it to its inverse
		grpact[i]='l' 
grpact=''.join(grpact)
rcount=(grpact.count('r')-grpact.count('l'))%n #right and left rotations cancel out 
#putting the grpact back together 
if rcount>=0:
	grpact='r'*rcount
grpact=grpact+('f'*(fsleft%2)) #f is a self inverse 
#if everything cancels its just the identify 
if grpact == '':
	grpact='e'
print "That sequence of group operations produces the same result as %s" % grpact
