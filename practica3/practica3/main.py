import rclpy
from mpmath import atan2
from rclpy.node import Node
import math
import time
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

from practica3.publisher_member_function import MinimalPublisher
from practica3.subscriber_member_function import MinimalSubscriber


class Controller(Node):
    def __init__(self, x = 0, y = 0):
        super().__init__('controller')

        self.minimal_publisher = MinimalPublisher()
        self.minimal_subscriber = MinimalSubscriber()
        self.x = x
        self.y = y
        self.pose = Pose()      #inicializa
    def main(self):
        self.set_turtle_position(1,1)       #ponerlo en la esquina
        self.set_turtle_color(255,255,0,5)  #ponerlob amarillo
        while rclpy.ok():
            self.move_in_circle(0.5, 0.2)
            time.sleep(1)

    def move_in_circle(self, lin, ang):
        msg = Twist()
        msg.linear.x = float(lin)  # escoger a que velocidad queremos que se mueva
        msg.angular.z = float(ang)  # escoger velocidad para girar
        self.minimal_publisher.publisher_.publish(msg)

    def update_pose(self, data):
        # Callback para actualizar la posición actual de la tortuga
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def set_turtle_position(self, x, y):
        # Método para inicializar la posición de la tortuga
        goal_pose = Pose()
        goal_pose.x = float(x)
        goal_pose.y = float(y)

        distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        while distance > 0.1:
            dx = x - self.x
            dy = y - self.y
            angle_to_target = atan2(dy, dx)
            # Assuming constant speed for simplicity
            self.x += 0.1 * math.cos(angle_to_target)
            self.y += 0.1 * math.sin(angle_to_target)
            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            time.sleep(0.1)

    def set_turtle_color(self, r, g, b, width):
        # Método para cambiar el color de la tortuga
        set_pen = self.create_client(SetPen, '/turtle1/set_pen')
        request = SetPen.Request()
        request.r = r  # Color rojo
        request.g = g  # Color verde
        request.b = b  # Color azul
        request.width = width  # Grosor del lápiz
        request.off = 0  # Dibujar encendido
        future = set_pen.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    controller.main()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


        #fer un while true
        #llamar al spin_once para que haga constantemte al publisher y al reciber
        #self.change_color(190,255,0,15) #poner pincel verde
        #self.go_to_goal()



