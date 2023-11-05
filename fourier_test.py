
import random
import time
from fft import fft
from fft_recursive import fft_recursive
from dft import dft
import matplotlib.pyplot as plt
from realFourier import fft_double, realfft

def create_random_array(n=10):
    return random.sample(range(2**14), n)

# TESTING THE VARIOUS DFT ALGORITHMS ON REAL DATA BY PLOTTING THE RUNNING TIMES

elements=list()
dft_times=list()
fft_times=list()
fft_rec_times=list()
fft_real_times=list()

for i in range(3,12):
    n=2**i
    h=create_random_array(n)

    start = time.time()
    dft(h)
    end = time.time()
    dft_times.append(end - start)
    print(n, "dft time ", end - start)

    start = time.time()
    fft(h)
    end = time.time()
    fft_times.append(end - start)
    print(n, "fft time ", end - start)

    start = time.time()
    fft_recursive(h)
    end = time.time()
    fft_rec_times.append(end - start)
    print(n, "rec_fft time ", end - start)

    start = time.time()
    realfft(h)
    end = time.time()
    fft_real_times.append(end-start)
    print(n, "realfft time ", end - start)

    elements.append(2 ** i)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements, dft_times, label ='DFT')
plt.plot(elements, fft_times, label ='FFT')
plt.grid()
plt.legend()
plt.show()

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements, fft_times, label ='FFT')
plt.plot(elements, fft_rec_times, label ='FFT_rec')
plt.plot(elements, fft_real_times, label ='realFFT')
plt.grid()
plt.legend()
plt.show()




