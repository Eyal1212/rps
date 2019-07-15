import socket
import random
#created by eyalb.s


HOST = "localhost"
PORT = 4445
RPS = ["r" , "p" , "s"]

    
while True:
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.bind((HOST , PORT))
        sock.listen()
        conn , addr = sock.accept()
        print ("connection from " + str(addr))
        with conn:
            while True:
                data = conn.recv(1024)
                win = 0 #0- tie , 1- player , 2 - pc
                if not data:
                    break
                data = data.decode('utf-8')
                ai = random.randint(0,2) #0 - rock 1 - papper 2 - scissors
                print(RPS[ai])
                if data == RPS[ai]:
                    print("tie!")
                elif data == "r":
                    if ai == 1:
                        print("You Lost!")
                        win = 2
                    elif ai == 2:
                        print("You Won!")
                        win = 1
                elif data == "p":
                    if ai == 0:
                        print("You Won!")
                        win = 1
                    elif ai == 2:
                        print("You Lost!")
                        win = 2
                elif data == "s":
                    if ai == 0:
                        win = 2
                        print("You Lost!")
                    elif ai == 1:
                        win = 1
                        print("You Won!")
                if win == 1:
                    conn.sendall(bytes(str("p"), "utf-8"))
                elif win == 2:
                    conn.sendall(bytes(str("c"), "utf-8"))
                else:
                    conn.sendall(bytes(str("t"), "utf-8"))
                sock.close()
