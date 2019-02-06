###############################
# Created by Pascal Böhler    #
# 06/02/2019 15:33            #
###############################

# imoprt socjet programming library
import socket

# import thread module
from _thread import *
import threading
print_lock = threading.Lock()

# Public variables
connectionList = []

# thread function
def threaded(c):
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break


        # Append data to message list and send message to all other clients
        sendToOthers(data)


    c.close()


def Main():
    host = ""

    # reverse a port on cour computer
    # in our case it is 8080 but it
    # can be anything
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print("Connected to: ", addr[0], ":", addr[1])

        connectionList.append(c)

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))

    s.close()

'''
def sendToOthers(data):
    for element in connectionList:
        element.send(data)

'''

if __name__ == '__main__':
    Main()