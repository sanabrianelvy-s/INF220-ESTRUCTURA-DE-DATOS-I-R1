Modelos de Representación de Datos

Resumen ejecutivo de los conceptos clave del Tema 1 para la materia Estructura de Datos 1.

1. ¿Qué es un Dato?

Es cualquier valor mínimo que se guarda en la memoria para ser procesado por un programa (ej. un número, un nombre o una nota). 

2. Tipo de Dato Abstracto (ADT)
   
Es la descripción de una estructura desde afuera (lo que ve el usuario). Define qué operaciones hace (ej. en una Pila: apilar y desapilar), pero oculta por completo cómo está programada por dentro (abstracción).

3. Datos Estáticos (Memoria Fija)

Estructuras con un tamaño definido desde el inicio que no puede cambiar durante la ejecución.
Ventaja: Acceso instantáneo a cualquier posición mediante índices (Eficiencia O(1)).
Desventaja: Si se llena e intentas meter más datos, el programa colapsa con un error de desorbdamiento (OverflowError).

4. Datos Dinámicos (Memoria Flexible)

Estructuras que crecen o se achican libremente en tiempo de ejecución en la memoria Heap.
Cómo funciona: Usa Nodos sueltos que se conectan entre sí mediante un puntero o enlace (siguiente).
Ventaja: Memoria ilimitada y adaptable; nunca se llena por tamaño fijo.
Desventaja: Acceso lento. No hay índices; hay que recorrer los nodos uno por uno desde el principio (Eficiencia O(n)).

5. Datos Simulados (Faker)

Datos ficticios generados por código (usando librerías como Faker y random) para llenar y probar el comportamiento de nuestras estructuras de datos con cientos de registros sin tener que escribirlos a mano.

6. Datos Persistentes
