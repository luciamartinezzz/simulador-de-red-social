# Simulador de propagación de información en una red social

Este proyecto es un programa sencillo hecho en Python para simular cómo se puede propagar un rumor o una información dentro de una red social.

La red está representada como un grafo. Cada persona es un nodo y cada amistad es una conexión entre dos nodos. Para guardar esas conexiones se usa un diccionario de Python, donde cada persona tiene una lista con sus amigos.

El programa te deja:

- mostrar la red social
- añadir personas
- añadir amistades
- buscar una persona
- simular cómo se propaga un rumor

La parte principal del proyecto es la simulación de la propagación. Para eso se usa BFS. Este algoritmo sirve para recorrer el grafo por niveles. En este caso, primero aparece la persona que empieza el rumor, después sus amigos, luego los amigos de esos amigos, y así hasta que ya no quedan más personas conectadas.


## Cómo ejecutar el programa

Para usarlo hay que abrir la terminal en la carpeta del proyecto y escribir:

```bash
python3 main.py
```

Después aparece un menú y se van eligiendo las opciones con números.

## Ejemplo de red

El programa empieza con esta red de ejemplo:

- Ana está conectada con Luis y Marta.
- Luis está conectado con Ana y Carlos.
- Marta está conectada con Ana y Sofia.
- Carlos está conectado con Luis.
- Sofia está conectada con Marta.

Así ya se puede probar la simulación sin tener que crear toda la red desde cero.

## Conclusión

Este proyecto sirve para practicar grafos y recorridos. Aunque es sencillo, representa una situación real, porque en una red social la información se mueve de persona a persona según las conexiones que tenga cada una.
