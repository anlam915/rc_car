#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from rc_car.msg import drive_param

STEER_RIGHT = 180
STEER_LEFT = 0
STEER_STRAIGHT = 90
FORWARD = 102
NEUTRAL = 90
REVERSE = 0


pub = rospy.Publisher('drive_parameters', drive_param, queue_size = 5 )

def callback(data):
	msg = drive_param()

	# rospy.loginfo("Thrust: %f", data.linear.x)
	# rospy.loginfo("Direction: %f", data.angular.z)

	thrust = data.linear.x
	angle = data.angular.z

	print "incoming angle:"
	print angle;

	if angle > 0:
		msg.angle = STEER_LEFT
	elif angle < 0:
		msg.angle = STEER_RIGHT
	else:
		msg.angle = STEER_STRAIGHT


	if thrust > 0:
		msg.velocity = FORWARD
	elif thrust < 0:
		print "Reverse"
	else:
		msg.velocity = NEUTRAL

	print "outgoing angle:"
	print msg.angle
	pub.publish(msg)


if __name__ == '__main__':
	print "Teleop to arduino node"
	rospy.init_node('teleop_to_arduino')
	rospy.Subscriber('cmd_vel', Twist, callback)
	rospy.spin()