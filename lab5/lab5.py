import matplotlib.pyplot as plt
import numpy as np


x = np.loadtxt("lab5/Train.csv", delimiter=",", usecols=(0, 2), skiprows=1)

# dates = np.loadtxt("lab5/Train.csv", delimiter=",", usecols=(1), dtype="Datetime")

x = np.asarray(x)
points = x[:, 0]
values = x[:, 1]

n = len(points)
fs = 24

X_mean = np.fft.fft(values - values.mean())
X_mean_abs = np.abs(X_mean)


def ex1():
  """
  Frecventa de esantionare mentionata este 1/3600 HZ
  """

def ex2():
  """
  numarul de ore ocupate
  """
  return len(points) * 1



def ex3():
  """
  esantionam pe ora deci frecventa maxima ce poate fi observata din semnal este de 1 la 2h
  """

def ex4():
  fix, axs = plt.subplots(2)
  
  freqs = np.fft.fftfreq(n, d=1/fs)
  
  axs[0].plot(points, values)
  axs[1].plot(freqs[:n//2], X_mean_abs[:n//2])
  plt.savefig("ex4.pdf")
  plt.show()

def ex5():
  X = np.fft.fft(values)
  print("|X[0]| = ", np.abs(X[0]))
  """
  |X[0]| =  2541266.0
  eliminarea componentei continue este eliminata in
  
  X_mean = np.fft.fft(values - values.mean())
  X_mean_abs = np.abs(X_mean)
  """

def ex6():
  freqs = np.fft.fftfreq(n, d=1/fs)
  
  X = X_mean_abs[1:n//2]
  freqss = freqs[1:n//2]

  idx = np.argsort(X)[-4:][::-1]
  top_F = freqss[idx]
  top_X = X[idx]

  title_res = ""
  for f, x in zip(top_F, top_X):
    title_res += f"f={f:.3f};|X|={x:.1f}   "

  plt.plot(freqss, X)
  plt.stem(top_F, top_X)
  plt.title(title_res)
  plt.savefig("ex6.pdf")
  plt.show()

def ex7():
  FIRST_MONDAY = 48 + 24 * 7  * 9 # 48 - first monday + 24 * 7 (1sapt) * 9 ca sa trecem de 1000
  END_OF_MONTH = FIRST_MONDAY + 24 * 30

  val = values[FIRST_MONDAY:END_OF_MONTH]

  idx = np.arange(
    start = 1,
    stop=len(val) + 1,
    step=1
  )

  plt.plot(idx, val)
  plt.show()





if __name__ == "__main__":
  ex7()






