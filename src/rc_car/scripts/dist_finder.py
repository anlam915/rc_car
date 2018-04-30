#!/usr/bin/env python

'''-----------------------------------DISTANCE FINDER NODE-------------------------------------------------------------------
	Tasks:
		(1) Read distance given by RP Lidar and calculate how far away from wall (desired distance)
		(2) Given the distance, determine whether or not there is an obstacle in front (front sector)
		(3) If there is no obstacle then clear flag to signify that vehicle should continue its normal path (parallel to wall)
			else set the flag to navigate around an obstacle
------------------------------------------------------------------------------------------------------------------------------
'''

import rospy
import math
from numpy import inf
from rc_car.msg import pid_input #<package><msg directory> import <msg type>
from sensor_msgs.msg import LaserScan


distance_offset = 41 #distance from front lidar sensor to front of car
danger_distance = 20 #20cm away from from of car --> avoid


# Driving Parallel variables
desired_trajectory = 1.0

velocity = 30
prev_error = 0
theta = 25
lidar_offset = 270 # Add this offset value when extracting range data from lidar message(aka when using getRange)

# Obstacle avoidance variables and constants
MAX_DISTANCE = 5.0
MIN_DISTANCE = 1.4

frontBlocked = False
leftBlocked = False
rightBlocked = False



pub = rospy.Publisher('error', pid_input, queue_size = 1)

# Function: getRange
# Parameters: 1) the lidar LaserScan msg instance 2) desired angle to find distance + offset if necessary
# Output: the distance at angle theta

def getRange(data,index):
# Get distance at theta
	distance = data.ranges[index]
	if(distance == float("inf")):
		return MAX_DISTANCE
	else:
		return distance

def checkFront(msg):
	for i in range(0,15):
		current = getRange(msg, i)
		if (current > 0 and current < MIN_DISTANCE):
			# rospy.loginfo("Angle: %i Distance = %f", i, current)
			return True
	for i in range(345, 359):
		current = getRange(msg, i)
		if (current > 0 and current < MIN_DISTANCE):
			# rospy.loginfo("Angle: %i Distance = %f", i, current)
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


# Function: callback
# performs getRange at angle 0 and theta to calculate error
def callback(data):
	global frontBlocked
	global leftBlocked
	global rightBlocked


	# Distance calculations:
	a = getRange(data, theta + lidar_offset)
	b = getRange(data, 0 + lidar_offset) # 0


	swing = math.radians(theta)
	alpha = math.atan((a * math.cos(swing) - b) / (a * math.sin(swing)))
	AB = b * math.cos(alpha)

	# rospy.loginfo("Time: %f,  Distance from wall %f", rospy.get_time(), AB)
	# rospy.loginfo("Alpha: %f", alpha)
	error = desired_trajectory - AB

	# (2) Get and set values for obstacle detection flags
	sweep(data)

	# Store range data into message and publish
	msg = pid_input()
	msg.frontBlocked = frontBlocked
	msg.leftBlocked = leftBlocked
	msg.rightBlocked = rightBlocked	
	msg.error = error
	msg.vel = velocity

	msg.alpha = alpha #used to determine the angle the car is facing

	pub.publish(msg)

if __name__ == '__main__':
	print("Distance finder node")
	rospy.init_node('dist_finder', anonymous = False)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()