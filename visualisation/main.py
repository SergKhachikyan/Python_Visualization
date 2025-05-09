import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_prism(n_sides):
    angle = np.linspace(0, 2 * np.pi, n_sides, endpoint=False)
    radius = 1
    z_bottom = 0
    z_top = 1

    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    bottom = list(zip(x, y, [z_bottom] * n_sides))
    top = list(zip(x, y, [z_top] * n_sides))

    faces = []

    for i in range(n_sides):
        faces.append([bottom[i],
                      bottom[(i + 1) % n_sides],
                      top[(i + 1) % n_sides],
                      top[i]])

    # Основания
    faces.append(bottom)
    faces.append(top[::-1])  

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.add_collection3d(Poly3DCollection(faces, facecolors='lightblue', edgecolors='black', linewidths=1, alpha=0.8))

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(0, 1.5)

    plt.axis('off')
    plt.show()

try:
    n = int(input("Введите количество углов (от 3 до 12): "))
    if 3 <= n <= 12:
        draw_prism(n)
    else:
        print("Поддерживаются значения от 3 до 12.")
except ValueError:
    print("Введите корректное целое число.")
