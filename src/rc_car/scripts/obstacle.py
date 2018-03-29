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


pub = rospy.Publisher('')

def getRange(msg,theta):
# Get distance at theta, data is the LaserScan
	data = lidar_scan()
	return data.ranges[theta]

'''
Pseduocode for obstacle detection

1. Get one sweep of ranges from lidar

2. Check three sectors for obstacles


3. Check current steering angle
	Right
		if(right blocked)
			if(front clear)
				STEER_STRAIGHT
			else if(left clear)
				STEER_LEFT
			else if(rear clear)
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
'''
def callback(msg)


if __name__ == '__main__'
	print("Obstacle detection node")
	rospy.init_node('obstacle', anonymous = True)
	rospy.Subscriber("scan", lidar_scan, callback)
	rospy.spin()