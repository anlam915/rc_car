#!/usr/bin/env python

import rospy
from rc_car.msg import drive_param
from rc_car.msg import pid_input

STEER_RIGHT = 180
STEER_LEFT = 0
STEER_STRAIGHT = 90
FORWARD = 100
NEUTRAL = 90
REVERSE = 0

kp = 14.0 * 4
kd = 0.09 * 3
servo_offset = 0.0
prev_error = 0.0 
integral = 0.0
vel_input = 102.0 
pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def control(data):
	global prev_error
	global vel_input
	global kp
	global kd

	msg = drive_param();

	# MODE 1: Obstacle avoidance #

	# 1. Scale the error
	# 2. Apply the PID equation on error
	# 3. Make sure the error is within bounds
	
	# if(data.obstacle_flag):
	# #obstacle avoidance algoithm
	# 	msg.velocity = NEUTRAL;
	# 	msg.angle = STEER_STRAIGHT
	# 	pub.publish(msg)
	# # MODE 2: Drive parallel #
	# else: 	

 	angle = kp * data.error + kd * (prev_error - data.error)
 	# if (angle > 90):
  #   	angle = 90
  # 	elif (angle < -90):
  #   	angle = -90
  	
 	prev_error = data.error #The current error will be used as prev_error the next time callback function is executed

	
	msg.velocity = vel_input	
	msg.angle = 90 - angle
	pub.publish(msg)
		# rospy.loginfo("Steering angle = %f", angle)
		# rospy.loginfo("Velocity = %f", vel_input)
		




if __name__ == '__main__':
	# global kp
	# global kd
	# global vel_input
	print("Listening to error for PID")
	# kp = input("Enter Kp Value: ")
	# kd = input("Enter Kd Value: ")
	# vel_input = input("Enter Velocity: ")
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	rospy.spin()