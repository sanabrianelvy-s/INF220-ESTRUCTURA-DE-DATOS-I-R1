from typing import Any, Optional

class _NodoMonomio:
    """Componente básico para almacenar un término del polinomio."""
    __slots__ = ['coeficiente', 'exponente', 'siguiente']
    
    def __init__(self, coeficiente: float, exponente: int) -> None:
        self.coeficiente: float = coeficiente
        self.exponente: int = exponente
        self.siguiente: Optional[_NodoMonomio] = None


class PolinomioModelo:
    """
    Representa un polinomio guardado de forma secuencial en memoria.
    No realiza reducciones algebraicas automáticas por diseño.
    """
    
    def __init__(self) -> None:
        self._cabeza: Optional[_NodoMonomio] = None
        self._tamanio: int = 0

    def registrar_termino(
        self, coeficiente: float, exponente: int
    ) -> None:
        """
        Inserta un nuevo término al final de la estructura.

        Args:
            coeficiente: El número que acompaña a la variable.
            exponente: La potencia de la variable.
        """
        nuevo = _NodoMonomio(coeficiente, exponente)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def vaciar_estructura(self) -> None:
        """Limpia todos los nodos de la memoria RAM."""
        self._cabeza = None
        self._tamanio = 0

    def obtener_cadena_texto(self) -> str:
        """
        Transforma los nodos guardados en una expresión matemática legible.

        Returns:
            Una cadena formateada, ej: "3X^4 + 2X^4 - 5X^1".
        """
        if self._cabeza is None:
            return "P(X) = 0"
            
        partes: list[str] = []
        actual = self._cabeza
        
        while actual is not None:
            # Damos formato visual al monomio individual
            signo = " + " if actual.coeficiente >= 0 else " - "
            val_coef = abs(actual.coeficiente)
            partes.append(f"{signo}{val_coef}X^{actual.exponente}")
            actual = actual.siguiente
            
        # Unimos las piezas y limpiamos el signo inicial si es positivo
        resultado = "".join(partes)
        if resultado.startswith(" + "):
            resultado = resultado[3:]
            
        return f"P(X) = {resultado}"
