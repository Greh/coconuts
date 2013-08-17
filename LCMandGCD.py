#I/O
#make a sieve big enough for the numbers 
#find a way to get prime factorization and calculate LCM and GCD 

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
print primes #this is for testing if you actually created an array of just prime numbers 
#Begin prime factorization and simultaneously solving for lcm and gcd 
#options: send both numbers through at the same time 
def primeindex(gamma, kappa):
	GCD=1
	LCM=1
	i=0
	while gamma>=primes[i] or kappa>=primes[i]: 
		if gamma%primes[i]==0 and kappa%primes[i]==0:
			gamma=gamma/primes[i]
			kappa=kappa/primes[i]
			GCD=GCD*primes[i]
			LCM=LCM*primes[i] 
			#print "alpha divided by ", primes[i], "is ", gamma, "beta divided by ", primes[i], "is ", kappa, "and the greatest common divisor is ", GCD
		elif gamma%primes[i]==0 and kappa%primes[i]!=0: 
			gamma=gamma/primes[i] 
			LCM=LCM*primes[i] #I FIGURED IT OUT!!!!!! ITS NOT ADDING UP PRIMES THAT WERE CAUGHT BY THE GCD TEST!!!
			#print "alpha divided by ", primes[i], "is ", gamma, "beta divided by ", primes[i], "is ", kappa, "and the least common multiple is ", LCM 
		elif gamma%primes[i]!=0 and kappa%primes[i]==0: 	
			kappa=kappa/primes[i]
			LCM=LCM*primes[i]
			#print "alpha divided by ", primes[i], "is ", gamma, "beta divided by ", primes[i], "is ", kappa, "and the least common multiple is ", LCM 
		else: 
			i=i+1
	return GCD, LCM 
GCD,LCM=primeindex(alpha, beta)
print "gcd is ",GCD, "lcm is ",LCM 
	
	
	

