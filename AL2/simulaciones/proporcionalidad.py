import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear figura y ejes 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Vector fijo: v = (3, 1, -2.5)
v = np.array([3, 1, 2.5])
ax.quiver(0, 0, 0, *v, color='fuchsia', label='v = (3, 1, 2.5)')

# Plano parametrizado: r(s, t) = (-1 + s + t, s, 5 - 5t)
x_vals = np.linspace(-10, 10, 30)
y_vals = np.linspace(-10, 10, 30)
x, y = np.meshgrid(x_vals, y_vals)

X = y - 1
Y = x
Z = np.full_like(X, 5)

# Dibujar el plano
ax.plot_surface(X, Y, Z, alpha=0.6, color='lightblue', edgecolor='gray')

# Agregar el vector u = (6, 2, 5)
u = np.array([6, 2, 5])
ax.quiver(0, 0, 0, *u, color='blue', label='u = (6, 2, 5)')

# Configurar ejes y etiquetas
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plano parametrizado con vectores v y u')
ax.legend()

# Mostrar gráfico
plt.show()
