# The 2023 Winter Seminar of KIEES

<a href="https://imgbb.com/"><img src="https://i.ibb.co/ZzGK08w/image.png" alt="image" border="0"></a>

## Overview


The purpose of this project is to implement for auto-moobile function of safety.

This Reposit includes a code that implements the autonomous Advanced Driver Assistance System(ADAS) function for implementing motion control of RC car, including remote control and automatic movement. These codes will most likely not work unless they are in the Ubunto 18.04, ROS melodic framework, and we recommend that you use them in the same way, referring to the **Software Version** specified below.

**Hardware:** 

1:10 scale RC cars

* Computer : JetsonNano

* Servo control board : PCA9685, controlled viai2c

* Servos: CLS6336HV x1

* Esc: Hobbywing WF brushed esc 60A

* Battery: 2s 5200 mAh Lipo

* other: XL4015 dc-dc stepdown converter


**Software: C++,Python**

Software version :

* Jetpack 4.5.1

* OpenCV 4.5.1

* CUDA 10.0

* CUDNN 8.0

* Tensorflow 2.5.0

* Darknet yoloV4

* ROS Melodic

The repository consists of catkin_work space in the ROS Melodic environment of Ubuntu 18.04 on top of Jetson nano.

## Lane Following Assist(LFA)

Line detection is divided two part to Lane Detection and Lane Keeping. 

# Line detection
Image mask filters were manufactured and applied to vehicles to detect only lanes in camera image data. And I got the Trainging data set used Operataion driving of ROS flamework

<a href="https://imgbb.com/"><img src="https://i.ibb.co/8xpcBJZ/test-00031.png" alt="test-00031" border="0"></a>
Training data from cars with image mask applied




