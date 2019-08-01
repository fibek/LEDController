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

def menu(event):
    if modes.get() == 'Static color':
        try:
            frame2.grid_forget()
        except:
            print('ni wim co to kurwa ten jebany frame2')
        #frame1 = Frame(root)
        print(modes.current(), modes.get())
        Label(frame1, text='\nSet static color', font=('none', 14), bg="#181b28", fg="#d3dae3") .grid(row=10, column=1)
        Label(frame1, text='R: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=11, column=1, sticky=S)
        entryr = Entry(frame1, width=4, bg='white', fg='black', borderwidth=0) 
        entryr.grid(row=11, column=1, sticky=E)
        Label(frame1, text='G: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=12, column=1, sticky=S)
        entryg = Entry(frame1, width=4, bg='white', fg='black', borderwidth=0) 
        entryg.grid(row=12, column=1, sticky=E)
        Label(frame1, text='B: ', font=('none', 12), bg="#181b28", fg="#d3dae3") .grid(row=13, column=1, sticky=S)
        entryb = Entry(frame1, width=4, bg='white', fg='black', borderwidth=0) 
        entryb.grid(row=13, column=1, sticky=E)
        Label(frame1, text='\n', font=('none', 3), bg="#181b28"). grid(row=14)
        Button(frame1, text='Set', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1, command=lambda: statclr(entryr.get(), entryg.get(), entryb.get())) .grid(row=15, column=1, sticky=S)
        frame1.grid(row=5, column=0)
        #frame2 = Frame(root)
    elif modes.get() == 'Rainbow':
        try:
            frame1.grid_forget()
        except:
            print('ni wim co to kurwa ten jebany frame1')
        #frame2 = Frame(root)
        print(modes.current(), modes.get())
        Label(frame2, text='\nRainbow', font=('none', 14), fg="#d3dae3", bg="#181b28") .grid(row=18, column=1, sticky=W)
        Label(frame2, text='Unlimited: time = 0', font=('none', 10), bg="#181b28", fg="#d3dae3") .grid(row=19, column=1, sticky=W) 
        Label(frame2, text='Time (s): ', font=('none', 12), fg="#d3dae3", bg="#181b28") .grid(row=20, column=1, sticky=S)
        entrytime = Entry(frame2, width=4, bg='white', fg='black', borderwidth=0)
        entrytime.grid(row=20, column=1, sticky=E)
        Label(frame2, text='\n', font=('none', 3), bg="#181b28", fg="#d3dae3"). grid(row=21)
        Button(frame2, text='Set', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1, command=lambda: rainbow(entrytime.get())) .grid(row=22, column=1, sticky=S)
        Button(frame2, text='Stop', fg='white', width=4, font=('none', 13), bg="#181b28", borderwidth=1,  command=lambda: r_interrupt()) .grid(row=22, column=2, sticky=W)
        frame2.grid(row=5, column=0)
        #frame2 = Frame(root)

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

frame1 = Frame(root)
frame2 = Frame(root)

modes.bind('<<ComboboxSelected>>', menu)

root.mainloop()
