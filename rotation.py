
# "rotation" calculates Z*W^m where W=e^(-i*2pi*m/N) and Z is any complex number
# INPUT: Z, an integer N=2^R greater or equal than 4, m integer greater than 0,
# T and S are two lists of length N/4 such as T[m]=tan(pi*m/N) and S[m]=sin(2*pi*m/N)

def rotation(Z, N, m, T, S):
    A=Z.real
    B=Z.imag
    m=int(m % N)
    if m<(N / 4):
        V = T[m] * A - B
        Re = A - S[m] * V
        Im = -V - T[m] * Re
    elif m < (N / 2):
        V = T[int(m - N / 4)] * B + A
        Re = B - S[int(m - N / 4)] * V
        Im = -V - T[int(m - N / 4)] * Re
    elif m < (3 * N / 4):
        V = T[int(m - N / 2)] * A - B
        Re = -(A - S[int(m - N / 2)] * V)
        Im = -(-V - T[int(m - N / 2)] * (-Re))
    else:
        V = T[int(m - (3*N/4))] * B + A
        Re = -(B - S[int(m - (3*N/4))] * V)
        Im = -(-V - T[int(m - (3*N/4))] * (-Re))
    return complex(Re,Im)

# Similarly,  "rotation_inverse" calculates Z*W^m where W=e^(i*2pi*m/N) and Z is any complex number.
# It is needed to compute the inverse DFT.

def rotation_inverse(Z, N, m, T, S):
    A=Z.real
    B=Z.imag
    m=int(m % N)
    if m<(N / 4):
        V = T[m] * A + B
        Re = A - S[m] * V
        Im = V + T[m] * Re
    elif m < (N / 2):
        V = -T[int(m - N / 4)] * B + A
        Re = -B - S[int(m - N / 4)] * V
        Im = V + T[int(m - N / 4)] * Re
    elif m < (3 * N / 4):
        V = T[int(m - N / 2)] * A + B
        Re = -(A - S[int(m - N / 2)] * V)
        Im = -(V + T[int(m - N / 2)] * (-Re))
    else:
        V = -T[int(m - (3*N/4))] * B + A
        Re = -(-B - S[int(m - (3*N/4))] * V)
        Im = -(V + T[int(m - (3*N/4))] * (-Re))
    return complex(Re,Im)

