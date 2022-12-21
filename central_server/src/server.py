import socket
import threading
import json

global CONNECTIONS
CONNECTIONS = []
global TOTAL_CONNECTIONS
TOTAL_CONNECTIONS = 0


class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        # self.sala = sala

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(1024)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                CONNECTIONS.remove(self)
                break
            if data != "":
                print("SALA " + str(self.id+1))
                print(data)
                # for client in CONNECTIONS:
                #     if client.id != self.id:
                #         client.socket.sendall(data)


def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global TOTAL_CONNECTIONS
        CONNECTIONS.append(Client(sock, address, TOTAL_CONNECTIONS, "Name", True))
        CONNECTIONS[len(CONNECTIONS) - 1].start()
        print("New connection at ID " + str(CONNECTIONS[len(CONNECTIONS) - 1]))
        TOTAL_CONNECTIONS += 1


def init_server():
    host = input("Host: ")
    port = int(input("Port: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    newConnectionsThread.start()