import random

def imprimir_tablero(tablero):
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

def verificar_ganador(tablero, jugador):
    combinaciones = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(tablero[a] == tablero[b] == tablero[c] == jugador for a, b, c in combinaciones)

def jugar():
    tablero = [" "] * 9
    jugadores = ["X", "O"]
    turno = 0
    
    print("Empieza el juego")
    while True:
        imprimir_tablero(tablero)
        jugador_actual = jugadores[turno % 2]
        try:
            movimiento = int(input(f"Jugador {jugador_actual}, elige posición (1-9): ")) - 1
            if tablero[movimiento] != " ":
                print("Esa posición ya está ocupada.")
                continue
            tablero[movimiento] = jugador_actual
        except (ValueError, IndexError):
            print("Entrada inválida. Elige un número del 1 al 9.")
            continue

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Felicidades! El jugador {jugador_actual} ha ganado.")
            break
        
        if " " not in tablero:
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break
            
        turno += 1

if __name__ == "__main__":
    jugar()
