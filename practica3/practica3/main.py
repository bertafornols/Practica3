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

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt

class TurtleController:

    def __init__(self):
        # Inicializar el nodo de ROS
        rospy.init_node('turtle_controller', anonymous=True)

        # Suscribirse al tópico de la posición de la tortuga
        rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        # Publicar en el tópico de control de velocidad para mover la tortuga
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        # Callback para actualizar la posición actual de la tortuga
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def set_turtle_position(self, x, y):
        # Función para mover la tortuga a una posición específica
        goal_pose = Pose()
        goal_pose.x = x
        goal_pose.y = y

        # Calcular la dirección hacia la posición objetivo
        dx = goal_pose.x - self.pose.x
        dy = goal_pose.y - self.pose.y
        distance = sqrt(dx**2 + dy**2)
        velocity = Twist()

        while distance > 0.1:
            # Calcular la velocidad lineal y angular para moverse hacia la posición objetivo
            velocity.linear.x = 1.5 * distance
            velocity.angular.z = 4 * (atan2(dy, dx) - self.pose.theta)
            
            # Publicar el comando de velocidad
            self.velocity_publisher.publish(velocity)
            
            # Actualizar la distancia a la posición objetivo
            dx = goal_pose.x - self.pose.x
            dy = goal_pose.y - self.pose.y
            distance = sqrt(dx**2 + dy**2)
            
            # Dormir durante un breve período para controlar la velocidad de la tortuga
            self.rate.sleep()

        # Una vez que la tortuga alcanza la posición objetivo, detenerla
        velocity.linear.x = 0
        velocity.angular.z = 0
        self.velocity_publisher.publish(velocity)



