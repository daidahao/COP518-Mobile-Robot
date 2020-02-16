# Mobile Robot

2019 COP518 Robotics & Intelligent Systems Coursework

Loughborough University



## Introduction

This project is based on a mobile robot that has been built with latest AI technology and various sensor capabilities. It could be programmed in Python. It has a latest Realsense camera from Intel, which could capture both colour RGB image and depth image and be processed with a Nvidia nano board which supports image processing and deep learning. It also has multiple proximity sensors at its front, sides and back.

The task we have done in this project is programming its behaviours and test them to see if it works fully functionally. There are two types of behaviour we have been working on, Reactive Behaviours and Following Behaviours.



### Reactive Behaviours

In this part we have designed robot’s behaviour simulate Braitenberg’s vehicle behaviour. There are four different behaviours: Love, Fear, Aggression as long as curious. We have used a black backpack as our targeted object and used deep learning to train the robot using its camera to recognize that specific backpack in a complex environment. When the robot has detected the targeted object, it will initiate the behaviour that we have assigned.



### Following Behaviours

In this part we programmed the robot to follow a human that has been detected by its RGBD camera and not only follow its movement, but also keep a safe distance from targeted human.



© Zhihao DAI 2020