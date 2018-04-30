#!/usr/bin/env python

import rospy
from functools import partial
from rc_car.msg import drive_param
from rc_car.msg import pid_input

STEER_RIGHT = 180
STEER_LEFT = 0
STEER_STRAIGHT = 90
FORWARD = 102
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

def step_one_avoidance(data):
	if(data.alpha == 0):
		if(data.leftBlocked):
			angle = STEER_RIGHT
		if(data.rightBlocked):
			angle = STEER_RIGHT
		else:
			angle = STEER_RIGHT
	elif(data.alpha > 0):
		if(data.leftBlocked):
			angle = STEER_RIGHT
		elif(data.rightBlocked):
			angle = STEER_LEFT
		else:
			angle = STEER_RIGHT
	elif(data.alpha < 0):
		if(data.leftBlocked):
			angle = STEER_RIGHT
		elif(data.rightBlocked):
			angle = STEER_LEFT
		else:
			angle = STEER_LEFT
	return angle





def control(data):
	global prev_error
	global vel_input
	global kp
	global kd
	global avoidance_step
	recent_turn_angle = STEER_STRAIGHT
	msg = drive_param();

	msg.velocity = FORWARD
	
	# MODE 1: Obstacle avoidance #



	if(data.frontBlocked):
		rospy.loginfo("Obstacle step 1")
	#obstacle avoidance algorithm
		#vehicle is facing straight

		avoidance_step = 2
		msg.angle = step_one_avoidance(data)
		recent_turn_angle = msg.angle 
		# rospy.loginfo("Obstacle ahead")
		pub.publish(msg)

	elif(avoidance_step == 2):
		rospy.loginfo("Obstacle step 2")
		if(recent_turn_angle == STEER_RIGHT and data.leftBlocked):
			msg.angle = STEER_STRAIGHT
			pub.publish(msg)
		elif(recent_turn_angle == STEER_LEFT and data.rightBlocked):
			if(data.rightBlocked):
				msg.angle = STEER_STRAIGHT
				pub.publish(msg)
		else:
			rospy.loginfo("Obstacle avoidance EXIT")
			avoidance_step = 1



	# MODE 2: Drive parallel #
	# 1. Scale the error
	# 2. Apply the PID equation on error
	# 3. Make sure the error is within bounds
	else: 	

 		angle = kp * data.error + kd * (prev_error - data.error)

 		if angle > 90:
 			angle = 90
		elif angle < -90:
			angle = -90
	  	
	  	msg.velocity = vel_input	
		msg.angle = 90 - angle
		pub.publish(msg)

 	prev_error = data.error # Store error for next iteration
	
if __name__ == '__main__':

	print("Listening to error for PID")

	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	rospy.spin()