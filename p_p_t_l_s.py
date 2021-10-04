#encoding:UTF-8
import random
import pickle
puntajePc = 0
puntajeUsuario = 0
puntajeTotal = 0

def porcentaje():
    if puntajeTotal > 0:
        x = ((puntajeTotal - puntajePc) / puntajeTotal) * 100
        return x
    elif puntajeTotal == 0:
        x = 0
    return x



while True: 
    ganaUsuario = 0
    ganaPc = 0
    aleatorio = random.randrange(0, 5)
    elijePc = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Mostrar Puntajes")
    print("7) Salir")
    opcion = int(input("Que eliges: "))
    
    if opcion == 1:
        eligeUsuario = "piedra"
    elif opcion == 2:
        eligeUsuario = "papel"
    elif opcion == 3:
        eligeUsuario = "tijera"
    elif opcion == 4:
        eligeUsuario = "lagarto"
    elif opcion == 5:
        eligeUsuario = "spock"
    elif opcion == 6:
        print ("Puntajes: ", puntajeTotal)
        print ("Usuario: ", puntajeUsuario)
        print ("Pc: ", puntajePc)
        print ("Porcentaje de victorias: ", porcentaje(), "%")
        continue
    elif opcion == 7:
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
        continue

        
    print("Tu eliges: ", eligeUsuario)   
    if aleatorio == 0:
        eligePc = "piedra"
    elif aleatorio == 1:
        eligePc = "papel"
    elif aleatorio == 2:
        eligePc = "tijera"
    elif aleatorio == 3:
        eligePc = "lagarto"
    elif aleatorio == 4:
        eligePc = "spock"
    print("PC eligio: ", eligePc)
    print("...")
    
    if eligePc == "piedra" and eligeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
        ganaUsuario = 1
    elif eligePc == "piedra" and eligeUsuario == "spock":
        print ("Ganaste, Spock vaporiza piedra")
        ganaUsuario = 1
    elif eligePc == "papel" and eligeUsuario == "tijera":
        print("Ganaste, tijera corta papel")
        ganaUsuario = 1
    elif eligePc == "tijera" and eligeUsuario == "piedra":
        print("Ganaste, piedra aplasta tijera")
        ganaUsuario = 1
    elif eligePc == "lagarto" and eligeUsuario == "piedra":
        print("Ganaste, piedra aplasta a lagarto")
        ganaUsuario = 1
    elif eligePc == "lagarto" and eligeUsuario == "tijera":
        print("Ganaste, tijera decapita a Lagarto")
        ganaUsuario= 1
    elif eligePc == "tijera" and eligeUsuario == "spock":
        print("Ganaste, Spock rompe tijera")
        ganaUsuario = 1
    elif eligePc == "spock" and eligeUsuario == "lagarto":
        print("Ganaste, lagarto envenena a Spock")
        ganaUsuario = 1
    elif eligePc == "papel" and eligeUsuario == "lagarto":
        print ("Ganaste, lagarto devora papel")
        ganaUsuario = 1
    elif eligePc == "spock" and eligeUsuario == "papel":
        print ("Ganaste, papel desautoriza a Spock")
        ganaUsuario = 1


    elif eligePc == "papel" and eligeUsuario == "piedra":
        print ("Perdiste, papel envuelve piedra")
        ganaPc = 1
    elif eligePc == "papel" and eligeUsuario == "spock":
        print ("Perdiste, papel desautoriza spock")
        ganaPc = 1
    elif eligePc == "piedra" and eligeUsuario == "lagarto":
        print ("Perdiste piedra aplasta lagarto")
        ganaPc = 1
    elif eligePc == "piedra" and eligeUsuario == "tijera":
        print ("Perdiste, piedra aplasta tijera")
        ganaPc = 1
    elif eligePc == "lagarto" and eligeUsuario == "spock":
        print ("Perdiste, lagarto envenena spock")
        ganaPc = 1
    elif eligePc == "lagarto" and eligeUsuario == "papel":
        print ("Perdiste, lagarto devora papel")
        ganaPc = 1
    elif eligePc == "spock" and eligeUsuario == "tijera":
        print("Perdiste, spock rompe tijera")
        ganaPc = 1
    elif eligePc == "spock" and eligeUsuario == "piedra":
        print("Perdiste, spock vaporiza piedra")
        ganaPc = 1
    elif eligePc == "tijera" and eligeUsuario == "lagarto":
        print("Perdiste, tijera decapita lagarto")
        ganaPc = 1
    elif eligePc == "tijera" and eligeUsuario == "papel":
        print("Perdiste, tijera corta papel")
        ganaPc = 1

    elif eligePc == eligeUsuario:
        print("Empate xd")

    puntajeUsuario = puntajeUsuario + ganaUsuario
    puntajePc = puntajePc + ganaPc
    puntajeTotal = puntajeUsuario + puntajePc

    again = input("Jugamos de nuevo? Si/No: ")
    if 'si' or 's' in again:
        continue
    elif 'no' or 'n' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")


