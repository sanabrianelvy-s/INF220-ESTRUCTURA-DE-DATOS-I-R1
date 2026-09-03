# 📚 Unidad II: ADT Polinomio y Conjuntos

## 🎯 Objetivo de la Unidad
Diseñar e implementar estructuras de datos lineales avanzadas para representar eficientemente conceptos matemáticos complejos en la memoria RAM, optimizando el uso de recursos mediante abstracción (ADT).

---

## 🧮 1. ADT Polinomio
Un polinomio es una expresión de la forma $P(x) = a_nx^n + ... + a_1x + a_0$. En computación, su representación se evalúa bajo dos enfoques de ingeniería:

### 💾 Modelos de Representación en Memoria

*   **Representación Estática (Array de Coeficientes)
    *   *Ventaja:* Acceso inmediato 
    *   *Desventaja:* Ineficiente en memoria para polinomios dispersos 
*   **Representación Dinámica (Lista de Términos):** Se almacenan únicamente los nodos cuyos coeficientes sean distintos de cero.

### ⚙️ Operaciones Principales del ADT
*   `grado()`: Retorna el exponente más alto registrado.
*   `evaluar(x)`: Calcula el resultado numérico para un valor dado de $x$.
*   `sumar(Q)` / `restar(Q)` / `multiplicar(Q)`: Operaciones aritméticas entre polinomios.
*   `derivar()`: Retorna el polinomio derivado $P'(x)$.

---

## 🔢 2. ADT Conjunto
Un conjunto es una colección de elementos **sin orden establecido** y **sin duplicados** en memoria.

### 📐 Operaciones Álgebraicas del ADT
*   `union(B)` ($A \cup B$): Elementos en $A$, en $B$ o en ambos.
*   `interseccion(B)` ($A \cap B$): Elementos presentes simultáneamente en $A$ y $B$.
*   `diferencia(B)` ($A - B$): Elementos que pertenecen a $A$ pero no a $B$.
*   `diferencia_simetrica(B)` ($A \triangle B$): Elementos en $A$ o en $B$, pero no en ambos.
*   `contiene(x)` ($x \in A$): Verificación de membresía del elemento.

### 🛠️ Estrategias de Implementación
*   **Set de Python:** Estructura nativa basada en tablas Hash de alta velocidad.
*   **BitVector:** Representación binaria compacta para conjuntos de enteros pequeños.
*   **Lista Ordenada:** Implementación manual con algoritmos de combinación en tiempo $O(n)$.

