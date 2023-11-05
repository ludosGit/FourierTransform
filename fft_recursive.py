import rotation
import math

# RECURSIVE IMPLEMENTATION OF FFT ALGORITHM

def fft_recursive(h):
    N= len(h) #power of 2
    if N==2:
        return [h[0]+h[1], h[0]-h[1]]
    H = [0] * N
    h_even = h[::2]
    h_odd = h[1::2]
    T = []
    S = []
    for m in range(int(N / 4)):
        T.append(math.tan(math.pi * m / N))
        S.append(math.sin(2 * math.pi * m / N))
    H0=fft_recursive(h_even)
    H1=fft_recursive(h_odd)
    for k in range(int(N/2)):
        rot=rotation.rotation(H1[k], N, k, T, S)
        H[k]=H0[k]+rot
        H[k+int(N/2)]=H0[k]-rot
    return H

