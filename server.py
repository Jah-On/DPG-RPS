import socket
import netifaces as ni
import threading

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientData = [b'', b'']


interfaces = ni.interfaces()
for i in range(0, (len(interfaces))):
    try:
        ip = ni.ifaddresses(interfaces[i])[ni.AF_INET][0]['addr']
    except:
        pass

s1.bind((ip, 4321))
s1.listen(2)

c1, addr1 = s1.accept()
c2, addr2 = s1.accept()

def clientGetter1():
    global clientData
    data = c1.recv(2)
    while (len(data) == 0):
        data = c1.recv(2)
        clientData[0] = data

def clientGetter2():
    global clientData
    data = c2.recv(2)
    while (len(data) == 0):
        data = c1.recv(2)
        clientData[1] = data

def serverMains():
    while ((clientData[0] not in [b'\x30', b'\x31', b'\x32']) or (clientData[1] not in [b'\x30', b'\x31', b'\x32'])):
        pass
    a, b = int(clientData[0], clientData[1])
    if (a == b):
        c1.send(b'\x30\x2d\x30') # 0 - 0
        c2.send(b'\x30\x2d\x30') # 0 - 0
    elif ((a + b) == 1):
        if (a > b): # A won
            c1.send(b'\x31\x2d\x30') # 1 - 0
            c2.send(b'\x30\x2d\x31') # 0 - 1
        else: # B won
            c1.send(b'\x30\x2d\x31') # 0 - 1
            c2.send(b'\x31\x2d\x30') # 1 - 0
    elif ((a + b) == 2):
        if (a < b): # A won
            c1.send(b'\x31\x2d\x30') # 1 - 0
            c2.send(b'\x30\x2d\x31') # 0 - 1
        else: # B won
            c1.send(b'\x30\x2d\x31') # 0 - 1
            c2.send(b'\x31\x2d\x30') # 1 - 0
    else:
        if (a > b): # A won
            c1.send(b'\x31\x2d\x30') # 1 - 0
            c2.send(b'\x30\x2d\x31') # 0 - 1
        else: # B won
            c1.send(b'\x30\x2d\x31') # 0 - 1
            c2.send(b'\x31\x2d\x30') # 1 - 0
