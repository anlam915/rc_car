#!/usr/bin/env python

import rospy
from functools import partial
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
	recent_turn_angle = FORWARD
	msg = drive_param();

	msg.velocity = FORWARD
	

	# if(data.front_blocked):
	# 	function = front
	# 	avoidance_step = 2
	# elif(step == 2):
	# 	if(!left_block):
	# 		avoiddance_step == 1
	# 	else:
	# 		function = left
	# else:
	# 	function = wall

 # 	angle = kp * data.error + kd * (data.error - prev_error)
 # 	if(angle > 90):
 # 		angle = 90
 # 	elif(angle < -90):
 # 		angle = -90

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
		#vehicle is facing straight
		if(data.alpha == 0): 
			if(data.leftBlocked):
				msg.angle = STEER_RIGHT
			elif(data.rightBlocked):
				msg.angle = STEER_LEFT
			else:
				msg.angle = STEER_RIGHT

		#vehicle is tilted toward the left
		if(data.alpha < 0): 
			if(data.leftBlocked):
				msg.angle = STEER_RIGHT
			elif(data.rightBlocked):
				msg.angle = STEER_LEFT
			else:
				msg.angle = STEER_RIGHT

		#vehicle is tilted toward the right
		if(data.alpha > 0):
			if(data.leftBlocked):
				msg.angle = STEER_RIGHT
			elif(data.rightBlocked):
				msg.angle = STEER_LEFT
			else:
				msg.angle = STEER_LEFT

		avoidance_step = 2
		recent_turn_angle = msg.angle 
		# rospy.loginfo("Obstacle ahead")
		pub.publish(msg)

	elif(avoidance_step == 2):
		if(recent_turn_angle == STEER_RIGHT):
			if(data.leftBlocked):
				msg.angle = STEER_STRAIGHT
		elif(recent_turn_angle == STEER_LEFT):
			if(data.rightBlocked):
				msg.angle = STEER_STRAIGHT
		else:
			# rospy.loginfo("Obstacle to left")
			avoidance_step = 1

		pub.publish(msg)

	# # MODE 2: Drive parallel #
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
	


 # 	Alpha_Dict = {"zero": }
	# Function_Dict = {"front": partial(front_funct, msg), "left": partial(left_funct,msg), "right": partial(right_funct,msg), "wall": partial(wall,msg,angle,vel_input)}[function]()
		
if __name__ == '__main__':

	print("Listening to error for PID")

	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	rospy.spin()