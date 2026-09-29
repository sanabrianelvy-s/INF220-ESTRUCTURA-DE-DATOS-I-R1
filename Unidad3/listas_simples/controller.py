from tkinter import messagebox
from model import ListaModelo
from view import ListaVista

class ListaControlador:
    """
    Coordina el flujo de datos entre el modelo de memoria y la interfaz view.
    """
    
    def __init__(self, model: ListaModelo, view: ListaVista) -> None:
        self._model = model
        self._view = view
        
        # Registramos las funciones que reaccionan a cada botón
        self._view.establecer_eventos(
            self._handler_inicio,
            self._handler_final,
            self._handler_eliminar,
            self._handler_vaciar
        )

    def _handler_inicio(self) -> None:
        """Procesa la inserción al principio de la estructura."""
        dato = self._view.obtener_dato()
        if not dato.strip():
            messagebox.showwarning("Aviso", "Por favor, ingrese un dato.")
            return
            
        self._model.insertar_inicio(dato)
        self._view.actualizar_pantalla(self._model.obtener_cadena_texto())
        self._view.limpiar_casilla()

    def _handler_final(self) -> None:
        """Procesa la inserción al final de la estructura."""
        dato = self._view.obtener_dato()
        if not dato.strip():
            messagebox.showwarning("Aviso", "Por favor, ingrese un dato.")
            return
            
        self._model.insertar_final(dato)
        self._view.actualizar_pantalla(self._model.obtener_cadena_texto())
        self._view.limpiar_casilla()

    def _handler_eliminar(self) -> None:
        """Captura excepciones de lista vacía de forma segura."""
        try:
            valor_removido = self._model.eliminar_inicio()
            messagebox.showinfo("Éxito", f"Se eliminó el dato: {valor_removido}")
        except IndexError as err:
            messagebox.showerror("Error de Operación", str(err))
            return
            
        self._view.actualizar_pantalla(self._model.obtener_cadena_texto())

    def _handler_vaciar(self) -> None:
        """Limpia los dos extremos de la arquitectura."""
        self._model.vaciar()
        self._view.actualizar_pantalla("None")
        self._view.limpiar_casilla()
