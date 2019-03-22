The socket Module
To create a socket, you must use the socket.socket() function available in socket module, which has the general syntax −

s = socket.socket (socket_family, socket_type, protocol=0)
Here is the description of the parameters −

socket_family − This is either AF_UNIX or AF_INET, as explained earlier.

socket_type − This is either SOCK_STREAM or SOCK_DGRAM.

protocol − This is usually left out, defaulting to 0.

Once you have socket object, then you can use required functions to create your client or server program. Following is the list of functions required −
#############################################
Server Socket Methods
Method & Description

s.bind() #This method binds address (hostname, port number pair) to socket.

s.listen() #This method sets up and start TCP listener.

s.accept() #This passively accept TCP client connection, waiting until connection arrives (blocking).
###############################################
Client Socket Methods
Sr.No.	Method & Description

s.connect() #This method actively initiates TCP server connection.
###############################################
General Socket Methods
Sr.No.	Method & Description

s.recv() #This method receives TCP message

s.send() #This method transmits TCP message

s.recvfrom() #This method receives UDP message

s.sendto() #This method transmits UDP message

s.close() #This method closes socket

socket.gethostname() #Returns the hostname.
##############################################
