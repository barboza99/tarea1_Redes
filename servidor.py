import socket

def decodificarMensaje(mensaje):
    print("Mensaje a decodificar: %s" % mensaje)
    d = [3, 5, 2]
    b = []
    j = 0
    for char in mensaje:
        character = ord(char)
        if character >= 65 and character <= 90:
            character = character + d[j]
            if character > 90:
                character = character - 91 + 65
        elif character == 126:
            character = 32
        b.append(character)
        if j < 2:
            j += 1
        else:
            j = 0

    mensajeDecodificado = ""
    for c in b:
        mensajeDecodificado += chr(c)
    return mensajeDecodificado

def iniciarServidor(host, puerto):
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, puerto))
    new_socket.listen(5) #escuchará hasta 5 peticiones
 
    while True:
        #se establece la conexión
        (c, addr) = new_socket.accept()

        print("Se estableció la conexión con: %s" %str(addr))
        msg = 'Conexión establecida con : %s' %socket.gethostname() + "/n/n"
        c.send(msg.encode('UTF-8'))
        msg_rec = c.recv(1024)
        print("Mensaje decodificado: %s" % decodificarMensaje(msg_rec.decode('ascii')) + "\n")
        c.close()

if __name__ == "__main__":
    host = ""
    puerto = 8000
    iniciarServidor(host, puerto)