#!/usr/bin/python3

#To-Do
#1. color picker in static mode
#2. music mode(change arduino code)

from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import serial
import time
import threading

baudrate = 57600
port     = '/dev/ttyUSB0'

ser = serial.Serial(port, baudrate)

if ser.is_open == False:
   ser.open()
   ser.close()
   ser.open()
elif ser.is_open == True:
   ser.close()
   ser.open()
   
def statclr(r, g, b):
    ser.write(b'0')
    time.sleep(1)
    ser.write(b'rgb')
    print('Static mode') #debug info
    cmd = '%s,%s,%s/' % (r,g,b)
    time.sleep(2)
    ser.write(cmd.encode('utf-8'))  #serial.write() doesn't support unicode strings 
    print('Color has been changed') #Debug info

def tRainbow(ttime):
    print('New thread started with target tRainbow') #Debug info
    time.sleep(3)
    ser.write(b'rainbow')
    time.sleep(ttime+8)
    ser.write(b'0')
    print('Interrupt')
    
def rainbow(etime):
    int_time = int(etime)
    if int_time == 0:
        print("Unlimited") #debug info
        time.sleep(2)
        ser.write(b'rainbow')
    else:
        rthread = threading.Thread(target=tRainbow, args=(int_time, ))
        rthread.start()
    
def r_interrupt():
    print('Intererrupt')
    ser.write(b'0')
    
root = Tk()
root.title("Python LED Controller")
root.geometry("633x487")
root.resizable(0, 0)
root.configure(bg="#181b28")
Font(family='Nano Sans')
Label(root, text='\t \t \t', bg="#181b28", fg="#d3dae3") .grid(row=0, column=0)
Label(root, text='Python LED Controller', font=('none', 22), bg="#181b28", fg="#d3dae3") .grid(row=2, column=2)
Label(root, text='Available modes:', font=('none', 18), bg="#181b28", fg="#d3dae3") .grid(row=3, column=2)

modes = ttk.Combobox(root, state='readonly', font=('none', 12),
                     values=[
                             "Rainbow",
                             "Static color",
                             "Choose mode from list:"])
modes.grid(row=4, column=2, sticky=S+N)
modes.current(2)

print(modes.current(), modes.get())


def menu(event):
    if modes.get() == 'Static color':
        Label(root, text='\nSet static color', font=('none', 14), bg="#181b28", fg="#d3dae3") .grid(row=10, column=1)
        Label(root, text='R: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=11, column=1, sticky=S)
        entryr = Entry(root, width=4, bg='white', fg='black', borderwidth=0) 
        entryr.grid(row=11, column=1, sticky=E)
        Label(root, text='G: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=12, column=1, sticky=S)
        entryg = Entry(root, width=4, bg='white', fg='black', borderwidth=0) 
        entryg.grid(row=12, column=1, sticky=E)
        Label(root, text='B: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=13, column=1, sticky=S)
        entryb = Entry(root, width=4, bg='white', fg='black', borderwidth=0) 
        entryb.grid(row=13, column=1, sticky=E)
        Label(root, text='\n', font=('none', 3), bg="#181b28"). grid(row=14)
        Button(root, text='Set', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1, command=lambda: statclr(entryr.get(), entryg.get(), entryb.get())) .grid(row=15, column=1, sticky=S)
    elif modes.get() == 'Rainbow':
        Label(root, text='\nRainbow', font=('none', 14), fg="#d3dae3", bg="#181b28") .grid(row=18, column=1, sticky=W)
        Label(root, text='Unlimited: time = 0', font=('none', 10), bg="#181b28", fg="#d3dae3") .grid(row=19, column=1, sticky=W) 
        Label(root, text='Time(s): ', font=('none', 12), fg="#d3dae3", bg="#181b28") .grid(row=20, column=1, sticky=S)
        entrytime = Entry(root, width=4, bg='white', fg='black', borderwidth=0)
        entrytime.grid(row=20, column=1, sticky=E)
        Label(root, text='\n', font=('none', 3), bg="#181b28", fg="#d3dae3"). grid(row=21)
        Button(root, text='Set', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1, command=lambda: rainbow(entrytime.get())) .grid(row=22, column=1, sticky=S)
        Button(root, text='Stop', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1,  command=lambda: r_interrupt()) .grid(row=22, column=2, sticky=W)

modes.bind('<<ComboboxSelected>>', menu)

root.mainloop()
