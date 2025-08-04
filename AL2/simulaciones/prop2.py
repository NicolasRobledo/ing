import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Vector fijo
v = np.array([3, 1, 2.5])

# Recta proporcional: r(λ) = (3λ, λ, 2.5λ)
lambdas = np.linspace(-5, 5, 200)
x_vals = 3 * lambdas
y_vals = lambdas
z_vals = 2.5 * lambdas

# Plano z = 5
X, Y = np.meshgrid(np.linspace(-10, 10, 30), np.linspace(-10, 10, 30))
Z = np.full_like(X, 5)

# Crear figura
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la recta
ax.plot(x_vals, y_vals, z_vals, label='Recta: (3λ, λ, 2.5λ)', linewidth=2)

# Graficar el vector desde el origen
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='fuchsia', label='Vector v = (3, 1, 2.5)', arrow_length_ratio=0.1)

# Graficar el plano z = 5 sin label
surf = ax.plot_surface(X, Y, Z, alpha=0.3, color='skyblue')

# Agregar punto (6, 2, 5) en rojo
ax.scatter(6, 2, 5, color='red', s=50, label='Punto (6, 2, 5)')
ax.text(6, 2, 5.5, '(6, 2, 5)', color='red')

# Crear proxy artist para el plano
custom_patch = Patch(facecolor='skyblue', edgecolor='gray', label='Plano z = 5')

# Mostrar leyenda
ax.legend(handles=[custom_patch, *ax.get_legend_handles_labels()[0]])

# Configurar ejes
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector, recta proporcional, plano z = 5 y punto (6, 2, 5)')

# Mostrar gráfico
plt.show()
