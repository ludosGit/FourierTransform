from fourierMultiply import fMultiply
import poly
import matplotlib.pyplot as plt
import random
import time

# TESTING THE TWO IMPLEMENTATIONS OF POLYNOMIAL MULTIPLICATION

# Test on polynomials with all the coefficients equal to 0 but the first and the last ones
def create_random_array(n=10):
    return random.sample(range(2**10), n)

n=146

random.seed(1)
c1=create_random_array(2)
p1=[0]*n
p1[0]=c1[0]
p1[n-1]=c1[1]

random.seed(2)
c2=create_random_array(2)
p2=[0]*n
p2[0]=c2[0]
p2[n-1]=c2[1]

p=fMultiply(p1,p2)

# a possible way of printing the array
# for i in range(len(p)):
#    if round(p[i].real) !=0:
#        print(p[i].real, "x^", i, "+")

p3=poly.Poly()
p3.add(c1[0],0)
p3.add(c1[1],n-1)
p4=poly.Poly()
p4.add(c2[1],n-1)
p4.add(c2[0],0)

#print(poly.pMultiply(p3,p4))

print("BINOMIAL PERFORMANCE:")
start = time.time()
fMultiply(p1,p2)
end = time.time()
print("fourier time", end - start)

start = time.time()
poly.pMultiply(p3,p4)
end = time.time()
print("linked list time ", end - start)

print("RANDOM POLYNOMIALS PERFORMANCE:")

random.seed(3)
p1=create_random_array(n)

random.seed(4)
p2=create_random_array(n)

start = time.time()
fMultiply(p1,p2)
end = time.time()
print("fourier time ", end - start)


p3=poly.Poly()
p4=poly.Poly()
for i in range(n):
    p3.add(p1[i], i)
    p4.add(p2[i], i)

start = time.time()
poly.pMultiply(p3,p4)
end = time.time()
print("linked list time ", end - start)





