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
    print('Color has been changed/set') #Debug info

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

def dblstatclr(r1, g1, b1, r2, g2, b2, rng1f, rng1t, rng2f, rng2t):
    ser.write(b'0')
    time.sleep(1)
    ser.write(b'dblrngrgb')
    print('Double static mode') #debug info
    cmd = '%s,%s,%s,%s:%s/%s,%s,%s,%s:%s/' % (r1, g1, b1, rng1f, rng1t, r2, g2, b2, rng2f, rng2t)
    print(cmd)
    time.sleep(3)
    ser.write(cmd.encode('utf-8'))  #serial.write() doesn't support unicode strings 
    print('Color has been changed/set') #Debug info

def menu(event):
    if modes.get() == 'Static color':
        try:
            frame2.grid_forget()
            frame3.grid_forget()
        except:
            print('ni wim co to kurwa ten jebany frame2')   #do not consider what does it mean,  it's only for me
        #frame1 = Frame(root)
        print(modes.current(), modes.get())
        Label(frame1, text='\nSet static color', font=('none', 14), bg=tk_bg, fg="#d3dae3") .grid(row=0, column=2)
        Label(frame1, text='R: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=1, column=2, sticky=S)
        entryr = Entry(frame1, width=4, bg='white', fg='black', borderwidth=0) 
        entryr.grid(row=1, column=2, sticky=E)
        Label(frame1, text='G: ', font=('none', 12),  bg=tk_bg,fg="#d3dae3") .grid(row=2, column=2, sticky=S)
        entryg = Entry(frame1, width=4, bg='white', fg='black', borderwidth=0) 
        entryg.grid(row=2, column=2, sticky=E)
        Label(frame1, text='B: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=3, column=2, sticky=S)
        entryb = Entry(frame1, width=4, bg='white', fg='black', borderwidth=0) 
        entryb.grid(row=3, column=2, sticky=E)
        Label(frame1, text='\n', font=('none', 3), bg=tk_bg). grid(row=4)
        Button(frame1, text='Set',  bg=tk_bg,fg='white', width=4, font=('none', 13),  borderwidth=1, command=lambda: statclr(entryr.get(), entryg.get(), entryb.get())) .grid(row=5, column=2, sticky=S)
        frame1.grid(row=5, column=2, sticky=S+E+N+W)
        #frame2 = Frame(root)
    elif modes.get() == 'Rainbow':
        try:
            frame1.grid_forget()
            frame3.grid_forget()
        except:
            print('ni wim co to kurwa ten jebany frame1') #...and this
        #frame2 = Frame(root)
        print(modes.current(), modes.get())
        Label(frame2, text='\nRainbow', font=('none', 14), bg=tk_bg,fg="#d3dae3") .grid(row=0, column=2, sticky=W)
        Label(frame2, text='Unlimited: time = 0', font=('none', 10), bg=tk_bg, fg="#d3dae3") .grid(row=1, column=2, sticky=W) 
        Label(frame2, text='Time (s): ', font=('none', 12), bg=tk_bg,fg="#d3dae3") .grid(row=20, column=2, sticky=S)
        entrytime = Entry(frame2, width=4, bg='white', fg='black', borderwidth=0)
        entrytime.grid(row=20, column=2, sticky=E)
        Label(frame2, text='\n', font=('none', 3), bg=tk_bg, fg="#d3dae3"). grid(row=21)
        Button(frame2, text='Set',  bg=tk_bg,fg='white', width=4, font=('none', 13),  borderwidth=1, command=lambda: rainbow(entrytime.get())) .grid(row=22, column=2, sticky=S)
        Button(frame2, text='Stop', bg=tk_bg, fg='white', width=4, font=('none', 13),  borderwidth=1,  command=lambda: r_interrupt()) .grid(row=22, column=3, sticky=W)
        frame2.grid(row=5, column=2, sticky=S+N+W+E)
        #frame2 = Frame(root)
    elif modes.get() == 'Double static color':
        try:
            frame2.grid_forget()
            frame1.grid_forget()
        except:
            print('Nie wiem co to kurwa frame1, ani frame2')   #...and this
        print(modes.current(), modes.get())
        Label(frame3, text='\nSet 1st color:', font=('none', 14), bg=tk_bg, fg="#d3dae3") .grid(row=0, column=1)
        Label(frame3, text='R: ', font=('none', 12),  bg=tk_bg,  fg="#d3dae3") .grid(row=1, column=1, sticky=S)
        entryr1 = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0) 
        entryr1.grid(row=1, column=1, sticky=E)
        Label(frame3, text='G: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=2, column=1, sticky=S)
        entryg1 = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0) 
        entryg1.grid(row=2, column=1, sticky=E)
        Label(frame3, text='B: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=3, column=1, sticky=S)
        entryb1 = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0) 
        entryb1.grid(row=3, column=1, sticky=E)
        Label(frame3, text='\n', font=('none', 3), bg=tk_bg). grid(row=4)
        Label(frame3, text='\n   Set 2nd color:', font=('none', 14), bg=tk_bg, fg="#d3dae3") .grid(row=0, column=2)
        Label(frame3, text='R: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=1, column=2, sticky=S)
        entryr2 = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0) 
        entryr2.grid(row=1, column=2, sticky=E)
        Label(frame3, text='G: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=2, column=2, sticky=S)
        entryg2 = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0) 
        entryg2.grid(row=2, column=2, sticky=E)
        Label(frame3, text='B: ', font=('none', 12), bg=tk_bg, fg="#d3dae3") .grid(row=3, column=2, sticky=S)
        entryb2 = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0) 
        entryb2.grid(row=3, column=2, sticky=E)
        Label(frame3, text='\n', font=('none', 3), bg=tk_bg). grid(row=4)
        Label(frame3, text='Choose 1st range\n of LEDs:', font=('none', 10),  fg="#d3dae3", bg=tk_bg) .grid(row=5, column=1)
        Label(frame3, text='Choose 2nd range\n of LEDs:', font=('none', 10),  fg="#d3dae3", bg=tk_bg) .grid(row=5, column=2)
        entryrng1f = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0)
        entryrng1f.grid(row=6,column=1, sticky=W)
        Label(frame3, text='-', font=('none', 15), bg=tk_bg, fg="#d3dae3") .grid(row=6, column=1, sticky=S)
        entryrng1t = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0)
        entryrng1t.grid(row=6, column=1, sticky=E)
        entryrng2f = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0)
        entryrng2f.grid(row=6,column=2, sticky=W)
        Label(frame3, text='-', font=('none', 15), bg=tk_bg, fg="#d3dae3") .grid(row=6, column=2, sticky=S)
        entryrng2t = Entry(frame3, width=4, bg='white', fg='black', borderwidth=0)
        entryrng2t.grid(row=6, column=2, sticky=E)
        Button(frame3, text='Set', bg=tk_bg, fg='white', width=4, font=('none', 13),  borderwidth=1, command=lambda: dblstatclr(entryr1.get(), entryg1.get(), entryb1.get(), entryr2.get(), entryg2.get(), entryb2.get(), entryrng1f.get(), entryrng1t.get(), entryrng2f.get(), entryrng2t.get())) .grid(row=7, column=1, sticky=E)
        frame3.grid(row=5, column=2, sticky=S+E+N+W)
        

root = Tk()
root.title("Python LED Controller")
root.geometry("633x487")
#root.resizable(0, 0)

tk_bg = "#31363b"
tk_fg = "#eff0f1"

root.configure(bg=tk_bg)
Font(family='Nano Sans')
Label(root, text='\t \t \t', bg=tk_bg, fg="#d3dae3") .grid(row=0, column=0)
Label(root, text='Python LED Controller', font=('none', 22),  bg=tk_bg,fg="#d3dae3") .grid(row=2, column=2)
Label(root, text='Available modes:', font=('none', 18),  bg=tk_bg,fg="#d3dae3") .grid(row=3, column=2)

modes = ttk.Combobox(root, state='readonly', font=('none', 12), 
                     values=[
                             "Rainbow",
                             "Static color",
                             "Double static color",
                             "Choose mode from list:"])
modes.grid(row=4, column=2, sticky=S+N)
modes.current(3)

print(modes.current(), modes.get())

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame1.configure(bg=tk_bg)
frame2.configure(bg=tk_bg)
frame3.configure(bg=tk_bg)

modes.bind('<<ComboboxSelected>>', menu)

root.mainloop()
