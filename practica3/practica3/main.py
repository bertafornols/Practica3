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

def set_turtle_position(self, x, y):
        # Método para inicializar la posición de la tortuga
        set_pen = self.create_client(SetPen, '/turtle1/set_pen')
        request = SetPen.Request()
        request.r = 0  # Color rojo
        request.g = 0  # Color verde
        request.b = 0  # Color azul
        request.width = 2  # Grosor del lápiz
        request.off = 1  # Dibujar apagado
        request.filling = 0  # No rellenar
        request.x = x  # Posición x
        request.y = y  # Posición y
        request.theta = 0  # Orientación theta
        future = set_pen.call_async(request)

    def set_turtle_color(self, r, g, b, width):
        # Método para cambiar el color de la tortuga
        set_pen = self.create_client(SetPen, '/turtle1/set_pen')
        request = SetPen.Request()
        request.r = r  # Color rojo
        request.g = g  # Color verde
        request.b = b  # Color azul
        request.width = width  # Grosor del lápiz
        request.off = 0  # Dibujar encendido
        request.filling = 1  # Rellenar
        request.x = 0  # Posición x (no afecta)
        request.y = 0  # Posición y (no afecta)
        request.theta = 0  # Orientación theta (no afecta)
        future = set_pen.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    controller.main()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

