import string
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

LETTERS = string.ascii_letters

NUMBERS = string.digits

punctuation = string.punctuation

# Hàm chức năng tạo mật khẩu
def password_generator(length = 8 , chu = False , so = False , ky_tu = False):
    chuoi = None
    if chu and so and ky_tu:
        chuoi = ''.join([ LETTERS , NUMBERS , punctuation ])

    elif (chu == True) and (so == True):

        chuoi = ''.join([ LETTERS , NUMBERS ])

    elif (chu == True) and (ky_tu == True):

        chuoi = ''.join([ LETTERS , punctuation ])

    elif (so == True) and (ky_tu == True):

        chuoi = ''.join([ NUMBERS , punctuation ])

    elif chu:

        chuoi = f'{LETTERS}'

    elif so:

        chuoi = f'{NUMBERS}'

    elif ky_tu:

        chuoi = f'{punctuation}'

    else:
        chuoi = f'{LETTERS}{NUMBERS}{punctuation}'


    # chuyen sang []
    chuoi = list(chuoi)
    random.shuffle(chuoi)

    random_password = random.choices(chuoi , k= length)
    random_password = ''.join(random_password)

    return str(random_password)
# hàm lấy trạng thái checkBox
def get_check_box(a):
    if a == 0:
        return False
    elif a == 1:
        return True
# hàm kiểm tra nhập số
def validation(txt):
    if str(txt).isdigit():
        return int(str(txt) )
    else:
        # messagebox
        messagebox.showinfo("Thông Báo" , 'Phải nhập số !!!' )
        return 0

# Tạo giao diện
window = Tk()
window.title("Generator PassWord")
# window.geometry("1280x720")

# Label
lb = tk.Label(window , text = "App Tạo Mật Khẩu" , fg= 'red' , font= ("Arial" , 30))
lb.grid(column= 1 , row = 0)

# Label
lb_2 = tk.Label(window , text = "Nhập độ dài mật khẩu " , fg= 'green' , font= ("Arial" , 14))
lb_2.grid(column= 1 , row = 1)

# Entry ( ô nhập )
txt = tk.Entry(window , width= 40 , font= ('Arial' , 16) )
txt.grid(column= 1, row = 2)

v = tk.StringVar()
def setText(word):
    v.set(word)

txt_2 = tk.Entry(window , width= 40 , font= ('Arial' , 16) ,textvariable= v , fg = 'blue')
txt_2.grid(column= 1 , row = 9)

# var là biến giúp ta lấy trạng thái checkBox
var = tk.IntVar()
c1 = tk.Checkbutton(window, text='Chữ' , variable=var , font = ('Arial' , 15) )
c1.grid(column= 1 , row = 4)

var_2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='Số' , variable=var_2 , font = ('Arial' , 15) )
c2.grid(column = 1 , row = 5)

var_3 = tk.IntVar()
c3 = tk.Checkbutton(window, text='Ký Tự' , font = ('Arial' , 15) , variable=var_3 )
c3.grid(column = 1 , row = 6)

def create():
    global txt
    # lb.configure(text = "Hi ," + 'My name is Python and :  ' + txt.get() )
    # messagebox
    # messagebox.showinfo("PassWord" , 'Độ dài Mật Khẩu :  ' + get_check_box(var.get()) )
    try:
        chu = get_check_box(var.get())

        so = get_check_box(var_2.get())

        ky_tu = get_check_box(var_3.get())

        text = password_generator( int(validation(txt.get())), chu=chu, so=so, ky_tu=ky_tu)

        setText(text)
    except Exception as ex:
        print(ex)
    return

# Button
btn_Create_password = tk.Button(window , text= 'Tạo Mật Khẩu' , command= create , font = ('Arial' , 14) )
btn_Create_password.grid(column= 1 , row = 7)

def create_2():
    global txt , lb_2
    # lb.configure(text = "Hi ," + 'My name is Python and :  ' + txt.get() )
    # messagebox
    # messagebox.showinfo("PassWord" , 'Độ dài Mật Khẩu :  ' + txt.get() )
    chu = get_check_box( var.get() )

    so = get_check_box( var_2.get() )

    ky_tu = get_check_box( var_3.get() )

    text = password_generator(random.randint(5 , 20) , chu= chu , so= so , ky_tu= ky_tu )

    setText(text)
    return

# Button
btn_Create_password_random = tk.Button(window , text= 'Tạo Mật Khẩu Ngẫu Ngiên' , command= create_2 , font = ('Arial' , 14) )
btn_Create_password_random.grid(column= 1 , row = 8)

window.mainloop()