import ctypes import *
import struct
import sys
import os
import socket

class TCP(Structure):
    _fields_=[
        ("dport",c_ubyte,4),
        ("sport",c_ubyte,4),
        ("tcp_seq",c_ubyte),
        ("tcp_ack_seq",c_ushort),
        ("offset",c_ushort),
        ("reserved", c_ubyte),
        ("tcp_flags",c_ubyte),
        ("tcp_wdw",c_ubyte),
        ("checksum",c_ushort),
        ("tcp_urg_ptr",c_long),
        
        ]
    def __new__(self, socket_buffer = None):
        return self.form_buffer_copy(socket_buffer)
    def __int__(self,socket_buffer = None):
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))

rfile = open("ip.bin","rb").read()
tcp =TCP(rfile[0:20])
print(tcp.src_address)
