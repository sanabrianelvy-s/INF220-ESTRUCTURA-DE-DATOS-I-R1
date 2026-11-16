"""Simulación comparativa de indexación utilizando Pilas (LIFO).

Compara el comportamiento de:
1. Una Pila tradicional que almacena registros completos (pesados).
2. Una Pila Índice ligera que guarda referencias (id, posicion) y accede
   al registro más reciente en O(1) o busca mediante una pila auxiliar.
"""

import random
import time

TOTAL_ESTUDIANTES = 100
NOMBRES_BASE = [
    "Ana", "Luis", "Carlos", "Marta",
    "Sofía", "Jorge", "Elena", "Diego",
]
CARRERAS_BASE = [
    "Sistemas", "Civil", "Industrial",
    "Comercial", "Arquitectura",
]


# ==============================================================================
# 1. PILA NORMAL (Almacena diccionarios pesados directamente)
# ==============================================================================
class PilaNormal:
    """Pila tradicional sin indexación que mueve registros completos."""

    def __init__(self):
        self.items = []

    def apilar(self, estudiante):
        """Inserta el registro completo en el tope (Push)."""
        self.items.append(estudiante)

    def simular_busqueda(self, id_objetivo):
        """Desapila registros completos hacia una pila auxiliar para buscar."""
        print(">>> 1. BÚSQUEDA EN PILA NORMAL (Moviendo registros pesados):")
        auxiliar = []
        pasos = 0
        encontrado = None

        while self.items:
            pasos += 1
            registro_pesado = self.items.pop()
            auxiliar.append(registro_pesado)

            if pasos <= 3 or pasos % 25 == 0 or registro_pesado["id"] == id_objetivo:
                print(
                    f"  [Desapilado {pasos:02d}] Moviendo registro completo -> "
                    f"ID: {registro_pesado['id']} ({registro_pesado['nombre']})"
                )
                time.sleep(0.2)

            if registro_pesado["id"] == id_objetivo:
                encontrado = registro_pesado
                print(f"  --> ¡ENCONTRADO! Dato: {encontrado}")
                break

        # Restaurar la pila original devolviendo todos los registros pesados
        while auxiliar:
            self.items.append(auxiliar.pop())

        print(f"  Pila restaurada. Total de movimientos pesados: {pasos}.\n")
        return encontrado, pasos


# ==============================================================================
# 2. PILA ÍNDICE (Almacena solo punteros ligeros: id y posición)
# ==============================================================================
class PilaIndice:
    """Índice LIFO ligero que apunta a la memoria principal."""

    def __init__(self):
        self.items = []

    def apilar_indice(self, id_clave, pos_real):
        """Agrega solo la clave y la posición al tope (Push)."""
        self.items.append((id_clave, pos_real))

    def consultar_ultimo_ingresado(self, memoria_principal):
        """Acceso directo O(1) al último registro sin desapilar nada."""
        if not self.items:
            return None
        _, pos_real = self.items[-1]
        return memoria_principal[pos_real]

    def simular_busqueda(self, memoria_principal, id_objetivo):
        """Desapila solo tuplas ligeras hasta hallar el puntero del ID."""
        print(">>> 2. BÚSQUEDA EN PILA ÍNDICE (Moviendo solo punteros ligeros):")
        auxiliar = []
        pasos = 0
        encontrado = None

        while self.items:
            pasos += 1
            id_actual, pos_real = self.items.pop()
            auxiliar.append((id_actual, pos_real))

            if pasos <= 3 or pasos % 25 == 0 or id_actual == id_objetivo:
                print(
                    f"  [Desapilado {pasos:02d}] Moviendo índice ligero -> "
                    f"ID: {id_actual} (Pos [{pos_real}])"
                )
                time.sleep(0.2)

            if id_actual == id_objetivo:
                encontrado = memoria_principal[pos_real]
                print(
                    f"  --> ¡PUNTERO HALLADO! Saltando a pos [{pos_real}] -> "
                    f"{encontrado}"
                )
                break

        # Restaurar la pila índice original
        while auxiliar:
            self.items.append(auxiliar.pop())

        print(f"  Índice restaurado. Total de movimientos ligeros: {pasos}.\n")
        return encontrado, pasos


def generar_estudiantes(cantidad):
    """Genera una lista de estudiantes con IDs únicos desordenados."""
    ids_unicos = random.sample(range(1000, 10000), cantidad)
    return [
        {
            "id": id_est,
            "nombre": random.choice(NOMBRES_BASE),
            "carrera": random.choice(CARRERAS_BASE),
        }
        for id_est in ids_unicos
    ]


def ejecutar_simulacion():
    """Orquesta la comparación entre Pila Normal y Pila Índice."""
    estudiantes = generar_estudiantes(TOTAL_ESTUDIANTES)
    pila_normal = PilaNormal()
    pila_indice = PilaIndice()

    for pos, est in enumerate(estudiantes):
        pila_normal.apilar(est)
        pila_indice.apilar_indice(est["id"], pos)

    print("=" * 66)
    print(" SIMULACIÓN DE INDEXACIÓN CON PILAS (LIFO)")
    print("=" * 66 + "\n")
    time.sleep(1)

    # Demostración 1: El verdadero fuerte de la pila índice (Acceso en 1 paso)
    ultimo = pila_indice.consultar_ultimo_ingresado(estudiantes)
    print(f"[VENTAJA LIFO - 1 PASO] Último estudiante registrado: {ultimo}\n")
    time.sleep(1.2)

    # Demostración 2: Búsqueda de un estudiante antiguo (posición 20 de 100)
    # Como entró al principio, está muy al fondo de la pila (paso 80)
    id_antiguo = estudiantes[63]["id"]
    print(f"Buscando estudiante antiguo con ID [{id_antiguo}] al fondo de la pila:\n")
    time.sleep(1)

    pila_normal.simular_busqueda(id_antiguo)
    time.sleep(1)
    pila_indice.simular_busqueda(estudiantes, id_antiguo)


if __name__ == "__main__":
    ejecutar_simulacion()
