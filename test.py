from tkinter import *
import tkinter
from tkinter import messagebox
import cv2
import PIL.Image , PIL.ImageTk
from time import sleep
from threading import Thread

windows = Tk()
windows.title("Tkinter Open CV")

video = cv2.VideoCapture(0)

canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)
canvas_H = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
canvas = Canvas(windows , width = canvas_w , height= canvas_H , bg= 'red')
canvas.pack()

bw = 0
def change_b_w():
    global bw
    bw = 1 - bw

def send_to_server():
    global btn
    sleep(10)
    btn.configure(text = "Nguyen Van A")
    return

count = 0
photo = None

def update_Frame():
    global canvas , photo , bw , count
    # doc tu camera
    ret , frame = video.read()
    #  resize anh
    # frame = cv2.resize(frame , dsize= None , fx= 0.5 , fy= 0.5)
    # chuyen he mau
    if bw == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # convert Image TK
    photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame) )
    #  show
    canvas.create_image(0 , 0 , image= photo , anchor= tkinter.NW)
    windows.after(15 , update_Frame )

    count += 1
    if count % 10 ==0:
        # send_to_server()
        thread = Thread(target= send_to_server )
        thread.start()

update_Frame()

btn = Button(windows , text='black and white' , command = change_b_w )
btn.pack()

windows.mainloop()

