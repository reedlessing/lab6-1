# Based on Tom Anastasio's habituationGWR.m
# this script sets up a very simple simulation of habituation
# of the Aplysia gill withdrawal reflex
#
# Modified for BU's RISE Practicum Comp Neuro lab by mbezaire@bu.edu

###############################
# import libraries with special
# functions needed in this script
###############################
import numpy as np
import matplotlib.pyplot as plt

###############################
# Define input stimulation
###############################
# TODO: Set a variable called stv to 4, this will define 
#        the weight of the connection from input to output
stv = 4

dec=.7 # set weight decrement for habituation

pls=[0, 0, 1, 0, 0] # set up a pulse

# TODO: then create a list of 6 pulses, called x, to use for input
x = pls*6 + [0]*10 + pls*6

v = stv # Set connection weight to start weight value

# NOT FINISHED: If T, allows model to stimulate the
# process of forgetting learned association
# forgetflag = True 

###############################
# Set up and run simulation
###############################

# TODO: Find the length of the input list (x)
#        and assign its value to a new variable, nTs
#        (which tracks the number of Time Steps)
nTs = len(x)

# TODO: Create a numpy array named y, a 1D vector
#        (row vector) padded with zeros, with one
#        element per each time step
y = np.zeros((1,nTs))

# TODO: use a for-loop to iterate 
#        through each time step in 
#        the input series and calculate
#        the output at each time step. Ex:
for t in range(nTs):  # t stands for time
    
#     then indent 4 spaces and write the equation that
#     describes how each input value in the vector x is 
#     transformed to the output value in the vector y
    y[0,t] = v*x[t]
    
# TODO: At each time step, check if the gill is receiving
#        stimulation and, if it is, cause the connection
#        weight to habituate (decrease)
    if x[t]>0: # some stimulation occured
        v *= dec # decrement weight

# forgetting the association if it doesn't happen for a while
    if t>3 and sum(x[t-4:t])==0 and v<stv: 
        v += (stv-v)*.05

###############################
# Plot the results
###############################

# Plot both the input series (vector x)
# and the resulting output series (vector y)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(x) #, color='white',  antialiased=False, edgecolors='black', linewidth=1, shade=False, alpha=1)
ax1.set_ylabel('Input')
ax1.set_xlim(0, nTs)
ax1.set_ylim(0, 1.1)

ax2 = fig.add_subplot(212)
ax2.plot(y[0]) #, color='white',  antialiased=False, edgecolors='black', linewidth=1, shade=False, alpha=1)
ax2.set_xlabel('Time step')
ax2.set_ylabel('Output')
ax2.set_xlim(0, nTs)
ax2.set_ylim(0, stv+0.5)

plt.show()
