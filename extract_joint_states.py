# only tested and working on ROS1, not ROS2

import os
import cv2
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import rospy
import datetime
import pandas as pd

bag = rosbag.Bag("/home/bimanual_robot/test_ws/2024-11-07-15-23-00.bag") # path to rosbag file
bridge = CvBridge()

count = 0

# topics
# ['/right/camera/color/image_raw','/right/camera/depth/image_raw','/right/my_gen3/base_feedback/joint_state']

# available data from /right/my_gen3/base_feedback/joint_state msg
# msg.header, msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id
# msg.name
# msg.position
# msg.velocity
# msg.effort

dt = []
seq_id = []
pos = []
vel = []
eff = []

for topic, msg, t in bag.read_messages(topics=['/right/my_gen3/base_feedback/joint_state']): # specify topic to retrieve messages from
    dt.append(datetime.datetime.fromtimestamp(t.to_sec()))
    seq_id.append(msg.header.seq)
    pos.append(msg.position)
    vel.append(msg.velocity)
    eff.append(msg.effort)

data = pd.DataFrame(
    {
        "datetime": dt, 
        "seq_id": seq_id,
        "position": pos,
        "velocity": vel,
        "effort": eff
        }
    )

print(data)
data.to_csv("joint_states.csv", index=False)

bag.close()