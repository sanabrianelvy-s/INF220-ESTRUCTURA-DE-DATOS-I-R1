from abc import ABC, abstractmethod
from typing import Any

# =====================================================================
# 1. INTERFAZ ADT MÍNIMA (El Contrato)
# =====================================================================
class ADTContenedor(ABC):
    """
    Tipo de Dato Abstracto base que define las operaciones mínimas
    para almacenar y recuperar información.
    """

    @abstractmethod
    def agregar(self, dato: Any) -> None:
        """Agrega un elemento al contenedor."""
        pass

    @abstractmethod
    def obtener(self, indice: int) -> Any:
        """Recupera el elemento en la posición especificada."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad actual de elementos guardados."""
        pass


# =====================================================================
# 2. CONSTRUCCIÓN DEL ARRAY ESTÁTICO (Validación de Límites)
# =====================================================================
class ArrayEstatico(ADTContenedor):
    """
    Estructura de tamaño fijo en memoria contigua simulada.
    Controla estrictamente sus límites de capacidad e índices.
    """

    def __init__(self, capacidad: int) -> None:
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero mayor a 0.")
        
        # Reservamos el bloque fijo de memoria contigua en el inicio
        self._datos: list[Any] = [None] * capacidad
        self._capacidad: int = capacidad
        self._tamanio: int = 0  # Rastrea cuántos espacios reales están ocupados

    def agregar(self, dato: Any) -> None:
        """
        Agrega un elemento al final de los datos ocupados.
        
        Raises:
            OverflowError: Si intentamos meter datos en una estructura llena.
        """
        # VALIDACIÓN DE LÍMITE SUPERIOR (Overflow)
        if self._tamanio >= self._capacidad:
            raise OverflowError(f"Array lleno. Capacidad máxima: {self._capacidad}")
        
        self._datos[self._tamanio] = dato
        self._tamanio += 1

    def obtener(self, indice: int) -> Any:
        """
        Acceso directo al elemento por su índice en tiempo O(1).
        
        Raises:
            IndexError: Si el índice solicitado no es válido o está vacío.
        """
        # VALIDACIÓN DE RANGOS DE ÍNDICE
        if not (0 <= indice < self._tamanio):
            raise IndexError(f"Índice {indice} fuera de rango. Elementos válidos: 0 a {self._tamanio - 1}")
        
        return self._datos[indice]

    def __len__(self) -> int:
        return self._tamanio

    def __str__(self) -> str:
        # Muestra visualmente qué celdas están ocupadas y cuáles siguen en None (_)
        ocupados = [str(self._datos[i]) for i in range(self._tamanio)]
        vacios = ["_"] * (self._capacidad - self._tamanio)
        return f"[{', '.join(ocupados + vacios)}] ({self._tamanio}/{self._capacidad})"


# =====================================================================
# 3. PRUEBA DE LOS MÉTODOS (Bloque Mecánico de Ejecución)
# =====================================================================
if __name__ == "__main__":
    print("--- Creando un Array Estático de capacidad 3 ---")
    arreglo = ArrayEstatico(capacidad=3)
    print(f"Estado inicial: {arreglo}")

    print("\n--- Insertando elementos válidos ---")
    arreglo.agregar("Ana")
    arreglo.agregar("Luis")
    print(f"Estado actual: {arreglo}")
    print(f"Tamaño reportado por len(): {len(arreglo)}")

    print("\n--- Probando acceso directo O(1) ---")
    print(f"Elemento en índice 0: {arreglo.obtener(0)}")

    print("\n--- Provocando y capturando IndexError (Caso borde) ---")
    try:
        # El índice 2 existe físicamente, pero está vacío en nuestro tamaño lógico
        print(arreglo.obtener(2))  
    except IndexError as error:
        print(f"Error controlado correctamente: {error}")

    print("\n--- Llenando el arreglo al máximo ---")
    arreglo.agregar("Carlos")
    print(f"Estado actual (Lleno): {arreglo}")

    print("\n--- Provocando y capturando OverflowError (Caso borde) ---")
    try:
        arreglo.agregar("Sofía")  # Ya no cabe
    except OverflowError as error:
        print(f"Error controlado correctamente: {error}")
