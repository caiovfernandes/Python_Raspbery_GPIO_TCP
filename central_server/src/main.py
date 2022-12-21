from threading import Thread
from server import init_server, CONNECTIONS
from time import sleep
import server_interface

def main():
    # init_server()
    server_thread  = Thread(target=init_server)
    server_thread.start()
    server_thread.join()

    interface_thread = Thread(target=server_interface.main)
    interface_thread.start()



    # message = input()
    # print(message)
    # for client in CONNECTIONS:
    #     print(client)
    #     client.socket.sendall(message.encode())



if __name__ == '__main__':
    main()
