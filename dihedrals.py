#i/o
print "We're going to make a dihedral. How many sides would you like it to have?" 
n = int(raw_input("Type an integer and press enter "))
print "Apply group actions. Type an 'f' for flip, 'l' for rotate left, and an 'r' for rotate right. You can type as many as you want." 
string=raw_input("Type a string and press enter ")
bucket= ""
fsleft=0 

#memoize rotations and ignore flips  
for i in string: 
	if (i=='l') or (i=='r'): 
		bucket=bucket + str(fsleft) #for bucket is a string 
	if i=='f': 
		fsleft=fsleft+1 #you don't need a placeholder in the bucket string, because f isn't added in until after r and l are resolved 
	#print "the string is %s, fsleft = %d, and bucket is %s" %(string, fsleft, bucket)
string=string.replace('f','')
#print string
string=list(string)
#switch every letter that had an odd index to its inverse 
for i in range(0,len(bucket)): 
	if int(bucket[i])%2==1: #so much pseudo code 
		if string[i]=='r':
			string[i]='l' 
			#print string
		elif string[i]=='l':
			string[i]='r'
			#print string
		else: 
			print "error", string[i]
#resolve rotations 
string=''.join(string)
rcount=(string.count('r')-string.count('l'))%n
#print "rcount", rcount
if rcount>=0: 
	string='r'*rcount 
#print string 

#add f back in 
string=string+('f'*(fsleft%2))  #super pseudo code, probably wont work 
#print string 

if string == '': 
	string='e'

print "That sequence of group operations produces the same result as %s" % string


