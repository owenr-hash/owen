def historia():
    print("Parte 1: El comienzo")
    print("Un día soleado, te encuentras en un bosque misterioso.")
    print("De repente, escuchas un ruido extraño.")
    print("¿Qué haces?")
    print("1. Investigar el ruido")
    print("2. Ignorar el ruido y seguir adelante")

    decision1 = input("Elige una opción (1 o 2): ")

    if decision1 == "1":
        print("Parte 2A: El encuentro")
        print("Al investigar el ruido, te encuentras con un ser mágico.")
        print("El ser te ofrece dos opciones:")
        print("1. Aceptar su ayuda")
        print("2. Rechazar su ayuda")

        decision2 = input("Elige una opción (1 o 2): ")

        if decision2 == "1":
            print("Parte 3A: El final feliz")
            print("Con la ayuda del ser mágico, encuentras un tesoro escondido y regresas a casa feliz.")
        elif decision2 == "2":
            print("Parte 3B: El desafío")
            print("Al rechazar la ayuda, te enfrentas a un desafío peligroso, pero logras superarlo con valentía.")
    elif decision1 == "2":
        print("Parte 2B: El camino solitario")
        print("Decides ignorar el ruido y sigues adelante, pero te encuentras perdido en el bosque.")
        print("De repente, encuentras un camino.")
        print("¿Qué haces?")
        print("1. Seguir el camino")
        print("2. Regresar por donde viniste")

        decision2 = input("Elige una opción (1 o 2): ")

        if decision2 == "1":
            print("Parte 3C: El descubrimiento")
            print("Al seguir el camino, descubres un hermoso paisaje y encuentras la salida del bosque.")
        elif decision2 == "2":
            print("Parte 3D: El regreso a casa")
            print("Decides regresar, pero te toma mucho tiempo encontrar el camino de vuelta a casa.")
    else:
        print("Opción inválida. Fin de la historia.")

historia()
