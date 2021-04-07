import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

window = tk.Tk()
window.title("Generator PassWord")
window.geometry("1280x720")

# Label
lb = tk.Label(window , text = "App Tạo Mật Khẩu" , fg= 'red' , font= ("Arial" , 30))
lb.grid(column= 0 , row = 0)

# TextBox
txt = tk.Entry(window , width= 40 )
txt.grid(column= 0, row = 1)

def change():
    # lb.configure(text = "Hi ," + 'My name is Python and :  ' + txt.get() )
    # messagebox
    messagebox.showinfo("PassWord" , 'dang hoc nha ! ! !')
    return

# Button
btn = tk.Button(window , text= 'hello' , command= change )
btn.grid(column= 0 , row = 2)

# ComboBox
combo = Combobox(window)
combo['values'] = ('gt_1' , 'gt_2' , 'gt_3')
combo.current(0)
combo.grid(column = 0 , row = 3)

def change_1():
    lb.configure(text = "Hello :\t" + combo.get() )
    return
btn_1 = tk.Button(window , text= 'ComboBox' , command= change_1 )
btn_1.grid(column= 1 , row = 3)



window.mainloop()