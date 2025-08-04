# 🧲 Nota completa: Campo magnético de un alambre recto y delgado con corriente

---

## 📘 Enunciado del problema

> **1.** Considere un alambre recto y delgado que conduce una corriente constante $I$ y que se coloca a lo largo del **eje x**, como se muestra en la figura. Determine la **magnitud y dirección del campo magnético** en el punto $P$ debido a esta corriente.

---

## 🧠 Interpretación del problema

- El alambre es **recto y largo**, y está ubicado a lo largo del eje $x$.
- El punto $P$ está ubicado a una distancia perpendicular $a$ sobre el eje $y$, es decir, sobre el eje vertical.
- Por la **regla de la mano derecha**, la corriente que circula por el alambre genera un **campo magnético circular** alrededor del alambre.
- Se desea calcular el **campo magnético total** en el punto $P$, que está en el plano perpendicular al alambre.

---

## 🧬 Ley de Biot–Savart: origen de la fórmula

La **Ley de Biot–Savart** se utiliza para calcular el campo magnético generado por un elemento de corriente:

$$
d\vec{B} = \frac{\mu_0}{4\pi} \cdot \frac{I\, d\vec{s} \times \hat{r}}{r^2}
$$

### Significado de cada término:
- $\mu_0$: permeabilidad del vacío (constante).
- $I$: corriente que circula por el conductor.
- $d\vec{s}$: elemento de longitud del alambre en la dirección de la corriente.
- $\vec{r}$: vector que une el elemento $d\vec{s}$ con el punto de observación $P$.
- $r = |\vec{r}|$: distancia desde el elemento al punto $P$.
- $\hat{r}$: vector unitario en la dirección de $\vec{r}$.
- El producto vectorial $d\vec{s} \times \hat{r}$ da la dirección del campo magnético: **perpendicular al plano formado por la corriente y el punto $P$**.

---

## 🔁 Sustitución con coordenadas angulares

Para facilitar la integración, se realiza un cambio de variable usando un ángulo $\theta$ medido desde el centro del alambre al punto $P$:

### Relaciones trigonométricas en el triángulo rectángulo:

- $x = a \tan\theta$: coordenada horizontal del elemento $dx$.
- $r = \frac{a}{\cos\theta}$: distancia desde el elemento al punto $P$.
- $dx = a \sec^2\theta \, d\theta$: diferencial de $x$ en función de $\theta$.

Estas relaciones permiten **reescribir la integral** del campo magnético en función de $\theta$.

---

## ✏️ Desarrollo completo con Biot-Savart

Aplicamos Biot–Savart para un elemento infinitesimal $dx$:

$$
dB = \frac{\mu_0}{4\pi} \cdot \frac{I\, dx \cdot \sin\theta}{r^2}
$$

### Sustituimos con las expresiones trigonométricas:

- $dx = a \sec^2\theta \, d\theta$
- $r^2 = \left( \frac{a}{\cos\theta} \right)^2 = \frac{a^2}{\cos^2\theta}$

Entonces:

$$
\begin{aligned}
dB &= \frac{\mu_0}{4\pi} \cdot \frac{I \cdot a \sec^2\theta \cdot \sin\theta \, d\theta}{a^2 / \cos^2\theta} \\
&= \frac{\mu_0 I}{4\pi a} \cdot \sin\theta \, d\theta
\end{aligned}
$$

---

## ∫ Integración

Ahora integramos desde $-\theta$ hasta $+\theta$, considerando la simetría del campo:

$$
B = \int_{-\theta}^{+\theta} \frac{\mu_0 I}{4\pi a} \cdot \sin\theta \, d\theta
$$

La función $\sin\theta$ es impar, y al integrar de $-\theta$ a $+\theta$, el resultado es el doble de la integral desde $0$ hasta $+\theta$:

$$
B = \frac{\mu_0 I}{2\pi a} \cdot \sin\theta
$$

---

## ✅ Resultado final

$$
\boxed{B = \frac{\mu_0 I}{2\pi a} \cdot \sin\theta}
$$

### Dirección del campo:
- Perpendicular al plano formado por el alambre y el punto $P$.
- Según la **regla de la mano derecha**, si la corriente va hacia la derecha, el campo magnético en el punto $P$ (arriba del alambre) entra en la hoja.

---

## 📁 Conclusiones

- Esta deducción permite comprender cómo la Ley de Biot-Savart se usa para calcular campos magnéticos generados por corrientes distribuidas.
- El cambio de variable a coordenadas angulares simplifica el problema y permite integrarlo.
- El campo depende de $\theta$, que representa el ángulo visual que el alambre forma respecto del punto $P$.

Este desarrollo es válido para un alambre **finito**. En el caso de un alambre **infinito**, $\theta \to 90^\circ \Rightarrow \sin\theta = 1$, y el campo magnético máximo es:

$$
B = \frac{\mu_0 I}{2\pi a}
$$

Esto coincide con el resultado conocido para un alambre recto e infinito.
