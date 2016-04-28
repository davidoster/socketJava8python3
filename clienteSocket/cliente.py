#!/usr/bin/env python
 
import socket
 
HOST = "192.168.0.22"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("SE ABRE CONECCION AL SOCKET")
sock.connect((HOST, PORT))

smshello = "Hello\n" 
print ("ENVIA Hello al SERVER")
sock.sendall(smshello.encode())
print ("RECIBE LA RESPUESTA DEL SERVER Y LA ALMACENA EN LA VARIABLE data")
data = sock.recv(1024)
print ("EL DATO RECIBIDO DESDE EL SERVER ES: ",data)
print ("EL DATO decodificado RECIBIDO DESDE EL SERVER ES: ",data.decode())
#print (repr(data.decode()) #no convierte a string un dato decodificado
dataDecodedByServer = data.decode()
print("guardo dato decodificado en una var. y luego la imprimo",dataDecodedByServer)
#if ( data == "olleH\n" ):
#if ((str(data.decode())) == "olleH" ):
#if ( data == "b'olleH\r\n'" ):
if (dataDecodedByServer == "olleH\r\n" ):
    print ("ENTRA AQUI SI EL DATO RECIBIDO ES olleH")
    smsbye = "Bye\n"
    sock.sendall(smsbye.encode())
    print ("ENVIA Bye AL SERVER")
    data = sock.recv(1024)
    print ("EL DATO RECIBIDO DESDE EL SERVER ES: ", data)
    dataDecodedByServer = data.decode()
    if (data == "eyB\r\n"):
        print ("ENTRA AQUI SI EL DATO RECIBIDO ES eyB")
        sock.close()
        print ("Socket closed")
