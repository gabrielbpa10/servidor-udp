import socket, time

PORT = 5000
ADDRESS = '127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as comunicacao:
    comunicacao.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    comunicacao.bind((ADDRESS,PORT))
    flag = True
    while flag:
        print('Aguardando conexão cliente...')
        data, addr = comunicacao.recvfrom(1024)
        print('Recebido de: ', addr)
        files = []
        file_name = data.decode()
        print(f"[{len(files)}] {file_name}")
        files.append(file_name)
        print(files[0])
        # file = open(files[0], "rb")
        
        # pacote_em_kilobytes = 512
        # pacote_em_bytes = pacote_em_kilobytes * 8
        # numero_de_pacotes = int.from_bytes(file, "little")

        # start = time.time()
        # for i in range(numero_de_pacotes):
        #     data = comunicacao.recv(pacote_em_bytes)
        #     file.write(data)
        #     porcentagem = f"Baixando... {round((100*(i+1))/numero_de_pacotes, 2)}%"
        #     # print(porcentagem)
        #     print('\r'+porcentagem, end='')

        # tempo_de_download = round(time.time()-start, 2)
        # print(f"\nO download foi completo em {tempo_de_download} sec")


        comunicacao.sendto(b'Hello, %s!' % data, addr)
        flag = False