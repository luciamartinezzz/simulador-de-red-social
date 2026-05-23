from collections import deque

red = {
    "Ana": ["Luis", "Marta"],
    "Luis": ["Ana", "Carlos"],
    "Marta": ["Ana", "Sofia"],
    "Carlos": ["Luis"],
    "Sofia": ["Marta"]
}

def mostrar_red():
    print("\nRed social:")
    for persona in red:
        print(persona, "->", red[persona])

def agregar_persona():
    nombre = input("Nombre de la persona: ")

    if nombre in red:
        print("Esa persona ya existe")
    else:
        red[nombre] = []
        print("Persona añadida")

def agregar_amistad():
    p1 = input("Primera persona: ")
    p2 = input("Segunda persona: ")

    if p1 not in red or p2 not in red:
        print("Alguna persona no existe")
    else:
        if p2 not in red[p1]:
            red[p1].append(p2)
        if p1 not in red[p2]:
            red[p2].append(p1)
        print("Amistad añadida")

def propagar():
    inicio = input("Persona que empieza el rumor: ")

    if inicio not in red:
        print("Esa persona no está en la red")
        return

    visitados = []
    cola = deque()
    cola.append((inicio, 0))

    print("\nPropagación del rumor:")

    while len(cola) > 0:
        persona, turno = cola.popleft()

        if persona not in visitados:
            visitados.append(persona)
            print("Turno", turno, ":", persona)

            for amigo in red[persona]:
                if amigo not in visitados:
                    cola.append((amigo, turno + 1))

def buscar_persona():
    nombre = input("Nombre a buscar: ")

    if nombre in red:
        print(nombre, "sí está en la red")
        print("Sus conexiones son:", red[nombre])
    else:
        print("No se ha encontrado")

def menu():
    opcion = ""

    while opcion != "6":
        print("\nMENU")
        print("1. Mostrar red")
        print("2. Añadir persona")
        print("3. Añadir amistad")
        print("4. Simular propagación")
        print("5. Buscar persona")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_red()
        elif opcion == "2":
            agregar_persona()
        elif opcion == "3":
            agregar_amistad()
        elif opcion == "4":
            propagar()
        elif opcion == "5":
            buscar_persona()
        elif opcion == "6":
            print("Fin del programa")
        else:
            print("Opción incorrecta")

menu()