#Import all neccessary libraries first are needed for Graphing Live

import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Import Time and Board features to get the ADS1115 working
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

# Everything from here has to do with making the Graph and have it Auto-Update
# Number of points to display along X axis, make this larger to show more Points.
x_len = 500

# Range of possible Y values to display, when using the gain value 16 this is a good maximum y_range for subtle movement.
#You can also adjust the viewing size of the graph in the live window
y_range = [-750, 750]  

# Create figure for plotting the LIVE Plot graph and some important variables
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

# Create a blank line variable. We will update the line in the LIVE animatation
line, = ax.plot(xs, ys)

# Add labels to the LIVE Graph Plot

plt.title('Geophone Data')
plt.xlabel('Data Points (Approximately 25 Readings each Second)')
plt.ylabel('Voltage Value Post Gain Adjustment')

# This function is called periodically from Function Animation
def animate(i, ys):

    #Value = ((chan.value))
    value = adc.read_adc_difference(0, gain=GAIN)

    # Add y to list - in this case we will plot the Gain adjusted Voltage Diferential Values
    ys.append(value)
    
    #Uncomment below to graph raw Voltage Differential Values instead (not gain adjusted)
    #ys.append(Volt)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=1,
    blit=True)
plt.show()
