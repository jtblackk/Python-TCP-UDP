import socket

#PROGRAM OPTIONS

USER_PRESSES_AUTO_RECEIVE_BUTTON = True

BUFFER_SIZE = 1024


# ----------- server socket setup ----------- #

# step 1: create udp socket
# IN-GAME: not 100% sure how we should represent socket creation
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# step 2: bind the socket to a port on the server module
# ask for socket info
server_address = input("please enter the ip address of this module: ")
server_port = int(input("please enter a port to use on this module: "))

# bind the socket
sock.bind((server_address, server_port))

# DEBUGGING: prints out the address & port bound to the socket
print("\tsocket address & port before sending data:", sock.getsockname())


# ----------- receive data ------------ #

if USER_PRESSES_AUTO_RECEIVE_BUTTON:
    while(True):
        # receive data
        data_received, data_sender_socket = sock.recvfrom(BUFFER_SIZE)
        
        # do something with the data

        # DEBUGGING: just some useful information about what's happening on the client side
        print("---------------------------------------------------------------")
        print("\tdata received:", "\'" + data_received.decode('utf-8') + "\'")
        print("\tdata received from:", data_sender_socket)
        # print("\tdata sent to:", (server_address, server_port))
        print("---------------------------------------------------------------")
else:
    print("need to handle this case")