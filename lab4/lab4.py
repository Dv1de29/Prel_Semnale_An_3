import numpy as np
import matplotlib.pyplot as plt
import math
import time
from scipy.io import wavfile


def signal(
  t,
  freq,
  fi=0,
):
  return np.sin(2 * np.pi * freq * t + fi)

def X_k(
  singn_points,
  N,
  k,
):
  n = np.arange(N)
  return np.sum(singn_points * np.exp(-2j * math.pi * k * n / N))


def dft(x):
  N = len(x)
  n = np.arange(N)
  k = n.reshape((N, 1))
  W = np.exp(-2j * math.pi * k * n / N)

  return W @ x


def fft(x):
  N = len(x)

  if N == 1:
    return x

  M = N // 2 
  W = np.exp(-2j * math.pi * np.arange(M) / N)

  diag = np.zeros((M, M))
  p = 0
  for i in range(M):
    diag[i][i] = W ** p
    p += 1

  zT = fft(x[::2])
  zB = fft(x[1::2])

  return np.concatenate[zT + zB, zT - zB]

def measure_dif(N):
  times_dft = []
  times_fft = []
  times_np_fft = []

  for n in N:
    points  = np.linspace(0, 1, n)
    sin_points = signal(points, 10)

    start = time.perf_counter()
    dft(sin_points)
    end = time.perf_counter()
    dft_res = end - start

    start = time.perf_counter()
    dft(sin_points)
    end = time.perf_counter()
    fft_res = end - start

    start = time.perf_counter()
    np.fft.fft(sin_points)
    end = time.perf_counter()
    np_fft_res = end - start

    times_fft.append(fft_res)
    times_dft.append(dft_res)
    times_np_fft.append(np_fft_res)

  plt.plot(N, times_dft)
  plt.plot(N, times_fft, "--")
  plt.plot(N, times_np_fft, ":")

  plt.savefig("ex1.pdf")
  plt.show()

  
def ex2(fs=10, f1=7, save_path="ex2.pdf",):
  points = np.linspace(0, (10 - 1) / fs, 500)

  points_samp = np.arange(10) / fs

  f2 = fs + f1
  f3 = fs * 3 + f1

  sin1 = signal(points, f1)
  sin2 = signal(points, f2)
  sin3 = signal(points, f3)

  fix, axs = plt.subplots(3)

  axs[0].plot(points, sin1)
  axs[0].stem(points_samp, signal(points_samp, f1))
  # axs[0].stem(points, sin1)
  axs[1].plot(points, sin2)
  axs[1].stem(points_samp, signal(points_samp, f2))
  # axs[1].stem(points, sin2)
  axs[2].plot(points, sin3)
  axs[2].stem(points_samp, signal(points_samp, f3))
  # axs[2].stem(points, sin3)

  plt.savefig(save_path)
  plt.show()

def ex3():
  fs = 20
  points = np.linspace(0, (10 - 1) / fs, 500)
  
  points_samp = np.arange(10) / fs

  f1 = 7
  f2 = 15
  f3 = 35
  
  sin1 = signal(points, f1)
  sin2 = signal(points, f2)
  sin3 = signal(points, f3)
  
  fix, axs = plt.subplots(3)
  
  axs[0].plot(points, sin1)
  axs[0].stem(points_samp, signal(points_samp, f1))
    # axs[0].stem(points, sin1)
  axs[1].plot(points, sin2)
  axs[1].stem(points_samp, signal(points_samp, f2))
    # axs[1].stem(points, sin2)
  axs[2].plot(points, sin3)
  axs[2].stem(points_samp, signal(points_samp, f3))
    # axs[2].stem(points, sin3)
  
  plt.savefig("ex_3.pdf")
  plt.show()

def ex4():
  """
  Semnalul poate avea frecventa maxima de 200Hz, deci trb sa esantionam cu >400Hz
  """
  pass

def ex5():
  pass

def ex6():
  rate, data = wavfile.read("wavesound.wav")
  print(rate, data.shape, data.dtype)
  pass  

def ex7():
  """
  SNRdb = 80 = 10*lg(SNR) -> 10*lg(P_semnal/P_zgomot)
        = 10 (lg(P_semanal) - lg(P_zgomot))
        = P_semanal dB - P_semanl dB -> P_zgomot dB = 10
  """


if __name__ == "__main__":
  # measure_dif([128, 256, 512, 1024, 2048, 4096, 8192])
  # ex2()
  # ex3()
  ex6()