#!/usr/bin/env python

import rospy
from rc_car.msg import drive_param
from rc_car.msg import pid_input

kp = 14.0
kd = 0.09
servo_offset = 0.0
prev_error = 0.0 
vel_input = 90.0

pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def control(data):
	global prev_error
	global vel_input
	global kp
	global kd

	## Your code goes here
	# 1. Scale the error
	# 2. Apply the PID equation on error
	# 3. Make sure the error is within bounds
	

 	angle = kp * data.error + kd * (prev_error - data.error)
 	prev_error = data.error #The current error will be used as prev_error the next time callback function is executed

	## END

	msg = drive_param();
	msg.velocity = vel_input	
	msg.angle = angle
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