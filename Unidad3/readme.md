# 📊 Unidad III: Estructuras Lineales - Listas Enlazadas

## 🎯 Objetivo de la Unidad
Implementar, dominar y evaluar las estructuras de datos lineales fundamentales en su variante dinámica (nodos enlazados en el Heap), garantizando la calidad del software mediante el patrón arquitectónico MVC y las buenas prácticas de codificación PEP 8.

---

## 🔗 1. Listas Enlazadas
Una lista enlazada es una colección secuencial de elementos dinámicos denominados **Nodos**, los cuales están interconectados en la memoria a través de referencias o punteros directos.

### 🧱 1 Lista Simple Dinámica (Unidireccional)
Es una secuencia de nodos donde cada uno contiene el dato almacenado y un único enlace apuntando al nodo `siguiente`. El recorrido es estrictamente unidireccional y el último componente apunta a la nada (`None`).


| Operación | Complejidad | Descripción Técnica |
| :--- | :--- | :--- |
| `insertar_inicio(dato)` | **O(1) Constante** ⚡ | Modificación inmediata del puntero de la cabeza, independiente del tamaño de la lista. |
| `insertar_final(dato)` | **O(n) Lineal** 🐌 | Requiere un recorrido secuencial obligatorio desde el inicio hasta hallar el nodo apuntando a `None`. |
| `eliminar_inicio()` | **O(1) Constante** ⚡ | Desengancha el primer elemento reasignando la cabeza al nodo siguiente en un solo paso. |
| `vaciar()` | **O(1) Constante** ⚡ | Rompe el enlace principal (`_cabeza = None`), permitiendo que el Garbage Collector libere el Heap. |


