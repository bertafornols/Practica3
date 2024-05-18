import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

from practica3.publisher_member_function import MinimalPublisher

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        self.minimal_publisher = MinimalPublisher()

    def pose_callback1(self,msg):
        self.t1_x = msg.x
        self.t1_y = msg.y
        self.t1_theta = msg.theta
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')

    def pose_callback2(self,msg):
        self.t2_x = msg.x
        self.t2_y = msg.y
        self.t2_theta = msg.theta
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')

    def pose_callback3(self,msg):
        self.t3_x = msg.x
        self.t3_y = msg.y
        self.t3_theta = msg.theta
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)
    #spin, ejecuta ros por detras, cuando le llega un call trabaja
    #spin_once: fa una sola iteracio
    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
