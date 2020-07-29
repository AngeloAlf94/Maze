#!/usr/bin/env python

import rospy
import time
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
    
def movimento(pub,x_start, y_start, x_goal, y_goal):
    
      
    speed=Twist()

    r=rospy.Rate(4)

    goal = Point()
    goal.x = x_goal
    goal.y = y_goal

    
    inc_x = goal.x - x_start
    inc_y = goal.y - y_start
    #print("incx,incy",inc_x, inc_y)
    #print("x,y:",x,y)   

    angle_to_goal=atan2(inc_y, inc_x)
    #print("atg,theta:",angle_to_goal,theta)
        
    print("diff:",angle_to_goal-theta)

    while abs(angle_to_goal - theta) > 0.05:
        speed.linear.x = 0.0
        speed.angular.z = 0.3
        pub.publish(speed)
    
    print("delta x:", x_goal-x)
    print("delta y:", y_goal-y)
    if x_goal != x_start and y_goal != y_start:
        while abs(x_goal-x) and abs(y_goal-y) > 0.05:
            speed.linear.x= 0.5
            speed.angular.z=0.0
            pub.publish(speed)

    if x_goal == x_start:   
        while abs(y_goal-y) > 0.05:
            speed.linear.x= 0.5
            speed.angular.z=0.0
            pub.publish(speed)
    if y_goal==y_start:
        while abs(x_goal-x) > 0.05:
            speed.linear.x= 0.5
            speed.angular.z=0.0
            pub.publish(speed)
    print("x e y attuali:",x,y)        
    r.sleep()

def main():
    rospy.init_node('talker', anonymous=True)

    sub=rospy.Subscriber('/ground_truth/state',Odometry,newOdom)
    pub = rospy.Publisher('/r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=10)
    
    movimento(pub,0,0,2,2)
    movimento(pub,2,2,4,2)
    movimento(pub,4,2,4,6)
    movimento(pub,4,6,2,6)
    movimento(pub,2,6,2,2)    


if __name__=="__main__":
    main()




    
       