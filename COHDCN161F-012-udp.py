import ctypes import *
import struct
import sys
import os
import socket

class UDP(Structure):
    _fields_=[
        
        ("sport",c_ubyte,4),
        ("dport",c_ubyte,4),
        ("udp_len",c_ubyte),
        ("checksum",c_ushort),
        ("data",c_long),
        
        ]
    def __new__(self, socket_buffer = None):
        return self.form_buffer_copy(socket_buffer)
    def __int__(self,socket_buffer = None):
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))

rfile = open("udp.bin","rb").read()
udp =UDP(rfile[0:20])
print(udp.src_address)
