from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os


root=Tk()
root.title('Python Music player App by @Pe_Da')
root.geometry("920x670+290+85")
root.configure(bg="#0e6ce6")
root.resizable(False, False)

mixer.init()

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def Play_Music():
    Playlist.get(ACTIVE)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


image_icon = PhotoImage(file="./proj_img/playerIcon.png")
root.iconphoto(False,image_icon)

Top = PhotoImage(file="./proj_img/top_image.png")
Label(root, image=Top, bg="#195cb3").pack()

Button_Play = PhotoImage(file="./proj_img/playButton.png")
Button(root, image=Button_Play, bg="#195cb3", bd=0, command=Play_Music).place(x=100, y=400, width=75, height=75)

Button_Stop = PhotoImage(file="./proj_img/stopButton.png")
Button(root, image=Button_Stop, bg="#195cb3", bd=0, command=mixer.music.stop).place(x=30, y=500, width=50, height=50)

Button_Resume = PhotoImage(file="./proj_img/resumeButton.png")
Button(root, image=Button_Resume, bg="#195cb3", bd=0, command=mixer.music.unpause).place(x=115, y=500, width=50, height=50)

Button_Pause = PhotoImage(file="./proj_img/pauseButton.png")
Button(root, image=Button_Pause, bg="#195cb3", bd=0, command=mixer.music.pause).place(x=200, y=500, width=50, height=50)

Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)

Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="White", bg="#03234c", command= Add_Music).place(x=745, y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",16), bg="#03234c", fg="white",selectbackground="#195cb3", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
