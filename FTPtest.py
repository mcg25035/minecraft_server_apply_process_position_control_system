from ftplib import FTP
import os
import sys
import configparser
import socket

def downloadfile(downftp, remotepath,localpath):
    bufsize=1024
    fp = open(localpath,'wb')     
    downftp.set_debuglevel(2)
    downftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    fp.close()   
	
def ftpconnect(host,username,password):
    ftp = FTP()
    #ftp.af = socket.AF_INET6
    ftp.set_pasv(False)
    ftp.connect(host=host,port=10022)
    ftp.login(username, password)
    return ftp

def uploadfile(ftp,remotepath, localpath):
    bufsize=1024
    fp=open(localpath,'rb')       
    ftp.set_debuglevel(0)
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    fp.close()
conftp = ftpconnect('42.0.75.201','cityofuniverse.116server','COU006123')
downloadfile(conftp,'/world/datapacks/sys/data/pgdc/functions/food.mcfunction','food.mcfunction')
