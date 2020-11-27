from dearpygui.core import *
from dearpygui.simple import *
import socket
import cv2
import threading

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
choice = -1

def socketer

def selector(num):
    global choice
    choice = num
    if (num == 1):
        s1.send(b'\x31') # Paper
    elif (num < 1):
        s1.send(b'\x30') # Rock
    else:
        s1.send(b'\x32') # Scissors

with window("_main"):
    pass
