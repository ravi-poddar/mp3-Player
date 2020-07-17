# Importing Modules
import pygame
import tkinter as tkr

# Creating Window
MusicPlayer = tkr.Tk()

# Mp3 Player Header
MusicPlayer.title("Mp3 Player")
MusicPlayer.geometry("300x400")

# Songs Events
file="Song.mp3"

def playSong():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

# Mp3 Player Layout
Button1 = tkr.Button(MusicPlayer, width=5, height=3, text="PLAY", command=playSong)
Button1.pack(fill="x")
Button2 = tkr.Button(MusicPlayer, width=5, height=3, text="STOP", command=stopSong)
Button2.pack(fill="x")
label1 = tkr.LabelFrame(MusicPlayer, text="Song Name")
label1.pack(fill="both", expand="yes")
content1 = tkr.Label(label1, text=file)
content1.pack()

# Activate Mp3 Player
MusicPlayer.mainloop()
