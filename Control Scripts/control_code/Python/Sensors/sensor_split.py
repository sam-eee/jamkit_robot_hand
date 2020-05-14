import numpy as np

#ADD INPUTS HERE. Fix accordingly
#Order of variables, Rotational potentiometers, 1D SS495A sensors, 3D MLX90393 
sensor_raw=sensor_data_arr     #RAW SENSOR INPUT sensor_data_arr from sensor_process.py

num_rot=16 #Number of rotational potentiometers
num_1d=2   #Number of 1D analog sensors
num_3d=3   #Number of MLX90393 I2C sensors



rot_data=sensor_raw[0:num_rot-1]    #rotational potentiometer data
hf_data=sensor_raw[num_rot:len(sensor_raw)-1] #1D then 3D hall effect sensors

return(rot_data,hf_data)
#OUTPUT DATA
#rot_data to rot_process.py
#hf_data to hf_process.py