import random

##
##      FUNCIONES
##
def recuadro(posiciones, partidas):
    print("Jugador X (tu)")
    print(f"Partida nº: {partidas}")
    print("    0   1   2")
    print("  ╔═══╦═══╦═══╗")
    print(f"0 ║ {posiciones[0][0]} ║ {posiciones[0][1]} ║ {posiciones[0][2]} ║")
    print("  ╠═══╬═══╬═══╣")
    print(f"1 ║ {posiciones[1][0]} ║ {posiciones[1][1]} ║ {posiciones[1][2]} ║")
    print("  ╠═══╬═══╬═══╣")
    print(f"2 ║ {posiciones[2][0]} ║ {posiciones[2][1]} ║ {posiciones[2][2]} ║")
    print("  ╚═══╩═══╩═══╝")

def saltoLinea():
    for i in range(10):
        print("\n")

def posicionAJugar(posiciones):
    try:
        altura = int(input("Posicion a poner (altura): "))
        anchura = int(input("Posicion a poner (anchura): "))
        if posiciones[altura][anchura] == " ":
            posiciones[altura][anchura] = "X"
            print("\n\n")
            return True
        else:
            print("\n")
            print("Posicion no aceptada")
            print("\n\n")
            return False
    except:
        print("ERROR: ingreso de numero incorrecto")
        return False


def comprobarGanador(posiciones, ganador):
    # Horizontal
    if posiciones[0][0] == posiciones[0][1] != " " and posiciones[0][1] == posiciones[0][2] != " ":
        if posiciones[0][0] == "X":
            ganador = 1
        if posiciones[0][0] == "O":
            ganador = 2

    if posiciones[1][0] == posiciones[1][1] != " " and posiciones[1][1] == posiciones[1][2] != " ":
        if posiciones[1][0] == "X":
            ganador = 1
        if posiciones[1][0] == "O":
            ganador = 2
    
    if posiciones[2][0] == posiciones[2][1] != " " and posiciones[2][1] == posiciones[2][2] != " ":
        if posiciones[2][0] == "X":
            ganador = 1
        if posiciones[2][0] == "O":
            ganador = 2
    
    # Vertical
    if posiciones[0][0] == posiciones[1][0] != " " and posiciones[1][0] == posiciones[2][0] != " ":
        if posiciones[0][0] == "X":
            ganador = 1
        if posiciones[0][0] == "O":
            ganador = 2

    if posiciones[0][1] == posiciones[1][1] != " " and posiciones[1][1] == posiciones[2][1] != " ":
        if posiciones[0][1] == "X":
            ganador = 1
        if posiciones[0][1] == "O":
            ganador = 2
    
    if posiciones[0][2] == posiciones[1][2] != " " and posiciones[1][2] == posiciones[2][2] != " ":
        if posiciones[2][2] == "X":
            ganador = 1
        if posiciones[2][2] == "O":
            ganador = 2

    # Esquinas
    if posiciones[0][0] == posiciones[1][1] != " " and posiciones[1][1] == posiciones[2][2] != " ":
        if posiciones[0][0] == "X":
            ganador = 1
        if posiciones[0][0] == "O":
            ganador = 2

    if posiciones[0][2] == posiciones[1][1] != " " and posiciones[1][1] == posiciones[2][0] != " ":
        if posiciones[1][1] == "X":
            ganador = 1
        if posiciones[1][1] == "O":
            ganador = 2

    
    return ganador

def ia():
    x = random.randint(0,2)
    y = random.randint(0,2)
    if posiciones[x][y] == " ":
        posiciones[x][y] = "O"
        return True
    else:
        return False

def comprobadorEmpate():
    espacios = 0
    for pos in posiciones:
        for pos2 in pos:
            if pos2 == " ":
                espacios += 1
    return espacios

##
##      DATOS
##
posiciones = [[" "," "," "],[" "," "," "],[" "," "," "]] # las posiciones de partida
partidas = 0 # La cantidad de partidas jugadas
ganador = 0 # Si es 0 nadie gana, si es 1 el jugador, 2 el ordenadory 3 empate.
correcto = False # Si la posicion no es correcta utiliza esto para entrar en un bucle
correctoIa = False # Si el pc ha acertado la posicion

##
##      CODIGO
##
print("╔══════════════════╗")
print("║   TRES EN RAYA   ║")
print("╚══════════════════╝")
input("Dale al enter para continuar:")
saltoLinea()

# Jugando la partida
while ganador == 0:
    # Datos
    partidas += 1
    correcto = False
    correctoIa = False

    # Funcionalidad
    recuadro(posiciones, partidas)

    while correcto == False:
        correcto = posicionAJugar(posiciones)
        if comprobadorEmpate() == True:
            correcto = True
            correctoIa = True

    while correctoIa == False:
        correctoIa = ia()
        if comprobadorEmpate() == True:
            correctoIa = True

    if comprobadorEmpate() == 0:
        ganador = 3

    ganador = comprobarGanador(posiciones,ganador)

recuadro(posiciones, partidas)
if ganador == 1:
    print("Felicidades has ganado")

if ganador == 2:
    print("Vaya has pedido")

if ganador == 3:
    print("Empate")
