from tkinter import *
from datetime import datetime
from tkinter.ttk import Progressbar
from tk_tools import *
from tkinter import Menu
import pygame
from tkinter import messagebox
pygame.mixer.init()
channel=pygame.mixer.find_channel()
alarmchannel=pygame.mixer.find_channel()
from tkinter.ttk import *
from tkinter import filedialog
import time
clock=Tk()
hour=0
clock.barmode=False
mins=0
secs=0
clock.settingalarm=False
def play_chime():
    if channel.get_busy()==False and clock.chime.get()>0:
        try:
            channel.play(pygame.mixer.Sound(str(clock.chime.get())+'.wav'))
        except:
            messagebox.showerror('Error', 'File '+str(clock.chime.get())+'.wav cannot be found.')
def set_alarm():
    errorLabel.config(text='')
    if not clock.settingalarm:
        clock.settingalarm=True
        clock.alarm.set(0)
        hourEntry.config(state='readonly')
        minuteEntry.config(state='readonly')
        offButton.config(state=DISABLED)
        onButton.config(state=DISABLED)
    else:
        if hourEntry.get()=='' or minuteEntry.get()=='':
            errorLabel.config(text='Error: Blank values!')
        else:
            clock.settingalarm=False
            clock.alarmhour=int(hourEntry.get())
            clock.alarmmins=int(minuteEntry.get())
            hourEntry.config(state=DISABLED)
            minuteEntry.config(state=DISABLED)
            offButton.config(state=NORMAL)
            onButton.config(state=NORMAL)
def stop_alarm():
    alarmchannel.stop()
    setButton.config(text='Set Alarm', command=set_alarm)
clock.config(bg='black')
clock.resizable(False, False)
clock.title('Tick v1.9 ©sserver')
day_percent=DoubleVar()
hourLabel=SevenSegmentDigits(clock, background='black', digit_color='#00ff00', height=100, digits=2)
hourLabel.grid(column=1, row=1)
colon1=Label(clock, text=':', foreground='white', background='black', font=('Century Gothic', 75))
colon1.grid(column=2, row=1)
minuteLabel=SevenSegmentDigits(clock, background='black', digit_color='#00ff00', height=100, digits=2)
minuteLabel.grid(column=3, row=1)
colon2=Label(clock, text=':', foreground='white', background='black', font=('Century Gothic', 75))
colon2.grid(column=4, row=1)
secondLabel=SevenSegmentDigits(clock, background='black', digit_color='#00ff00', height=100, digits=2)
secondLabel.grid(column=5, row=1)
Progressbar(clock, mode='determinate', variable=day_percent, length=350).place(x=10, y=130)
clock.chime=IntVar()
clock.alarm=IntVar()
clock.lift()
clock.alarmhour=0
clock.alarmmins=0
Radiobutton(clock, 
               text="Off",
               variable=clock.chime, 
               value=0, command=channel.stop).place(x=20, y=160)
Radiobutton(clock, 
               text="1",
               variable=clock.chime, 
               value=1).place(x=60, y=160)
Radiobutton(clock, 
               text="2",
               variable=clock.chime, 
               value=2).place(x=88, y=160)

Radiobutton(clock, 
               text="3",
               variable=clock.chime, 
               value=3).place(x=116, y=160)
Radiobutton(clock, 
               text="4",
               variable=clock.chime, 
               value=4).place(x=144, y=160)
Label(clock, text='↑Chime Options                                               Alarm Options↓', background='black', foreground='white').place(x=20, y=190)
errorLabel=Label(clock, background='black', foreground='red', text='')
errorLabel.place(x=120,y=190)
clock.mode=False
clock.keepontop=False
clock.geometry('370x250')
playButton=Button(clock, text='Play Chime', command=play_chime)
offButton=Radiobutton(clock, 
               text="Off",
               variable=clock.alarm, 
               value=0, command=stop_alarm, state=DISABLED)
offButton.place(x=20, y=220)
onButton=Radiobutton(clock, 
               text="On",
               variable=clock.alarm, 
               value=1, state=DISABLED)
onButton.place(x=60, y=220)
setButton=Button(clock, text='Set Alarm', command=set_alarm)
setButton.place(x=260, y=220)
hourEntry=Spinbox(clock, from_=0, to=23, width=10, state=DISABLED)
hourEntry.place(x=100, y=220)
minuteEntry=Spinbox(clock, from_=0, to=59, width=10, state=DISABLED)
minuteEntry.place(x=180, y=220)
playButton.place(x=290, y=160)
clock.options_open=False
def close():
    clock.destroy()
    if clock.options_open:
        clock.options.destroy()
clock.protocol('WM_DELETE_WINDOW', close)
def reset():
    clock.options_open=False
    clock.options.destroy()
def options():
    def update_values():
        if chk.instate(['selected']):
            clock.mode=True
        else:
            clock.mode=False
        if chk1.instate(['selected']):
            clock.keepontop=True
        else:
            clock.keepontop=False
    def barmode_off():
        clock.barmode=False
    def barmode_on():
        clock.barmode=True
    if not clock.options_open:
        clock.options=Tk()
        clock.options.title('Options')
        chk=Checkbutton(clock.options, command=update_values, text='Show part of day/hour remaining in bar')
        chk.pack()
        chk1=Checkbutton(clock.options, command=update_values, text='Keep on top')
        chk1.pack()
        Label(clock.options, text='What do you want to show on the progress bar?').pack()
        rb=Radiobutton(clock.options, 
               text="Part of day",
               command=barmode_off, 
               value=0)
        rb.pack()
        rb1=Radiobutton(clock.options, 
               text="Part of hour",
               command=barmode_on)
        rb1.pack()
        if clock.barmode:
            rb1.invoke()
        else:
            rb.invoke()
        chk.state(['!alternate'])
        chk1.state(['!alternate'])
        if clock.mode:
            chk.state(['selected'])
        if clock.keepontop:
            chk1.state(['selected'])
        if clock.iconpresent:
            clock.options.iconbitmap('clock.ico')
        clock.options.protocol('WM_DELETE_WINDOW', reset)
        clock.options.resizable(False, False)
        clock.options_open=True
    else:
        clock.options.lift()
Button(clock, text='Options', command=options).place(x=200, y=160)
clock.iconpresent=True
try:
    clock.iconbitmap('clock.ico')
except:
    messagebox.showerror('Icon Error', 'App icon is missing or corrupt')
    clock.iconpresent=False
while True:
    try:
        d = datetime.now()
        hour = d.strftime("%I")
        hour2=d.strftime('%H')
        mins = d.strftime("%M")
        secs = d.strftime("%S")
        day =  d.strftime("%A")
        part_of_day=d.strftime("%p")
        hourLabel.set_value(hour)
        minuteLabel.set_value(mins)
        secondLabel.set_value(secs)
        clock.update()
        if clock.keepontop:
            clock.call('wm', 'attributes', '.', '-topmost', True)
        else:
            clock.call('wm', 'attributes', '.', '-topmost', False)
        if not clock.barmode:
            if clock.mode:
                day_percent.set(((86400-((int(hour2)*3600+int(mins)*60+int(secs))))/86400)*100)
            else:
                day_percent.set(((int(hour2)*3600+int(mins)*60+int(secs))/86400)*100)
        else:
            if clock.mode:
                day_percent.set(((3600-(int(mins)*60+int(secs)))/3600)*100)
            else:
                day_percent.set(((int(mins)*60+int(secs)))/3600*100)
        if clock.alarm.get()==1 and (int(mins)==clock.alarmmins and int(hour2)==clock.alarmhour and secs=='00') and (not alarmchannel.get_busy()):
            try:
                alarmchannel.play(pygame.mixer.Sound('alarm.wav'), -1)
                setButton.config(text='Stop Alarm', command=stop_alarm)
            except:
                messagebox.showerror('Error', 'File alarm.wav cannot be found.')
        if mins=='00' and secs=='00':
            play_chime()
        time.sleep(0.01)
    except:
        break
