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

desired_trajectory = .85
velocity = 30
prev_error = 0
theta = 25
lidar_offset = 270 # Add this offset value when extracting range data from lidar message(aka when using getRange)

pub = rospy.Publisher('error', pid_input, queue_size = 10)

# Function: getRange
# Parameters: 1) the lidar LaserScan msg instance 2) desired angle to find distance + offset if necessary
# Output: the distance at angle theta

def getRange(data,index):
# Get distance at theta
	distance = data.ranges[index]
	if(distance == float("inf")):
		return 5
	else:
		return distance

# Function: checkSector
# Parameters: Sector to be examined (Left, Right, Straight)
# Output: true or false (whether or not sector is blocked)
def checkSector(sector):
	if(sector == "STRAIGHT"):

		return 0
	if(sector == "LEFT"):
		return 0
	if(sector == "RIGHT"):
		return 0



# Function: callback
# performs getRange at angle 0 and theta to calculate error
def callback(data):

	# Check distances of two rays
	a = getRange(data, theta + lidar_offset)
	b = getRange(data, 0 + lidar_offset) # 0
	

	# Check if obstacle in front
	front_dist = getRange(data, 0)
	front_obstacle_flag = False
	if(front_dist > .1 and front_dist < 1):
		front_obstacle_flag = True
		# rospy.loginfo("Obstacle detected")

	# rospy.loginfo("Distance = %f", front_dist)
	

	#implement distance finding equations
	swing = math.radians(theta)
	alpha = math.atan((a * math.cos(swing) - b) / (a * math.sin(swing)))
	AB = b * math.cos(alpha)

	# rospy.loginfo("Time: %f,  Distance from wall %f", rospy.get_time(), AB)
	error = desired_trajectory - AB
	# rospy.loginfo("A = %f B = %f", a , b)
	# rospy.loginfo("Alpha = %f", math.degrees(alpha))
	# rospy.loginfo("Distance from wall = %f", AB)
	# rospy.loginfo("Error = %f", error)


	#check lenght of ranges array
	# print len(data.ranges)


	# store calculated values into a message and publish
	msg = pid_input()
	msg.error = error
	msg.vel = velocity
<<<<<<< HEAD
	msg.flag = checkSector(STRAIGHT)
=======
	msg.obstacle_flag = front_obstacle_flag
>>>>>>> eded1ba6bed8daf90ac003e68b298d1b5e82d125
	pub.publish(msg)

if __name__ == '__main__':
	print("Distance finder node")
	rospy.init_node('dist_finder', anonymous = False)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()