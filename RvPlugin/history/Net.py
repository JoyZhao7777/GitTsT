#coding:utf8
import os
import re
import json
import socket
import threading


try:
    from PySide2.QtWidgets import *
    from PySide2.QtCore    import *
except:
    from PySide.QtGui  import *
    from PySide.QtCore import *
    
    
    
class Server( QThread ):
    signal = Signal( str )
    m_size = 1024*10
    m_buff = ""
    def __init__( self, Ip="127.0.0.1", Port=14250 ):
        QThread.__init__( self )
        self.Ip   = Ip
        self.Port = Port
        self.start()
    def run( self ):
        self.m_server_socket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.m_server_socket.bind( (self.Ip, self.Port) )
        while True:
            data, addr = self.m_server_socket.recvfrom( self.m_size )
            self.signal.emit( data )
class Client():
    def __init__( self, Ip="127.0.0.1", Port=14250 ):
        self.Ip   = Ip
        self.Port = Port
    def sendMessage( self, data ):
        self.m_client_socket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   
        self.m_client_socket.sendto( data, (self.Ip, self.Port))    
        self.m_client_socket.close()

def GetPort( Port=14250 ):
    t_res = os.system( """netstat -ano|findstr \"%d\""""%(Port) )
    if t_res == 0:
        return GetPort( Port + 1 )
    else:
        return Port

if __name__ == "__main__":
    pass
    #m = "C:/assssssss/bbb.mov"
    #Client().sendMessage( "rv.commands.addSources(['C:/Users/zhangtianshun/Desktop/zts_test/aaaa/bb.0003.mov'])\nrv.command.play()" )
    #print GetPort()