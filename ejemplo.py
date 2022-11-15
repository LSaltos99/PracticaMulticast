import socket
import struct
import serial, time

arduino = serial.Serial('COM6', 9600)

multicast_addr = '224.0.0.1'
bind_addr = '0.0.0.0'
port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((bind_addr, port))

while True:
    message, address = sock.recvfrom(255)
    mensaje = message.decode('utf-8')
    print("Recibiendo datos del emisor: ", mensaje)
    arduino.write(message)
    time.sleep(1)