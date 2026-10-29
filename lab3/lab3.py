import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

from matplotlib.animation import FuncAnimation

def signal(
  t,
  freq,
  fi=0,
):
  return np.sin(2 * np.pi * freq * t + fi)

def get_Fourier(
  N
):
  F = np.zeros((N, N), dtype=complex)
  
  for omega in range(N):
    for n in range(N):
      F[omega, n] = math.e ** (math.pi * -2j * omega * n / N)

  return F


def ex1():
  fig, axs = plt.subplots(N, 2, figsize=(8, 12), sharex=True, sharey=True)
  
  for omega in range(N):
    axs[omega, 0].stem(F[omega].real, basefmt=" ")
    axs[omega, 0].plot(F[omega].real)
    axs[omega, 1].stem(F[omega].imag, linefmt="C1-", markerfmt="C1o", basefmt=" ")
    axs[omega, 1].plot(F[omega].imag)
    axs[omega, 0].set_ylabel(f"omega={omega}")
  
  axs[0,0].set_title('Real')
  axs[0,1].set_title("Imaginar")
  plt.savefig("ex1.pdf")
  plt.show()

  FH = F.conj().T
  print(np.allclose(FH @ F, N * np.eye(N)))



def ex2():
  fs = 1000
  points = np.arange(
    start=0,
    stop=1,
    step=1/fs
  )


  ## fig 1
  sign_points = signal(points, 7)
  y_points = sign_points * np.exp(-2j * math.pi * points)

  fig, axs = plt.subplots(2)

  axs[0].plot(points, sign_points)
  axs[1].scatter(y_points.real, y_points.imag, c=np.abs(y_points), cmap="viridis", s=2)
  axs[1].set_aspect('equal')

  plt.savefig("fig1-static.pdf")
  plt.show()

  ## fig 2
  fix, axs = plt.subplots(4)
  for i, omega in enumerate([1, 2, 5, 7]):
    z_points = sign_points * np.exp(-2j * math.pi * points * omega)

    axs[i].scatter(z_points.real, z_points.imag, c=np.abs(z_points), cmap="viridis", s=2)
    axs[i].set_title(f"omega={omega}")
    axs[i].set_aspect('equal')

  plt.savefig("fig2-static.pdf")
  plt.show()



def ex2_animatie():
  fs = 1000
  points = np.arange(
    start=0,
    stop=1,
    step=1/fs
  )

  sign_points = signal(points, 7)
  y_points = sign_points * np.exp(-2j * math.pi * points)
  dist = np.abs(y_points)

  def update(frame, step = 5):
    
    k = frame * step
    sc_time.set_offsets(np.column_stack([points[:k], sign_points[:k]]))
    sc_time.set_array(dist[:k])
    sc_circ.set_offsets(np.column_stack([y_points.real[:k], y_points.imag[:k]]))
    sc_circ.set_array(dist[:k])

    i = min(k, len(points) - 1)
    dot_time.set_data([points[i]], [sign_points[i]])
    stick_time.set_data([points[i], points[i]], [0, sign_points[i]])
    dot_circ.set_data([y_points.real[i]], [y_points.imag[i]])
    stick_circ.set_data([0, y_points.real[i]], [0, y_points.imag[i]])

    return sc_time, sc_circ, dot_time, stick_time, dot_circ, stick_circ

  
  ## fig 1
  
  
  fig, axs = plt.subplots(1, 2)

  axs[0].set_xlim(0, 1);       axs[0].set_ylim(-1.1, 1.1)
  axs[1].set_xlim(-1.1, 1.1);  axs[1].set_ylim(-1.1, 1.1)
  axs[1].set_aspect('equal')

  sc_time = axs[0].scatter([], [], c=[], cmap='viridis', vmin=0, vmax=1, s=2)
  sc_circ = axs[1].scatter([], [], c=[], cmap='viridis', vmin=0, vmax=1, s=2)

  dot_time, = axs[0].plot([], [], 'ro')
  stick_time, = axs[0].plot([] , [], 'r-')
  dot_circ, = axs[1].plot([], [], 'ro')
  stick_circ, = axs[1].plot([], [], 'r-')

  step = 5

  anim = FuncAnimation(
    fig,
    update,
    frames=len(points) // 5 + 1,
    interval=20,
    blit=True,
    repeat=False
  )

  plt.show()
    

def ex3():
  fs = 1000
  points = np.arange(
    start=0,
    stop=1,
    step=1/fs
  )

  sign = 3 * signal(points, 10) + 7 * signal(points, 25) + 0.5 * signal(points, 75) + 1.5 * signal(points, 40)

  fix, axs = plt.subplots(2)

  axs[0].plot(points, sign)
  N = len(sign)
  omegas = range(1, 101)

  X = np.zeros(len(omegas), dtype=complex)
  for i, omega in enumerate(omegas):
    s = 0 + 0j
    for n in range(N):
      s += sign[n] * np.exp(-2j * math.pi * n * omega / N)
    X[i] = s

  mod = np.abs(X)

  axs[1].plot(omegas, mod)
  plt.savefig("ex3.pdf")
  plt.show()



if __name__ == "__main__":  
  N = 8
  F = get_Fourier(N)

  # print(F)
  # ex1()
  # ex2()
  # ex2_animatie()
  ex3()






    
  
  