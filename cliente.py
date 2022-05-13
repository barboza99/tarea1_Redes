import socket

def codificarMensaje(mensaje):
    print("Mensaje a encriptar: %s" % mensaje)
    d = [3, 5, 2]
    b = []
    j = 0
    for char in mensaje:
        character = ord(char)
        if character >= 65 and character <= 90:
            character = character - d[j]
            if character < 65:
                character = character - 64 + 90
        elif character == 32:
            character = 126
        b.append(character)
        if j < 2:
            j += 1
        else:
            j = 0
    mensajeEncriptado = ""
    for c in b:
        mensajeEncriptado += chr(c)
    print("Mensaje encriptado: %s" % mensajeEncriptado)
    return mensajeEncriptado



def iniciarCliente(host, puerto, msg_env):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, puerto))
    msg_rec = c.recv(1024)
    print(msg_rec.decode('UTF-8'))
    c.send(msg_env.encode('ascii'))
    c.close()

if __name__ == "__main__":
    host = '192.168.0.2'
    puerto = 8000
    msg = ""
    while True:
        print("Digite el mensaje a enviar: ", end="")
        msg = input()
        iniciarCliente(host, puerto, codificarMensaje(msg))
        print()