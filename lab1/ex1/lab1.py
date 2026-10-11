import matplotlib.pyplot as plt
import numpy as np

NUMBER = 200
STEP = 0.0005

def x(t):
  return np.cos(520 * np.pi * t + np.pi / 3)

def y(t):
  return np.cos(280 * np.pi * t - np.pi / 3)

def z(t):
  return np.cos(120 * np.pi * t + np.pi / 3)

def plot_with_stem(x_points, y_points, axs):  
  axs.plot(x_points ,y_points)
  axs.stem(x_points, y_points)



if __name__ == "__main__":
  points = np.arange(
    start=0, 
    stop=3,
    step=STEP
  )

  # ex 1:
  x_points = [x(t) for t in points]
  y_points = [y(t) for t in points]
  z_points = [z(t) for t in points]

  fig, axs = plt.subplots(3)
  LEN_PER_SEC = len(points) // 3
  FREQ = 200
  UP_BOUND = LEN_PER_SEC // FREQ 

  # plot_with_stem(
  #   points[0: LEN_PER_SEC: UP_BOUND], 
  #   x_points[0: LEN_PER_SEC: UP_BOUND], 
  #   axs[0]
  # )
  # plot_with_stem(
  #   points[0: LEN_PER_SEC: UP_BOUND], 
  #   y_points[0: LEN_PER_SEC: UP_BOUND], 
  #   axs[1]
  # )
  # plot_with_stem(
  #   points[0: LEN_PER_SEC: UP_BOUND], 
  #   z_points[0: LEN_PER_SEC: UP_BOUND], 
  #   axs[2]
  # )

  fig.savefig("1c.pdf", bbox_inches="tight")
  plt.show()

  print("FINISHED")