#!/usr/bin/env python
import roslib
import rospy

import nav_msgs.msg as nav_msg



pub = rospy.Publisher('odom', nav_msg.Odometry, queue_size = 5 )

def callback(data):
	covariance_adjusted = nav_msg.Odometry()
	covariance_adjusted = data

	covariance_adjusted.pose.covariance = [1, 0, 0, 0, 0, 0,
										   0, 1, 0, 0, 0, 0,
										   0, 0, 1, 0, 0, 0,
										   0, 0, 0, 1, 0, 0,
										   0, 0, 0, 0, 1, 0,
										   0, 0, 0, 0, 0, 1]


	pub.publish(covariance_adjusted)



if __name__ == '__main__':
	rospy.init_node('Odom_ekf_node')

	rospy.Subscriber("scanmatch_odom", nav_msg.Odometry, callback)
	rospy.spin()