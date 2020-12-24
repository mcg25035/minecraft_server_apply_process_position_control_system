import socket
import threading
import time

host = "qaz02546sd.servegame.com"
port = 10022
recv_port = 0

def FTP(ID,password):
    global recv_port
    def subthread_RETR(ID,password):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host,recv_port))
        print(recv_port)
        f = open('food.mcfunction','w+')
        info = 'a'
        info_all = ''
        while not info == '':
            info = client.recv(1024).decode("utf-8",errors='ignore')
            info_all = info_all+info
        f.write(info_all)
        f.close()
        f = open('food.mcfunction','r+')
        ace = f.read().split('\n')
        f.close()
        f = open('food.mcfunction','w+')
        ace.insert(140,'execute as @a[tag=!login,name='+ID+',scores={login='+password+'}] at @s run tp @s 5949 63 6025\nexecute as @a[tag=!login,name='+ID+',scores={login='+password+'}] at @s run gamemode creative @s\nexecute as @a[tag=!login,name='+ID+',scores={login='+password+'}] at @s run tellraw @s "\u00a7c成功解除門禁!"\nexecute as @a[tag=!login,name='+ID+',scores={login='+password+'}] at @s run tag @s add login')
        acd = ''
        for i in ace:
            if acd == '':
                acd = acd + i
            else:
                acd = acd + '\n' + i
        f.write(acd)
        f.close()
    def subthread_STOR():
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host,recv_port))
        f = open('food.mcfunction','r+')
        a = f.read()
        f.close()
        client.send(a.encode("utf-8",errors='strict'))
        client.close()
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    client.recv(1024)
    client.send('USER cityo***************TW_#068'.encode("utf-8",errors='strict'))
    client.recv(1024)
    client.send('PASS COU******'.encode("utf-8",errors='strict'))
    client.recv(1024)
    client.send('PASV'.encode("utf-8",errors='strict'))
    temp_str = client.recv(1024).decode("utf-8")
    recv_port = (int(temp_str.split('(')[1].split(')')[0].split(',')[4])*256)+(int(temp_str.split('(')[1].split(')')[0].split(',')[5]))
    t = threading.Thread(target = subthread_RETR,args = (ID,password))
    t.start()
    time.sleep(0.1)
    client.send('CWD /world/datapacks/sys/data/pgdc/functions/'.encode("utf-8",errors='strict'))
    client.recv(1024)
    client.send('RETR food.mcfunction'.encode("utf-8",errors='strict'))
    client.recv(1024)
    time.sleep(3)
    client.send('PASV'.encode("utf-8",errors='strict'))
    client.recv(1024)
    client.send('DELE food.mcfunction'.encode("utf-8",errors='strict'))
    client.recv(1024)
    recv_port = (int(temp_str.split('(')[1].split(')')[0].split(',')[4])*256)+(int(temp_str.split('(')[1].split(')')[0].split(',')[5]))
    client.send('STOR food.mcfunction'.encode("utf-8",errors='strict'))
    client.recv(1024)
    t = threading.Thread(target = subthread_STOR)
    t.start()
    time.sleep(0.2)
    client.recv(1024)
    
