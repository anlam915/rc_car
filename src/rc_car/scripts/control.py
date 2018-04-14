#!/usr/bin/env python

import rospy
from rc_car.msg import drive_param
from rc_car.msg import pid_input

STEER_RIGHT = 180
STEER_LEFT = 0
STEER_STRAIGHT = 90
FORWARD = 103
NEUTRAL = 90
REVERSE = 0

kp = 14 * 2.5
kd = 0.09 * 2.25
kd = 0
servo_offset = 0.0
prev_error = 0.0 
integral = 0.0
vel_input = NEUTRAL 
# vel_input = FORWARD

avoidance_step = 1

pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def control(data):
	global prev_error
	global vel_input
	global kp
	global kd
	global avoidance_step
	msg = drive_param();

	'''
	PSUEDOCODE:
	if flag:
		turnRight
		step = 2
	elif step == 2:
		goStraight
		if(leftClear):
			step == 3

	START for Mode1/2 code

	'''
	# MODE 1: Obstacle avoidance #

	# 1. Scale the error
	# 2. Apply the PID equation on error
	# 3. Make sure the error is within bounds

	if(data.frontBlocked):
	#obstacle avoidance algoithm
		avoidance_step = 2
		msg.velocity = FORWARD;
		msg.angle = STEER_RIGHT
		# rospy.loginfo("Obstacle ahead")
		pub.publish(msg)
	elif(avoidance_step == 2):
		if(not data.leftBlocked):
			avoidance_step = 1

		else:
			# rospy.loginfo("Obstacle to left")
			msg.velocity = FORWARD
			msg.angle = STEER_STRAIGHT
			pub.publish(msg)
	# # MODE 2: Drive parallel #
	else: 	
		# rospy.loginfo("Clear")
 		angle = kp * data.error + kd * (prev_error - data.error)

 		if angle > 90:
 			angle = 90
		elif angle < -90:
			angle = -90
	  	
	  	msg.velocity = vel_input	
		msg.angle = 90 - angle
		pub.publish(msg)

	'''
	END for Mode1/Mode2 Code
	'''
	# angle = kp * data.error + kd * (data.error - prev_error)

	# if angle > 90:
	# 	angle = 90
	# elif angle < -90:
	# 	angle = -90
  	
 #  	msg.velocity = vel_input	
	# msg.angle = 90 - angle
	# pub.publish(msg)

 	prev_error = data.error # Store error for next iteration
	
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