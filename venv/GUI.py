
#import adafruit_ads1x15.ads1115 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn

import datetime as dt
import numpy
import time
import tkinter as tk
import tkinter.font as tkFont
import threading
import time
import PressureGaugeSet
#import board
#import busio
#import adafruit_mcp4725

# Main script

# Create the main window
root = tk.Tk()
root.title("PROTO")

#global variables
stop_threads = False
t1 = threading.Thread()
chan_voltage = None
emerg_stop = False
temp = float

#pressure variables
psi1 = tk.StringVar()
psi2 = tk.StringVar()
psi3 = tk.StringVar()
psi4 = tk.StringVar()
psi5 = tk.StringVar()
psi6 = tk.StringVar()
psi7 = tk.StringVar()

psi_initial1 = tk.StringVar()
psi_initial2 = tk.StringVar()
psi_initial3 = tk.StringVar()
psi_initial4 = tk.StringVar()
psi_initial5 = tk.StringVar()
psi_initial6 = tk.StringVar()
psi_initial7 = tk.StringVar()
psi_final1 = tk.StringVar()
psi_final2 = tk.StringVar()
psi_final3 = tk.StringVar()
psi_final4 = tk.StringVar()
psi_final5 = tk.StringVar()
psi_final6 = tk.StringVar()
psi_final7 = tk.StringVar()
psi_rate1 = tk.StringVar()
psi_rate2 = tk.StringVar()
psi_rate3 = tk.StringVar()
psi_rate4 = tk.StringVar()
psi_rate5 = tk.StringVar()
psi_rate6 = tk.StringVar()
psi_rate7 = tk.StringVar()
wait_time1 = tk.StringVar()
wait_time2 = tk.StringVar()
wait_time3 = tk.StringVar()
wait_time4 = tk.StringVar()
wait_time5 = tk.StringVar()
wait_time6 = tk.StringVar()
wait_time7 = tk.StringVar()



final_temp = tk.StringVar()
#declare global variables
fullscreen = False
font = None
frame = tk.StringVar()

# Create the main container
frame = tk.Frame(root)

# Lay out the main container (expand to fit window)
frame.pack(fill=tk.BOTH, expand=3)

# Create dynamic font for text
dfont = tkFont.Font(size=-10)

#font variables
large_font = ('Verdana',30)
small_font = ('Verdana',10)
#quit program before ending


# Create widgets for pressure
label_pressure_rate = tk.Label(frame, text="Rate in Psi: ", font=dfont)
label_pressure_title = tk.Label(frame, text="Pressure(Psi):", font=dfont)
label_pressure_reading = tk.Label(frame,textvariable = chan_voltage, font=dfont)
label_pressure_reading_title = tk.Label(frame, text="Pressure reading:", font=dfont)
label_pressure_initial  = tk.Label(frame, text="Initial:", font=dfont)
label_pressure_final = tk.Label(frame, text="Final:", font=dfont)

entry_pressure_initial1 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial1)
entry_pressure_initial2 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial2)
entry_pressure_initial3 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial3)
entry_pressure_initial4 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial4)
entry_pressure_initial5 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial5)
entry_pressure_initial6 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial6)
entry_pressure_initial7 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_initial7)

entry_pressure_final1 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final1)
entry_pressure_final2 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final2)
entry_pressure_final3 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final3)
entry_pressure_final4 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final4)
entry_pressure_final5 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final5)
entry_pressure_final6 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final6)
entry_pressure_final7 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_final7)


entry_pressure_rate1 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate1)
entry_pressure_rate2 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate2)
entry_pressure_rate3 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate3)
entry_pressure_rate4 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate4)
entry_pressure_rate5 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate5)
entry_pressure_rate6 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate6)
entry_pressure_rate7 = tk.Entry(frame, width=7, font = dfont, textvariable = psi_rate7)

entry_wait1 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time1)
entry_wait2 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time2)
entry_wait3 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time3)
entry_wait4 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time4)
entry_wait5 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time5)
entry_wait6 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time6)
entry_wait7 = tk.Entry(frame, width=7, font = dfont, textvariable = wait_time7)


#########pressure settings#########
def main_thread():
    global stop_threads, t1
    wait_times = [
        float(wait_time1.get()),
        float(wait_time2.get()),
        float(wait_time3.get()),
        float(wait_time4.get()),
        float(wait_time5.get()),
        float(wait_time6.get()),
        float(wait_time7.get()),
    ]
    t1 = threading.Thread(target=PressureGaugeSet.set_pressure, args=(wait_times, stop_threads))
    t1.start()

def stop_main_thread(): #stop the set_pressure function
    global stop_threads, t1
    stop_threads = True
    print(stop_threads)
    t1.join()
    print('Thread Killed')

button_set_pressure = tk.Button(frame, text="Set Pressure", font = dfont, command = main_thread)
button_stop_thread = tk.Button(frame, text="Stop", font = dfont, command = stop_main_thread)

# create temp widgets
label_temp = tk.Label(frame, text="Temperature:", font=dfont)
label_to_widget = tk.Label(frame, text="to", font=dfont)
entry_temperature_initial = tk.Entry(frame, textvariable = final_temp, width=7, font = dfont)
label_current_temp = tk.Label(frame, text = "Temperature(°C)", font=dfont)
label_current_temp_reading = tk.Label(frame, font=dfont)

label_wait = tk.Label(frame, width=7, font = dfont, text="Hold(s)")

button_quit = tk.Button(frame, text="Quit", font=dfont, command=root.destroy)
button_set_temp = tk.Button(frame,command = PressureGaugeSet.set_temp, text="Set temp", font = dfont)

# Lay out widgets for temp
label_wait.grid(row=1, column=5, padx=0, pady=5)
label_temp.grid(row=0, column=0, padx=0, pady=5)
label_current_temp_reading.grid(row=0, column=5, padx=0, pady=5)
label_current_temp.grid(row=0, column=4, padx=0, pady=5)
entry_temperature_initial.grid(row=0, column=2, padx=0, pady=5)
button_set_temp.grid(row=0, column=3, padx=5, pady=5)

# Lay out widgets for pressure
label_pressure_rate.grid(row=1, column=4, padx=5, pady=5)
label_pressure_title.grid(row=1, column=0, padx=0, pady=5)
label_pressure_reading.grid(row=3, column=0, padx=5, pady=5)
label_pressure_reading_title.grid(row=2, column=0, padx=5, pady=5)
label_pressure_initial.grid(row=1, column=2, padx=0, pady=5)
label_pressure_final.grid(row=1, column=3, padx=0, pady=5)


entry_wait1.grid(row=2, column=5, padx=0, pady=5)
entry_wait2.grid(row=3, column=5, padx=0, pady=5)
entry_wait3.grid(row=4, column=5, padx=0, pady=5)
entry_wait4.grid(row=5, column=5, padx=0, pady=5)
entry_wait5.grid(row=6, column=5, padx=0, pady=5)
entry_wait6.grid(row=7, column=5, padx=0, pady=5)
entry_wait7.grid(row=8, column=5, padx=0, pady=5)

entry_pressure_rate1.grid(row=2, column=4, padx=0, pady=5)
entry_pressure_rate2.grid(row=3, column=4, padx=0, pady=5)
entry_pressure_rate3.grid(row=4, column=4, padx=0, pady=5)
entry_pressure_rate4.grid(row=5, column=4, padx=0, pady=5)
entry_pressure_rate5.grid(row=6, column=4, padx=0, pady=5)
entry_pressure_rate6.grid(row=7, column=4, padx=0, pady=5)
entry_pressure_rate7.grid(row=8, column=4, padx=0, pady=5)

entry_pressure_initial1.grid(row=2, column=2, padx=0, pady=5)
entry_pressure_initial2.grid(row=3, column=2, padx=0, pady=5)
entry_pressure_initial3.grid(row=4, column=2, padx=0, pady=5)
entry_pressure_initial4.grid(row=5, column=2, padx=0, pady=5)
entry_pressure_initial5.grid(row=6, column=2, padx=0, pady=5)
entry_pressure_initial6.grid(row=7, column=2, padx=0, pady=5)
entry_pressure_initial7.grid(row=8, column=2, padx=0, pady=5)

entry_pressure_final1.grid(row=2, column=3, padx=0, pady=5)
entry_pressure_final2.grid(row=3, column=3, padx=0, pady=5)
entry_pressure_final3.grid(row=4, column=3, padx=0, pady=5)
entry_pressure_final4.grid(row=5, column=3, padx=0, pady=5)
entry_pressure_final5.grid(row=6, column=3, padx=0, pady=5)
entry_pressure_final6.grid(row=7, column=3, padx=0, pady=5)
entry_pressure_final7.grid(row=8, column=3, padx=0, pady=5)

button_set_pressure.grid(row=4, column=0, padx=5, pady=5)
button_stop_thread.grid(row=6, column = 0)

#Misc button and label layout
button_quit.grid(row=9, column=5, padx=5, pady=5)

# Make it so that the grid cells expand out to fill window
for i in range(0,10):
    frame.rowconfigure(i, weight=5)
for i in range(0, 7):
    frame.columnconfigure(i, weight=5)

# Lay out the main container (expand to fit window)
frame.pack(fill=tk.BOTH, expand=1)

# Toggle fullscreen
def toggle_fullscreen(event=None):
    global root
    global fullscreen

    # Toggle between fullscreen and windowed modes
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    resize()
def resize(event=None):
    global dfont
    global frame

    # Resize font based on frame height (minimum size of 12)
    # Use negative number for "pixels" instead of "points"
    new_size = -max(12, int((frame.winfo_height() / 20)))
    dfont.configure(size=new_size)

def end_fullscreen(event=None):
    global root
    global fullscreen

    # Turn off fullscreen mode
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize()


# Bind F11 to toggle fullscreen and ESC to end fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)
root.bind('<s>', stop_main_thread)

# Have the resize() function be called every time the window is resized
root.bind('<Configure>', resize)
root.mainloop()
##########Threading##########






