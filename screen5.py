import time

try:
    import Tkinter as tk
    from Tkinter import *
except ImportError:
    import tkinter as tk
    from tkinter import *

def tick(time1=''):
    time2 = time.strftime('%M:%S')

##
## WIND Angle
    windrenk = time.strftime('%S')
    windrenk = int(windrenk)
    if windrenk > 45:
        awa_label.config(fg='cyan')
    elif windrenk > 20:
        awa_label.config(fg='#bfbfbf')
    else: awa_label.config(fg='#a42121')
        
    if windrenk < 30:
      ctr_left.config(bg='green')
      ctr_right.config(bg='#1a1a1a')
    else:
      ctr_left.config(bg='#1a1a1a')
      ctr_right.config(bg='#a42121')

##
## RUDDER position
    if windrenk < 10:
        rudder_pos_x = ((windrenk * -12) +375)
        sog_label.config(text=rudder_pos_x)
        w.coords(rudder_pos, 375, 0, rudder_pos_x, 82)
        w.itemconfig(rudder_pos, fill="#9d9d9d")
    elif windrenk >= 10 and windrenk <= 20:
        rudder_pos_x = ((windrenk * -12) +375)
        sog_label.config(text=rudder_pos_x)
        w.coords(rudder_pos, 375, 0, rudder_pos_x, 82)
        w.itemconfig(rudder_pos, fill="#f7c16c")
    elif windrenk > 20 and windrenk < 30:
        rudder_pos_x = ((windrenk * -12) +375)
        sog_label.config(text=rudder_pos_x)
        w.coords(rudder_pos, 375, 0, rudder_pos_x, 82)
        w.itemconfig(rudder_pos, fill="#a42121")
    else:
        rudder_pos_x = ((windrenk -30) * 12) +425
        sog_label.config(text=rudder_pos_x)
        w.itemconfig(rudder_pos, fill="#9d9d9d")
        w.coords(rudder_pos, 425, 0, rudder_pos_x, 82)

    
## SAAT ayarları    
    if time2 != time1:
        time1 = time2
        clock_label.config(text=time2)
        clock_label.after(200, tick)

## Main Window
root = Tk()
root.title("Screen GUI")
root.overrideredirect(True)
root.geometry('800x1280-0+0')

## fontlar ##
Font208 = ('digiGA2', 156)
Font168 = ('digiGA2', 126)
Font104 = ('digiGA2', 78)

# create all of the main containers
awind_frame = Frame(root, bg='cyan', width=800, height=732, pady=0, padx=0)
twind_frame = Frame(root, bg='blue', width=800, height=200, padx=0, pady=0)
rudder_frame = Frame(root, bg='#656565', width=800, height=80, padx=0, pady=0)
info01_frame = Frame(root, bg='red', width=800, height=140, padx=0, pady=0)
info02_frame = Frame(root, bg='green', width=800, height=140, padx=0, pady=0) 

# layout all of the main containers
awind_frame.grid(row=0, sticky="ew")
twind_frame.grid(row=2, sticky="nsew")
rudder_frame.grid(row=1, sticky="ew")
info01_frame.grid(row=3, sticky="ew")
info02_frame.grid(row=4, sticky="ew")

# create the widgets for the awind_frame

ctr_left = Frame(awind_frame, bg='#1a1a1a', width=100, height=732)
ctr_mid = Frame(awind_frame, bg='black', width=600, height=732)
ctr_right = Frame(awind_frame, bg='red', width=100, height=732)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

# create the widgets for the awind_frame ctr_mid
awa_label = Label(ctr_mid, text='123', font=Font208, padx="20", pady="17", bg='black', fg='#bfbfbf')
awa_label.grid(row=0, column=0)

aws_label = Label(ctr_mid, text='21.7', font=Font208, padx="80", pady="16", bg='black', fg='white')
aws_label.grid(row=1, column=0)

sog_label = Label(ctr_mid, text='7.5', font=Font208, padx="0", pady="16", bg='black', fg='white')
sog_label.grid(row=2, column=0)

##
## create the FRAME for the TWIND
##

twind_left = Frame(twind_frame, bg='green')
twind_right = Frame(twind_frame, bg='green')

twind_left.grid(row=0, column=0, sticky="w")
twind_right.grid(row=0, column=1, sticky="e")


## create the WIDGETS for the TWIND
twa_label = Label(twind_left, text='112', font=Font168, padx="15", pady="14", bg='black', fg='#bfbfbf')
twa_label.grid(row=0, column=0)

tws_label = Label(twind_right, text='19.3', font=Font168, padx="39", pady="14", bg='black', fg='white')
tws_label.grid(row=0, column=1)

##
## create the WIDGETS for the RUDDER_FRAME
##
w = Canvas(rudder_frame, width=800, height=80, bg="beige", border="0")
w.grid(row=0,column=0)
w.pack()

w.create_rectangle(375, 0, 425, 82, fill="black", width=0)

rudder_pos_coords = (425, 0 , 525, 82)
rudder_pos = w.create_rectangle(425, 0 , 525, 82, fill="#9d9d9d", width=0)


##
## create the FRAME for the INFO01_FRAME
##

info01_left = Frame(info01_frame, bg='green')
info01_mid = Frame(info01_frame, bg='green')
info01_right = Frame(info01_frame, bg='red')

info01_left.grid(row=0, column=0, sticky="w")
info01_mid.grid(row=0, column=1, sticky="we")
info01_right.grid(row=0, column=2, sticky="e")

## create the WIDGETS for the INFO01_FRAME
clock_label = Label(info01_left, text='59:59', font=Font104, padx="10", pady="14", bg='black', fg='#e065ff')
clock_label.grid(row=0, column=0)

gps_label = Label(info01_mid, text='212', font=Font104, padx="22", pady="14", bg='black', fg='white')
gps_label.grid(row=0, column=1)

depth_label = Label(info01_right, text='04.3', font=Font104, padx="10", pady="14", bg='#a42121', fg='white')
depth_label.grid(row=0, column=2)

##
## create the FRAME for the INFO02_FRAME
##

info02_left = Frame(info02_frame, bg='green')
info02_mid = Frame(info02_frame, bg='green')
info02_right = Frame(info02_frame, bg='black')

info02_left.grid(row=0, column=0, sticky="w")
info02_mid.grid(row=0, column=1, sticky="ns")
info02_right.grid(row=0, column=2, sticky="w")

## create the WIDGETS for the INFO02_FRAME
volt_label = Label(info02_left, text='11.4', font=Font104, padx="11", pady="14", bg='#a42121', fg='white')
volt_label.grid(row=0, column=0)

ivme_label = Label(info02_mid, text='199', font=Font104, padx="55", pady="14", bg='black', fg='white')
ivme_label.grid(row=0, column=1)

SpeWind_label = Label(info02_right, text='99.9', font=Font104, padx="10", pady="14", bg='black', fg='#7529bb')
SpeWind_label.grid(row=0, column=2)

               
                 

clock_label.pack(fill='none', expand=0)
tick()
                 



root.mainloop()

