#!/usr/bin/env python
import rospy
from common_msgs.msgs import comm_msg

def callback(msg):
    print "subscribe:", msg.int_data, msg.point_data.x, msg.point_data.y, msg.point_data.z

rospy.init_node('algorithm')
sub = rospy.Subscriber('algorithm_msg', comm_msg, callback)
rospy.spin()
