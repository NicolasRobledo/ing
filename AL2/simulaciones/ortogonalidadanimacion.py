import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crear figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configurar límites y etiquetas
ax.set_xlim(0, 30)
ax.set_ylim(-6, 6)
ax.set_zlim(-2, 6)
ax.set_xlabel('x²')
ax.set_ylabel('x−1')
ax.set_zlabel('z = 3')
ax.set_title('Vector U(x) = (x², x−1, 3) animado con vectores fijos')

# Rango de x para animación
x_vals = np.linspace(-5, 5, 100)
X = x_vals**2
Y = x_vals - 1
Z = np.full_like(x_vals, 3)

# Dibujar trayectoria curva
ax.plot(X, Y, Z, color='gray', linestyle='--', linewidth=1.5, label='Trayectoria de U(x)')

# 🔴 Vector fijo en x = -1 → (1, -2, 3)
ax.quiver(0, 0, 0, 1, -2, 3, color='red', label='U(-1) = (1, -2, 3)')

# 🟢 Vector fijo en x = 2 → (4, 1, 3)
ax.quiver(0, 0, 0, 4, 1, 3, color='green', label='U(2) = (4, 1, 3)')

# 🟣 Vector adicional V = (1, -1, -1)
ax.quiver(0, 0, 0, 1, -1, -1, color='purple', label='V = (1, -1, -1)')

# Inicializar vector animado y texto
vector = ax.quiver(0, 0, 0, 0, 0, 0, color='blue')
text_x = ax.text2D(0.05, 0.95, "", transform=ax.transAxes)

# Función de actualización
def update(frame):
    global vector
    vector.remove()  # eliminar vector anterior

    x = x_vals[frame]
    u_x = x**2
    u_y = x - 1
    u_z = 3

    # Dibujar vector animado en azul
    vector = ax.quiver(0, 0, 0, u_x, u_y, u_z, color='blue')

    # Mostrar valor actual de x
    text_x.set_text(f"x = {x:.2f}")
    return vector, text_x

# Crear animación
ani = FuncAnimation(fig, update, frames=len(x_vals), interval=60, blit=False)

# Mostrar leyenda y gráfico
ax.legend()
plt.show()

