###############################
# Created by Pascal Böhler    #
# 06/02/2019 15:33            #
###############################

# Imports
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser()

# Add the arguments (--help is included by default)
parser.add_argument("-p", "--Port", help="Hands over the port the server listens on for new connections (Standard 33000)", default=33000, type=int)


# Parse the arguments (make them useable)
args = parser.parse_args()

clients = {}
addresses = {}

HOST = ''
PORT = args.Port
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def accept_incoming_connections():
    """Sets up handling for incoming clients"""
    while True:
        client, client_addr = SERVER.accept()
        print("%s:%s has connected." % client_addr)
        client.send(bytes("Greetings from the cave!" + " Now type your name and press enter!", "utf8"))
        addresses[client] = client_addr
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    # Takes client socket argument.
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit or press the disconnect button in your toolbar.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            # if the message is not {quit}, send the received message to all other clients
            broadcast(msg, name+": ")
        else:
            # if the client quits a message will be send to all connected clients.
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    # prefix is for name identification
    """Broadcasts a message to all the clients"""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


if __name__ == "__main__":
    SERVER.listen(5) # Listens for 5 connections at max.
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start() # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
