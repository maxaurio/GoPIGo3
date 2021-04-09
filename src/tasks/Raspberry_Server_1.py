#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:08:28 2021

@author: bernat
"""

#!/usr/bin/env python3
import easygopigo3 as easy
my_gpg3 = easy.EasyGoPiGo3()
import socket
#import time    # import the time library for the sleep function
#import gopigo3 # import the GoPiGo3 drivers

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#GPG = gopigo3.GoPiGo3() 

def forward():
    my_gpg3.forward()

def backward():
    my_gpg3.backward()

def left():
    my_gpg3.left()

def right():
    my_gpg3.right()

def stop():
    my_gpg3.stop()
    
def program1():
    pass


if __name__=="__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True: #Add timeout to this infinite loop
            conn, addr = s.accept() 
            with conn:
                print('Connected by', addr)
                while True:
                    rawdata = conn.recv(1024)
                    data = repr(rawdata)
                    datarefined = data[2:len(data)-1:]
                    if not rawdata:
                        break
                    print("Received",datarefined)
                    if datarefined == "w":
                        conn.sendall(bytes("forward", 'utf-8'))
                        forward()
                    elif datarefined == "s":
                        conn.sendall(bytes("backward", 'utf-8'))
                        backward()
                    elif datarefined == "a":
                        conn.sendall(bytes("left", 'utf-8'))
                        left()
                    elif datarefined == "d":
                        conn.sendall(bytes("right", 'utf-8'))
                        right()
                    elif datarefined == " ":
                        conn.sendall(bytes("stop", 'utf-8'))
                        stop()
                    elif datarefined == "1":
                        conn.sendall(bytes("program 1", 'utf-8'))
                        program1()
                    else:
                        conn.sendall(bytes("unknown", 'utf-8'))