import math
from rotation import rotation
from fft import fft
# INPUT: f,g real sequence of length N=2^R
# OUTPUT: a tuple with the two DFTs of f and g

def fft_double(f,g):
    N=len(f)
    h=list((complex(f[j], g[j]) for j in range(N)))
    H=fft(h)
    F=[0]*N
    G=[0]*N
    F[0]=H[0].real
    G[0]=H[0].imag
    for k in range(1,N):
        F[k]=1/2*(H[N-k].conjugate()+H[k])
        G[k]=complex(0,1/2)*(H[N-k].conjugate()-H[k])
    return F, G

def realfft(f):
    N=len(f)
    f_even = f[::2]
    f_odd = f[1::2]
    F01=fft_double(f_even , f_odd)
    F0=F01[0]
    F1=F01[1]
    F=[0]*N
    T = []
    S = []
    # now i write the butterfly iteration, each term of the past iteration contributes two times at computing
    # the new terms H
    for m in range(int(N / 4)):
        T.append(math.tan(math.pi * m / N))
        S.append(math.sin(2 * math.pi * m / N))
    for k in range(int(N/2)):
        rot=rotation(F1[k], N, k, T, S)
        F[k]=F0[k]+rot
        F[k+int(N/2)]=F0[k]-rot
    return F

