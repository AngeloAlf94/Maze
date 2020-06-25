#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point,Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2

theta=0.0

def newOdom(msg):
    global x
    global y
    global theta
    
    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

#def movimento(x_start, y_start, x_goal, y_goal):
x= 0
y= 0


rospy.init_node('talker', anonymous=True)

sub=rospy.Subscriber('/r2d2_diff_drive_controller/odom',Odometry,newOdom)
pub = rospy.Publisher('/r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=10)

  
speed=Twist()

r=rospy.Rate(1)

goal = Point()
goal.x = 2
goal.y = 2

while not rospy.is_shutdown():
    inc_x = goal.x - x
    inc_y = goal.y - y
    print("incx,incy",inc_x, inc_y)
    print("x,y:",x,y)   

    angle_to_goal=atan2(inc_y, inc_x)
    print("atg,theta:",angle_to_goal,theta)
        
    print("diff:",angle_to_goal-theta)

    if abs(angle_to_goal - theta) > 0.1:
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0

    pub.publish(speed)
    r.sleep()


#movimento(0,0,2,2)
#movimento(2,2,4,2)    





    
       