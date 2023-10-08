import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import pygame
from pygame.locals import *
from pygame import mixer

window=tk.Tk()
window.title("Build an Ocean Garden!")
window.geometry('1124x800')
window.config(bg = '#76819C')

taskbar=tk.Frame(master=window,width=1124)#contains labels and buttons
taskbar.pack()

display=tk.Frame(master=window,width=1124,background='#BBD2EC')#contains output
display.pack()
airplane=tk.Frame(master=display,width=532,background='#BBD2EC')
airplane.pack(side=RIGHT)
spacer=tk.Frame(master=display,width=60,background='#BBD2EC')
spacer.pack(side=RIGHT)
garden = tk.Frame(master=display,width=532,background='#BBD2EC')
garden.pack(side=RIGHT)

bottombar=tk.Frame(master=window,width=1124, height=100,background='#90B1DB')
bottombar.pack(side=BOTTOM)


sun = 0
nutrients = 0
wind = 0

class button(Button): #makes my buttons
    def __init__(self, master, command, text, colour='#BBD2EC', font = 'Courier 15 bold',**kwargs): 
        self.text = text
        self.command = command
        self.colour= colour
        self.font = font
        super().__init__(master,text=text,command=command,font=font,bg=colour)
        self.pack(side=LEFT,padx=50,pady=10)#change to grid if time
        #this displays the buttons as pushed vs not pushed
        def save(self):
            self.config(relief=SUNKEN)
        def stop(self):
            self.config(relief=RAISED)

class taskframe(Frame): #makes my frames
    def __init__(self, colour,master=taskbar,width=250,height=100): 
        self.width=width
        self.height=height
        self.colour = colour
        self.master=master
        super().__init__(master,bg=colour)

#makes the button frames
sun_button_frame = taskframe('#FFE566')
nutrients_button_frame = taskframe('#9DC183')
wind_button_frame = taskframe('#9E7BB5')
submit_button_frame = taskframe('#4169E1')
button_frames = [sun_button_frame,nutrients_button_frame,wind_button_frame,submit_button_frame]
#for bottombar
exit_button_frame=taskframe('#90B1DB',bottombar,width=1124,height=50)
exit_button_frame.pack(side=LEFT)
music_on_frame = taskframe('#90B1DB', bottombar)
music_on_frame.pack(side=RIGHT)
music_off_frame = taskframe('#90B1DB', bottombar) 
music_off_frame.pack(side=RIGHT)

#makes my label frames
sun_label_frame = taskframe('#3E77B6')
nutrients_label_frame = taskframe('#3E77B6')
wind_label_frame = taskframe('#3E77B6')
submit_label_frame = taskframe('#90B1DB')
label_frames = [sun_label_frame,nutrients_label_frame,wind_label_frame,submit_label_frame]

#puts the frames in their correct locations
for i in range(4):
    label_frames[i].grid(row=0,column=i)
    button_frames[i].grid(row=1,column=i)

#makes labels
class labelMaker(Label):
    def __init__(self,text,master=submit_label_frame,font = 'Courier 8 bold',width=21):
        self.master=master
        self.text=text
        self.width=width
        self.font=font

        super().__init__(master=master,bg='#90B1DB',text=text,width=width,font=font)

#this updates the labels to indicate what buttons were selected
def labelUpdater(label,val,coor,master=submit_label_frame, font='Courier 8 bold',width=21):        
    label.destroy()
    label =labelMaker(val,master,font,width)
    label.grid(row=coor,column=0)

#function for processing images
def processImage(file, basewidth):
    img = Image.open(file)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    img.save(file)
    img = ImageTk.PhotoImage(img)
    return img

    
#making the labels and giving them their initial spots
sun_val_label =labelMaker('Super Low Sunlight')
sun_val_label.grid(row=0,column=0)
nutrients_val_label=labelMaker('Super Low Nutrients')
nutrients_val_label.grid(row=1,column=0)
wind_val_label=labelMaker('Super Low Wind')
wind_val_label.grid(row=2,column=0)

#functions that the buttons run
def sun_low(): 
    global sun
    sun = 3
    labelUpdater(sun_val_label, 'Low Sunlight', 0 )
    pygame.mixer.init()
    sound = pygame.mixer.Sound("sun.wav")
    pygame.mixer.Sound.play(sound)
def sun_high(): 
    global sun
    sun = 4
    labelUpdater(sun_val_label, 'High Sunlight', 0 )
    pygame.mixer.init()
    sound = pygame.mixer.Sound("sun.wav")
    pygame.mixer.Sound.play(sound)
def nutrients_low(): 
    global nutrients
    nutrients = 2
    labelUpdater(nutrients_val_label, 'Low Nutrients', 1 )
    pygame.mixer.init()
    sound = pygame.mixer.Sound("nutrients.wav")
    pygame.mixer.Sound.play(sound)
def nutrients_high(): 
    global nutrients
    nutrients = 3
    labelUpdater(nutrients_val_label, 'High Nutrients', 1 )
    pygame.mixer.init()
    sound = pygame.mixer.Sound("nutrients.wav")
    pygame.mixer.Sound.play(sound)
def wind_low(): 
    global wind
    wind = 1
    labelUpdater(wind_val_label, 'Low Wind', 2 )
    pygame.mixer.init()
    sound = pygame.mixer.Sound("wind.wav")
    pygame.mixer.Sound.play(sound)
def wind_high(): 
    global wind
    wind = 2
    labelUpdater(wind_val_label, 'High Wind', 2 )
    pygame.mixer.init()
    sound = pygame.mixer.Sound("wind.wav")
    pygame.mixer.Sound.play(sound)
def exit():
    window.destroy()
def soundOn():
    global pause
    pygame.mixer.music.unpause()
    pause = False
def soundOff():
    pygame.mixer.music.pause()

#creating "empty" labels
airplaneCongrats = labelMaker("",airplane)
airplaneMessage=labelMaker("",airplane)

#Process all images
musicImage = processImage("music.png", 50)
muteImage = processImage("mute.png", 50)
airplaneImage = processImage("airplane.png", 500)
airplaneImageLabel = tk.Label(master=airplane,text="")

#importing and resizing the airplane image
#airplaneImage = Image.open('airplane.png')
#airplaneBasewidth=500
#wpercent=(airplaneBasewidth/float(airplaneImage.size[0]))
#hsize=int((float(airplaneImage.size[1])*float(wpercent)))
#airplaneImage = airplaneImage.resize((airplaneBasewidth,hsize), Image.Resampling.LANCZOS)
#airplaneImage.save('airplane.png')
#airplaneImage = ImageTk.PhotoImage(airplaneImage)

#Load all plytoplankton images
basewidth = 175
codes = ["p1.png","p2.png", "p3.png", "p4.png", "p5.png", "p6.png", "p7.png", "p8.png", "p9.png"]
img_list = []
for i in codes:
    #Process the image and add to list
    img = processImage(i, 175)
    img_list.append(img)

#displays the airplane image
def airplaneImageCreate():
    airplaneImageLabel = tk.Label(master=airplane,image=airplaneImage,background='#BBD2EC')
    airplaneImageLabel.grid(row=1,column=0)

#creates the airplane display
def airplaneDisplayCreate(years):
    labelUpdater(airplaneCongrats,"Congrats Gardener!",0,airplane,'Courier 30 bold',21)
    airplaneImageCreate()
    message="That's equal to " + str(years) + " years of \n CO2 emissions from all planes"
    labelUpdater(airplaneMessage,message,2,airplane, "Courier 20 bold",31)

#Make 9x9 grid of phytoplanktons
def make_garden(numPlankton, img_list):
    count = 0
    for i in range(3):
        for j in range(3):
            if count < numPlankton:
                phyto = tk.Label(master=garden, image=img_list[count],background='#BBD2EC')
                phyto.grid(row=i,column=j)
            count += 1

#creates the display window
def change():
    number_of_plankton=sun+wind+nutrients
    years=3.9*number_of_plankton
    make_garden(number_of_plankton, img_list)
    airplaneDisplayCreate(years)
    pygame.mixer.init()
    sound = pygame.mixer.Sound("banjo.wav")
    pygame.mixer.Sound.play(sound)
    return

#instantiates the buttons in their frames
sun_high_button = button(sun_button_frame,sun_high, "high")
sun_low_button = button(sun_button_frame,sun_low, "low")
nutrients_high_button = button(nutrients_button_frame,nutrients_high, "high")
nutrients_low_button = button(nutrients_button_frame,nutrients_low, "low")
wind_high_button = button(wind_button_frame,wind_high, "high")
wind_low_button = button(wind_button_frame,wind_low, "low")
submit_button = button(submit_button_frame,change, 'Go!')
exit_button=button(exit_button_frame,exit,"Exit")

#creates the labels in their frames
sun_label =tk.Label(master = sun_label_frame,text='Sunlight', font ='Courier 25 bold',background='#FFFFCC',padx=78,pady=10)
sun_label.pack()
nutrients_label =tk.Label(master = nutrients_label_frame,text='Nutrients', font ='Courier 25 bold',background='#D0F0C0',padx=67,pady=10)
nutrients_label.pack()
wind_label =tk.Label(master = wind_label_frame,text='Wind', font ='Courier 25 bold',background='#CBC3E3',padx=118,pady=10)
wind_label.pack()

#create sound buttons
pygame.mixer.init()
musicOn = tk.Button(master=music_on_frame, image = musicImage, command=soundOn)
musicOn.pack(pady=20)
musicOff = tk.Button(master=music_off_frame, image = muteImage, command=soundOff)
musicOff.pack(pady=20)

#Play the music
pygame.mixer.music.load("plankton_tunes.mp3")
pygame.mixer.music.play(-1)

window.mainloop()