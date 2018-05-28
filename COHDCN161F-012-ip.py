import ctypes import *
import struct
import sys
import os
import socket

class IP(Structure):
    _fields_=[
        ("version",c_ubyte,4),
        ("ihl",c_ubyte,4),
        ("tos",c_ubyte),
        ("length",c_ushort),
        ("ident",c_ushort),
        ("offset",c_ushort),
        ("ttl", c_ubyte),
        ("protocol",c_ubyte),
        ("checksum",c_ushort),
        ("src",c_long),
        ("dest",c_long)
        ]
    def __new__(self, socket_buffer = None):
        return self.form_buffer_copy(socket_buffer)
    def __int__(self,socket_buffer = None):
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))

rfile = open("ip.bin","rb").read()
ip =IP(rfile[0:20])
print(ip.src_address)
