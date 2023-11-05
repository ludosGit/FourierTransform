import math
import rotation
from bitreverse import bitreverse3

# Computes the FFT of a sequence of length N=2^R using the decimation in time radix2 fast algorithm


def fft(h):
    N=len(h)
    R=int(math.log(N,2))
    if N==2:
        top = h[0] + h[1]
        bottom = h[0] - h[1]
        h[0]=top
        h[1]=bottom
        return h
    h=bitreverse3(h)
    T = []
    S = []
    for m in range(int(N/4)):
        T.append(math.tan(math.pi*m/N))
        S.append(math.sin(2*math.pi*m/N))
    #BUTTEFLY COMPUTATIONS
    for stage in range(R):
        future_blocks = int(math.pow(2, R - stage-1)) # number of future blocks, decreases when stage increases
        length = int(math.pow(2, stage)) # length of half future block=length one current (old) block
        for L in range(future_blocks):  # L determines the current block

            start = L * 2 *length
            middle = start + length - 1
            end = middle + length
            top=[]
            bottom=[]
            for k in range(start,middle+1): # computation of the new block through the butterflies
                m = math.pow(2, R - stage - 1) * k
                rot=rotation.rotation(h[k+length], N, m, T, S)
                top.append(h[k] + rot)  # top of the butterfly with +
                bottom.append(h[k] - rot)  # low of the butterfly with -
            h[start:middle+1] = top
            h[middle + 1: end+1] = bottom
    return h

# FFT_INVERSE to calculate the inverse dft; it is implemented identically as FFT.

def fft_inverse(h):
    N=len(h)
    R=int(math.log(N,2))
    h=bitreverse3(h)
    T = []
    S = []
    if N==2:
        top = h[0] + h[1]
        bottom = h[0] - h[1]
        h[0]=top*1/N
        h[1]=bottom*1/N
        return h
    for m in range(int(N/4)):
        T.append(math.tan(math.pi*m/N))
        S.append(math.sin(2*math.pi*m/N))
    for stage in range(R):
        future_blocks = int(math.pow(2, R - stage-1))
        length = int(math.pow(2, stage))
        for L in range(future_blocks):
            start = L * 2 *length
            middle = start + length - 1
            end = middle + length
            top=[]
            bottom=[]
            for k in range(start,middle+1):
                m = math.pow(2, R - stage - 1) * k
                rot=rotation.rotation_inverse(h[k+length], N, m, T, S)
                top.append(h[k] + rot)
                bottom.append(h[k] - rot)
            h[start:middle+1] = top
            h[middle + 1: end+1] = bottom
    h=list(i/N for i in h) # multiply each element by 1/N
    return h

