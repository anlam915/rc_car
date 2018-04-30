#!/usr/bin/env python
import roslib
import rospy
import tf, tf2_ros
import geometry_msgs.msg as geo_msg
import nav_msgs.msg as nav_msg


# Read an odometry message and establish tf transforms
# Listen to map transform, broadcast to base_frame

def callback(data, args):
	broadcaster = tf2_ros.TransformBroadcaster()
	tf1 = geo_msg.TransformStamped()

	tf1.header.stamp = rospy.Time.now()
	tf1.header.frame_id = args[0]
	tf1.child_frame_id = args[1]
	tf1.transform.translation = data.pose.pose.position
	tf1.transform.rotation = data.pose.pose.orientation

	broadcaster.sendTransform(tf1)

if __name__ == '__main__':
	rospy.init_node('Odom node')
	odom_input = rospy.get_param("~odom_input");
	tf_output = rospy.get_param("~tf_output");
	rospy.Subscriber(odom_input, nav_msg.Odometry, callback, [odom_input, tf_output] )
	rospy.spin()