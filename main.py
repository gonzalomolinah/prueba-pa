from dccasillas import DCCasillas
from funciones import validar_numero, validar_nombre, validar_configuracion


def imprimir_bienvenida(usuario: str, puntaje: int, resueltos: int, totales: int) -> None:
    print(f'''
¡Bienvenido a DCCasillas!
Usuario: {usuario}, Puntaje: {puntaje}
Tableros resueltos: {resueltos} de {totales}
''')

def menu_juegos() -> None:
    print('''
*** Menú de Juego ***
[1] Iniciar juego nuevo
[2] Continuar juego
[3] Guardar estado de juego
[4] Recuperar estado de juego
[5] Salir del programa
''')

def menu_acciones() -> None:
    print('''
*** Menú de Acciones ***
[1] Mostrar tablero
[2] Habilitar/deshabilitar casillas
[3] Verificar solución
[4] Encontrar solución
[5] Volver al menú de Juego
''')

def iniciar_juego_nuevo_1() -> None:
    usuario = input("Ingrese su nombre de usuario: ")
    while not validar_nombre(usuario):
        print("Nombre de usuario no válido. Intente de nuevo.")
        usuario = input("Ingrese su nombre de usuario: ")
    config = input("Ingrese el archivo de configuracion (ej: configuracion.txt): ")
    while not validar_configuracion(config):
        print("Archivo de configuración no válido. Intente de nuevo.")
        config = input("Ingrese el archivo de configuracion (ej: configuracion.txt): ")
    return [usuario, config]

def iniciar_juego_nuevo_2(usuario: DCCasillas) -> None:
    pregunta = input("Desea cambiar el usuario (si/no)")
    while pregunta.lower() not in ["si", "no"]:
        print("Tu respuesta no fue valida. Intente de nuevo")
        pregunta = input("Desea cambiar el usuario (si/no): ")

    if pregunta.lower() in ["si", "sí"]:
        [usuario, config] = iniciar_juego_nuevo_1()
        return [usuario, config]
    return [-1, -1, -1]

def main() -> None:


    Jugando = True
    acciones = False
    imprimir_bienvenida("UUU", 0, 0, 0)
    usuario = ""
    vueltas = 0

    while Jugando:


        # imprimir_bienvenida(juego.usuario, juego.puntaje, num_resueltos, len(juego.tableros))
        # menu_juegos()

        #Print inicial. Usuario uno por defecto, todo lo demas 0 por poner algo
        #Muestra el menu, y el nombre del usuario se asgina un string vacio

        if vueltas > 0:
            num_resueltos = 0
            for tablero in juego.tableros:
                if tablero.estado:
                    num_resueltos += 1
            imprimir_bienvenida(juego.usuario, juego.puntaje, num_resueltos, len(juego.tableros))

        #Menu de juegos

        menu_juegos()

        opcion_usuario = input("Seleccione una opción: ")
        opciones_validas = ["1", "2", "3", "4", "5"]

        while opcion_usuario not in opciones_validas or not validar_numero(opcion_usuario):
            print("Opción no válida. Intente nuevamente.")
            opcion_usuario = input("Seleccione una opción: ")

        opcion_usuario = int(opcion_usuario)

        if opcion_usuario == 1:
            if usuario == "":
                lista = iniciar_juego_nuevo_1()
                usuario = lista[0]
                config = lista[1]
                juego = DCCasillas(usuario, config)

            else:
                lista = iniciar_juego_nuevo_2(juego)
                if len(lista) == 2:
                    usuario = lista[0]
                    config = lista[1]
                    juego = DCCasillas(usuario, config)

        elif opcion_usuario == 2:
            numero_max = len(juego.tableros) - 1
            if usuario == "":
                print("No hay un juego en curso. Debes marcar la opcion 1 en el menu de opciones.")
            else:
                num = int(input(f"Ingrese el número del tablero (entre 0 y {numero_max}): "))

                while num < 0 or num > numero_max:
                    print("Número de tablero no válido.")
                    num = int(input(f"Ingrese el número del tablero (entre 0 y {numero_max}): "))
                juego.abrir_tablero(num)
                acciones = True

        elif opcion_usuario == 3:
            if not juego.guardar_estado:
                print("Error al guardar el estado del juego. Intente nuevamente.")
            # juego.guardar_estado()
            print("Estado del juego guardado.")

        elif opcion_usuario == 4:
            if not juego.recuperar_estado():
                print("Error al recuperar el estado del juego. Intente nuevamente.")
            print("Estado del juego recuperado.")

        elif opcion_usuario == 5:
            print("Nos vemosssssss!")
            Jugando = False
        

        #Seccion del menu de acciones

        while acciones:
            num_resueltos = 0
            for tablero in juego.tableros:
                if tablero.estado:
                    num_resueltos += 1
            imprimir_bienvenida(juego.usuario, juego.puntaje, num_resueltos, len(juego.tableros))
            menu_acciones()

            opcion_usuario = input("Seleccione una opción: ")

            while opcion_usuario not in opciones_validas or not validar_numero(opcion_usuario):
                print("Opción no válida. Intente nuevamente.")
                opcion_usuario = input("Seleccione una opción: ")

            opcion_usuario = int(opcion_usuario)

            tablero = juego.tableros[juego.tablero_actual]

            if opcion_usuario == 1:
                tablero.mostrar_tablero()

            elif opcion_usuario == 2:
                fila = input("Seleccione la fila: ")
                columna = input("Seleccione la columna: ")
                bool1 = validar_numero(fila)
                bool2 = validar_numero(columna)
                if not bool1 or not bool2:
                    bool3 = True
                    bool4 = True
                else:
                    bool3 = int(fila) < 0 or int(fila) >= len(tablero.tablero)
                    bool4 = int(columna) < 0 or int(columna) >= len(tablero.tablero[0])

                while not bool1 or (not bool2) or (bool3) or bool4:
                    print("Fila o columna no válida. Intente nuevamente.")
                    print(bool1, bool2, bool3, bool4)
                    fila = input("Seleccione la fila: ")
                    columna = input("Seleccione la columna: ")
                    bool1 = validar_numero(fila)
                    bool2 = validar_numero(columna)
                    if not bool1 or not bool2:
                        bool3 = True
                        bool4 = True
                    else:
                        bool3 = int(fila) < 0 or int(fila) >= len(tablero.tablero)
                        bool4 = int(columna) < 0 or int(columna) >= len(tablero.tablero[0])

                fila = int(fila)
                columna = int(columna)
                tablero.modificar_casilla(fila, columna)

            elif opcion_usuario == 3:
                tablero.validar()
                if tablero.validar():
                    print("La solución es válida.")
                    print("Movimientos realizados:", tablero.movimientos)
                    juego.puntaje += tablero.movimientos
                else:
                    print("La solución no es válida, sigue intentando.")

            elif opcion_usuario == 4:
                tablero.encontrar_solucion()

            elif opcion_usuario == 5:
                acciones = False

        vueltas += 1

if __name__ == "__main__":
    main()
