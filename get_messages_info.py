# only tested and working on ROS1, not ROS2

import os
import cv2
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

bag = rosbag.Bag("/home/bimanual_robot/test_ws/2024-11-07-15-23-00.bag") # path to rosbag file
bridge = CvBridge()

print(bag.get_message_count(topic_filters=['/right/camera/depth/image_raw']))