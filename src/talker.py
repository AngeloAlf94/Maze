#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point,Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2
x=0.0
y=0.0
theta=0.0

def newOdom(msg):
    global x
    global y
    global theta
    
    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    
def movimento(x_start, y_start, x_goal, y_goal):
    
      
    speed=Twist()

    r=rospy.Rate(4)

    goal = Point()
    goal.x = x_goal
    goal.y = y_goal

    while not rospy.is_shutdown():
        inc_x = goal.x - x_start
        inc_y = goal.y - y_start
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

def main():
    rospy.init_node('talker', anonymous=True)

    sub=rospy.Subscriber('/r2d2_diff_drive_controller/odom',Odometry,newOdom)
    pub = rospy.Publisher('/r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=10)
    
    movimento(0,0,2,2)
    movimento(2,2,4,2)    


if __name__=="__main__":
    main()




    
       