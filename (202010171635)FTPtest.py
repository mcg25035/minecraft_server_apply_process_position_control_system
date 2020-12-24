import socket
import threading
import time
def i():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,recv_port))
    f = open('food.mcfunction','w+')
    info = 'a'
    info_all = ''
    while not info == '':
        info = client.recv(1024).decode("utf-8",errors='ignore')
        info_all = info_all+info
    f.write(info_all)
    f.close()
    

    
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "qaz02546sd.servegame.com"
port = 10022
client.connect((host,port))
client.recv(1024)
client.send('USER cityo************ver'.encode("utf-8",errors='strict'))
client.recv(1024)
client.send('PASS COU******'.encode("utf-8",errors='strict'))
client.recv(1024)
client.send('PASV'.encode("utf-8",errors='strict'))
temp_str = client.recv(1024).decode("utf-8")
recv_port = (int(temp_str.split('(')[1].split(')')[0].split(',')[4])*256)+(int(temp_str.split('(')[1].split(')')[0].split(',')[5]))
t = threading.Thread(target = i)
t.start()
client.send('CWD /world/datapacks/sys/data/pgdc/functions/'.encode("utf-8",errors='strict'))
client.recv(1024)
client.send('RETR food.mcfunction'.encode("utf-8",errors='strict'))

