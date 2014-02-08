import re
print "We're going to make a dihedral. How many sides would you like it to have?" 
n = int(raw_input("Type an integer and press enter "))
print "Apply group actions. Type an 'f' for flip  and an 'r' for rotate right. You can type as many as you want." 
string=raw_input("Type a string and press enter.\n")
while re.search('[^rf]', string) is not None: #this doesn't work
	string = raw_input("Try again. Type a string with only the letter 'f' and the letter 'r'. Then press enter.\n") 
print string
bucket= ""
fsleft=0 
for i in string: 
	if i=='r': 
		bucket=bucket + str(fsleft)  
	if i=='f': 
		fsleft=fsleft+1  
string=string.replace('f','')
string=list(string)
for i in range(0,len(bucket)): 
	if int(bucket[i])%2==1:  
		if string[i]=='r':
			string[i]='l' 
		else: 
			print "error", string[i]
string=''.join(string)
rcount=(string.count('r')-string.count('l'))%n
if rcount>=0: 
	string='r'*rcount 
string=string+('f'*(fsleft%2))  
if string == '': 
	string='e'
print "That sequence of group operations produces the same result as %s" % string
