import socket

#PROGRAM OPTIONS

# if true, the server automatically accepts incoming connections
# if false, the user must press a button every time they want to accept a
# new incoming connection
USER_PRESSES_AUTO_ACCEPT_BUTTON = True

# if true, the server automatically processes packets sent to it.
# if false, the server only processes a packet after the user presses enter
USER_PRESSES_AUTO_RECEIVE_BUTTON = True

BUFFER_SIZE = 1024




# ----------- server socket setup ----------- #

# step 1: create tcp socket
# IN-GAME: not 100% sure how we should represent socket creation
input("press enter to create a socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print()

# step 2: bind the socket to a port on the server module
#IN-GAME: after they press "bind" and type in the port to bind to, 
# the port on the module's port that they specified should visibly open up.
input("press enter to bind the socket to an ip address & port")

# ask for socket info
server_address = input("\tplease enter the ip address of this module: ") # this can be handled automatically in-game
server_port = int(input("\tplease enter a port to use on this module: "))

# bind the socket
sock.bind((server_address, server_port))
print()

# step 3: start listening for an incoming connection
# IN-GAME: maybe an indicator starts blinking to show that the socket is now listening for connections 
input("press enter to start listening for incoming connections")
sock.listen(1)
print("\tnow listening on server socket: ", sock.getsockname())




# ----------- receive data ----------- #

# step 4: receive and process data. close connection when finished.
while(True):
    # accept an incoming connection, get a handle to it's socket for data transmission
    if not USER_PRESSES_AUTO_ACCEPT_BUTTON:
        input("\npress enter to accept an incoming connection")
    else: 
        print()

    client_socket, client_address = sock.accept()
    print("\taccepted connection: ", client_address)
    
    # receive data
    while True:
        # prompt user
        if not USER_PRESSES_AUTO_RECEIVE_BUTTON:
            input("\npress enter to process data")
        data_received = client_socket.recv(BUFFER_SIZE)

        # break loop if no more data
        if not data_received: break;

        # do something with the data

        # DEBUGGING: just some userful information about what's going on on the server side
        print("\n---------------------------------------------------------------")
        print("\tdata received at: ", sock.getsockname(), "[server socket address/this module]")
        print("\tdata received from:", client_address)
        print("\tdata received:", "\'" + data_received.decode('utf-8') + "\'")
        print("---------------------------------------------------------------")

    # close the connection
    # input("press enter to close the connection")
    client_socket.close()
    print("connection with", client_address, "closed")