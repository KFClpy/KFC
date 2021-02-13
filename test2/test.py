import socket
import numpy
HOST = '127.0.0.1'
PORT = 9999
BufferSize = 1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('172.26.102.167',10001))
while(1):
   ReceiveData=s.recv(BufferSize)
   print(ReceiveData.decode('gb2312'))
   if  ReceiveData.decode('gb2312') ==  'name' :
       InputData='于于的牛'
       s.sendall(InputData.encode('gb2312'))








