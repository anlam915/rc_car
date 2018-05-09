# Autonomous RC Car with SLAM
Self-driving RC car built on Robot Operating System (ROS indigo) platform. Uses RPLIDAR  to carry out the following tasks: map generation, localization, PID control, and obstacle avoidance. Arduino used for regulating car steering and velocity.

## Components
- RPLidar A2
- Traxxas RC car
- Arduino Mega
- Ubuntu 14.04 and Raspberry Pi 3(Ubuntu Mate)

## Package descriptions (src/)
- rc_car/
  -/scripts/
    - **dist_finder.py**: calculates error for PID control and detect obstacles based on laser scan distance data
    - **control.py**: generates commands for car movement
    - **odom_tf.py**: given an geometry_msg/Odometry, broadcasts the tf transform from scanmatch_odom->base_frame
    - **teleop_to_arduino.py**: translates teleoperation commands to steering angle and velocity for full keyboard control of rc car


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
