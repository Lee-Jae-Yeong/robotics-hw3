#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import comm_msg

rospy.init_node('sensor')
pub = rospy.Publisher('algorithm_msg', comm_msg, queue_size=1)
msg = comm_msg()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.int_data.data = 1
    msg.point_data = Point(x=100%6, y=100%9, z=100%7)
    pub.publish(msg)
  
    print "publish:", msg.int_data, msg.point_data.x, msg.point_data.y,msg.point_data.z
    rate.sleep()
