import fft
import math

#Fourier multiplication of polynomials
#I assume that p1 and p2 are two list of length N=2^R

def fMultiply(p1,p2):
    n1=len(p1)
    n2=len(p2)
    R=int(math.log(max(n1,n2) , 2))+1
    N=2**R
    while n1 < (2*N):
        n1 += 1
        p1.append(0)
    while n2 < (2*N):
        n2+=1
        p2.append(0)
    f1=fft.fft(p1)
    f2=fft.fft(p2)
    f3=list(f1[k]*f2[k] for k in range(2*N) )
    return fft.fft_inverse(f3)








