"""Simulación comparativa de indexación utilizando Colas (FIFO).

Compara el comportamiento de:
1. Una Cola tradicional que mueve registros pesados completos.
2. Una Cola Índice ligera que guarda referencias (id, posicion) para
   gestionar turnos en O(1) y realizar búsquedas sin mover datos pesados.
"""

from collections import deque
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
# 1. COLA NORMAL (Almacena y mueve registros pesados directamente)
# ==============================================================================
class ColaNormal:
    """Cola tradicional sin indexación que almacena registros completos."""

    def __init__(self):
        self.cola = deque()

    def encolar(self, estudiante):
        """Agrega el registro completo al final de la fila (Enqueue)."""
        self.cola.append(estudiante)

    def simular_busqueda(self, id_objetivo):
        """Desencola registros completos hacia una cola auxiliar para buscar."""
        print(">>> 1. BÚSQUEDA EN COLA NORMAL (Moviendo registros pesados):")
        auxiliar = deque()
        pasos = 0
        encontrado = None

        while self.cola:
            pasos += 1
            registro_pesado = self.cola.popleft()
            auxiliar.append(registro_pesado)

            if (
                pasos <= 3
                or pasos % 25 == 0
                or registro_pesado["id"] == id_objetivo
            ):
                print(
                    f"  [Turno {pasos:02d}] Moviendo registro pesado -> "
                    f"ID: {registro_pesado['id']} ({registro_pesado['nombre']})"
                )
                time.sleep(0.2)

            if registro_pesado["id"] == id_objetivo:
                encontrado = registro_pesado
                print(f"  --> ¡ENCONTRADO! Dato: {encontrado}")
                # Terminamos de vaciar a la auxiliar para no perder el orden FIFO
                while self.cola:
                    auxiliar.append(self.cola.popleft())
                break

        # Restauramos la cola original manteniendo el orden de llegada exacto
        self.cola = auxiliar
        print(f"  Fila restaurada. Total de revisiones: {pasos} pasos.\n")
        return encontrado, pasos


# ==============================================================================
# 2. COLA ÍNDICE (Almacena solo punteros ligeros: id y posición)
# ==============================================================================
class ColaIndice:
    """Índice FIFO ligero que gestiona turnos apuntando a memoria."""

    def __init__(self):
        self.cola = deque()

    def encolar_indice(self, id_clave, pos_real):
        """Agrega solo la clave y la posición al final (Enqueue)."""
        self.cola.append((id_clave, pos_real))

    def simular_atencion_turnos(self, memoria_principal, cantidad_turnos):
        """Atiende los primeros turnos en O(1) saltando a memoria principal."""
        print(">>> VENTANA DE ATENCIÓN FIFO (Despachando primeros turnos):")
        for turno in range(1, cantidad_turnos + 1):
            if not self.cola:
                break

            id_actual, pos_real = self.cola.popleft()
            registro = memoria_principal[pos_real]
            print(
                f"  [Atendiendo Turno {turno}] Ficha ID {id_actual} -> "
                f"Saltando a Pos [{pos_real}]: {registro['nombre']} "
                f"({registro['carrera']})"
            )
            time.sleep(0.5)
        print("  ¡Turnos despachados sin mover datos pesados en memoria!\n")

    def simular_busqueda(self, memoria_principal, id_objetivo):
        """Busca un ID moviendo solo fichas ligeras hacia una cola auxiliar."""
        print(">>> 2. BÚSQUEDA EN COLA ÍNDICE (Moviendo fichas ligeras):")
        auxiliar = deque()
        pasos = 0
        encontrado = None

        while self.cola:
            pasos += 1
            id_actual, pos_real = self.cola.popleft()
            auxiliar.append((id_actual, pos_real))

            if pasos <= 3 or pasos % 25 == 0 or id_actual == id_objetivo:
                print(
                    f"  [Ficha {pasos:02d}] Revisando índice ligero -> "
                    f"ID: {id_actual} (Pos [{pos_real}])"
                )
                time.sleep(0.2)

            if id_actual == id_objetivo:
                encontrado = memoria_principal[pos_real]
                print(
                    f"  --> ¡FICHA HALLADA! Saltando a pos [{pos_real}] -> "
                    f"{encontrado}"
                )
                while self.cola:
                    auxiliar.append(self.cola.popleft())
                break

        self.cola = auxiliar
        print(f"  Índice restaurado. Total de revisiones: {pasos} pasos.\n")
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
    """Orquesta la comparación justa entre Cola Normal y Cola Índice."""
    estudiantes = generar_estudiantes(TOTAL_ESTUDIANTES)
    cola_normal = ColaNormal()
    cola_indice = ColaIndice()

    # Llenamos ambas colas con los 100 estudiantes completos
    for pos, est in enumerate(estudiantes):
        cola_normal.encolar(est)
        cola_indice.encolar_indice(est["id"], pos)

    print("=" * 66)
    print(" SIMULACIÓN DE INDEXACIÓN CON COLAS (FIFO - 100 ESTUDIANTES)")
    print("=" * 66 + "\n")
    time.sleep(1)

    # Demostración 1: Búsqueda en igualdad de condiciones (100 vs 100)
    id_buscar = estudiantes[27]["id"]
    print(f"Buscando estudiante con ID [{id_buscar}] dentro de la fila completa:\n")
    time.sleep(1)

    cola_normal.simular_busqueda(id_buscar)
    time.sleep(1)
    cola_indice.simular_busqueda(estudiantes, id_buscar)
    time.sleep(1.2)

    # Demostración 2: Despacho de turnos FIFO al final (sin afectar la búsqueda)
    cola_indice.simular_atencion_turnos(estudiantes, cantidad_turnos=3)


if __name__ == "__main__":
    ejecutar_simulacion()
