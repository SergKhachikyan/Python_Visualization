import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def generate_prism_faces(n_sides):
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

    faces.append(bottom)
    faces.append(top[::-1])

    return faces

def draw_rotating_prism(n_sides, save_as_gif=True):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])

    faces = generate_prism_faces(n_sides)

    poly = Poly3DCollection(faces, facecolors='lightblue', edgecolors='black', linewidths=1, alpha=0.8)
    ax.add_collection3d(poly)

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(0, 1.5)
    plt.axis('off')

    def update(angle):
        ax.view_init(elev=20, azim=angle)

    anim = FuncAnimation(fig, update, frames=np.linspace(0, 360, 120), interval=50)

    if save_as_gif:
        anim.save("rotating_prism.gif", writer='pillow', fps=24)
        print("Saved as rotating_prism.gif ✅")
    else:
        anim.save("rotating_prism.mp4", writer='ffmpeg', fps=24)
        print("Saved as rotating_prism.mp4 ✅")

    plt.show()

try:
    n = int(input("Enter number of sides (between 3 and 12): "))
    if 3 <= n <= 12:
        draw_rotating_prism(n, save_as_gif=True)
    else:
        print("Only values from 3 to 12 are supported.")
except ValueError:
    print("Please enter a valid integer.")