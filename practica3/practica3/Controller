from turtle import *

import rclpy
from mpmath import atan2
from rclpy.node import Node
import math
import time
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

from practica3.publisher_member_function import MinimalPublisher
from practica3.subscriber_member_function import MinimalSubscriber

class Controller(Node):
    def __init__(self, x = 0, y = 0):
        super().__init__('controller')
        #self.node = rclpy.create_node('spawn_client')
        self.inicializa_subscriptores()
        self.minimal_publisher = MinimalPublisher()
        self.minimal_subscriber = MinimalSubscriber()
        self.x = x
        self.y = y
        self.pose = Pose()      #inicializa
        self.var = 0

    def inicializa_subscriptores(self):
        self.pose_subscription1 = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback1, 10)
        self.pose_subscription1  # prevent unused variable warning

        self.pose_subscription = self.create_subscription(Pose, '/turtle2/pose', self.pose_callback2, 10)
        self.pose_subscription  # prevent unused variable warning

        self.pose_subscription3 = self.create_subscription(Pose, '/turtle3/pose', self.pose_callback3, 10)
        self.pose_subscription3  # prevent unused variable warning

    def pose_callback1(self, msg):
        self.t1_x = msg.x
        self.t1_y = msg.y
        self.t1_theta = msg.theta
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')

    def pose_callback2(self, msg):
        self.t2_x = msg.x
        self.t2_y = msg.y
        self.t2_theta = msg.theta
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')

    def pose_callback3(self, msg):
        self.t3_x = msg.x
        self.t3_y = msg.y
        self.t3_theta = msg.theta
        # leer en que posicion estamos
        self.get_logger().info(f'Received pose -x: {msg.x}, y: {msg.y}, theta: ´{msg.theta}')

    def main(self):
        client = self.create_client(Spawn,'/spawn')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warning('error')

        request = Spawn.Request()
        request.x = 9.0
        request.y = 9.0
        request.theta = 0.0
        request.name = 'turtle2'
        self.future = client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)

        time.sleep(1)

        request = Spawn.Request()
        request.x = 5.15
        request.y = 4.0
        request.theta = 0.0
        request.name = 'turtle3'
        self.future = client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)

        while rclpy.ok():
            if self.var == 0:
                self.set_turtle_color(0, 0, 0, 10, '/turtle3/set_pen')
                self.do_house()
                self.set_turtle_color(50, 50, 0, 40, '/turtle3/set_pen')
                self.do_path(1)
                self.var = 1

            self.set_turtle_color(0, 255, 0, 20, '/turtle1/set_pen')
            self.move_straight(1)

            self.set_turtle_color(255, 255, 0, 60, '/turtle2/set_pen')  # ponerlob amarillo
            self.move_in_circle(0.5, 0.8)

            time.sleep(1)

    def move_in_circle(self, lin, ang):
        msg = Twist()
        msg.linear.x = float(lin)  # escoger a que velocidad queremos que se mueva
        msg.angular.z = float(ang)  # escoger velocidad para girar
        self.minimal_publisher.publisher_.publish(msg)

    def move_straight(self, lin):
        msg = Twist()
        msg.linear.x = float(lin)
        msg.angular.z = 0.0
        self.minimal_publisher.publisher1_.publish(msg)

    def do_path(self, lin):
        msg = Twist()

        collision_x_limit = 10.0

        # Mover en una dirección hasta el límite
        while self.t3_x < collision_x_limit:
            msg.linear.x = float(lin)
            msg.linear.y = float(-lin)
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            rclpy.spin_once(self)

        # Detenerse al alcanzar el límite
        msg.linear.x = 0.0
        self.minimal_publisher.publisher3_.publish(msg)
        rclpy.spin_once(self)
        time.sleep(1)  # Esperar un segundo


    def do_house(self):
        msg = Twist()
        for i in range(0,40):       ###PARED DERECHA
            msg.linear.y = 1.0
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)

        for a in range(0,25):       ###TEJADO DERECHO
            msg.linear.y = 1.0
            msg.linear.x = -1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)

        for a in range(0,25):       ###TEJADO IZQUIERDO
            msg.linear.y = -1.0
            msg.linear.x = -1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)

        for i in range(0,40):       ###PARED IZQUIERDA
            msg.linear.y = -1.0
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)

        for i in range(0,46):       ###SUELO
            msg.linear.y = 0.0
            msg.linear.x = 1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)

        distance_to_initial = 5.15 - self.t3_x
        while distance_to_initial > 0: #para llegar otra vez a la posicion inicial de la casa
            msg.linear.y = 0.0
            msg.linear.x = 1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)
        for i in range(0, 30):  # atras
            msg.linear.y = 0.0
            msg.linear.x = -1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)
        for i in range(0, 20):  # arriba
            msg.linear.y = 1.0
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)
        for i in range(0, 10):  # izquierda
            msg.linear.y = 0.0
            msg.linear.x = -1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)
        for i in range(0, 20):  # abajo
            msg.linear.y = -1.0
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)
        for i in range(0, 5):  # izquierda
            msg.linear.y = 0.0
            msg.linear.x = 1.0
            msg.angular.z = 0.0
            self.minimal_publisher.publisher3_.publish(msg)
            time.sleep(0.1)

    def set_turtle_color(self, r, g, b, width, name):
        # Método para cambiar el color de la tortuga
        set_pen = self.create_client(SetPen, name)
        request = SetPen.Request()
        request.r = r  # Color rojo
        request.g = g  # Color verde
        request.b = b  # Color azul
        request.width = width  # Grosor del lápiz
        request.off = 0  # Dibujar encendido
        future = set_pen.call_async(request)
        rclpy.spin_until_future_complete(self, future)

def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    controller.main()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
