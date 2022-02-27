import RPi.GPIO as GPIO
from time import sleep
import atexit
import cv2
import numpy as np
import math

def tonum(num):  # 用于处理角度转换的函数
    fm = 10.0 / 180.0
    num = num * fm + 2.5
    num = int(num * 10) / 10.0
    return num

servopin1 = 20   #舵机1,方向为左右转
servopin2 = 21   #舵机2,方向为上下转
GPIO_TRIGGER = 23 #超声波控制
GPIO_ECHO = 24   #超声波反馈

GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
p1 = GPIO.PWM(servopin1,50) #50HZ
p2 = GPIO.PWM(servopin2,50) #50HZ

p1.start(tonum(95)) #初始化角度
p2.start(tonum(25)) #初始化角度
sleep(1)
p1.ChangeDutyCycle(0) #清除当前占空比，使舵机停止抖动
p2.ChangeDutyCycle(0) #清除当前占空比，使舵机停止抖动
sleep(0.5)

#信号处理
def distance():
    # 发送高电平信号到 Trig 引脚
    GPIO.output(GPIO_TRIGGER, True)
 
    # 持续 10 us 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    start_time = time.time()
    stop_time = time.time()
 
    # 记录发送超声波的时刻1
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
 
    # 记录接收到返回超声波的时刻2
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
 
    # 计算超声波的往返时间 = 时刻2 - 时刻1
    time_elapsed = stop_time - start_time
    # 声波的速度为 340m/s， 转化为 34000cm/s。
    distance = (time_elapsed * 34000) / 2
 
    return distance
g=0
if __name__ == '__main__':
        while g<=70 :
            g += 1
            p1.ChangeDutyCycle(tonum(g)) #执行角度变化，跳转到q列表中对应第c位元素的角度
            sleep(0.1)
            p1.ChangeDutyCycle(0)  #清除当前占空比，使舵机停止抖动
            sleep(0.01)
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            time.sleep(0.1)
        while g>=0 :
            g -= 1
            p1.ChangeDutyCycle(tonum(g)) #执行角度变化，跳转到q列表中对应第c位元素的角度
            sleep(0.1)
            p1.ChangeDutyCycle(0)  #清除当前占空比，使舵机停止抖动
            sleep(0.01)
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            time.sleep(0.1)
