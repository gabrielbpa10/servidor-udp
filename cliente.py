import socket, os

PORT = 5000
ADDRESS = '127.0.0.1'
path = './arquivo-enviar'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect((ADDRESS,PORT))
    # sock.sendall(b"Hello World")
    # sock.sendto(b'Comunicacao UDP',(ADDRESS, PORT))

    files_path = os.listdir(path)
    for file in files_path:
        sock.sendall(file.encode())

    # file_size = os.path.getsize(files_path[0])
    # pacote_em_kilobytes = 512
    # pacote_em_bytes = pacote_em_kilobytes * 8

    # # 9 Enviando o numero de pacotes ao servidor
    # numero_de_pacotes = (file_size // pacote_em_bytes) + 1
    # sock.sendall(numero_de_pacotes.to_bytes(4, "little"))
    
    data = sock.recv(1024)
    print(f"Começar: {data.decode('utf8')}")