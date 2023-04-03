#import all necessary functionality to the Script
import time
import Adafruit_ADS1x15

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

#Create a aribitary counter which will be used for the looping section
Start = 0

#Create a name for the Text file that we will write to. Keep in mind this file will be overwritten
#Each time this script is run.
f = open('Geophone_Data.txt','w')

#We will use this as a small counter to determine how long it took to recieve all the data points
t0 = time.time()

#If you want the script to run for a whole day this will enable that to happen
t_end = time.time() + (60 * 60 * 24)

#This is a looping section that will take the data from the ADC as fast as python will let it. Adjust the 100 to larger values to record longer time.
#System runs at approximately 25 readings per second. Note -If you do not print data to the shell this will go much faster.

#while (Start < 100):

#To do a whole day (24hours) of recording data you would want to Comment out the above While Loop and Uncomment the Below Loop
while (time.time() < t_end):
    
    # Read the difference between channel 0 and 1 (i.e. channel 0 minus channel 1).
    # Note you can change the differential value to the following:
    #  - 0 = Channel 0 minus channel 1
    #  - 1 = Channel 0 minus channel 3
    #  - 2 = Channel 1 minus channel 3
    #  - 3 = Channel 2 minus channel 3
    value = adc.read_adc_difference(0, gain=GAIN)
    # Note you can also pass an optional data_rate parameter above, see
    # simpletest.py and the read_adc function for more information.
    # Value will be a signed 12 or 16 bit integer value (depending on the ADC
    # precision, ADS1015 = 12-bit or ADS1115 = 16-bit).
    f.write(str((value))+'\n')
    
    #Add one to the counter
    Start = Start + 1
    
    print('Channel 0 minus 1: {0}'.format(value))
    # Pause for half a second.
    
    
#As soon as the loop is complete the total time taken for looping to complete is determined and recorded
t1=time.time()
total= t1-t0

#This time is then printed to shell.
print('This is the time in seconds it took to complete data collection '+ str(total))

#This is to finalise the text file manipulations. Once below happens nothing will alter the text file.
f.close()
        