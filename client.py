import socket
import os

def menu():
    while True:
        print('1 - Messenger')
        print('2 - Calculator')
        print('0 - Quit')
        op1 = int(input('Choose an option:'))

        if op1 == 1:
            while True:
                # Aqui, aparece um input para o client introduzir uma mensagem quando escolhe a opção 1 do menu inicial que lhe aparece quando se autentica ao server.
                # Caso escrever uma mensagem, esta é codificada usando o algoritmo "utf-8" e é enviada para o server, onde será transmitida no cmd
                # Caso escreva "/return", dá break e envia o cliente de volta para o menu inicial.
                message = input("Enter your message (type '/return' to go back to menu): ")
                if message == "/return":
                    break
                client_socket.send(message.encode("utf-8"))

        elif op1 == 2:
            operation = input('Introduce your mathematic operation:')
            
            # Tenta realizar a operação matematica, caso sejam introduzidos letras ou a sintaxe esteja errada, é mostrado uma exception na linha de comandos do cliente
            # De seguida, passamos a variável "res" para string, de modo a evitarmos erros na codificação e envio da "mensagem"
            try:
                res = eval(operation)
                res_str = str(res)
                client_socket.send(f"calc_result: {res_str}".encode("utf-8"))
                print(f'The final result of the calculation is: {res_str}')
            except Exception as e:
                print(f"An Error has appeared: {e}")

        elif op1 == 0:

            # Quando o cliente escolhe a ultima opção, é perguntado se deseja mesmo sair do programa e caso escolha "y", o socket da close à ligação entre o cliente e o servidor e a consola é limpa, usando a biblioteca os.
            response = input('Are you sure you want to leave the application? (y/n):')
            if response == 'y':
                print('Leaving the program ...')
                client_socket.close()
                os.system('cls')
                break

        else:
            print('Choose a valid option:')

# Configurações do cliente
host = socket.gethostname()
port = 12345
ip = socket.gethostbyname(host)

# Limitar o números de bits (usado na calculadora)
HEADER_LENGTH = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ip, port))

# Introdução do nome do cliente
name = input('Introduce your name:')
client_socket.send(name.encode("utf-8"))

menu()