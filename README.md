# Autonomous RC Car with SLAM
Self-driving RC car built on Robot Operating System (ROS indigo) platform. Uses RPLIDAR  to carry out the following tasks: map generation, localization, PID control, and obstacle avoidance. Arduino used for regulating car steering and velocity.

## Components
- RPLidar A2
- Traxxas RC car
- Arduino Mega
- Ubuntu 14.04 // Raspberry Pi 3(Ubuntu Mate)

## Package descriptions (src/)
- hector_slam/
- navigation/amcl
  - **amcl**: node for Adaptive Monte Carlo Localization
- rc_car/
  - **dist_finder.py**: calculates error for PID control and detect obstacles based on laser scan distance data
  - **control.py**: generates commands for car movement
  - **odom_tf.py**: given an geometry_msg/Odometry, broadcasts the tf transform from scanmatch_odom->base_frame
  - **teleop_to_arduino.py**: translates teleoperation commands to steering angle and velocity for full keyboard control of rc car
  - **tutorial.launch**: launches map generation via hector_mapping
  - **localization.launch**: execution of localization within a saved map via amcl
- rosserial/rosserial_python
  - **serial_node.py**: forwards messages between ROS and Arduino via serial port
- rplidar_ros
  - **rplidar.launch**: initiates lidar scanning



## System setup
1. Flash Arduino with pid_to_servo.ino, found in the root directory 
2. Build ROS workspace via catkin_make
3. Start up lidar and we may choose one of the following tasks
```
roslaunch rplidar_ros rplidar.launch
```
- PID control
```
roslaunch rc_car pid.launch
```
- Map Generation
```
roslaunch rc_car tutorial.launch
```
- Localization
```
roslaunch rc_car localization.launch
```
