#!/usr/bin/python3

from tkinter import *
import serial
import time

ser = serial.Serial()
ser.baudrate = 57600
ser.port = '/dev/ttyUSB0'
ser.timeout = 2
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
    cmd = '%s,%s,%s/' % (r,g,b)
    time.sleep(2)
    ser.write(cmd.encode('utf-8'))  #serial.write() doesn't support unicode strings 

def rainbow(etime):
    int_time = int(etime)
    ser.write(b'rainbow')
    if time != 0:
        time.sleep(int_time)
        ser.write(b'0')
        
    
window = Tk()
window.title("Python LED Controller")
window.geometry("633x487")
Label(window, text='\t') .grid(row=0, column=0)
Label(window, text='Python LED Controller', font=('none', 22)) .grid(row=3, column=2)
Label(window, text='Available modes:', font=('none', 18)) .grid(row=4, column=2)
Label(window, text='\nSet static color', font=('none', 14)) .grid(row=10, column=1)

Label(window, text='R: ', font=('none', 12)) .grid(row=11, column=1, sticky=S)
entryr = Entry(window, width=4, bg='white', fg='black') 
entryr.grid(row=11, column=1, sticky=E)
Label(window, text='G: ', font=('none', 12)) .grid(row=12, column=1, sticky=S)
entryg = Entry(window, width=4, bg='white', fg='black') 
entryg.grid(row=12, column=1, sticky=E)
Label(window, text='B: ', font=('none', 12)) .grid(row=13, column=1, sticky=S)
entryb = Entry(window, width=4, bg='white', fg='black') 
entryb.grid(row=13, column=1, sticky=E)
Label(window, text='\n', font=('none', 3)). grid(row=14)
Button(window, text='Set', fg='white', width=4, font=('none', 13), borderwidth=1, command=lambda: statclr(entryr.get(), entryg.get(), entryb.get())) .grid(row=15, column=1, sticky=S)

Label(window, text='\nRainbow', font=('none', 14)) .grid(row=18, column=1, sticky=W)
Label(window, text='Unlimited: time = 0', font=('none', 10)) .grid(row=19, column=1, sticky=W) 
Label(window, text='Time(s): ', font=('none', 12)) .grid(row=20, column=1, sticky=S)
entrytime = Entry(window, width=4, bg='white', fg='black')
entrytime.grid(row=20, column=1, sticky=E)
Label(window, text='\n', font=('none', 3)). grid(row=21)
Button(window, text='Set', fg='white', width=4, font=('none', 13), borderwidth=1, command=lambda: rainbow(entrytime.get())) .grid(row=22, column=1, sticky=S)

window.mainloop()
