import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("127.0.0.1", 5555)
s.bind(addr)
s.listen(5)
print ("[+] 正在监听连接.....")

while True:
    c_s, c_addr = s.accept()
    print (f"[+] 来自{c_s}的用户连接成功！")
    
    c_s.sendall("[+] 欢迎连接socket test server_1!")
    
    tmp_data = c_s.recv(1024)
    try:
        with open('testdata', 'rb') as f:
            data_recv = pickle.load(f)
    except:
        print ("[-] Error:This file or directory was not found!Check your address.")
        
    while True:
        if tmp_data:
            tmp_data = c_s.recv(1024)
            with open('testdata','wb') as f:
                pickle.dump(data_recv,f)
        break
        
        
    print ("[+] Your data_file is here:")
    print ("\n")
    print (data_recv)
    
    
