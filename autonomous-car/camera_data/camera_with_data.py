from re import S
import cv2 
import time
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import load_model #


def img_preprocess(frame):
    height , _, _=frame.shape
    save_image = frame[int(height/2):,:,:]  
    save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV) 
    save_image =cv2.GaussianBlur(save_image ,(3,3),0)
    save_image = cv2.resize(save_image, (200, 66))
    save_image = save_image/255
    
    return save_image


def main():
    camera=cv2.VideoCapture('/home/yongs/Downloads/IMG_0074.MOV')
    camera.set(4,1024)
    camera.set(3,768)

    model_path = '/home/yongs/2lab/data/lane_navigation_final.h5'
    model = load_model(model_path)


    while (camera.isOpened()):

        keyValue = cv2.waitKey(1)
        

        
        ret,frame=camera.read() 
        frame = cv2.flip(frame,1)
        cv2.imshow('original',frame)
        
        preprocessed = img_preprocess(frame)

        cv2.imshow('pre',preprocessed)

        X = np.asarray([preprocessed])
        steering_angle= int(model.predict(X)[0]) -24
        print("predict angle: ", steering_angle)

        if cv2.waitKey(1) ==ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
