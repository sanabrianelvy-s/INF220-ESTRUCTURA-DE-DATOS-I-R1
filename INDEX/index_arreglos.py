"""Simulación de indexación utilizando arreglos y búsqueda binaria.

Este módulo genera una base de datos simulada de 100 estudiantes
desordenados y compara el rendimiento paso a paso entre una búsqueda
secuencial tradicional y una búsqueda optimizada mediante un índice.
"""

import random
import time

# Constantes globales (PEP 8: en MAYUSCULAS_CON_GUIONES_BAJOS)
TOTAL_ESTUDIANTES = 500
NOMBRES_BASE = [
    "Ana", "Luis", "Carlos", "Marta",
    "Sofía", "Jorge", "Elena", "Diego",
]
CARRERAS_BASE = [
    "Sistemas", "Civil", "Industrial",
    "Comercial", "Arquitectura",
]


def generar_estudiantes(cantidad):
    """Genera una lista de diccionarios con datos de estudiantes al azar."""
    ids_unicos = random.sample(range(1000, 10000), cantidad)
    lista_estudiantes = []

    for id_est in ids_unicos:
        estudiante = {
            "id": id_est,
            "nombre": random.choice(NOMBRES_BASE),
            "carrera": random.choice(CARRERAS_BASE),
        }
        lista_estudiantes.append(estudiante)

    return lista_estudiantes


def crear_indice_arreglo(lista_estudiantes):
    """Construye y ordena un índice ligero de tuplas (id, posicion)."""
    indice = [
        (est["id"], idx)
        for idx, est in enumerate(lista_estudiantes)
    ]
    indice.sort()
    return indice


def simular_busqueda_secuencial(lista_estudiantes, id_objetivo):
    """Simula una búsqueda tradicional sin índice paso a paso."""
    print(">>> INICIANDO BÚSQUEDA SIN ÍNDICE (Recorrido secuencial):")
    pasos = 0

    for idx, estudiante in enumerate(lista_estudiantes):
        pasos += 1
        id_actual = estudiante["id"]

        # Muestra avances periódicos para visualizar el recorrido en consola
        if idx < 4 or idx % 15 == 0 or id_actual == id_objetivo:
            print(
                f"  [Paso {pasos:02d}] Revisando casilla {idx:02d} "
                f"-> ID: {id_actual}"
            )
            time.sleep(0.2)

        if id_actual == id_objetivo:
            print(f"  --> Dato encontrado: {estudiante}")
            print(f"  ¡ENCONTRADO! Total de revisiones: {pasos} pasos.\n")
            return estudiante, pasos

    return None, pasos


def simular_busqueda_indexada(indice, lista_estudiantes, id_objetivo):
    """Simula una búsqueda binaria sobre el índice y salta al registro."""
    print(">>> INICIANDO BÚSQUEDA CON ÍNDICE (Búsqueda Binaria):")
    izquierda = 0
    derecha = len(indice) - 1
    pasos = 0

    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        id_actual, pos_real = indice[medio]

        print(
            f"  [Salto {pasos:02d}] Rango [{izquierda:02d}..{derecha:02d}] "
            f"-> Medio (Pos {medio:02d}): ID {id_actual}"
        )
        time.sleep(0.7)

        if id_actual == id_objetivo:
            print(f"  --> ¡CLAVE HALLADA! Puntero indica ir a posición [{pos_real}].")
            time.sleep(0.7)
            registro = lista_estudiantes[pos_real]
            print(f"  --> Saltando a memoria principal... Dato: {registro}")
            print(f"  ¡LISTO! Total de saltos: {pasos} pasos.\n")
            return registro, pasos

        if id_actual < id_objetivo:
            print(f"      Como {id_actual} < {id_objetivo}, descarto mitad izquierda.\n")
            izquierda = medio + 1
        else:
            print(f"      Como {id_actual} > {id_objetivo}, descarto mitad derecha.\n")
            derecha = medio - 1

    return None, pasos


def ejecutar_simulacion():
    """Función principal que orquesta la simulación completa."""
    estudiantes = generar_estudiantes(TOTAL_ESTUDIANTES)
    indice_arreglo = crear_indice_arreglo(estudiantes)

    # Seleccionamos el estudiante ubicado en la posición 88 para la prueba
    id_objetivo = estudiantes[138]["id"]

    print("=" * 62)
    print(f" SIMULACIÓN EN VIVO: Buscando estudiante con ID [{id_objetivo}]")
    print("=" * 62 + "\n")
    time.sleep(1)

    _, pasos_sin = simular_busqueda_secuencial(estudiantes, id_objetivo)
    time.sleep(1.2)
    _, pasos_con = simular_busqueda_indexada(
        indice_arreglo, estudiantes, id_objetivo
    )

    if pasos_con > 0:
        eficiencia = pasos_sin // pasos_con
        print(f"RESUMEN: El índice fue ~{eficiencia} veces más eficiente en pasos.")


if __name__ == "__main__":
    ejecutar_simulacion()
