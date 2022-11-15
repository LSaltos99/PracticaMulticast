# PROGRAMA RECEPTOR EN UNA COMUNICACIÓN MULTICAST
import serial, time
import socket
import struct

multicast_addr = '224.0.0.1'
bind_addr = '0.0.0.0'
port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((bind_addr, port))
arduino = serial.Serial('COM6', 9600)

while True:
    message, address = sock.recvfrom(255)
    recibido = message.decode('utf-8')
    #print (recibido)
    
    #valor = recibido[2:3]
    #print(valor)
    print (recibido)
    
    #time.sleep(2)

    if recibido == 'd' :
        arduino.write(message)
        #print("encendido")
        #arduino.close()
        time.sleep(1)

    else : 
        arduino.write(message)
        #print ("apagado")
        #arduino.close()
        time.sleep(1)
    
    