"""
Unidad 1: Datos Estáticos y Dinámicos

Este ejercicio muestra la diferencia entre una estructura de datos
estática y una estructura de datos dinámica mediante el almacenamiento
de estudiantes.

La estructura estática trabaja con una capacidad fija, mientras que
la estructura dinámica puede crecer durante la ejecución del programa.
"""


class ArrayEstatico:
    """Estructura de tamaño fijo para almacenar estudiantes."""

    def __init__(self, capacidad):
        self.datos = [None] * capacidad
        self.tamanio = 0
        self.capacidad = capacidad

    def agregar(self, estudiante):
        """Agrega un estudiante si existe espacio disponible."""
        if self.tamanio >= self.capacidad:
            print("El array está lleno.")
            return

        self.datos[self.tamanio] = estudiante
        self.tamanio += 1

    def mostrar(self):
        """Muestra los estudiantes almacenados."""
        for i in range(self.tamanio):
            print(self.datos[i])


class ListaDinamica:
    """Estructura que puede crecer durante la ejecución."""

    def __init__(self):
        self.datos = []

    def agregar(self, estudiante):
        """Agrega un estudiante a la lista."""
        self.datos.append(estudiante)

    def mostrar(self):
        """Muestra los estudiantes almacenados."""
        for estudiante in self.datos:
            print(estudiante)


# Estructura estática
estudiantes_estaticos = ArrayEstatico(3)

estudiantes_estaticos.agregar("Ana")
estudiantes_estaticos.agregar("Luis")
estudiantes_estaticos.agregar("Carlos")
estudiantes_estaticos.agregar("María")

print("ESTRUCTURA ESTÁTICA:")
estudiantes_estaticos.mostrar()


# Estructura dinámica
estudiantes_dinamicos = ListaDinamica()

estudiantes_dinamicos.agregar("Ana")
estudiantes_dinamicos.agregar("Luis")
estudiantes_dinamicos.agregar("Carlos")
estudiantes_dinamicos.agregar("María")

print("\nESTRUCTURA DINÁMICA:")
estudiantes_dinamicos.mostrar()
