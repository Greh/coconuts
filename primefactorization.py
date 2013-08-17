#I/O
#make a sieve big enough for the numbers 
#find a way to get prime factorization of a number
#use prime factorization to find least common multiple 
#use prime factorization to fid greatest common divisor

#Begin I/O
alpha=int(raw_input("pick a number and press enter "))
beta=int(raw_input("pick another number and press enter ")) 
#print alpha, beta #for testing purposes, might be added back later to verify correct numbers 
#eratosthenes
end= max(alpha+1, beta+1) #because the index starts at zero it will end at alpha/beta not one number higher 
bucket = [];
primes = []; 
for i in range(0,end): #creates an array of zeroes length end 
    bucket.append(0);
#print bucket
j=2
while j**2<=end: 
	for i in range(j+j, len(bucket), j): 
		bucket[i]=1
	#print bucket #soley for testing each step of the sieve 
	j=j+1
bucket[0]=1 #this line tells the sieve that 0 is not prime 
bucket[1]=1 #this line tells the sieve that 1 is not a prime 
#print bucket #for testing the sieve after it has finished (will give you an array of 0s and 1s where the 0s are primes
for i in range(0,len(bucket)):  #this for loop puts the prime numbers in bucket into the array named primes
	if bucket[i]==0: 
		primes.append(i); 
	i=i+1 #this line shouldn't be necessary 
#print primes #this is for testing if you actually created an array of just prime numbers 
#Begin prime factorization 
def primeindex(gamma): 
	gammaprimeindex = [0,0]; #gamma is a placeholder for now 
	i=0
	while gamma>=i: #divide gamma by increasingly larger prime numbers 
		if gamma%primes[i]==0: #if gamma is divisible by the ith prime 
			gamma=gamma/primes[i]
			#print gamma #for testing 
			gammaprimeindex[i]=gammaprimeindex[i]+1
		else: 
			i=i+1 
			gammaprimeindex.append(0); 
	while len(gammaprimeindex)<len(primes): 
		gammaprimeindex.append(0); 
	return gammaprimeindex
	#print gammaprimeindex #for testing if it found the prime index properly
alphaindex=primeindex(alpha) #alphaindex is the prime factorization of alpha stored as an array
betaindex=primeindex(beta) #betaindex is the prime factorization of beta stored as an array
#print alphaindex #for verifying if the prime factorization is correct
#print betaindex #for verifying if the prime factorization is correct
#Begin finding GCD using prime factorization 
delta=1; 
for i in range(0,len(primes)): 
	if alphaindex[i]>=betaindex[i]: 
		delta=delta*(primes[i]**betaindex[i])
	else: 
		delta=delta*(primes[i]**alphaindex[i]) 
print "the greatest common divisor is ", delta 
#Begin finding LCM using prime factorization 
kappa=1;
for i in range(0,len(primes)):
	if alphaindex[i]>=betaindex[i]:
		kappa=kappa*(primes[i]**alphaindex[i])
	else:
		kappa=kappa*(primes[i]**betaindex[i])
print "the least common multiple is ", kappa

#I should have labelled delta and kappa GCD and LCM







	
