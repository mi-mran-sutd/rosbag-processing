# only tested and working on ROS1, not ROS2

import os
import cv2
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
from datetime import datetime

bag = rosbag.Bag("/home/bimanual_robot/test_ws/2024-11-07-15-23-00.bag") # path to rosbag file
bridge = CvBridge()

# topics (these can be obtained from get_messages_info script)
# ['/right/camera/color/image_raw','/right/camera/depth/image_raw','/right/my_gen3/base_feedback/joint_state']

for topic, msg, t in bag.read_messages(topics=['/right/camera/depth/image_raw']): # specify topic to retrieve messages from
    dt = datetime.fromtimestamp(t.to_sec())
    cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
    cv2.imwrite(os.path.join("/home/bimanual_robot/test_ws/2024-11-07-15-23-00_depth_rosbag_imgs/", f"frame_{dt.strftime('%Y_%m_%d-%H_%M_%S_%f')}.png"), cv_img)
    print(f"Saved frame_{dt.strftime('%Y_%m_%d-%H_%M_%S_%f')}.png")

bag.close()