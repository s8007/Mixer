from tkinter import *
from tkinter.ttk import *
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox
mixer.init()
root=Tk()
channel1=mixer.Channel(0)
channel2=mixer.Channel(1)
channel3=mixer.Channel(2)
channel4=mixer.Channel(3)
channel5=mixer.Channel(4)
channel6=mixer.Channel(5)
channel7=mixer.Channel(6)
channel8=mixer.Channel(7)
root.meter1=DoubleVar()
root.meter2=DoubleVar()
root.meter3=DoubleVar()
root.meter4=DoubleVar()
root.meter5=DoubleVar()
root.meter6=DoubleVar()
root.meter7=DoubleVar()
root.meter8=DoubleVar()
root.meter9=DoubleVar()
root.track=0
root.filename1=''
root.filename2=''
root.filename3=''
root.filename4=''
root.filename5=''
root.filename6=''
root.filename7=''
root.filename8=''
root.midfile=''
root.paused=False
root.playing=False
root.track=1
root.title('Mixer v1.0 ©sserver')
root.pan1=0
root.volume1=1
root.volumeL1=1
root.volumeR1=1
root.pan2=0
root.volume2=1
root.volumeL2=1
root.volumeR2=1
root.volume3=1
root.pan3=0
root.volumeL3=1
root.volumeR3=1
root.volume4=1
root.pan4=1
root.volumeL4=1
root.volumeR4=1
root.volume5=1
root.pan5=0
root.volumeL5=0
root.volumeR5=0
root.pan6=0
root.volume6=1
root.volumeL6=1
root.volumeR6=1
root.volume7=1
root.pan7=0
root.volumeL7=1
root.volumeR7=1
root.pan8=0
root.volume8=1
root.volumeL8=1
root.volumeR8=1
root.grid()
root.resizable(False, False)
root.stopped=True
def open_file(channel):
    if not mixer.music.get_busy() and not channel1.get_busy() and not channel2.get_busy() and not channel3.get_busy() and not channel4.get_busy() and not channel5.get_busy() and not channel6.get_busy() and not channel7.get_busy() and not channel8.get_busy() and not root.paused:
        if channel==1:
            root.filename1=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])
        elif channel==2:
            root.filename2=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])
        elif channel==3:
            root.filename3=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])
        elif channel==4:
            root.filename4=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])
        elif channel==5:
            root.filename5=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])       
        elif channel==6:
            root.filename6=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])
        elif channel==7:
            root.filename7=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])       
        elif channel==8:
            root.filename8=filedialog.askopenfilename(filetypes=[('WAV Files', '*.wav'), ('MP3 Files', '*.mp3'), ('M4A Files', '*.m4a')])
        elif channel==9:
            root.midfile=filedialog.askopenfilename(filetypes=[('MID Files', '*.mid')])
    else:
            messagebox.showerror('', "Can't add file to channel while playing")
def clear(channel):
    if not mixer.music.get_busy() and not channel1.get_busy() and not channel2.get_busy() and not channel3.get_busy() and not channel4.get_busy() and not channel5.get_busy() and not channel6.get_busy() and not channel7.get_busy() and not channel8.get_busy() and not root.paused:
        if channel==1:
            root.filename1=''
        elif channel==2:
            root.filename2=''
        elif channel==3:
            root.filename3=''
        elif channel==4:
            root.filename4=''
        elif channel==5:
            root.filename5=''       
        elif channel==6:
            root.filename6=''
        elif channel==7:
            root.filename7=''       
        elif channel==8:
            root.filename8=''
        elif channel==9:
            root.midfile=''
        messagebox.showinfo('', 'Channel cleared.')
    else:
        messagebox.showerror('', "Can't clear channel while playing")
def detect():
    if root.playing and not mixer.music.get_busy() and not channel1.get_busy() and not channel2.get_busy() and not channel3.get_busy() and not channel4.get_busy() and not channel5.get_busy() and not channel6.get_busy() and not channel7.get_busy() and not channel8.get_busy() and not root.paused and not root.stopped:
        if loop.instate(['selected']):
            play()
        else:
            if root.stopped:
                return
            else:
                stop()
                return
    root.update()
    root.after(10, detect)
def play():
    try:
        playButton.config(text='||')
        if root.paused:
            channel1.unpause()
            channel2.unpause()
            channel3.unpause()
            channel4.unpause()
            channel5.unpause()
            channel6.unpause()
            channel7.unpause()
            channel8.unpause()
            mixer.music.unpause()
            root.paused=False
        else:
            if not root.filename1=='':
                channel1.play(mixer.Sound(root.filename1))
            if not root.filename2=='':
                channel2.play(mixer.Sound(root.filename2))
            if not root.filename3=='':
                channel3.play(mixer.Sound(root.filename3))
            if not root.filename4=='':
                channel4.play(mixer.Sound(root.filename4))
            if not root.filename5=='':
                channel5.play(mixer.Sound(root.filename5))
            if not root.filename6=='':
                channel6.play(mixer.Sound(root.filename6))
            if not root.filename7=='':
                channel7.play(mixer.Sound(root.filename7))
            if not root.filename8=='':
                channel8.play(mixer.Sound(root.filename8))
            if not root.midfile=='':
                mixer.music.load(root.midfile)
                mixer.music.play()
            detect()
        root.playing=True
        root.title('Mixer-Playing')
        update_volume()
        root.stopped=False
    except ImportError:
        pass
def pause():
    if root.playing:
        root.playing=False
        root.paused=True
        update_volume()
        channel1.pause()
        channel2.pause()
        channel3.pause()
        channel4.pause()
        channel5.pause()
        channel6.pause()
        channel7.pause()
        channel8.pause()
        mixer.music.pause()
        playButton.config(text='|>')
        root.title('Mixer-Paused')
def stop():
    root.stopped=True
    channel1.stop()
    channel2.stop()
    channel3.stop()
    channel4.stop()
    channel5.stop()
    channel6.stop()
    channel7.stop()
    channel8.stop()
    mixer.music.stop()
    root.playing=False
    update_volume()
    playButton.config(text='|>')
    root.title('Mixer v1.0 ©sserver')
def update_volume():
    if root.pan1==0:
        root.volumeL1=root.volume1
        root.volumeR1=root.volume1
    elif root.pan1>0:
        root.volumeL1=root.volume1-(root.volume1*root.pan1)
        root.volumeR1=root.volume1
    else:
        root.volumeL1=root.volume1
        root.volumeR1=root.volume1+(root.volume1*root.pan1)
    if root.pan2==0:
        root.volumeL2=root.volume2
        root.volumeR2=root.volume2
    elif root.pan2>0:
        root.volumeL2=root.volume2-(root.volume2*root.pan2)
        root.volumeR2=root.volume2
    else:
        root.volumeL2=root.volume2
        root.volumeR2=root.volume2+(root.volume2*root.pan2)
    if root.pan3==0:
        root.volumeL3=root.volume3
        root.volumeR3=root.volume3
    elif root.pan3>0:
        root.volumeL3=root.volume3-(root.volume3*root.pan3)
        root.volumeR3=root.volume3
    else:
        root.volumeL3=root.volume3
        root.volumeR3=root.volume3+(root.volume3*root.pan3)
    if root.pan4==0:
        root.volumeL4=root.volume4
        root.volumeR4=root.volume4
    elif root.pan4>0:
        root.volumeL4=root.volume4-(root.volume4*root.pan4)
        root.volumeR4=root.volume4
    else:
        root.volumeL4=root.volume4
        root.volumeR4=root.volume4+(root.volume4*root.pan4)
    if root.pan5==0:
        root.volumeL5=root.volume5
        root.volumeR5=root.volume5
    elif root.pan5>0:
        root.volumeL5=root.volume5-(root.volume5*root.pan5)
        root.volumeR5=root.volume5
    else:
        root.volumeL5=root.volume5
        root.volumeR5=root.volume5+(root.volume5*root.pan5)
    if root.pan6==0:
        root.volumeL6=root.volume6
        root.volumeR6=root.volume6
    elif root.pan6>0:
        root.volumeL6=root.volume6-(root.volume6*root.pan6)
        root.volumeR6=root.volume6
    else:
        root.volumeL6=root.volume6
        root.volumeR6=root.volume6+(root.volume6*root.pan6)
    if root.pan7==0:
        root.volumeL7=root.volume7
        root.volumeR7=root.volume7
    elif root.pan7>0:
        root.volumeL7=root.volume7-(root.volume7*root.pan7)
        root.volumeR7=root.volume7
    else:
        root.volumeL7=root.volume7
        root.volumeR7=root.volume7+(root.volume7*root.pan7)
    if root.pan8==0:
        root.volumeL8=root.volume8
        root.volumeR8=root.volume8
    elif root.pan8>0:
        root.volumeL8=root.volume8-(root.volume8*root.pan8)
        root.volumeR8=root.volume8
    else:
        root.volumeL8=root.volume8
        root.volumeR8=root.volume8+(root.volume8*root.pan8)
    channel1.set_volume(root.volumeL1, root.volumeR1)
    channel2.set_volume(root.volumeL2, root.volumeR2)
    channel3.set_volume(root.volumeL3, root.volumeR3)
    channel4.set_volume(root.volumeL4, root.volumeR4)
    channel5.set_volume(root.volumeL5, root.volumeR5)
    channel6.set_volume(root.volumeL6, root.volumeR6)
    channel7.set_volume(root.volumeL7, root.volumeR7)
    channel8.set_volume(root.volumeL7, root.volumeR8)
    root.update()
def change_volume1(v):
    root.volume1=-1*int(float(v))/20
    update_volume()
def change_pan1(v):
    root.pan1=int(float(v))/10
    update_volume()
def change_volume2(v):
    root.volume2=-1*int(float(v))/20
    update_volume()
def change_pan2(v):
    root.pan2=int(float(v))/10
    update_volume()
def change_volume3(v):
    root.volume3=-1*int(float(v))/20
    update_volume()
def change_pan3(v):
    root.pan3=int(float(v))/10
    update_volume()
def change_volume4(v):
    root.volume4=-1*int(float(v))/20
    update_volume()
def change_pan4(v):
    root.pan4=int(float(v))/10
    update_volume()
def change_volume5(v):
    root.volume5=-1*int(float(v))/20
    update_volume()
def change_pan5(v):
    root.pan5=int(float(v))/10
    update_volume()
def change_volume6(v):
    root.volume4=-1*int(float(v))/20
    update_volume()
def change_pan6(v):
    root.pan4=int(float(v))/10
    update_volume()
def change_volume7(v):
    root.volume7=-1*int(float(v))/20
    update_volume()
def change_pan7(v):
    root.pan7=int(float(v))/10
    update_volume()
def change_volume8(v):
    root.volume8=-1*int(float(v))/20
    update_volume()
def change_pan8(v):
    root.pan8=int(float(v))/10
    update_volume()
def play_pause():
    if root.playing:
        pause()
    else:
        play()
playButton=Button(root, text='|>', command=play_pause)
playButton.grid(column=5, row=6)
Button(root, text='×', command=stop).grid(column=5, row=7)
Label(root, text='1').grid(column=1, row=1)
Label(root, text='2').grid(column=2, row=1)
Label(root, text='3').grid(column=3, row=1)
Label(root, text='4').grid(column=4, row=1)
Label(root, text='5').grid(column=5, row=1)
Label(root, text='6').grid(column=6, row=1)
Label(root, text='7').grid(column=7, row=1)
Label(root, text='8').grid(column=8, row=1)
Label(root, text='MIDI CHANNEL').grid(column=9, row=1)
Progressbar(root, mode='determinate',variable=root.meter1, orient=VERTICAL).grid(column=1, row=0)
Progressbar(root, mode='determinate',variable=root.meter2, orient=VERTICAL).grid(column=2, row=0)
Progressbar(root, mode='determinate',variable=root.meter3, orient=VERTICAL).grid(column=3, row=0)
Progressbar(root, mode='determinate',variable=root.meter4, orient=VERTICAL).grid(column=4, row=0)
Progressbar(root, mode='determinate',variable=root.meter5, orient=VERTICAL).grid(column=5, row=0)
Progressbar(root, mode='determinate',variable=root.meter6, orient=VERTICAL).grid(column=6, row=0)
Progressbar(root, mode='determinate',variable=root.meter7, orient=VERTICAL).grid(column=7, row=0)
Progressbar(root, mode='determinate',variable=root.meter8, orient=VERTICAL).grid(column=8, row=0)
Progressbar(root, mode='determinate', orient=VERTICAL).grid(column=9, row=0)
volumeSlider1=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume1)
volumeSlider1.grid(column=1, row=3)
volumeSlider1.set(-20)
Scale(root, from_=-10, to=10, command=change_pan1).grid(column=1, row=2)
Button(root, text='File', command=lambda: open_file(1)).grid(column=1, row=4)
Button(root, text='Clear', command=lambda: clear(1)).grid(column=1, row=5)
volumeSlider2=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume2)
volumeSlider2.grid(column=2, row=3)
volumeSlider2.set(-20)
Scale(root, from_=-10, to=10, command=change_pan2).grid(column=2, row=2)
Button(root, text='File', command=lambda: open_file(2)).grid(column=2, row=4)
Button(root, text='Clear', command=lambda: clear(2)).grid(column=2, row=5)
volumeSlider3=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume3)
volumeSlider3.grid(column=3, row=3)
volumeSlider3.set(-20)
Scale(root, from_=-10, to=10, command=change_pan3).grid(column=3, row=2)
Button(root, text='File', command=lambda: open_file(3)).grid(column=3, row=4)
Button(root, text='Clear', command=lambda: clear(3)).grid(column=3, row=5)
volumeSlider4=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume4)
volumeSlider4.grid(column=4, row=3)
volumeSlider4.set(-20)
Scale(root, from_=-10, to=10, command=change_pan4).grid(column=4, row=2)
Button(root, text='File', command=lambda: open_file(4)).grid(column=4, row=4)
Button(root, text='Clear', command=lambda: clear(4)).grid(column=4, row=5)
volumeSlider5=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume5)
volumeSlider5.grid(column=5, row=3)
volumeSlider5.set(-20)
Scale(root, from_=-10, to=10, command=change_pan5).grid(column=5, row=2)
Button(root, text='File', command=lambda: open_file(5)).grid(column=5, row=4)
Button(root, text='Clear', command=lambda: clear(5)).grid(column=5, row=5)
volumeSlider6=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume6)
volumeSlider6.grid(column=6, row=3)
volumeSlider6.set(-20)
Scale(root, from_=-10, to=10, command=change_pan6).grid(column=6, row=2)
Button(root, text='File', command=lambda: open_file(6)).grid(column=6, row=4)
Button(root, text='Clear', command=lambda: clear(6)).grid(column=6, row=5)
volumeSlider7=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume7)
volumeSlider7.grid(column=7, row=3)
volumeSlider7.set(-20)
Scale(root, from_=-10, to=10, command=change_pan7).grid(column=7, row=2)
Button(root, text='File', command=lambda: open_file(7)).grid(column=7, row=4)
Button(root, text='Clear', command=lambda: clear(7)).grid(column=7, row=5)
volumeSlider8=Scale(root, from_=-20, to=0, orient=VERTICAL, command=change_volume8)
volumeSlider8.grid(column=8, row=3)
volumeSlider8.set(-20)
Scale(root, from_=-10, to=10, command=change_pan8).grid(column=8, row=2)
Button(root, text='File', command=lambda: open_file(8)).grid(column=8, row=4)
Button(root, text='Clear', command=lambda: clear(8)).grid(column=8, row=5)
Button(root, text='File', command=lambda: open_file(9)).grid(column=9, row=4)
Button(root, text='Clear', command=lambda: clear(9)).grid(column=9, row=5)
loop=Checkbutton(root, text='Loop')
loop.state(['!alternate'])
loop.grid(column=1, row=7)
try:
    root.iconbitmap('play.ico')
except:
    messagbox.showerror('Error', 'App icon photo is missiong or corrupt')
root.mainloop()
