#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

enum Wheel { RADIUS = .5, LENGTH = 3.14*RADIUS*RADIUS}

int main(int argc, char** argv){
	ros::init(argc, argv, "odometry");

	ros::NodeHandle nh;
	ros::Publisher odom_pub = nh.advertise<nav_msgs::Odometry>("odom", 50); // buffersize = 50
	tf::TransformBroadcaster odom_broadcaster;

	// The robot will start at the origin of odom
	double x = 0.0;
	double y = 0.0;
	double th = 0.0;

	// Linear velocities in x and y direction, + angular velocity th
	double vx = 0.0;
	double vy = 0.0;
	double vth = 0.0;

	ros::Time current_time, last_time;
	current_time = ros::Time::now();
	last_time = ros::Time::now();

	ros::Rate r(1.0); // Publish odometry at rate of 1Hz

	while(nh.ok()){
		ros::spinOnce(); // checks for incoming messages
		current_time = ros::Time::now();

		/* Perform calculations to estimate position given rpm ticks */
		double dt = (current_time - last_time).toSec();
		vx = 

		last_time = current_time;
		r.sleep();
	}
}