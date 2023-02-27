#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String
import os
import cv2 
import time
import keyboard
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
 
sub= rospy.Subscriber('detect_inform', String,queue_size=1)


def callback(msg):

        print("Recieved object => ",format(msg.data))
        if msg.data == 'car':
            print("Car is detected" , end = "")
        return msg
	    


rospy.init_node('listen', anonymous=False)

sub= rospy.Subscriber('detect_inform', String,callback,queue_size=1)
time.sleep(0.1)


ros.spin()





		
