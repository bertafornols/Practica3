import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.velocity_subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.velocity_callback,
            10)
        self.velocity_subscription  # prevent unused variable warning

        self.pose_subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        self.pose_subscription  # prevent unused variable warning

    def velocity_callback(self, msg):
        #leer velocidades
        self.get_logger().info(f'Received velocity - linear.x: {msg.linear.x}, angular.z: {msg.angular.z}')

    def pose_callback(self, msg):
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)
    #spin, ejecuta ros por detras, cuando le llega un call trabaja
    #spin_once: fa una sola iteracio
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()