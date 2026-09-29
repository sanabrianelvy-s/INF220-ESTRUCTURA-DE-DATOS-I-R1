from typing import Any, Optional

class _Nodo:
    """Componente básico que almacena el dato y el enlace al siguiente."""
    __slots__ = ['dato', 'siguiente']
    
    def __init__(self, dato: Any) -> None:
        self.dato: Any = dato
        self.siguiente: Optional[_Nodo] = None


class ListaModelo:
    """
    Estructura lineal dinámica que administra la lógica de punteros.
    """
    
    def __init__(self) -> None:
        self._cabeza: Optional[_Nodo] = None
        self._tamanio: int = 0

    def insertar_inicio(self, dato: Any) -> None:
        """Inserta un nodo al principio de la lista en tiempo O(1)."""
        nuevo = _Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        self._tamanio += 1

    def insertar_final(self, dato: Any) -> None:
        """Inserta un nodo al final de la lista en tiempo O(n)."""
        nuevo = _Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def eliminar_inicio(self) -> Any:
        """
        Elimina el primer nodo y retorna su valor.

        Raises:
            IndexError: Si la lista está vacía.
        """
        if self._cabeza is None:
            raise IndexError("No se puede eliminar: Lista vacía.")
            
        valor = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return valor

    def vaciar(self) -> None:
        """Limpia todos los nodos liberando la memoria RAM."""
        self._cabeza = None
        self._tamanio = 0

    def obtener_cadena_texto(self) -> str:
        """Convierte los enlaces en una cadena visual para la pantalla."""
        elementos: list[str] = []
        actual = self._cabeza
        while actual is not None:
            elementos.append(f"[{actual.dato}]")
            actual = actual.siguiente
        elementos.append("None")
        return " → ".join(elementos)

    def __len__(self) -> int:
        return self._tamanio
