# Autonomous RC Car with SLAM
Self-driving RC car built on Robot Operating System (ROS indigo) platform. 

## Components
- RPLidar A2
- Traxxas RC car
- Arduino Mega
- Raspberry Pi 3

## Description
The rc_car ROS package contain source code for launch files, nodes, and message data types. Communication between nodes is managed by the ros master.

### Hector SLAM
```
roslaunch hector_slam_launch tutorial.launch
```
### Parallel wall w/ PID control
```
roslaunch rc_car pid.launch
```
### Adaptive Monte Carlo Localization
```
roslaunch rc_car amcl_test2.launch
```
