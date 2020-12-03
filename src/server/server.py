# import socket
# import netifaces as ni

# s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# interfaces = ni.interfaces()
# for i in range(0, (len(interfaces))):
#     try:
#         ip = ni.ifaddresses(interfaces[i])[ni.AF_INET][0]['addr']
#     except:
#         pass

# s1.bind((ip, 4321))
