# only tested and working on ROS1, not ROS2

import rosbag
from cv_bridge import CvBridge
import numpy as np

bag = rosbag.Bag("/home/bimanual_robot/test_ws/2024-11-07-15-23-00.bag") # path to rosbag file
bridge = CvBridge()

topics = []

for topic, msg, t in bag.read_messages():
    topics.append(topic)

topics = np.array(topics)
print(np.unique(topics))

bag.close()