import time
# Again we import the necessary socket python module
import socket
# Here we define the UDP IP address as well as the port number that we have 
# already defined in the client python script.
UDP_IP_ADDRESS = ""
UDP_PORT_NO = 10110

# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

###### MPU6560 data starts #####
from sense_emu import SenseHat
OrjYa = 40.0
OrjYb = 40.0
OrjXY = 40.0

Xgyro = 0.0
Ygyro = 0.0

xAcce_val = 0.0

sense = SenseHat()
sense.clear()

###### MPU6560 data ends #######

try:
    import Tkinter as tk
    from Tkinter import *
except ImportError:
    import tkinter as tk
    from tkinter import *

def blink_cer(cer_name):
   blinkTime = time.strftime('%S')
   blinkTime2 = (int(float(blinkTime)) / 2.0)
   if (blinkTime2 ** (1.0/3)).is_integer():
       (cer_name).config(fg='#a42121', bg='yellow')
   else:
       (cer_name).config(fg='yellow', bg='#a42121')


def rightClick(event): sys.exit()

########## MAIN SCREEN starts ##############

## Main Window
root = Tk()
root.title("Screen GUI")
root.overrideredirect(True)
root.geometry('800x1280-0-0')

## fontlar ##
Font208 = ('digiGA2', 156)
Font168 = ('digiGA2', 126)
Font104 = ('digiGA2', 78)

##
## create all of the main containers
awind_frame = Frame(root, bg='cyan', width=800, height=732, pady=0, padx=0)
twind_frame = Frame(root, bg='blue', width=800, height=200, padx=0, pady=0)
rudder_frame = Frame(root, bg='#656565', width=800, height=88, padx=0, pady=0)
info01_frame = Frame(root, bg='red', width=800, height=130, padx=0, pady=0)
info02_frame = Frame(root, bg='green', width=800, height=130, padx=0, pady=0) 

##
## layout all of the main containers
awind_frame.grid(row=0, sticky="ew")
twind_frame.grid(row=1, sticky="nsew")
rudder_frame.grid(row=2, sticky="ew")
info01_frame.grid(row=3, sticky="w")
info02_frame.grid(row=4, sticky="ew")

##
## create the WIDGETS for the awind_frame
ctr_left = Frame(awind_frame, bg='#1a1a1a', width=100, height=732)
ctr_mid = Frame(awind_frame, bg='black', width=600, height=732)
ctr_right = Frame(awind_frame, bg='#d32f2f', width=100, height=732)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

##
## create the WIDGETS for the awind_frame ctr_mid
awa_cer = Frame(ctr_mid, width=600, height=244)
awa_cer.pack_propagate(0)
awa_cer.pack(side = TOP)
awa_label = Label(awa_cer, anchor="e", text='999', font=Font208, padx="85", pady="17", bg='black', fg='#c6c6c6')
awa_label.pack(fill=BOTH, expand=1)

aws_cer = Frame(ctr_mid, width=600, height=244)
aws_cer.pack_propagate(0)
aws_cer.pack(side = TOP)
aws_label = Label(aws_cer, anchor="e", text='999', font=Font208, padx="85", pady="16", bg='black', fg='white')
aws_label.pack(fill=BOTH, expand=1)

sog_cer = Frame(ctr_mid, width=600, height=244)
sog_cer.pack_propagate(0)
sog_cer.pack(side = TOP)
sog_label = Label(sog_cer, anchor="e", text='9.9', font=Font208, padx="85", pady="17", bg='black', fg='#ffffff')
sog_label.bind('<Button-3>', rightClick)
sog_label.pack(fill=BOTH, expand=1)

##
## create the WIDGETS for the TWIND
twa_cer = Frame(twind_frame, width=375, height=200)
twa_cer.pack_propagate(0)
twa_cer.pack(side = LEFT)
twa_label = Label(twa_cer, anchor="e", text='999', font=Font168, padx="15", pady="14", bg='black', fg='#9f9f9f')
twa_label.pack(fill=BOTH, expand=1)

tws_cer = Frame(twind_frame, width=425, height=200)
tws_cer.pack_propagate(0)
tws_cer.pack(side = LEFT)
tws_label = Label(tws_cer, anchor="e", text='99.9', font=Font168, padx="25", pady="14", bg='black', fg='#9f9f9f')
tws_label.pack(fill=BOTH, expand=1)

##
## create the WIDGETS for the RUDDER_FRAME
w = Canvas(rudder_frame, width=800, height=88, bg="#7f7f7f")
w.pack_propagate(0)
w.pack(side = LEFT)

w.create_rectangle(325, 0, 475, 89, fill="#42a5f5", width=0)

earth_pos = w.create_polygon(325, OrjYa, 475, OrjYb, 475, 88, 325, 88, fill="#d32f2f", width=0)
rudder_pos = w.create_rectangle(475, 0 , 525, 89, fill="#b0b0b0", width=0)

##
## create the WIDGETS for the INFO01_FRAME
clock_cer = Frame(info01_frame, width=318, height=130)
clock_cer.pack_propagate(0)
clock_cer.pack(side = LEFT)
clock_label = Label(clock_cer, anchor="e", text='59:59', font=Font104, padx="15", pady="14", bg='black', fg='#90caf9')
clock_label.pack(fill=BOTH, expand=1)

gps_cer = Frame(info01_frame, width=237, height=130)
gps_cer.pack_propagate(0)
gps_cer.pack(side = LEFT)
gps_label = Label(gps_cer, anchor="e", text='999', font=Font104, padx="22", pady="14", bg='black', fg='white')
gps_label.pack(fill=BOTH, expand=1)

depth_cer = Frame(info01_frame, width=245, height=130)
depth_cer.pack_propagate(0)
depth_cer.pack(side = LEFT)
depth_label = Label(depth_cer, anchor="e", text='99.9', font=Font104, padx="15", pady="14", bg='#000000', fg='#9f9f9f')
depth_label.pack(fill=BOTH, expand=1)

##
## create the WIDGETS for the INFO02_FRAME
volt_cer = Frame(info02_frame, width=250, height=130)
volt_cer.pack_propagate(0)
volt_cer.pack(side = LEFT)
volt_label = Label(volt_cer, anchor="e", text='99.9', font=Font104, padx="15", pady="20", bg='#000000', fg='#9f9f9f')
volt_label.pack(fill=BOTH, expand=1)

ivme_cer = Frame(info02_frame, width=305, height=130)
ivme_cer.pack_propagate(0)
ivme_cer.pack(side = LEFT)
ivme_label = Label(ivme_cer, anchor="e", text='00', font=Font104, padx="55", pady="14", bg='black', fg='#9f9f9f')
ivme_label.pack(fill=BOTH, expand=1)

SpeWind_cer = Frame(info02_frame, width=245, height=130)
SpeWind_cer.pack_propagate(0)
SpeWind_cer.pack(side = LEFT)
SpeWind_label = Label(SpeWind_cer, anchor="e", text='99.9', font=Font104, padx="15", pady="14", bg='black', fg='#9f9f9f')
SpeWind_label.pack(fill=BOTH, expand=1)

root.update()

########### MAIN SCREEN ends ###############

############# SPLASH starts ################
splash = Tk()
splash.title("Screen GUI")
splash.overrideredirect(1)
splash.geometry('700x1180-50+50')
canvas = Canvas(splash,width=700,height=1180,bg="blue")
canvas.pack(expand=YES, fill=BOTH)
gif1 = PhotoImage(master = canvas, file='at.gif')
canvas.create_image((0, 0), image = gif1, state = "normal", anchor=NW)

splash.update()
splash.lift()

time.sleep(4)
splash.destroy()
############# SPLASH ends ################

while True:

    def rightClick(event): sys.exit()

# read RECEIVED data
    nmea_data, addr = serverSock.recvfrom(1024)
    nmea_header = nmea_data [3:6]
    nmea_data = str(nmea_data)
    print (nmea_data)

############# NMEA TYPES ################

# **HDT Heading true
    if nmea_header == b'HDT':
       a1,a2,a3 = nmea_data.split(',')
       a2=int(float(a2))
       gps_label.config(text=a2)

## **RSA RUDDER position
    if nmea_header == b'RSA':
       a1,a2,a3 = nmea_data.split(',')
       a2=int(float(a2))
       if a2 >= 60:
           rudder_pos_x = (a2 * 3.0) + 475
           w.coords(rudder_pos, 475, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#d32f2f")
       elif a2 >= 40:
           rudder_pos_x = (a2 * 3.0) + 475
           w.coords(rudder_pos, 475, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#ff5252")
       elif a2 >= 30:
           rudder_pos_x = (a2 * 3.0) + 475
           w.coords(rudder_pos, 475, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#c6c6c6")
       elif a2 >= 0:
           rudder_pos_x = (a2 * 3.0) + 475
           w.coords(rudder_pos, 475, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#9f9f9f")
       elif a2 >= -30:
           rudder_pos_x = (a2 * 3.0) + 325
           w.coords(rudder_pos, 325, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#9f9f9f")
       elif a2 >= -40:
           rudder_pos_x = (a2 * 3.0) + 325
           w.coords(rudder_pos, 325, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#c6c6c6")
       elif a2 >= -60:
           rudder_pos_x = (a2 * 3.0) + 325
           w.coords(rudder_pos, 325, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#ff5252")
       else:
           rudder_pos_x = (a2 * 3.0) + 325
           w.coords(rudder_pos, 325, 0, rudder_pos_x, 88)
           w.itemconfig(rudder_pos, fill="#d32f2f")

# **VTG speed over ground (SOG)
    if nmea_header == b'VTG':
       a1,a2,a3,a4,a5,a6,a7,a8,a9= nmea_data.split(',')
       a6="{0:.1f}".format(float(a6))
       sog_label.config(text=a6)
       if float(a6) > 9:
           sog_label.config(fg='#90caf9')
       else: sog_label.config(fg='white')

# WIMWV wind angle and speed
    if nmea_header == b'MWV':
       a1,a2,a3,a4,a5,a6 = nmea_data.split(',')
       a2=float(a2)
       if int(a2) > 180:
           ctr_left.config(bg='#52b848') # yesil
           ctr_right.config(bg='#1a1a1a')
           a2 = ((int(a2) - 360) * -1)
       else:
           ctr_left.config(bg='#1a1a1a')
           ctr_right.config(bg='#d32f2f') # kırmızı
       if a3 == 'R':
           awa_label.config(text=str(int(a2)))
           if a2 >= 130:
               awa_label.config(fg='#90caf9')
           elif a2 >= 29:
               awa_label.config(fg='#c6c6c6')
           elif a2 >= 23:
               awa_label.config(fg='#ff5252')
           else: awa_label.config(fg='#d32f2f')
           if a5 == 'K':
               a4_data = "{0:.1f}".format(float(a4) * 0.5399568034557235)
               aws_label.config(text=(a4_data))
           elif a5 == 'N':
               a4_data = a4
               aws_label.config(text=a4)
           else:
               a4_data = "{0:.1f}".format(float(a4) * 0.0005399568034557235)
               aws_label.config(text=str(a4_data))

           if float(a4_data) > 30:
               aws_label.config(fg='d32f2f', bg='b0b0b0')
               blink_cer(aws_label)
           elif float(a4_data) > 20:
               aws_label.config(fg='#ff5252', bg='black')
           elif float(a4_data) > 16:
               aws_label.config(fg='#ebe35e', bg='black')
           elif float(a4_data) > 4:
               aws_label.config(fg='white', bg='black')
           else: aws_label.config(fg='#90caf9', bg='black')

       else: # true wind
           twa_label.config(text=str(int(a2)))
           if a2 >= 130:
               twa_label.config(fg='#90caf9')
           elif a2 >= 29:
               twa_label.config(fg='#9f9f9f')
           elif a2 >= 23:
               twa_label.config(fg='#ff5252')
           else: twa_label.config(fg='#d32f2f')
           
           if a5 == 'K':
               a4_data = "{0:.1f}".format(float(a4) * 0.5399568034557235)
               tws_label.config(text=(a4_data))
           elif a5 == 'N':
               a4_data = a4
               tws_label.config(text=a4)
           else:
               a4_data = "{0:.1f}".format(float(a4) * 0.0005399568034557235)
               tws_label.config(text=str(a4_data))
               
           if float(a4_data) > 30:
               tws_label.config(fg='#d32f2f', bg='#b0b0b0')
               blink_cer(tws_label)
           elif float(a4_data) > 20:
               tws_label.config(fg='#ff5252', bg='black')
           elif float(a4_data) > 16:
               tws_label.config(fg='#ebe35e', bg='black')
           elif float(a4_data) > 4:
               tws_label.config(fg='#9f9f9f', bg='black')
           else: tws_label.config(fg='#90caf9', bg='black')

# **DPT Depth in meters
    if nmea_header == b'DPT':
       a1,a2,a3 = nmea_data.split(',')
       a2=float(a2)
       depth_label.config(text=a2)
       if int(a2) > 20:
           depth_label.config(fg='#7f7f7f', bg='black')
       elif int(a2) > 15:
           depth_label.config(fg='#9f9f9f', bg='black')
       elif int(a2) > 5:
           depth_label.config(fg='#c6c6c6', bg='black')
       elif int(a2) > 4:
           depth_label.config(fg='#ebe35e', bg='black')
       elif int(a2) > 3:
           depth_label.config(fg='#ff5252', bg='black')
       else:
           depth_label.config(fg='#d32f2f', bg='#b0b0b0')
           blink_cer(depth_label)

# **PWR Battery PowerxAcce_val
    if nmea_header == b'PWR':
       a1,a2,a3 = nmea_data.split(',')
       a2=float(a2)
       volt_label.config(text=a2)
       if int(a2) > 13:
           volt_label.config(fg='#7f7f7f', bg='black')
       elif int(a2) >= 12:
           volt_label.config(fg='#b0b0b0', bg='black')
       elif int(a2) >= 11.5:
           volt_label.config(fg='#ff5252', bg='black')
       else:
           volt_label.config(fg='#d32f2f', bg='#b0b0b0')
           blink_cer(volt_label)

# **ZDA Time & Date
    if nmea_header == b'ZDA':
       a1,a2,a3,a4,a5,a6,a7 = nmea_data.split(',')
       a2min = a2 [2:4]
       a2sec = a2 [4:6]
       a2time = a2min + ":" + a2sec
       clock_label.config(text = a2time)

##### MPU6560 progs START
    acceleration = sense.get_accelerometer_raw()
    xAcce = acceleration['x']

    o = sense.get_orientation()
    Gpitch = o["pitch"]
    Groll = o["roll"]
    
    if xAcce != xAcce_val:
        xAcce = int(xAcce * -100)
        ivme_label.config(text = xAcce)
        xAcce_val = xAcce
    else:
        xAcce = 0.0
        ivme_label.config(text = '00')

    if Gpitch <= 180.0:
        OrjXY = (Gpitch / 1.5)
        OrjYa = OrjXY + 40
        OrjYb = OrjXY + 40
        w.coords(earth_pos, 325, OrjYa, 475, OrjYb, 475, 88, 325, 88)
        w.itemconfig(earth_pos)
        w.update()
    elif Gpitch > 180.0:
        OrjXY = ((Gpitch - 360) / 1.5)
        OrjYa = OrjXY + 40
        OrjYb = OrjXY + 40
        w.coords(earth_pos, 325, OrjYa, 475, OrjYb, 475, 88, 325, 88)
        w.itemconfig(earth_pos)
        w.update()

    if Groll <= 180.0:
        OrjYa = OrjYa + Groll
        OrjYb = OrjYb - Groll
        w.coords(earth_pos, 325, OrjYa, 475, OrjYb, 475, 88, 325, 88)
        w.itemconfig(earth_pos)
        w.update()
    elif Groll > 180.0:
        Groll = (Groll - 360)
        OrjYa = OrjYa + Groll
        OrjYb = OrjYb - Groll
        w.coords(earth_pos, 325, OrjYa, 475, OrjYb, 475, 88, 325, 88)
        w.itemconfig(earth_pos)
        w.update()
##### MPU6560 progs ENDS


############# NMEA edit end #############################

#root.update()
root.mainloop()