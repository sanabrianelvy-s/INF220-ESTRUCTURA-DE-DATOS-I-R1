import tkinter as tk
from modelo_polinomio import PolinomioModelo
from vista_polinomio import PolinomioVista
from controlador_polinomio import PolinomioControlador

def main() -> None:
    # 1. Inicializamos Tkinter
    raiz = tk.Tk()
    
    # 2. Instanciamos las capas del MVC de forma independiente
    modelo = PolinomioModelo()
    vista = PolinomioVista(raiz)
    
    # 3. El controlador une ambas capas
    controlador = PolinomioControlador(modelo, vista)
    
    # 4. Encendemos el bucle infinito de escucha de la ventana
    raiz.mainloop()

if __name__ == "__main__":
    main()
