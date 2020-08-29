from pygame import mixer
from tkinter import *
from tkinter import filedialog

from mutagen.mp3 import MP3



def adjusts(value,total_length):

    # position = Label(source, text="current time")
    # position.grid(row=0, column=0)
    def set_time(val,total_length):
        print("val1= ", val)
        print("total length = ", total_length)
        val = (float(val)+1)
        print("val1= ", val)
        mixer.music.rewind()
        mixer.music.set_pos(val)
        pos= mixer.music.get_pos()
        print("current position: ",pos)

        # print(val)
        # pos = mixer.music.get_pos()
        #
        # position['text'] = "elapsed time:" + str(pos)




    #SOUND_FILE = 'c:/temp/JMJ.mp3'
    # SOUND_FILE =  directory
    mixer.pre_init(44100, -16, 2, 0) # if missing, the play speed will be too slow
    # mixer.init()
    # mixer.music.load(SOUND_FILE.name)
    value = float(value)
    mixer.music.play( start=value) # 1626 seconds from beginning
    ratio = value / total_length
    print(ratio)


    # audio = MP3(SOUND_FILE)
    # total_length =  audio.info.length-10
    #
    #
    # print("total length: ", total_length)
    # scale = Scale(source, from_=0, to=total_length, orient=HORIZONTAL, command=set_time, showvalue=0, sliderrelief=SUNKEN)  # min and max values
    # scale.set(0)  # the default value of the scale when the music player starts
    # # mixer.music.set_volume(0.7)
    # scale.grid(row=2, columnspan = 3)
    # set_time(value,total_length)



