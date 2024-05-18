import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.publisher1_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.publisher3_ = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        #INDICAMOS A QUE VELOCIDAD QUEREMOS QUE SE MUEVA

        self.get_logger().info(f'velocity linear.x: {msg.linear.x} angular.z: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
