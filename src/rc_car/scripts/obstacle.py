#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from rc_car.msg import drive_param

#PWM values for Servo and ESC
STEER_RIGHT = 180
STEER_LEFT = 0
STEER_STRAIGHT = 90
FORWARD = 100
NEUTRAL = 90
REVERSE = 0

vel_input = 100.0
MAX_DISTANCE = 5.0
MIN_DISTANCE = .6

frontBlocked = False
leftBlocked = False
rightBlocked = False

pub = rospy.Publisher('drive_parameters', drive_param, queue_size = 1)

def getRange(msg,angle):
# Get distance at theta, data is the LaserScan
	return msg.ranges[angle]

'''
Pseduocode for obstacle detection

1. Get one sweep of ranges from lidar

2. Check three sectors for obstacles(LaserScan ranges array indices)
	a) Front sector: 0..15, 345..359 
		if an object
	b)


3. Check current steering angle
	Right
		if(right blocked)
			if(front clear)
				STEER_STRAIGHT
			else if(left clear)
				STEER_LEFT
	Left
		if(left blocked)
			if(front clear)
					STEER_STRAIGHT
			else if(right clear)
				STEER_RIGHT
	Straight
		if(front blocked)
			if(right clear)
				STEER_RIGHT
			if(left clear)
				STEER_LEFT




	Go Straight
	while(front blocked)
		Steer Right    (obstacle is on left)
	while(left blocked)
		Steer straight



'''
def checkFront(msg):
	for i in range(0,15):
		current = getRange(msg, i)
		if (current > 0 and current < MIN_DISTANCE):
			rospy.loginfo("Angle: %i Distance = %f", i, current)
			return True
	for i in range(345, 359):
		current = getRange(msg, i)
		if (current > 0 and current < MIN_DISTANCE):
			rospy.loginfo("Angle: %i Distance = %f", i, current)
			return True
	return False

def checkLeft(msg):
	for i in range(16, 45):
		current = getRange(msg, i)
		if (current > 0 and current < MIN_DISTANCE):
			return True
	return False

def checkRight(msg):
	for i in range(315, 344):
		current = getRange(msg, i)
		if (current > 0 and current < MIN_DISTANCE):
			return True
	return False

def sweep(msg):
	global frontBlocked
	global leftBlocked
	global rightBlocked
	frontBlocked = checkFront(msg)
	leftBlocked = checkLeft(msg)
	rightBlocked = checkRight(msg)




def callback(msg):
	sweep(msg)
	msg = drive_param()
	msg.velocity = vel_input
	if frontBlocked:
		# rospy.loginfo("Obstacle detected in front: ")
		if  not rightBlocked:
			msg.angle = STEER_RIGHT
			# print("Steer Right")
		elif not leftBlocked:
			msg.angle = STEER_LEFT
			# print("Steer Left")
	else:
		msg.angle = STEER_STRAIGHT
		# print("Steer Straight")

	pub.publish(msg)
	
if __name__ == '__main__':
	print("Obstacle detection node")
	rospy.init_node('obstacle', anonymous = True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()