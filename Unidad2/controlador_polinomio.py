from tkinter import messagebox
from modelo_polinomio import PolinomioModelo
from vista_polinomio import PolinomioVista

class PolinomioControlador:
    """
    Director de orquesta del patrón MVC para el polinomio.
    """
    
    def __init__(
        self, modelo: PolinomioModelo, vista: PolinomioVista
    ) -> None:
        self._modelo = modelo
        self._vista = vista
        
        # Le indicamos a la vista qué funciones debe disparar al hacer clics
        self._vista.establecer_eventos(
            self._evento_agregar, self._evento_limpiar
        )

    def _evento_agregar(self) -> None:
        """Proceso ejecutado al hacer clic en 'Agregar Término'."""
        txt_coef, txt_exp = self._vista.obtener_entradas()
        
        # VALIDACIÓN DE SEGURIDAD: Evita que el programa explote si meten texto
        try:
            coeficiente = float(txt_coef)
            exponente = int(txt_exp)
        except ValueError:
            messagebox.showerror(
                "Error de Entrada", 
                "Por favor ingrese números válidos en los campos."
            )
            return

        # Mandamos los datos limpios al Modelo (RAM)
        self._modelo.registrar_termino(coeficiente, exponente)
        
        # Recuperamos la cadena final y refrescamos la pantalla (Vista)
        polinomio_texto = self._modelo.obtener_cadena_texto()
        self._vista.actualizar_pantalla(polinomio_texto)
        
        # Dejamos las cajas limpias para el siguiente monomio
        self._vista.limpiar_entradas()

    def _evento_limpiar(self) -> None:
        """Proceso ejecutado al hacer clic en 'Nuevo Polinomio'."""
        # 1. Vaciamos la memoria Heap del Modelo
        self._modelo.vaciar_estructura()
        
        # 2. Forzamos a la vista a volver a su estado inicial
        self._vista.actualizar_pantalla("P(X) = 0")
        self._vista.limpiar_entradas()
