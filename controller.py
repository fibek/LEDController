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
    ser.write(b'rgb')
    cmd = '%s,%s,%s/' % (r,g,b)
    time.sleep(2)
    ser.write(cmd.encode('utf-8'))
    
window = Tk()
window.title("Python LED Controller")
window.geometry("600x700")
Label(window, text='Available modes:', font=('none', 16)) .grid(row=4, column=8)
Label(window, text='Set static color', font=('none', 14)) .grid(row=10, column=1)

Label(window, text='R: ', font=('none', 13)) .grid(row=11, column=0, sticky=E)
entryr = Entry(window, width=4, bg='white', fg='black') 
entryr.grid(row=11, column=1, sticky=W)
Label(window, text='G: ', font=('none', 13)) .grid(row=12, column=0, sticky=E)
entryg = Entry(window, width=4, bg='white', fg='black') 
entryg.grid(row=12, column=1, sticky=W)
Label(window, text='B: ', font=('none', 13)) .grid(row=13, column=0, sticky=E)
entryb = Entry(window, width=4, bg='white', fg='black') 
entryb.grid(row=13, column=1, sticky=W)
Button(window, text='Set', fg='white',width=4, font=('none', 14), borderwidth=0, command=lambda: statclr(entryr.get(), entryg.get(), entryb.get())) .grid(row=14, column=1, sticky=W)

window.mainloop()

#print(ser)
#time.sleep(2)
#ser.write(b'rainbow')
#print('rainbow')
#time.sleep(15)
#ser.write(b'0')
#print('0')
#time.sleep(3)
#ser.write(b'rgb')
#print('rgb')
#time.sleep(2)
#ser.write(b'180,40,30/')
#print('180,40,30/')
#ser.close()
