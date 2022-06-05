import socket, os

PORT = 5000
ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as comunicacao:
    comunicacao.bind((ADDRESS,PORT))

    while True:
        print('Aguardando conexão cliente...')
        filename, addr = comunicacao.recvfrom(1024)
        filesize, addr = comunicacao.recvfrom(1024)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        
        with open(filename, 'wb',filesize) as f:
            while True:
                bytes_read = comunicacao.recv(BUFFER_SIZE)
                if not bytes_read:    
                    break
                print(bytes_read)
                f.write(bytes_read)
                break
        break