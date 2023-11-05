# BRUTE FORCE IMPLEMENTATION OF BITREVERSE ALGORITHM

import math

# INPUT: two integers n and k, where k is the number of bits
# OUTPUT: list representing the bit reversed permutation of the binary representation of n

def bitrev(n,k):
    if n>=(2**k):
        return None
    b=[0]*k
    k=int(math.log(n,2))+1
    # I start from the log because the other elements are 0
    r=1
    while r>0:
        q=n//(2**(k-1))
        r=n%(2**(k-1))
        if q>0:
            b[k-1]=1
            n=r
        k-=1
    return b

# INPUT: a list of 0 and 1 bits
# OUTPUT: the decimal representation of the binary number

def decimal(b):
    x=0
    R=len(b)
    for k in range(R):
        if b[R-k-1]!=0:
            x+=2**k
    return x


# INPUT: h list of length N power of 2
# OUTPUT: list with the elements of h sorted in bit reversed order
def bitreverse(h):
    N=len(h) #power of 2
    R=int(math.log(N,2))
    k=[0]*N
    for i in range(1,N):
        b=decimal(bitrev(i,R))
        k[b]=h[i]
    return k


# BUNEMAN'S ALGORITHM
# INPUT: a radix 2 number N=2^R
# OUTPUT: a list with the bitreversal permutation of 0,1,.., N-1

def bitreverse2(N):
    if N==2:
        return [0,1]
    y=[2*l for l in bitreverse2(N/2)]
    z=[_+1 for _ in y]
    return y+z


# MOST EFFICIENT BITREVERSE ALGORITHM

# INPUT: a list of length N=2^R
# OUTPUT: list with the elements of h sorted in bit reversed order

def bitreverse3(h):
    N=len(h)
    R=int(math.log(N,2))
    if R==1:
        return h
    rev=h[:]
    if R % 2 == 0:
        M=int(math.sqrt(N))
        y=bitreverse3(list(range(M)))
        for K in range(1 , M):
            for L in range(K):
                n=int(y[K]*M+L)
                nrev=int(y[L]*M+K)
                rev[n]=h[nrev]
                rev[nrev]=h[n]
        return rev
    else:
        M = int(math.sqrt(N/2))
        y = bitreverse3(list(range(M)))
        for K in range(1, M):
            for L in range(K):
                n = y[K]*2*M+L
                nrev = y[L]*2*M+K
                #4 swaps for c=0 and c=1
                rev[n] = h[nrev]
                rev[nrev] = h[n]
                rev[n+M]=h[nrev+M]
                rev[nrev+M]=h[n+M]
        return rev
