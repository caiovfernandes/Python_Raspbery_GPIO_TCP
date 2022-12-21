import json
from sala import Sala
from client import Server
import threading
import sys
import socket

# global SALAS
# SALAS = {
#     "1": Sala(1),
#     "2": Sala(2)
# }

def main():
    print("Informe a sala a ser monitorada (1 ou 2):")
    numero_sala = int(input())
    if numero_sala not in [1, 2]:
        print("Valor incorreto para número da sala (1 ou 2)")
        return 1

    sala = Sala(numero_sala)
    newConnectionsThread = threading.Thread(target=sala.update_states)
    newConnectionsThread.start()

    # estado_sala.update_states()
    # newConnectionsThread.join()
    # clientTCPThread = threading.Thread(target=init_client, args=(sala.host, sala.port))
    # clientTCPThread.start()

    print(sala.host)
    print(sala.port)
    try:
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCK.connect((sala.host, sala.port))
    except:
        print("Could not make a connection to the server")
        input("Press enter to quit")
        sys.exit(0)

    serverConnectionThread = Server(SOCK, True, sala)
    serverConnectionThread.run()

if __name__ == "__main__":
    main()