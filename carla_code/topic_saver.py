#! /usr/bin/python
# Copyright (c) 2020, ARIL, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import math
import os

# Instantiate CvBridge
bridge1 = CvBridge()
bridge2 = CvBridge()
bridge3 = CvBridge()
bridge4 = CvBridge()

# Global variable

img_c = None
img_l = None
img_r = None
img_map = None
steer = None
count = 0

global_path = 'data/'
file_list = os.listdir(global_path)

count = len(file_list)
print(count)

rate = 0.5

def image_callback_c(msg):
	global img_c, img_l, img_r, img_map, steer,count
	# print("Received an center image!")
	if steer != None:
		print("save!!")
		# Save your OpenCV2 image as a jpeg
		if not os.path.exists(global_path+str(count)):
			os.makedirs(global_path+str(count))
		cv2.imwrite(global_path+'{}/center_{:.4f}.png'.format(count,steer) ,img_c)
		cv2.imwrite(global_path+'{}/left_{:.4f}.png'.format(count,steer) ,img_l)
		cv2.imwrite(global_path+'{}/right_{:.4f}.png'.format(count,steer) ,img_r)
		cv2.imwrite(global_path+'{}/map_{:.4f}.png'.format(count,steer) ,img_map)
		rospy.sleep(rate)
		count += 1
	try:
	# Convert your ROS Image message to OpenCV2
		img_c = bridge1.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError:
		print("Error")

	

def image_callback_l(msg):
	global img_l
	# print("Received an left image!")
	try:
		img_l = bridge2.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError:
		print("error_l")

def image_callback_r(msg):
	global img_r
	# print("Received an right image!")
	try:
		img_r = bridge3.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError:
		print("error_r")

def map_callback(msg):
	global img_map
	# print("Received an map image!")
	try:
		img_map = bridge4.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError as e:
		print(e)

def odom_callback(msg):
	global steer
	# print("Received an Odometry!")
	v = msg.twist.twist.linear
	vel = math.sqrt(v.x**2 + v.y**2 + v.z**2)
	theta = msg.twist.twist.angular.z

	if vel < 1:
		steer = None
	else:
		steer = theta/vel

def main():
	rospy.init_node('image_listener')
	# Define your image topic
	image_c_topic = "/carla/hero/camera/rgb/center/image_color"
	image_l_topic = "/carla/hero/camera/rgb/left/image_color"
	image_r_topic = "/carla/hero/camera/rgb/right/image_color"
	map_topic = "/coarsemap"
	odom_topic = "/carla/hero/odometry"

    # Set up your subscriber and define its callback
	rospy.Subscriber(image_c_topic, Image, image_callback_c)
	rospy.Subscriber(image_l_topic, Image, image_callback_l)
	rospy.Subscriber(image_r_topic, Image, image_callback_r)
	rospy.Subscriber(map_topic, Image, map_callback)
	rospy.Subscriber(odom_topic, Odometry, odom_callback)
	# Spin until ctrl + c
	rospy.spin()

if __name__ == '__main__':
	main()