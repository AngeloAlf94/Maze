#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    regions=[
        min(min(msg.ranges[0:143]),10),
        min(min(msg.ranges[144:287]),10),
        min(min(msg.ranges[288:431]),10),
        min(min(msg.ranges[432:575]),10),
        min(min(msg.ranges[576:719]),10),
    ]

    rospy.loginfo(msg)

def main():
    rospy.init_node("reading_sensor")

    sub=rospy.Subscriber("/scan",LaserScan,clbk_laser)

    rospy.spin()

if __name__ == "__main__":
    main()
