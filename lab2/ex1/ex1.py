import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sound

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(t, freq, fi = 0, a = 1):
  return a * np.sin( 2 * np.pi * freq * t + fi)

def cosinus(t, freq, fi = 0, a = 1):
  return a * np.cos( 2 * np.pi * freq * t + fi)

def saw_tooth(t, freq, fi): 
  new_t = 2 * np.pi * freq * t + fi
  return np.abs(new_t - np.floor(new_t))


def plot_with_stem(x_points, y_points, axs = plt):  
  axs.plot(x_points ,y_points)
  axs.stem(x_points, y_points)

def plot(x_points, y_points, axs = plt):  
  axs.plot(x_points ,y_points)


def gen_sound(vec, path = "wavesound.wav", play=False):
  rate = 44100

  vec = vec / np.max(np.abs(vec))
  vec = vec.astype(np.float32)
  wavfile.write(path, rate, vec)

  if play:
    sound.play(vec, rate)
    sound.wait()

def ex1():
  fig, axs = plt.subplots(2)

  points = np.arange(
    start=0,
    stop=1,
    step=0.002
  )

  sin_points = sinusoidal(points, 10, 0)
  cos_points = cosinus(points + np.pi / 2, 10, 0)

  plot(points, sin_points, axs[0])
  plot(points, cos_points, axs[1])

  fig.savefig("ex1.pdf")
  fig.show()

def ex2():
  points = np.arange(
    start=0,
    stop=1,
    step=0.002
  )

  sin_points1 = sinusoidal(points, 10, 0)
  # sin_points2 = sinusoidal(points, 10, 3)
  # sin_points3 = sinusoidal(points, 10, np.pi / 4)
  # sin_points4 = sinusoidal(points, 10, np.pi * 1.5)

  # plot(points, sin_points1, plt)
  # plot(points, sin_points2, plt)
  # plot(points, sin_points3, plt)
  # plot(points, sin_points4, plt)

  for SNR in [0.1, 1, 10, 100]:
    z = np.random.normal(size=sin_points1.shape)
    sinus = sin_points1 + z

    lamb = np.sqrt(np.linalg.norm(sinus) ** 2 / (SNR * np.linalg.norm(sin_points1) ** 2))

    new_signal = sin_points1 + lamb * sinus

    plt.plot(points, new_signal)
    plt.savefig(f"ex2.SNR_{SNR}.pdf")
    plt.show()

  # plt.savefig("ex2.1.pdf")
  # plt.show()

def ex4():
  fig, axis = plt.subplots(3)

  points = np.arange(
    start=0,
    stop=1,
    step=0.00002
  )
  
  sin_points = sinusoidal(points, 5, 0)
  saw_tooth_points = saw_tooth(points, 5, 0)

  sum_points = sin_points + saw_tooth_points

  plot(points, sin_points, axis[0])
  plot(points, saw_tooth_points, axis[1])
  plot(points, sum_points, axis[2])


  fig.savefig("ex4.pdf")
  fig.show()

def ex5():
  points = np.arange(
    start=0,
    stop=1,
    step=0.00002
  )

  sin_points1 = sinusoidal(points, 500, 0)
  sin_points2 = sinusoidal(points, 7500, 0)

  concat_sin = np.concatenate((sin_points1, sin_points2))
  concat_points = np.concatenate((points, points + 1))

  plot(concat_points, concat_sin)
  plt.show()

  gen_sound(concat_sin, play=True)

def ex6():
  fs = 50

  points = np.arange(
    start=0,
    stop=1,
    step=(1/fs)
  )

  sin_points1 = sinusoidal(points, fs / 2, 0)
  sin_points2 = sinusoidal(points, fs / 4, 0)
  # sin_points2 = sinusoidal(points, fs / 8, 0)
  sin_points3 = sinusoidal(points, 0, 0)

  fig, axs = plt.subplots(3)

  plot(points, sin_points1, axs[0])
  plot(points, sin_points2, axs[1])
  plot(points, sin_points3, axs[2])

  fig.savefig("ex6.pdf")
  fig.show()

def ex7():
  fs = 1000
  points = np.arange(
    start=0,
    stop=1,
    step=(1/fs)
  )

  fig, axs = plt.subplots(3)

  sin_points = sinusoidal(points, 300, 0)

  axs[0].set_title("Sin initial")
  axs[1].set_title("Decimal 1/4")
  axs[2].set_title("Decimal 1/4 de la al 2 element")
  plot(points, sin_points, axs[0])
  plot(points[:: 4], sin_points[:: 4], axs[1])
  plot(points[1:: 4], sin_points[1:: 4], axs[2])

  fig.savefig("ex7.pdf")
  fig.show()
  

if __name__ == "__main__":
  # ex1()
  # ex2()
  # ex3()
  # ex4()
  #ex5()            # frecventa crescuta dupa la doilea vector ascuteste semnalul
  # ex6()
  ex7()
