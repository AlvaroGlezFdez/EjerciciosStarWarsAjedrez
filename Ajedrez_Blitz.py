import time
# Creación de las varianbles (tiempos y jugador)v
tiempo_carlsen = 180
tiempo_nakamura = 180
tiempo_movimiento = 10
jugador_actual = "Carlsen"


# Creación de una estructuta de bucle while que establece las reglas, menú y tiempo de juego
while tiempo_carlsen > 0 and tiempo_nakamura > 0:
    print("tiempo actual - Carlsen:,",tiempo_carlsen" segundos, Nakamura:",tiempo_nakamura, "segundos")
    print("Es el turno de",jugador_actual)

    movimiento = input("Ingrese el jugador que realiza el movimiento ('Carlsen' o 'Nakamura') o 'Salir' para terminar: ")

    if movimiento == "Salir":
        print("La partida ha finalizado.")
        break
    elif movimiento == "Carlsen" and jugador_actual == "Carlsen":
        tiempo_carlsen -= tiempo_movimiento
    elif movimiento == "Nakamura" and jugador_actual == "Nakamura":
        tiempo_nakamura -= tiempo_movimiento
    else:
        print("Movimiento inválido. Intenta de nuevo.")
        continue

    if tiempo_carlsen <= 60 or tiempo_nakamura <= 60:
        tiempo_movimiento = 5

#última condición que establece el ganador por tiempo
if tiempo_carlsen <= 0 or tiempo_nakamura <= 0:
    ganador = "Carlsen" if tiempo_nakamura <= 0 else "Nakamura"
    print("La partida ha finalizado",ganador, "ha ganado!")