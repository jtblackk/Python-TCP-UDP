# program that models the behavior of the server module when using UDP


import socket


#PROGRAM OPTIONS
# if true, the server automatically processes datagrams sent to it.
# if false, the server only processes a datagram after the user presses enter
USER_PRESSES_AUTO_RECEIVE_BUTTON = True

BUFFER_SIZE = 1024





# ----------- server socket setup ----------- #

# step 1: create udp socket
# IN-GAME: not 100% sure how we should represent socket creation
input("press enter to create a socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print()

# step 2: bind the socket to a port on the server module
#IN-GAME: after they press "bind" and type in the port to bind to, 
# the port on the module's port that they specified should visibly open up.
input("press enter to bind the socket to an ip address & port")

# ask for socket info
server_address = input("\tplease enter the ip address of this module: ")
server_port = int(input("\tplease enter a port to use on this module: "))

# bind the socket
sock.bind((server_address, server_port))

# DEBUGGING: prints out the address & port bound to the socket
print("\nready to received data on server socket with address & port: ", sock.getsockname())





# ----------- receive data ------------ #

# step 4: receive and process data
#IN-GAME: a datagram flies from the client into the server via the opened port. when the
#         user presses the "receive" button, the packet gets processed and server does
#         something with the message (e.g., prints it out into the game world) 
while(True):
    # receive data
    if not USER_PRESSES_AUTO_RECEIVE_BUTTON:
        input("\npress enter to process data")
    data_received, data_sender_socket = sock.recvfrom(BUFFER_SIZE)
    
    # do something with the data

    # DEBUGGING: just some useful information about what's happening on the server side
    print("\n---------------------------------------------------------------")
    print("\tdata received at: ", sock.getsockname(), "[server socket/this module]")
    print("\tdata received from:", data_sender_socket)
    print("\tdata received:", "\'" + data_received.decode('utf-8') + "\'")
    print("---------------------------------------------------------------")
