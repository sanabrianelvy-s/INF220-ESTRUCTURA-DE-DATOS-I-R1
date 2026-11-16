"""Simulación comparativa de indexación en Listas Enlazadas.

Compara el rendimiento paso a paso entre:
1. Una Lista Enlazada tradicional desordenada (sin índice).
2. Una Lista Enlazada auxiliar ordenada (índice ligero con punteros).
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
# 1. ESTRUCTURA SIN ÍNDICE (Lista Enlazada Pesada y Desordenada)
# ==============================================================================
class NodoPesado:
    """Nodo tradicional que almacena todo el registro del estudiante."""

    def __init__(self, datos_estudiante):
        self.datos = datos_estudiante
        self.siguiente = None


class ListaEnlazadaNormal:
    """Lista enlazada simple sin ordenamiento ni indexación."""

    def __init__(self):
        self.cabeza = None

    def agregar_al_inicio(self, datos_estudiante):
        """Inserta el registro completo sin ningún orden."""
        nuevo = NodoPesado(datos_estudiante)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def simular_busqueda(self, id_objetivo):
        """Recorre nodo por nodo desde la cabeza hasta el final."""
        print(">>> 1. BÚSQUEDA EN LISTA ENLAZADA NORMAL (Sin Índice):")
        actual = self.cabeza
        pasos = 0

        while actual is not None:
            pasos += 1
            id_actual = actual.datos["id"]

            if pasos <= 3 or pasos % 20 == 0 or id_actual == id_objetivo:
                print(f"  [Nodo {pasos:02d}] Revisando nodo pesado -> ID: {id_actual}")
                time.sleep(0.2)

            if id_actual == id_objetivo:
                print(f"  --> ¡ENCONTRADO! Dato: {actual.datos}")
                print(f"  Total de nodos visitados: {pasos}.\n")
                return actual.datos, pasos

            actual = actual.siguiente

        print(f"  --> NO EXISTE. Tuve que revisar TODA la lista ({pasos} nodos).\n")
        return None, pasos


# ==============================================================================
# 2. ESTRUCTURA CON ÍNDICE (Lista Enlazada Ligera y Ordenada)
# ==============================================================================
class NodoIndice:
    """Nodo ligero que solo guarda la clave y la posición en memoria."""

    def __init__(self, id_clave, pos_real):
        self.id_clave = id_clave
        self.pos_real = pos_real
        self.siguiente = None


class ListaEnlazadaIndice:
    """Índice dinámico ordenado ascendentemente por ID."""

    def __init__(self):
        self.cabeza = None

    def insertar_ordenado(self, id_clave, pos_real):
        """Enlaza el nuevo nodo en su posición ordenada sin mover memoria."""
        nuevo = NodoIndice(id_clave, pos_real)

        if self.cabeza is None or id_clave < self.cabeza.id_clave:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while (
            actual.siguiente is not None
            and actual.siguiente.id_clave < id_clave
        ):
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def simular_busqueda(self, memoria_principal, id_objetivo):
        """Busca en el índice ordenado y salta al arreglo principal."""
        print(">>> 2. BÚSQUEDA EN LISTA ENLAZADA INDEXADA (Con Índice):")
        actual = self.cabeza
        pasos = 0

        while actual is not None:
            pasos += 1

            if pasos <= 3 or pasos % 20 == 0 or actual.id_clave >= id_objetivo:
                print(
                    f"  [Nodo Índice {pasos:02d}] ID: {actual.id_clave} "
                    f"-> Puntero a pos [{actual.pos_real}]"
                )
                time.sleep(0.2)

            if actual.id_clave == id_objetivo:
                registro = memoria_principal[actual.pos_real]
                print(f"  --> ¡CLAVE HALLADA! Saltando a memoria -> {registro}")
                print(f"  Total de nodos índice visitados: {pasos}.\n")
                return registro, pasos

            # Parada anticipada: si ya pasamos el número, dejamos de buscar
            if actual.id_clave > id_objetivo:
                print(
                    f"  --> PARADA ANTICIPADA en nodo {pasos}: {actual.id_clave} > "
                    f"{id_objetivo}. No hace falta revisar el resto.\n"
                )
                return None, pasos

            actual = actual.siguiente

        print(f"  --> NO EXISTE. Nodos revisados: {pasos}.\n")
        return None, pasos


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
    """Ejecuta la comparativa entre Lista Enlazada normal e indexada."""
    estudiantes = generar_estudiantes(TOTAL_ESTUDIANTES)

    # Llenamos ambas estructuras con los mismos 100 estudiantes
    lista_normal = ListaEnlazadaNormal()
    lista_indexada = ListaEnlazadaIndice()

    for pos, est in enumerate(estudiantes):
        lista_normal.agregar_al_inicio(est)
        lista_indexada.insertar_ordenado(est["id"], pos)

    # PRUEBA A: Buscar un estudiante que SÍ existe (ubicado al final)
    id_existente = estudiantes[95]["id"]
    print("=" * 66)
    print(f" PRUEBA A: Buscando estudiante EXISTENTE con ID [{id_existente}]")
    print("=" * 66 + "\n")
    time.sleep(1)

    lista_normal.simular_busqueda(id_existente)
    time.sleep(1)
    lista_indexada.simular_busqueda(estudiantes, id_existente)
    time.sleep(1.5)

    
if __name__ == "__main__":
    ejecutar_simulacion()
