print "We're going to make a dihedral. How many sides would you like it to have?" 
n = int(raw_input("Type an integer and press enter "))
print "Apply group actions. Type an 'f' for flip  and an 'r' for rotate right. You can type as many as you want." 
string=raw_input("Type a string and press enter ")
bucket= ""
fsleft=0 
for i in string: 
	if i=='r': 
		bucket=bucket + str(fsleft) #for bucket is a string 
	if i=='f': 
		fsleft=fsleft+1 #you don't need a placeholder in the bucket string, because f isn't added in until after r and l are resolved 
string=string.replace('f','')
string=list(string)
for i in range(0,len(bucket)): 
	if int(bucket[i])%2==1: #so much pseudo code 
		if string[i]=='r':
			string[i]='l' 
		else: 
			print "error", string[i]
string=''.join(string)
rcount=(string.count('r')-string.count('l'))%n
if rcount>=0: 
	string='r'*rcount 
string=string+('f'*(fsleft%2))  #super pseudo code, probably wont work 
if string == '': 
	string='e'
print "That sequence of group operations produces the same result as %s" % string
