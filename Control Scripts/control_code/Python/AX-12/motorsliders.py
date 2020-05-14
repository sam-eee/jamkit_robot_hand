from tkinter import *
import time
from dxl_control.Ax12 import Ax12 #From https://github.com/cckieu/dxl_control by Aary Kieu

#This code is designed to allow to user to move sliders to control the motors.
#It is recommended that either this method or direct function motor control is used
#as they cannot be used simultaneously by design.

    Ax12.open_port() #Connects to the Robotis U2D2 using the default port in Ax12.py
    Ax12.set_baudrate() #Uses the motor default 1000000 baud rate.
    
#Functions for changing servo angles, needed unique functions for the sliders
def F1(angle1):
    motor_object= Ax12(1)
    motor_object.set_position(angle1)
    
def F2(angle2):
    motor_object= Ax12(2)
    motor_object.set_position(angle2)  
    
def F3(angle3):
    motor_object= Ax12(3)
    motor_object.set_position(angle3)
    
def F4(angle4):
    motor_object= Ax12(4)
    motor_object.set_position(angle4)
    
def F5(angle5):
    motor_object= Ax12(5)
    motor_object.set_position(angle5) 
    
def F6(angle6):
    motor_object= Ax12(6)
    motor_object.set_position(angle6)  

def F7(angle7):
    motor_object= Ax12(7)
    motor_object.set_position(angle7)
    
def F8(angle8):
    motor_object= Ax12(8)
    motor_object.set_position(angle8)

def F9(angle9):
    motor_object= Ax12(9)
    motor_object.set_position(angle9)
    
def F10(angle10):
    motor_object= Ax12(10)
    motor_object.set_position(angle10)
    
def F11(angle11):
    motor_object= Ax12(11)
    motor_object.set_position(angle11)
    
def F12(angle12):
    motor_object= Ax12(12)
    motor_object.set_position(angle12)
    
#GUI creation with sliders that control servos between 0-300 in steps 0-1023.
#Updates the sliders on initialisation to get current motor positions.
root =Tk()
time.sleep(1) #Pause for loading of GUI

w1=Scale(root,orient='vertical', command=F1, from_ =0, to=1023)
w1.set(ax.get_ax(1))
w2=Scale(root,orient='vertical', command=F2, from_ =0, to=1023)
w2.set(ax.get_ax(2))
w3=Scale(root,orient='vertical', command=F3, from_ =0, to=1023)
w3.set(ax.get_ax(3))
w4=Scale(root,orient='vertical', command=F4, from_ =0, to=1023)
w4.set(ax.get_ax(4))
w5=Scale(root,orient='vertical', command=F5, from_ =0, to=1023)
w5.set(ax.get_ax(5))
w6=Scale(root,orient='vertical', command=F6, from_ =0, to=1023)
w6.set(ax.get_ax(6))
w7=Scale(root,orient='vertical', command=F7, from_ =0, to=1023)
w7.set(ax.get_ax(7))
w8=Scale(root,orient='vertical', command=F8, from_ =0, to=1023)
w8.set(ax.get_ax(8))
w9=Scale(root,orient='vertical', command=F9, from_ =0, to=1023)
w9.set(ax.get_ax(9))
w10=Scale(root,orient='vertical', command=F10, from_ =0, to=1023)
w10.set(ax.get_ax(10))
w11=Scale(root,orient='vertical', command=F11, from_ =0, to=1023)
w11.set(ax.get_ax(11))
w12=Scale(root,orient='vertical', command=F12, from_ =0, to=1023)
w12.set(ax.get_ax(12))


Label(root, text="F1").grid(column=0,row=1)
Label(root, text="F2").grid(column=1,row=1)
Label(root, text="F3").grid(column=2,row=1)
Label(root, text="F4").grid(column=3,row=1)
Label(root, text="F5").grid(column=4,row=1)
Label(root, text="F6").grid(column=5,row=1)
Label(root, text="F7").grid(column=6,row=1)
Label(root, text="F8").grid(column=7,row=1)
Label(root, text="F9").grid(column=8,row=1)
Label(root, text="F10").grid(column=9,row=1)
Label(root, text="F11").grid(column=10,row=1)
Label(root, text="F12").grid(column=11,row=1)

w1.grid(column=0,row=0)
w2.grid(column=1,row=0)
w3.grid(column=2,row=0)
w4.grid(column=3,row=0)
w5.grid(column=4,row=0)
w6.grid(column=5,row=0)
w7.grid(column=6,row=0)
w8.grid(column=7,row=0)
w9.grid(column=8,row=0)
w10.grid(column=9,row=0)
w11.grid(column=10,row=0)
w12.grid(column=11,row=0)


root.mainloop()