import matplotlib.pyplot as plt
import numpy as np


FREQ = 400
FI = 0

def f_semnal(
  t,
  freq,
  fi,
):
  return np.sin(freq * np.pi * t + fi)


def square(t, freq, fi): 
  return np.sign(np.sin(2 * np.pi * freq * t + fi))

def sine(t, freq, fi):
  return np.sin(2 * np.pi * t * freq + fi)

def triangle(t, freq, fi):
  new_t = 2 * np.pi * freq * t + fi
  return new_t - np.floor(new_t + 0.5)

def saw_tooth(t, freq, fi): 
  new_t = 2 * np.pi * freq * t + fi
  return np.abs(new_t - np.floor(new_t))



def plot_with_stem(x_points, y_points, axs):  
  axs.plot(x_points ,y_points)
  axs.stem(x_points, y_points)

def plot(x_points, y_points, axs):  
  axs.plot(x_points ,y_points)




def ex_2a():
  points = np.arange(
    start=0,
    stop=1,
    step=1 / 1600
  )
  
  f_points = [f_semnal(t, FREQ, FI) for t in points]
  
  plot_with_stem(points[0: 100], f_points[0: 100], plt)
  plt.savefig("2a.pdf")
  plt.show()

def ex_2b():
  points = np.arange(
    start=0,
    stop=3,
    step=0.002
  )
  
  # f_points = [square(t) for t in points]
  f_points = [f_semnal(t, 800, 0) for t in points]
  
  plot_with_stem(points[0: 100], f_points[0: 100], plt)
  plt.savefig("2b.pdf")
  plt.show()

def ex_2c():
  points = np.arange(
    start=0,
    stop=3,
    step=0.002
  )

  f_points = [saw_tooth(t, 240, 0) for t in points]

  plot_with_stem(points[0: -1: 10], f_points[0: -1: 10], plt)
  plt.savefig("2c.pdf")
  plt.show()

def ex_2d():
  points = np.arange(
    start=0,
    stop=3,
    step=0.0001
  )

  fig, axs = plt.subplots(2)

  f_points = [square(t, 300, 0) for t in points]

  # plot_with_stem(points[0: -1: 10], f_points[0: -1: 10], plt)
  plot(points, f_points, axs[0])
  plot(points[0:100], f_points[0:100], axs[1])
  fig.savefig("2d.pdf")
  plt.show()

def ex_2e():
  points = np.random.rand(128, 128)
  plt.imshow(points)
  plt.savefig("2e.pdf")
  plt.show()

def ex_2f():
  def gen_image():
    row = 128
    cols = 128

    dist = 30

    image = np.zeros((row, cols))

    center_r = row // 2
    center_c = cols // 2

    for i in range(row):
      for j in range(cols):
        distance = np.sqrt((i - center_r)**2 + (j - center_c)**2)
        if distance < dist:
          image[i, j] = np.random.rand()

    return image

  points = gen_image()
  plt.imshow(points)
  plt.savefig("2f.pdf")
  plt.show()

if __name__ == "__main__":
  # ex_2a()
  # ex_2b()
  # ex_2c()
  # ex_2d()
  # ex_2e()
  ex_2f()


