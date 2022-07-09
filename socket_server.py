import socket
import threading

def handle_client(c,addr):
    print(addr, "connected.")

    while True:
        data = c.recv(1024)
        if not data:
            break
        c.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 1234))
    s.listen()
    print("监听链接.....")
    while True:
        c, addr = s.accept()
        print("链接成功！")
        print("有一位shabi连接了")

        t = threading.Thread(target=handle_client, args=(c,addr))
        t.start()


