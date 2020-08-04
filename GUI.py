
#import adafruit_ads1x15.ads1115 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn
import numpy
import time
import tkinter as tk
import tkinter.font as tkFont
from pynput import keyboard
#import board
#import busio
#import adafruit_mcp4725

# Main script

# Create the main window
root = tk.Tk()
root.title("PROTO")

# Start in fullscreen mode and run



#declare global variables

font = None
frame = None
#pressure variables
psi = tk.StringVar()
psi_initial = tk.StringVar()
psi_final = tk.StringVar()
psi_rate = tk.StringVar()
#dac = adafruit_mcp4725.MCP4725(i2c)
#i2c = busio.I2C(board.SCL, board.SDA)



#temp variables
temp_initial = None
temp_final = None
fullscreen = False
chan_voltage = None
temp_rate = float

# Create the main container
frame = tk.Frame(root)

# Lay out the main container (expand to fit window)
frame.pack(fill=tk.BOTH, expand=1)

# Variables for holding temperature and light data
#temp_c = tk.DoubleVar()
#lux = tk.DoubleVar()

# Create dynamic font for text
dfont = tkFont.Font(size=-10)

#font variables
large_font = ('Verdana',30)
small_font = ('Verdana',10)
#quit program before ending

#########temp and pressure settings#########
def set_pressure():
    #for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi in numpy.arange(float(psi_initial.get()), float(psi_final.get()), float(psi_rate.get())):
            #the initial Psi value desired will scale to a value readable by the pi
            psi_scaled = (psi*409.5/50)
            #dac.raw_output = psi_scaled
            print(psi)
            #print (dac.raw_output)
            print (psi_scaled)
            #per minute
            time.sleep(5)

    except:
        pass
        print('failed')

# Create widgets for pressure
label_pressure_rate = tk.Label(frame, text="Rate in Psi: ", font=dfont)
label_presure_title = tk.Label(frame, text="Pressure:", font=dfont)
label_pressure = tk.Label(frame,textvariable = chan_voltage, font=dfont)
label_unit_pressure = tk.Label(frame, text="Psi", font=dfont)
entry_pressure_initial = tk.Entry(frame, width=5, font = dfont, textvariable = psi_initial)
entry_pressure_final = tk.Entry(frame, width=5, font = dfont, textvariable = psi_final)
entry_pressure_rate = tk.Entry(frame, width=5, font = dfont, textvariable = psi_rate)
button_set_pressure = tk.Button(frame, text="Go", font = dfont, command = set_pressure)
#button_set_pressure.bind('set_pressure',set_pressure(psi_rate,psi_final,psi_rate))
#button_set_pressure['command'] = set_pressure(psi_initial,psi_final,psi_rate)

# create temp widgets
label_temp = tk.Label(frame, text="Temperature:", font=dfont)
label_unit_temp = tk.Label(frame, text="°C", font=dfont)
label_to_widget = tk.Label(frame, text="to", font=dfont)
label_temp_rate = tk.Label(frame, text="Rate in °C: ", font=dfont)
label_to_widget1 = tk.Label(frame, text="to", font=dfont)
entry_temp_rate = tk.Entry(frame, width=5, font = dfont)
entry_temperature_initial = tk.Entry(frame, width=5, font = dfont)
entry_temperature_final = tk.Entry(frame, width=5, font = dfont)

button_quit = tk.Button(frame, text="Quit", font=dfont, command=root.destroy)
button_set_temp = tk.Button(frame, text="Go", font = dfont)


# Lay out widgets for temp
label_temp.grid(row=0, column=0, padx=0, pady=5, sticky=tk.E)
label_to_widget1.grid(row=0, column=2, padx=0, pady=5)
label_unit_temp.grid(row=0, column=4, padx=20, pady=5, sticky=tk.W)
entry_temp_rate.grid(row=1, column=1, padx=0, pady=5, sticky=tk.E)
entry_temperature_initial.grid(row=0, column=1, padx=0, pady=5, sticky=tk.E)
entry_temperature_final.grid(row=0, column=3, padx=0, pady=5, sticky=tk.E)
button_set_temp.grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)
label_temp_rate.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

# Lay out widgets for pressure
label_pressure_rate.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
label_to_widget.grid(row=2, column=2, padx=0, pady=5)
label_presure_title.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
label_pressure.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
label_unit_pressure.grid(row=2, column=4, padx=20, pady=5, sticky=tk.W)
entry_pressure_rate.grid(row=3, column=1, padx=0, pady=5, sticky=tk.W)
entry_pressure_initial.grid(row=2, column=1, padx=0, pady=5, sticky=tk.W)
entry_pressure_final.grid(row=2, column=3, padx=0, pady=5, sticky=tk.W)
button_set_pressure.grid(row=2, column=5, padx=5, pady=5, sticky=tk.W)

#Misc button and label layout
button_quit.grid(row=3, column=5, padx=5, pady=5)

# Make it so that the grid cells expand out to fill window
for i in range(0,3):
    frame.rowconfigure(i, weight=5)
for i in range(0, 7):
    frame.columnconfigure(i, weight=5)


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
    new_size = -max(12, int((frame.winfo_height() / 10)))
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

# Have the resize() function be called every time the window is resized
root.bind('<Configure>', resize)

# Schedule the poll() function to be called periodically
#root.after(500, poll)

def read_adc_input():
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)
    print(chan.value, chan.voltage)
    chan_voltage = chan.value

#run GUI
root.mainloop()






