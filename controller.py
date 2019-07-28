#!/usr/bin/python3

#To-Do
#1. color picker in static mode
#2. music mode(change arduino code)
#3. /dev/tty... listbox(?)
from tkinter import *
from tkinter.font import Font
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
    
window = Tk()
window.title("Python LED Controller")
window.geometry("633x487")
window.resizable(0, 0)
window.configure(bg="#181b28")
Font(family='Nano Sans')
Label(window, text='\t', bg="#181b28", fg="#d3dae3") .grid(row=0, column=0)
Label(window, text='Python LED Controller', font=('none', 22), bg="#181b28", fg="#d3dae3") .grid(row=2, column=2)
Label(window, text='Available modes:', font=('none', 18), bg="#181b28", fg="#d3dae3") .grid(row=3, column=2)
Label(window, text='\nSet static color', font=('none', 14), bg="#181b28", fg="#d3dae3") .grid(row=10, column=1)

Label(window, text='R: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=11, column=1, sticky=S)
entryr = Entry(window, width=4, bg='white', fg='black', borderwidth=0) 
entryr.grid(row=11, column=1, sticky=E)
Label(window, text='G: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=12, column=1, sticky=S)
entryg = Entry(window, width=4, bg='white', fg='black', borderwidth=0) 
entryg.grid(row=12, column=1, sticky=E)
Label(window, text='B: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=13, column=1, sticky=S)
entryb = Entry(window, width=4, bg='white', fg='black', borderwidth=0) 
entryb.grid(row=13, column=1, sticky=E)
Label(window, text='\n', font=('none', 3), bg="#181b28"). grid(row=14)
Button(window, text='Set', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1, command=lambda: statclr(entryr.get(), entryg.get(), entryb.get())) .grid(row=15, column=1, sticky=S)

Label(window, text='\nRainbow', font=('none', 14), fg="#d3dae3", bg="#181b28") .grid(row=18, column=1, sticky=W)
Label(window, text='Unlimited: time = 0', font=('none', 10), bg="#181b28", fg="#d3dae3") .grid(row=19, column=1, sticky=W) 
Label(window, text='Time(s): ', font=('none', 12), fg="#d3dae3", bg="#181b28") .grid(row=20, column=1, sticky=S)
entrytime = Entry(window, width=4, bg='white', fg='black', borderwidth=0)
entrytime.grid(row=20, column=1, sticky=E)
Label(window, text='\n', font=('none', 3), bg="#181b28", fg="#d3dae3"). grid(row=21)
Button(window, text='Set', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1, command=lambda: rainbow(entrytime.get())) .grid(row=22, column=1, sticky=S)
Button(window, text='Stop', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1,  command=lambda: r_interrupt()) .grid(row=22, column=2, sticky=W)

window.mainloop()
