from camera import camera
from threading import Thread
from time import sleep
from hardware import botao, piscarLed,steps

senhasPermitidas = []
senhaAtual = ''
contador = 0
class Estado():
    est = 0

estado = Estado()

def abrirHardware():
    steps(500)
    sleep(5)
    steps(-500)

def abrirPorta(senha):
    if senha in senhasPermitidas:
        abrirHardware()
    else:
        print("trancado")

def menu():
    while True:
        contador = botao()
        if contador > 5000:
            estado.est = 1
            print(estado.est)
        elif contador > 0:
            print(contador)
            abrirHardware()
        if estado.est == 1:
            piscarLed()
        
th2 = Thread(target=menu)

th2.start()

while True:
    senhaAtual = camera()
    print(senhaAtual)
    if estado.est == 0:
        abrirPorta(senhaAtual)
    elif estado.est == 1:
        senhasPermitidas.append(senhaAtual)
        estado.est = 0
    print(estado,senhasPermitidas)
    
