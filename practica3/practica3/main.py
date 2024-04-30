import rclpy
from rclpy.node import Node
import math
import time
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

#class Turtle(Node):



class Controller(Node):
    def main(self):
        self.go_to_goal(3,2)
        #fer un while true
        #llamar al spin_once para que haga constantemte al publisher y al reciber
        #self.change_color(190,255,0,15) #poner pincel verde
        #self.go_to_goal()



