import numpy as np

#ADD INPUTS HERE. Fix accordingly
#import rot_data
#Data is in order of ports on KA-12 shield from port 1.

rot_data=rot_data
num_rot=16

    #Defined KA-12 ports for rotational potentiometers, J1 is the base joint and
    #J2 is the middle joint and J3 is the fingertip joint:
    Little finger link joints: J1=1, J2=2, J3=3
    Ring finger link joints: J1=4, J2=5, J3=6
    Middle finger link joints: J1=7, J2=8, J3=9
    Index finger link joints: J1=10, J2=11, J3=12
    Thumb opposable joint: J1=13
    Thumb AA joint: J2=14
    Thumb link joints: J3=15, J4=16
        
#Guaranteed linearity is between +/- 160 degrees
#All link sensors for ROT 1 to 13 and 15 to 16 are orientated as defined when looking at the
#palmar side from fully extended (0 degree) to fully flexed (90 degree etc):
    #left side potentiometers output for L2 on all fingers; not including thumb
        #= -90 degree to 0 degree
    #right side potentiometers output for L1 and L3 on all fingers and 2 thumb
        #links = 90 degree to 0 degree
    
    #All 1-12 and 15-16 link rotational potentiometers are converted as they all start at
    #-90 degree or 90 degree as shown above, so the absolute values are 
    #the same as they approach 0 degree
    #The other 2 thumb potentiometers are dealt separately.
    
    #Joints have been designed to have a max displacement range of 90 degrees.
    #The displacement range will be controlled by testing and programming the AX-12 motors
    #Potentiometers do not travel greater than 90 degree from their
    #starting position while staying within the range of +/- 166.65 degrees.
    
for i in range(num_rot-5):
    rot_data[i]=90-abs(np.interp(rot_data[i],[0,5],[-166.65,166.65]))

for i in range(num_rot-2,num_rot-1):
    rot_data[i]=90-abs(np.interp(rot_data[i],[0,5],[-166.65,166.65]))


    #ROT 14 has a range of 60 degrees, from potentiometer readings of 30 degree to
    #-30 degree, mapped between 0 degree to 60 degree respectively.    
rot_data[num_rot-3]=30-np.interp(rot_data[i],[0,5],[-166.65,166.65])

    #ROT 13 has a range of 90 degrees, from potentiometer readings of 0 degree
    #to -90 degree, mapped between 0 degree to 90 degree respectively.
rot_data[num_rot-4]=abs(np.interp(rot_data[i],[0,5],[-166.65,166.65]))

#It has been configured such that all potentiometers; except the Thumb AA joint
#will output either all positive or negative angles that are then converted to their
#absolute values. A displacement range greater than 90 degrees is not required for 
#the desired functionality, so a more complicated solution involving both positive and minus
#values from a potentiometer was not required.

return rot_data
#OUTPUT rot_data array of potentiometer angles in an array.