
#import adafruit_ads1x15.ads1115 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn
import datetime as dt
import numpy
import time
import tkinter as tk
import tkinter.font as tkFont
import threading
import time



#import board
#import busio
#import adafruit_mcp4725




#dac = adafruit_mcp4725.MCP4725(i2c)
#i2c = busio.I2C(board.SCL, board.SDA)

########Temperature settings###########
def set_temp():
     for temp in numpy.arange (0.0, float(final_temp.get())+.1, .1):
        if 100 < temp or temp < -1:
            print('Temperature not in range')
            print(temp)
            break
        temp_out = temp
        print(temp_out)
        time.sleep(.1)

##########Safety#############
#If pressure in the cell hits 0, the regulator will stop pumping in air.
def set_pressure_zero(chan_voltage):
    if chan_voltage == 0:
        dac.raw_output = 0

#############Feedback from Pressure regulator###################
def read_adc_input():
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)
    print(chan.value, chan.voltage)
    chan_voltage = chan.value

def set_pressure1():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi1 in numpy.arange(float(psi_initial1.get()), float(psi_final1.get()) + .1, float((psi_rate1.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi1 > 551 or psi1 < -1:
                print('not in range')
                break

            psi_scaled = (psi1 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi1)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)

    except:
        print('Failed')
        pass

def set_pressure2():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi2 in numpy.arange(float(psi_initial2.get()), float(psi_final2.get()) + .1, float((psi_rate2.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi2 > 551 or psi2 < -1:
                print('not in range')
                break

            psi_scaled = (psi2 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi2)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)

    except:
        pass


def set_pressure3():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi3 in numpy.arange(float(psi_initial3.get()), float(psi_final3.get()) + .1, float((psi_rate3.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi3 > 551 or psi3 < -1:
                print('not in range')
                break

            psi_scaled = (psi1 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi3)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)
    except:
        pass


def set_pressure4():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi4 in numpy.arange(float(psi_initial4.get()), float(psi_final4.get()) + .1, float((psi_rate4.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi4 > 551 or psi4 < -1:
                print('not in range')
                break

            psi_scaled = (psi4 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi4)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)
    except:
        pass


def set_pressure5():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi5 in numpy.arange(float(psi_initial5.get()), float(psi_final5.get()) + .1, float((psi_rate5.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi5 > 551 or psi5 < -1:
                print('not in range')
                break
            psi_scaled = (psi5 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi5)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)
    except:
        pass


def set_pressure6():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi6 in numpy.arange(float(psi_initial6.get()), float(psi_final6.get()) + .1, float((psi_rate6.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi6 > 551 or psi6 < -1:
                print('not in range')
                break
            psi_scaled = (psi6 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi6)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)
    except:
        pass


def set_pressure7():
    # for loop sarting at initial value, ending at final value. goiing up at a specified rate
    try:
        for psi7 in numpy.arange(float(psi_initial7.get()), float(psi_final7.get()) + .1, float((psi_rate7.get()))):
            # the initial Psi value desired will scale to a value readable by the pi
            if psi7 > 551 or psi7 < -1:
                print('not in range')
                break
            psi_scaled = (psi7 * 409.5 / 50)
            # dac.raw_output = psi_scaled
            print(psi7)
            # print (dac.raw_output)
            print(psi_scaled)
            # per minute
            time.sleep(.5)
    except Exception as e:
        print(e)
        pass


def set_pressure(wait_times, stop_threads):
#make list of all set pressure functions and wait times#
    commands = [
        (set_pressure1, wait_times[0]),
        (set_pressure2, wait_times[1]),
        (set_pressure3, wait_times[2]),
        (set_pressure4, wait_times[3]),
        (set_pressure5, wait_times[4]),
        (set_pressure6, wait_times[5]),
        (set_pressure7, wait_times[6]),
    ]

    while not stop_threads: #stop_threads[0]:
        print('Going', stop_threads)
        time.sleep(1)
        for func, wait_time in commands: #making the Pressure hold at certain level
            if not stop_threads: #stop_threads[0]:
                func()
                time.sleep(wait_time)
    print('Gone')