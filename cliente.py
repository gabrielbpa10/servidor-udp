import socket, os

PORT = 5000
ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096
filename = "./arquivo-enviar/foguete.png"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect((ADDRESS,PORT))

    filesize = os.path.getsize(filename)
    sock.send(filename.encode())
    sock.send(f"{filesize}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            sock.sendall(bytes_read)