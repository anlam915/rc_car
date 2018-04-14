#!/usr/bin/env python

import rospy
from functools import partial
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

def front_funct(msg):
	msg.velocity = NEUTRAL
	msg.angle = STEER_STRAIGHT
	pub.publish(msg)

def left_funct(msg):
	msg.velocity = NEUTRAL
	msg.angle = STEER_RIGHT
	pub.publish(msg)

def right_funct(msg):
	msg.velocity = NEUTRAL
	msg.angle = STEER_LEFT
	pub.publish(msg)

def wall(msg, angle, velocity):
	msg.velocity = = velocity
	msg.angle = 90 - angle
	pub.publish(msg) 



def control(data):
	global prev_error
	global vel_input
	global kp
	global kd

	msg = drive_param();
	

	if(data.front_blocked):
		function = front
		step = 2
	elif(step == 2):
		if(!left_block):
			step == 1
		else:
			function = left
	else:
		function = wall

 	angle = kp * data.error + kd * (data.error - prev_error)
 	if(angle > 90):
 		angle = 90
 	elif(angle < -90):
 		angle = -90

  	
 	prev_error = data.error #The current error will be used as prev_error the next time callback function is executed

	
	# msg.velocity = vel_input	
	# msg.angle = 90 - angle
	# pub.publish(msg)
		# rospy.loginfo("Steering angle = %f", angle)
		# rospy.loginfo("Velocity = %f", vel_input)
	Function_Dict = {"front": partial(front_funct, msg), "left": partial(left_funct,msg), "right": partial(right_funct,msg), "wall": partial(wall,msg,angle,vel_input)}[function]()
		




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