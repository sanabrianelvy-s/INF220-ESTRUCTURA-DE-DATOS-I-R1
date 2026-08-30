import random
import time
from abc import ABC, abstractmethod
from typing import Any, Optional

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
        """Inserta un elemento en la estructura."""
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
# 2. REPRESENTACIÓN ESTÁTICA
# =====================================================================
class ArrayEstatico(ADTContenedor):
    """
    Estructura de tamaño fijo en memoria contigua simulada.
    Controla estrictamente sus límites de capacidad e índices.
    """

    def __init__(self, capacidad: int) -> None:
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0.")
        self._datos: list[Any] = [None] * capacidad
        self._capacidad: int = capacidad
        self._tamanio: int = 0

    def agregar(self, dato: Any) -> None:
        """
        Agrega un elemento al final de los datos ocupados.

        Args:
            dato: El valor de cualquier tipo que se almacenará.

        Raises:
            OverflowError: Si la estructura ya está llena.
        """
        if self._tamanio >= self._capacidad:
            raise OverflowError("Array lleno.")
        self._datos[self._tamanio] = dato
        self._tamanio += 1

    def obtener(self, indice: int) -> Any:
        """
        Acceso directo al elemento por su índice en tiempo O(1).

        Args:
            indice: Posición lógica del elemento a recuperar.

        Raises:
            IndexError: Si el índice está fuera del rango válido.
        """
        if not (0 <= indice < self._tamanio):
            raise IndexError("Índice fuera de rango.")
        return self._datos[indice]

    def __len__(self) -> int:
        return self._tamanio


# =====================================================================
# 3. REPRESENTACIÓN DINÁMICA: Nodos Enlazados en el Heap
# =====================================================================
class _Nodo:
    """Componente básico para almacenar el dato y la flecha."""
    __slots__ = ['dato', 'siguiente']
    
    def __init__(self, dato: Any) -> None:
        self.dato: Any = dato
        self.siguiente: Optional[_Nodo] = None


class ListaDinamica(ADTContenedor):
    """
    Lista enlazada simple que crece en ejecución sin límites contiguos.
    """
    
    def __init__(self) -> None:
        self._cabeza: Optional[_Nodo] = None
        self._tamanio: int = 0

    def agregar(self, dato: Any) -> None:
        """
        Inserta un nuevo elemento al final de la lista. Operación O(n).

        Args:
            dato: El valor de cualquier tipo que se almacenará.
        """
        nuevo_nodo = _Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamanio += 1

    def obtener(self, indice: int) -> Any:
        """
        Acceso secuencial al elemento por su índice. Operación O(n).

        Args:
            indice: Posición lógica del elemento a recuperar.

        Raises:
            IndexError: Si el índice está fuera del rango válido.
        """
        if not (0 <= indice < self._tamanio):
            raise IndexError("Índice fuera de rango.")
        
        actual = self._cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato

    def __len__(self) -> int:
        return self._tamanio


# =====================================================================
# 4. GENERACIÓN DE DATOS SIMULADOS
# =====================================================================
def generar_alumnos_simulados(cantidad: int) -> list[str]:
    """
    Genera una lista de nombres de alumnos aleatorios para pruebas.

    Args:
        cantidad: El número total de alumnos simulados a crear.

    Returns:
        Una lista de cadenas con nombres y apellidos aleatorios.
    """
    nombres = ["Ana", "Luis", "Carlos", "Sofía", "María", "Pedro", "Jorge"]
    apellidos = ["Quispe", "Mamani", "García", "López", "Flores", "Vargas"]
    return [
        f"{random.choice(nombres)} {random.choice(apellidos)}"
        for _ in range(cantidad)
    ]


# =====================================================================
# 5. PRUEBA COMPARATIVA DE RENDIMIENTO (Zona de Acción)
# =====================================================================
if __name__ == "__main__":
    # SUPUESTOS DE PRUEBA (Formateados a menos de 79 caracteres):
    # 1. Se evalúa con una muestra mediana de 2,000 alumnos simulados.
    # 2. Se mide el costo de acceder 500 veces al último elemento.
    
    CANTIDAD_ALUMNOS = 2000
    ACCESOS = 500
    
    print("--- INICIANDO NIVEL B: PRUEBA DE RENDIMIENTO ---")
    print(f"Generando {CANTIDAD_ALUMNOS} alumnos ficticios...")
    alumnos_test = generar_alumnos_simulados(CANTIDAD_ALUMNOS)
    
    # Llenamos el Array Estático
    arr_estatico = ArrayEstatico(capacidad=CANTIDAD_ALUMNOS)
    for alumno in alumnos_test:
        arr_estatico.agregar(alumno)
        
    # Llenamos la Lista Dinámica
    lista_dinamica = ListaDinamica()
    for alumno in alumnos_test:
        lista_dinamica.agregar(alumno)

    print("\n--- ⏱️ Midiendo tiempo de acceso al ÚLTIMO elemento ---")
    ultimo_indice = CANTIDAD_ALUMNOS - 1

    # Cronómetro para el Array Estático
    inicio_estatico = time.perf_counter()
    for _ in range(ACCESOS):
        _ = arr_estatico.obtener(ultimo_indice)
    tiempo_estatico = time.perf_counter() - inicio_estatico

    # Cronómetro para la Lista Dinámica
    inicio_dinamico = time.perf_counter()
    for _ in range(ACCESOS):
        _ = lista_dinamica.obtener(ultimo_indice)
    tiempo_dinamico = time.perf_counter() - inicio_dinamico

    # Mostramos los resultados en milisegundos (ms)
    print(f" Array Estático [O(1)]: {tiempo_estatico * 1000:.2f} ms")
    print(f" Lista Dinámica [O(n)]: {tiempo_dinamico * 1000:.2f} ms")
    
    if tiempo_estatico > 0:
        multiplo = tiempo_dinamico / tiempo_estatico
        # Rompimos el texto largo en dos líneas usando los paréntesis de PEP 8
        print(
            f"\n CONCLUSIÓN: ¡El Array Estático fue ~{multiplo:.0f}x "
            "más rápido para leer datos!"
        )

