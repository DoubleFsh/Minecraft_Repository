import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("127.0.0.1", 23333)
print ("[+] 正在连接......")

try:
    s.connect(addr)
    print ("[+] 连接成功")
    recv_mes = s.recv(1024)
    print (recv_mes)
    while True:
        message = str(input("[!] input something: "))
        s.sendall(bytes(message))
        print ("[+] 发送成功！")
        exit(0)
        
    
except Exception as s:
    print (f"[-] Error: {str(s)}")

    
