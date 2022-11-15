import serial, time
import socket
import struct

#Comando para abrir puerto
arduino = serial.Serial('COM5', 9600)
time.sleep(2)
#arduino.write(b'1')

#ESTE ES EL VALOR QUE TENGO QUE ENVIAR POR EL SOCKET
valor = arduino.readline()
variable = str(valor)
message = variable[2:5]
print(message)
arduino.close()


# Codifica el mensaje a bytes
bytes_mesaage = str.encode(message)

#multicast_addr = '224.0.0.1'
#port = 10000
grupo_multicast = ('224.0.0.1', 10000)

# Crea el socket de tipo datagrama
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TTL (Time To Live), el valor por defecto es 1, significa que el paquete
# no sera redireccionado por el router mas allá del segmento de red actual.
# el valor puede ir de 1 a 255.
ttl = struct.pack('b', 1)
# El socket se configura con ese valor de tiempo de vida para los mesajes.
# El TTL controla cuantas redes (saltos) se realizarán para recibir el mensaje
# la llamda al sistema setsockopt() pasa información al kernel 
# Se configrua el TTL con la opción IP_MULTICAST_TTL, y se indica que se utilizará el protocolo IP
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

print("Enviando datos a los receptores: ", message)
# Llamada al sistema para enviar los datos por el socket
sock.sendto(bytes_mesaage, grupo_multicast)
sock.close()


