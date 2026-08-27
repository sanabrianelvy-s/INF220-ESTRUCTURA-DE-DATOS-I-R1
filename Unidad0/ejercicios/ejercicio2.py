def buscar_nota_maxima(lista_notas):
    """
    Encuentra la calificacion mas alta dentro de una lista.

    Parameters:
    lista_notas (lists): Una lista con numero int o float.

    Returns:
    int or float: La nota mas alta encontrada en la lista.
    """
    if len(lista_notas) == 0:
        return 0

    nota_maxima = max(lista_notas)
    return nota_maxima

if __name__ == "__main__":
    # Estructura de datos lineal basica (Arreglo con notas de ejemplo)
    mis_calificaciones = [70, 85, 50, 60, 100]

    # Llamada a la funcion pasandole la lista como parametro
    mejor_nota = buscar_nota_maxima(mis_calificaciones)

    # Mostramos los resultados 
    print(f"Lista de notas: {mis_calificaciones}")
    print(f"La calificación más alta del semestre es: {mejor_nota}")
