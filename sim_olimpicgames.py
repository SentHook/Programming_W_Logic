print('Simulador de Juegos Olímpicos')

while True:

    print('\n1. Registro de eventos')
    print('2. Registro de participantes')
    print('3. Simulación de eventos')
    print('4. Creación de informes')
    print('5. Salir del programa')

    option = input("Selección de una acción: ")

    match option:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del simulador")
            break
        case _:
            print("Opción inválida. Por favor, selecciona una nueva.")
