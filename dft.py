import math
from rotation import rotation

# Radix 2 DFT using the rotation function

def dft(h):
    N=len(h) #must be a power of 2
    T=[]
    S=[]
    H=[0]*N
    if N==2:  # case in which we cannot compute the sines and tangents
        H[0]=h[0]+h[1]
        H[1]=h[0]-h[1]
        return H

    for m in range(int(N/4)):
        T.append(math.tan(math.pi*m/N))
        S.append(math.sin(2*math.pi*m/N))
    for k in range(N):
        for j in range(N):
            m=j*k
            H[k]+=rotation(h[j],N,m,T,S)
    return H




