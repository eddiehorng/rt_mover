#!/usr/bin/python
import socket, struct                             

def ip2int(addr):                                                               
    return struct.unpack("!I", socket.inet_aton(addr))[0]                       


def int2ip(addr):                                                               
    return socket.inet_ntoa(struct.pack("!I", addr)) 

# create a socket object
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    print 'Listen on port %s' % port
    
    # establish a connection
    clientsocket,addr = serversocket.accept()     
   
    print addr
    #print("Got a connection from %s (%d)" % (str(addr), ip2int(str(addr))))
    while True:
        buf=clientsocket.recv(1024)
        if not buf:
            break
        print "read from client: %s" % buf
    clientsocket.close()