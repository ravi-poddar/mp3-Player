# Importing Modules
import pygame
import tkinter as tkr
import os

# Creating Window
MusicPlayer = tkr.Tk()

# Mp3 Player Header
MusicPlayer.title("Mp3 Player")
MusicPlayer.geometry("300x400")

# Songs Playlist Directory set
file = "C:/Users/Ravi/PycharmProjects/mp3-Player"
os.chdir(file)
# print(os.getcwd)
songsList = os.listdir()

# Songs Playlist
playList = tkr.Listbox(MusicPlayer, highlightcolor="blue", selectmode = tkr.SINGLE)
print(songsList)
for song in songsList:
    pos = 0
    playList.insert(pos, song)
    pos = pos + 1

# pygame init
pygame.init()
pygame.mixer.init()

# Song Action Events
def playSong():
    pygame.mixer.music.load(playList.get(tkr.ACTIVE))
    songName.set(playList.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

# Mp3 Player Layout
Button1 = tkr.Button(MusicPlayer, width=5, height=3, text="PLAY", command=playSong)
Button2 = tkr.Button(MusicPlayer, width=5, height=3, text="STOP", command=stopSong)
Button3 = tkr.Button(MusicPlayer, width=5, height=3, text="PAUSE", command=pauseSong)
Button4 = tkr.Button(MusicPlayer, width=5, height=3, text="RESUME", command=resumeSong)

# song name
songName = tkr.StringVar()
songTitle = tkr.Label(MusicPlayer, textvariable = songName)


# Place Widgets
songTitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playList.pack(fill="both", expand="yes")
# Activate Mp3 Player
MusicPlayer.mainloop()
