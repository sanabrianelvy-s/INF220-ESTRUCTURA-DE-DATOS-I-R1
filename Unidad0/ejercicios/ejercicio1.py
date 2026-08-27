def calcular_promedio(lista_notas):
    """Calcula el promedio de una lista de claificaciones.

    Parameters:
    lista_notas (list); Una lista con muneros int o float.

    Returns:
    float: El promedio aritmetico de las notas.
    """
    if len(lista_notas) == 0:
        return 0.0

    suma_total = sum(lista_notas)
    promedio = suma_total / len(lista_notas)
    return promedio


if __name__ == "__main__":
    # Usamos una lista de python (una estructura de datos lineal basica)
    mis_calificaciones = [70, 85, 50, 60, 100]

    # Llamada la funcion pasandole la lista como parametro
    resultado_promedio = calcular_promedio(mis_calificaciones)

    # Mostramos los resultados
    print(f"Notas del semestre: {mis_calificaciones}")
    print(f"el promedio final es: {resultado_promedio}")
