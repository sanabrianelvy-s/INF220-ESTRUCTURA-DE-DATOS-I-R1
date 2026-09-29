import tkinter as tk
from typing import Callable

class ListaVista:
    """
    Dibuja y administra la ventana y componentes gráficos en pantalla.
    """
    
    def __init__(self, ventana: tk.Tk) -> None:
        self._ventana = ventana
        self._ventana.title("Laboratorio de Listas - MVC")
        self._ventana.geometry("400x260")
        
        # 1. Campo de Entrada para el Dato
        self._lbl_dato = tk.Label(ventana, text="Ingrese un Valor / Dato:")
        self._lbl_dato.pack(pady=5)
        self._txt_dato = tk.Entry(ventana)
        self._txt_dato.pack(pady=2)
        
        # 2. Fila de Botones de Inserción
        self._frame_botones = tk.Frame(ventana)
        self._frame_botones.pack(pady=5)
        
        self._btn_inicio = tk.Button(self._frame_botones, text="Insertar Inicio")
        self._btn_inicio.pack(side=tk.LEFT, padx=5)
        
        self._btn_final = tk.Button(self._frame_botones, text="Insertar Final")
        self._btn_final.pack(side=tk.LEFT, padx=5)
        
        # 3. Botones de Control y Limpieza
        self._btn_eliminar = tk.Button(ventana, text="Eliminar del Inicio")
        self._btn_eliminar.pack(pady=5)
        
        self._btn_vaciar = tk.Button(ventana, text="Vaciar Lista completa")
        self._btn_vaciar.pack(pady=5)
        
        # 4. Zona de Visualización del Monitor en Vivo
        self._lbl_monitor = tk.Label(
            ventana, text="None", font=("Arial", 11, "bold")
        )
        self._lbl_monitor.pack(pady=10)

    def establecer_eventos(
        self, 
        cb_inicio: Callable, 
        cb_final: Callable, 
        cb_eliminar: Callable, 
        cb_vaciar: Callable
    ) -> None:
        """Conecta los clics de los botones con el controlador."""
        self._btn_inicio.config(command=cb_inicio)
        self._btn_final.config(command=cb_final)
        self._btn_eliminar.config(command=cb_eliminar)
        self._btn_vaciar.config(command=cb_vaciar)

    def obtener_dato(self) -> str:
        """Retorna el texto escrito en la casilla de entrada."""
        return self._txt_dato.get()

    def limpiar_casilla(self) -> None:
        """Borra el contenido escrito dentro de la caja de texto."""
        self._txt_dato.delete(0, tk.END)

    def actualizar_pantalla(self, representacion: str) -> None:
        """Actualiza la flecha de nodos en la interfaz."""
        self._lbl_monitor.config(text=representacion)
