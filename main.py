import os
import time
import threading
from tkinter import *
from PIL.ImageTk import PhotoImage
from pygame import mixer
from tkinter import colorchooser
from ttkthemes import themed_tk as tk
from tkinter import ttk  # this one improves the style of the element
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import filedialog
from mutagen.mp3 import MP3
import adjust

playlist_path = []


# playlist_path contains the full path and the file names
# PLaylist contains only the file name
# Full path + filename is required to play music inside playMusic function

def browseFile():
    global filename_path
    filename_path = filedialog.askopenfilename()

    try:
        if os.path.basename((filename_path)) != "":
            add_to_playlist(filename_path)
    except:
        print('erreur')


# This one is for the shortcut
def browse_file(event):
    global filename_path
    global index
    filename_path = filedialog.askopenfilename()
    try:
        if os.path.basename((filename_path)) != "":
            add_to_playlist(filename_path)
    except:
        print('canceled')

artwork=[]
# this is for adding several songs in a folder
def select_playlist():
    global index
    global width
    directory = filedialog.askdirectory()
    for r, d, f in os.walk(directory):
        for file in f:
            if '.mp3' in file:
                filename = os.path.basename(file)
                playlist.insert(index, filename)
                playlist_path.insert(index, r + "/" + filename)
                width = list_width()
                playlist.configure(width=width)
                index += 1


index = 0


# update the playlist box by changing it's with
def list_width():
    width = 20
    for i in range(len(playlist_path)):
        name = os.path.basename(playlist_path[i])

        if width < len(name):
            if len(name)<40:
                width = len(name)
        else:
            continue
    return width + 1


def add_to_playlist(filename):
    global index
    global width
    filename = os.path.basename(filename)
    playlist.insert(index, filename)
    playlist_path.insert(index, filename_path)
    width = list_width()
    playlist.configure(width=width)
    index += 1
    print(playlist_path)


def delete_song():
    global index
    try:
        selected_song = playlist.curselection()
        selectedsong = int(selected_song[0])
        playlist.delete(selectedsong)
        playlist_path.pop(selectedsong)
        index -= 1
    except:
        tkinter.messagebox.showerror("Can't delete", "No song selected or playlist is empty")


def background_color():
    color = colorchooser.askcolor(title="Select color")
    root.configure(background=color[1])
    leftframe.configure(background=color[1])
    buttonsFrame.configure(background=color[1])
    listFrame.configure(background=color[1])
    rightframe.configure(background=color[1])
    topframe.configure(background=color[1])
    middleframe.configure(background=color[1])
    bottomframe.configure(background=color[1])
    # songname.configure(background= color[1])


global theme
theme = "plastik"


def set_theme_aquativo():
    global theme
    theme = "aquativo"
    root.set_theme(theme)

def set_theme_black():
    global theme
    theme = "black"
    root.set_theme(theme)

def set_theme_blue():
    global theme
    theme = "blue"
    root.set_theme(theme)

def set_theme_clearlooks():
    global theme
    theme = "clearlooks"
    root.set_theme(theme)

def set_theme_elegance():
    global theme
    theme = "elegance"
    root.set_theme(theme)

def set_theme_itft1():
    global theme
    theme = "itft1"
    root.set_theme(theme)

def set_theme_keramik():
    global theme
    theme = "keramik"
    root.set_theme(theme)

def set_theme_kroc():
    global theme
    theme = "kroc"
    root.set_theme(theme)

def set_theme_plastik():
    global theme
    theme = "plastik"
    root.set_theme(theme)

def set_theme_radiance():
    global theme
    theme = "radiance"
    root.set_theme(theme)

def set_theme_smog():
    global theme
    theme = "smog"
    root.set_theme(theme)

def set_theme_winxpblue():
    global theme
    theme = "winxpblue"
    root.set_theme(theme)



root = tk.ThemedTk()
root.get_themes()  # returns a list of all themes that can be set
root.set_theme(theme)  # Sets an available theme
mixer.init()  # initializing the mixer

# usable Fonts are: Arial (corresponds to helvetica), courier new(courier), comic sans ms, Fixedsys,
# Ms sans serif, Ms serif, symbol, system, Times new roman (Times), verdana...

# usable Styles are: normal , boldn roman, italic, underline, overstrike.

statusbar = ttk.Label(root, text="Welcome to Spotify", relief=SUNKEN, anchor=W, font="Helvetica 10 normal")
statusbar.pack(side=BOTTOM, fill=X)

# ***** Menu Bar *****
menubar = Menu(root)
root.config(menu=menubar)

# Root frame - statusbar, leftframe, rightframe
# LeftFrame - The listbox(playlist), addbutton, deletebutton
# RightFrame - TopFrame, MiddleFrame, and the BottomFrame

root.geometry('600x400')
root.title("FMA player")
root.iconbitmap(r'images\logo.ico')

# add file shortcut
leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=20, pady=20)

# **** PLaylist ****
listFrame = Frame(leftframe)
listFrame.pack(fill=X, expand=True)
xscrollbar = ttk.Scrollbar(listFrame, orient='horizontal')
xscrollbar.pack(side=BOTTOM, fill=X)
width = list_width()
yscrollbar = ttk.Scrollbar(listFrame)
yscrollbar.pack(side=RIGHT, fill=Y)
playlist = Listbox(listFrame, selectmode=BROWSE, width=width)  # , width="" + width)
playlist.pack(fill=BOTH, expand=1)
yscrollbar.config(command=playlist.yview)
xscrollbar.config(command=playlist.xview)
playlist.config(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

buttonsFrame = Frame(leftframe)
buttonsFrame.pack(pady=5)
addphoto = PhotoImage(file='images/add.png')
addbutton = ttk.Button(buttonsFrame, image=addphoto, command=browseFile)
addbutton.pack(side=LEFT, padx=5)

deletephoto = PhotoImage(file="images/minus.png")
deletebutton = ttk.Button(buttonsFrame, image=deletephoto, command=delete_song)
deletebutton.pack(side=LEFT)

folderphoto = PhotoImage(file="images/folder.png")
selectfolderbutton = ttk.Button(buttonsFrame, image=folderphoto, command=select_playlist)
selectfolderbutton.pack(side=LEFT, padx=5)

rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()


def aboutUs():
    tkinter.messagebox.showinfo("About US", "This music player was made by FMA built using Python tkinter")


# **** Sub menues ****
fileMenu = Menu(menubar, tearoff=0)  # tearoff removes the dashed line at the beginning of the dropdown menu
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="include file", command=browseFile)
fileMenu.add_command(label="include folder", command=select_playlist)
fileMenu.add_command(label="Exit", command=root.destroy)

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About Us", command=aboutUs)

parametersMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Parameters", menu=parametersMenu)
parametersMenu.add_command(label="Background color", command=background_color)
thememenu = Menu(parametersMenu, tearoff=0)
parametersMenu.add_cascade(label="Theme", menu=thememenu)
thememenu.add_command(label="aquativo", command=set_theme_aquativo)
thememenu.add_command(label = "black", command = set_theme_black)
thememenu.add_command(label = "blue", command = set_theme_blue)
thememenu.add_command(label = "clearlooks", command = set_theme_clearlooks)
thememenu.add_command(label = "elegance", command = set_theme_elegance)
thememenu.add_command(label = "itft1", command = set_theme_itft1)
thememenu.add_command(label = "keramik", command = set_theme_keramik)
thememenu.add_command(label = "kroc", command = set_theme_kroc)
thememenu.add_command(label = "plastik(default)", command = set_theme_plastik)
thememenu.add_command(label = "radiance", command = set_theme_radiance)
thememenu.add_command(label = "smog", command = set_theme_smog)
thememenu.add_command(label = "winxpblue", command = set_theme_winxpblue)

songname = LabelFrame(topframe, text="Song:", font=("bebas neue", 12, "bold"))
songname.pack()
name = Label(songname, text="Select a song", relief=SUNKEN, font=("bebas neue", 15, "bold"), fg="#3596FC")
name.pack()
lengthlabel = ttk.Label(topframe, text="Total length:  --:---", font=("Arial", 10, "normal"))
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text="Current time:  --:---", relief=GROOVE)
currenttimelabel.pack()


# labelphoto = Label(root, image=photo)
# labelphoto.pack()

total_length=100
def show_details(play_song):
    global total_length
    file_data = os.path.splitext(play_song)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length

    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()
    # progress_scale['to'] = (total_length-1)
    progress_bar['maximum'] = total_length  # this sets the length of the file to the max of the progress bar
    # div = total_length /60 , mod = total_length%60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total length" + " " + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    global playlist_path
    global repeat
    current_time = 0
    if current_time == 0:
        progress_bar["value"] = 0
    while current_time <= t and mixer.music.get_busy():  # returns false when we press the stop button
        if paused:
            continue
        else:

            progress_bar["value"] = int(current_time) + 1
            progress_bar.update()
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current time:" + " " + timeformat
            time.sleep(1)
            current_time += 1
    if not mixer.get_busy():
        progress_bar["value"]= t
        if current_song == len(playlist_path) - 1:
                if repeat:
                    next_music()
                else:
                    stopMusic()
        else:
            next_music()


def play_selected_music(event):
    global paused
    global repeat
    global current_song
    last_song = 0
    selected_song = playlist.curselection()
    selected = int(selected_song[0])
    if selected != None:
        if last_song != selected:
            current_song = selected
    last_song = selected


current_song = 0


def play_music():
    global current_song
    global paused
    global repeat
    if paused:

        mixer.music.unpause()
        statusbar['text'] = "Music resumed"
        paused = False
    else:
        try:
            stopMusic()
            time.sleep(1)
            play = playlist_path[current_song]
            mixer.music.load(play)
            mixer.music.play()
            statusbar['text'] = "playing music:" + " " + os.path.basename(play)
            show_details(play)
            name['text'] = os.path.basename(play)
            # progress_scale['state']= NORMAL

        except:
            try:
                play_selected_music()

            except:
                if playlist_path == []:
                    # tkinter.messagebox.showerror("File not Found","Could not find the file to play please select a file first")
                    print("hello world")


def stopMusic():
    global paused
    paused = False
    mixer.music.stop()
    statusbar['text'] = "music stopped"
    progress_bar.stop()


def rewindMusic():
    play_music()
    statusbar['text'] = "Music rewinded"


paused = False


def pauseMusic():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music paused"


def setVolume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)  # the set volume function of mixer only takes values from 0 to 1
    if volume != 0:
        volumeButton.configure(image=volumephoto)


def next_music():
    global current_song
    global playlist_path
    if current_song < len(playlist_path) - 1:
        current_song += 1

    else:
        current_song = 0
    play_music()


def previous_music():
    global current_song
    global playlist_path
    if current_song > 0:
        current_song -= 1

    else:
        current_song = len(playlist_path) - 1
    play_music()


repeat = FALSE


def repeat_music():
    global repeat
    if repeat == FALSE:
        repeat = TRUE

    else:
        repeat = FALSE
    print(repeat)


muted = FALSE


def muteMusic():
    global muted
    if muted:  # unmute the music
        mixer.music.set_volume(0.7)
        volumeButton.configure(image=volumephoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeButton.configure(image=mutephoto)
        scale.set(0)
        muted = TRUE


def on_closing():
    stopMusic()
    answer = tkinter.messagebox.askquestion("Exit", "Are you sure you want to exit FMA Player?")
    if answer == "yes":
        root.destroy()

def set_time(val):
    global position
    global slider
    global current_song
    global playlist_path
    global total_length
    global length
    if playlist_path!= []:

        # audio = MP3(playlist_path[current_song])
        # length = int(audio.info.length - 1)
        # progress_scale['to']= length
        # mixer.music.rewind()
        # stopMusic()
        # print(length)
        # val = float(val)/10
        # print("val =  ",val)
        # mixer.music.set_pos(val)
        # slider = mixer.music.get_pos()
        adjust.adjusts(val,total_length)





first_time = 0


def play_music_shortcut(event):
    global paused
    global first_time

    if first_time == 0:
        play_music()
        first_time += 1
    else:
        if paused:
            play_music()
        else:
            pauseMusic()


# ******************************************************
# ********* Middle frame for player buttons ***********

middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)

playphoto = PhotoImage(file='images/play.png')
playButton = ttk.Button(middleframe, image=playphoto, command=play_music)
playButton.grid(row=0, column=0, padx=10)

stopphoto = PhotoImage(file='images/stop2.png')
stopButton = ttk.Button(middleframe, image=stopphoto, command=stopMusic)
stopButton.grid(row=0, column=1, padx=10)

pausephoto = PhotoImage(file='images/pause3.png')
pauseButton = ttk.Button(middleframe, image=pausephoto, command=pauseMusic)
pauseButton.grid(row=0, column=2, padx=10)

progress_bar = ttk.Progressbar(middleframe, orient='horizontal', length=260, mode='determinate')
progress_bar.grid(row=1, columnspan=3, pady=10)




# progress_scale = ttk.Scale(middleframe, from_=0, to=1, orient=HORIZONTAL,length=260, command=set_time, state = DISABLED)  # min and max values, , showvalue=0 to hide values
# progress_scale.set(0)
# progress_scale.grid(row=2, columnspan= 3)


# ****************************************************************
# ******** Bottom frame for volume rewind and mute etc  *********

bottomframe = Frame(rightframe)
bottomframe.pack()

rewindphoto = PhotoImage(file='images/rewind2.png')
rewindButton = ttk.Button(bottomframe, image=rewindphoto, command=rewindMusic)
rewindButton.grid(row=0, column=1)

nextphoto = PhotoImage(file='images/next.png')
nextButton = ttk.Button(bottomframe, image=nextphoto, command=next_music)
nextButton.grid(row=0, column=2)

previousphoto = Image.open('images/next.png')
previousphoto = ImageTk.PhotoImage(previousphoto.rotate(180))
previousButton = ttk.Button(bottomframe, image=previousphoto, command=previous_music)
previousButton.grid(row=0, column=0)

repeatphoto = PhotoImage(file='images/repeat.png')
repeatButton = ttk.Button(bottomframe, image=repeatphoto, command=repeat_music)
repeatButton.grid(row=0, column=5, padx=5)

mutephoto = PhotoImage(file='images/mute.png')
volumephoto = PhotoImage(file='images/volume.png')
volumeButton = ttk.Button(bottomframe, image=volumephoto, command=muteMusic)
volumeButton.grid(row=0, column=3)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=setVolume)  # min and max values
scale.set(70)  # the default value of the scale when the music player starts
mixer.music.set_volume(0.7)
scale.grid(row=0, column=4, pady=15, padx=30)

playlist.bind('<<ListboxSelect>>', play_selected_music)

root.bind('<Control-o>', browse_file)  # this one is a shortcut fot open file
root.bind('<space>', play_music_shortcut)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
