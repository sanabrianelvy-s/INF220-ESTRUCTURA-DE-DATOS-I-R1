import tkinter as tk
from typing import Any, Callable

class PolinomioVista:
    """
    Dibuja y administra los componentes gráficos en la pantalla.
    """
    
    def __init__(self, ventana: tk.Tk) -> None:
        self._ventana = ventana
        self._ventana.title("Gestor de Polinomios - MVC")
        self._ventana.geometry("400x250")
        
        # 1. Etiquetas y campos de texto para Coeficiente
        self._lbl_coef = tk.Label(ventana, text="Coeficiente:")
        self._lbl_coef.pack(pady=2)
        self._txt_coef = tk.Entry(ventana)
        self._txt_coef.pack(pady=2)
        
        # 2. Etiquetas y campos de texto para Exponente
        self._lbl_exp = tk.Label(ventana, text="Exponente:")
        self._lbl_exp.pack(pady=2)
        self._txt_exp = tk.Entry(ventana)
        self._txt_exp.pack(pady=2)
        
        # 3. Botón para Agregar Término
        self._btn_agregar = tk.Button(ventana, text="Agregar Término")
        self._btn_agregar.pack(pady=5)
        
        # 4. Botón para Nuevo Polinomio (Limpiar)
        self._btn_limpiar = tk.Button(ventana, text="Nuevo Polinomio")
        self._btn_limpiar.pack(pady=5)
        
        # 5. Etiqueta grande donde se muestra el resultado en vivo
        self._lbl_resultado = tk.Label(
            ventana, text="P(X) = 0", font=("Arial", 12, "bold")
        )
        self._lbl_resultado.pack(pady=15)

    def establecer_eventos(
        self, callback_agregar: Callable, callback_limpiar: Callable
    ) -> None:
        """Conecta las acciones de los botones con el controlador."""
        self._btn_agregar.config(command=callback_agregar)
        self._btn_limpiar.config(command=callback_limpiar)

    def obtener_entradas(self) -> tuple[str, str]:
        """Retorna los textos crudos escritos por el usuario."""
        return self._txt_coef.get(), self._txt_exp.get()

    def limpiar_entradas(self) -> None:
        """Borra el contenido escrito dentro de las cajas de texto."""
        self._txt_coef.delete(0, tk.END)
        self._txt_exp.delete(0, tk.END)

    def actualizar_pantalla(self, expresion: str) -> None:
        """Modifica la etiqueta del polinomio en la pantalla."""
        self._lbl_resultado.config(text=expresion)
