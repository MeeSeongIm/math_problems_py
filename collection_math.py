# P1: the sum of all multiples of 3 or 5 below 5000
m=5000
mult_three = 0
for i in range(m):
    if i % 3==0:
        mult_three += i
mult_three  

mult_five = 0
for i in range(m):
    if i %5 ==0:
        mult_five += i 
        mult_five

common_intersection = 0
for i in range(m):
    if i %3 ==0 and i % 5==0:
        common_intersection += i
        common_intersection
    
total = mult_three + mult_five - common_intersection
print(total)


# P2: the sum of even fibonacci numbers less than 10000000. 
# fib num: 1, 2, 3, 5, 8, ...  

def fib_seq(n):
    result = []
    a = 1 
    b = 2 
    while a < n:
        result.append(a)
        a, b = b, a + b  # change input simultaneously! 
     
    subset = []
    for n in result:
        if n % 2 == 0:
            subset.append(n)
    return subset 
        
print(sum(fib_seq(10000000))) 


#P3: largest prime factor of 600851475143 
def prime_num(n):
    i=2
    while i**2 < n:
        while n % i ==0:
            n = n/i
        i+=1
    return n

print(prime_num(600851475143))


#P4: Largest palindrome integer which is the product of two 3-digit integers.
set = []
for x in range(99,1000):
    for y in range(99,1000):
        if str(x*y)==str(x*y)[::-1]:
            set.append(x*y)
new_set = []
while set:
    min = set[0]
    for x in set:
        if x < min:
            min = x
    new_set.append(min)
    set.remove(min)
print (new_set[len(new_set)-1])
# a slight problem with my code: new_set prints each palindromic number twice. 


#P6: the difference between the square of the sum of the first 100 natural numbers
#    and the sum of the squares of the first 1000 natural numbers.  

m = 0
n = 0

k = 1000

for i in range(1,k+1):
    m += i**2
    n += i
    
n = n**2

print(n-m)


#P8: 
num = str(73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450)

n = [int(num[i]) for i in range(0, len(num))] 
k=13
l=[] 
 
for i in range(0, len(n)-k+1):
    if i !=0:        # write a recursion such that if any of the items of n between (i)th to (i+k)th position equals 0, then ignore all computation below. 
        l.append(n[i]*n[i+1]*n[i+2]*n[i+3]*n[i+4]*n[i+5]*n[i+6]*n[i+7]*n[i+8]*n[i+9]*n[i+10]*n[i+11]*n[i+12]) # using python 3.*: figure out the correct syntax (iteration) to make this more compact.
print(max(l))


#P9: find abc for which (a,b,c) is the Pythagorean tuple for which a+b+c = 1000. 
#a = int(a) < b
#b = int(b) < c
#c = int(c) < 1000

for c in range(1,1000):
    for b in range(1,c):
        for a in range(1,b):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a*b*c)




# P25: the first term in the Fibonacci sequence to contain 1000 digits.  

list = []
a = 1
b = 1
n = 5*10**1000
while a < n:
    list.append(a)
    a, b = b, a+b

 
 
for k in range(len(list)):
    if list[k] > 10**999:
        print(list[k])
        print(k)
        

#P44. find the minimum among the difference of those pentagonal numbers whose difference and sum are also pentagonal numbers. 
def penta(n):
    for i in range(1,n+1):
        yield i*(3*i-1)/2

set_penta = set(penta(3000))
output = {m-n for m in set_penta for n in set_penta if m-n in set_penta and m+n in set_penta}
print(min(output))

#P45. find the triangle number greater than 40755 which is also pentagonal and hexagonal. 
#Note: if x is a hexagonal number, then it is also a triangular number. Prove this by replacing n with 2n-1.
 
def triangle(n):
    for i in range(1,n+1):
        yield i*(i+1)/2

def pentagonal(n):
    for i in range(1,n+1):
        yield i*(3*i-1)/2

def hexagonal(n):
    for i in range(1,n+1):
        yield i*(2*i-1)

triangle_set = set(triangle(56000))
pentagonal_set = set(pentagonal(40000))

print({m for m in pentagonal_set if m in triangle_set and m >5482660})


#P48. Find the last 10 digits of the finite sum  \sum_i=1^{1000} i^i

N = sum(i**i for i in range(1,1001))
M = str(N)
print(M[len(M)-10:len(M)])





#P50. Which prime below 1000000 can be written as the sum of the most consecutive primes?
# Example: 41 can be written as the sum of 6 consecutive primes. 
# 41 = 2+ 3 + 5 + 7 + 11+ 13
# rewrite this code with lower complexity and remove unnecessary computations.  

N = 1000000

import math
def detecting_primes(n):
    if n < 1:
        return []
    prime_list = [2]
    j = 3
    while n > len(prime_list):
        for i in range(len(prime_list)):
            if j % prime_list[i] == 0:
                break
            if prime_list[i] > math.sqrt(j):
                prime_list.append(j)
                break

        j += 2
    return prime_list

print(detecting_primes(N)) 

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
        else:
            return True
 
sum_of_consecutive_primes = []
   
for j in list(range(N))[::-1]:
    for i in list(range(0,N)):
        partial_sum = sum(detecting_primes(N)[k] for k in range(i,j))  
        if is_prime(partial_sum) == True:
            sum_of_consecutive_primes.append(partial_sum)  

print(sum_of_consecutive_primes)    
 







