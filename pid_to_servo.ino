/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <rc_car/drive_param.h>

#define SERVO_PIN 9
#define ESC_PIN 10
#define RPM_PIN 11 // RPM Sensor pulse

ros::NodeHandle  nh;

Servo servo;
Servo esc;

void servo_cb( const rc_car::drive_param& msg){
  float steering_angle = msg.angle;

  servo.write(steering_angle); //set servo angle, should be from 0-180  
  esc.write(msg.velocity);
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}


ros::Subscriber<rc_car::drive_param> sub("drive_parameters", servo_cb);

void setup(){
  pinMode(13, OUTPUT);
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.subscribe(sub);
  
  servo.attach(9); //attach it to pin 9
  esc.attach(10);
  esc.write(90);
  delay(1);
}

void loop(){
  nh.spinOnce();
  delay(1);
}
