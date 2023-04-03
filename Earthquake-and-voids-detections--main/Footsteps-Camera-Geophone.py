#import all necessary functionality to the Script
import time
import Adafruit_ADS1x15
import os

# Create an ADS1115 ADC (16-bit) instance. Note you can change the I2C address from its default (0x48) and/or bus number
#adc = Adafruit_ADS1x15.ADS1115()
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 16


#This is a looping section that will take the data from the ADC as fast as python will let it. Adjust the 100 to larger values to record longer time.
#System runs at approximately 25 readings per second. Note -If you do not print data to the shell this will go much faster. To do a whole day (24hours) you would want to use 2160000 as the value. |86400 seconds in 24 hours * 25 readings/second
while True:
    
    #Extract data from Geophone
    #Voltage = chan.voltage
    
    #obtain the Gain adjusted Voltage
    Value = adc.read_adc_difference(0, gain=GAIN)
    #print to shell the Gain adjusted voltage value if uncommented
    print(Value)
    
    #This is where the magic happens. If the value recieved is higher or lower than the threshold values below it will trigger this If statement to run
    #If you find this is too sensitive then increase the below values, say | Value > 500 or Value < -500: |
    if Value > 50 or Value < -50:
        
        #This IF statement will then use type the below terminal command into the terminal. This will take a quick photo of whatever it sees, give it a Date-Time Label and then continue the system. 
        os.system('sudo libcamera-still --datetime')

