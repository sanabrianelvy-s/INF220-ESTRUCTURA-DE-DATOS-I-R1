import tkinter as tk
from model import ListaModelo
from view import ListaVista
from controller import ListaControlador

def main() -> None:
    # 1. Creamos la raíz visual de Tkinter
    raiz = tk.Tk()
    
    # 2. Inicializamos los componentes con sus nombres de capa exactos
    modelo = ListaModelo()
    vista = ListaVista(raiz)
    
    # 3. El controlador enlaza la arquitectura
    _ = ListaControlador(modelo, vista)
    
    # 4. Ponemos en marcha la ventana
    raiz.mainloop()

if __name__ == "__main__":
    main()
