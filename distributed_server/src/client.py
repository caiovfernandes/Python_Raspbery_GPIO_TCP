import socket
import threading
import sys
import json


#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string

class Server(threading.Thread):
    def __init__(self, socket, signal, sala):
        threading.Thread.__init__(self)
        self.socket = socket
        self.signal = signal
        self.sala = sala

    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(1024)
                # print("RECEIVED DATA:")
                # print(str(data.decode("utf-8")))
            except:
                print("You have been disconnected from the server")
                self.signal = False
                break
            if data != "":
                self.tratar_mensagem_servidor(data.decode("utf-8"))

    def tratar_mensagem_servidor(self, message): 
        print(message)
        message = eval(message)
        operation = message["operation"]
        print("RECEIVED MESSAGE:")
        print(message)
        if operation == "get_informacoes_sala":
            response = self.sala.get_informacoes_sala()
            print("RESPONSE")
            print(str(response))
            self.socket.sendall(str.encode(json.dumps(response)))
        elif operation == "set_informacoes_sala":
            self.sala.set_attribute_value_by_name(message["attribute"], message["estado"])



def init_client(host, port):
    print("Iniciando cliente")


    #Attempt connection to server
    try:
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCK.connect((host, port))
    except:
        print("Could not make a connection to the server")
        input("Press enter to quit")
        sys.exit(0)

    #Create new thread to wait for data
    receiveThread = threading.Thread(target = receive, args = (SOCK, True))
    receiveThread.start()

    return SOCK

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
# while True:
#     message = input()
#     sock.sendall(str.encode(message))
