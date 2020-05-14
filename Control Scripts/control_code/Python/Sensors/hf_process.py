import numpy as np

#ADD INPUTS HERE. Fix accordingly
#input hd_data
#Order of variables, 1D SS495A sensors, 3D MLX90393 (x,y,z) readings per sensor

hf_data=hf_data
num_1d=2   #Number of 1D analog sensors
num_3d=3   #Number of MLX90393 I2C sensors

#Convert 1D voltage readings to μT as per typical values from SS495A datasheet.
#Assuming a 5V input voltage.
#May need calibration to validate readings
for i in range(num_1d-1):
    hf_data[i]=np.interp(hf_data[i],[0.2,4.8],[-67000,67000])

return hf_data
#OUTPUT DATA
#output hf_data array of hall effect sensor data in μT units in an array.
