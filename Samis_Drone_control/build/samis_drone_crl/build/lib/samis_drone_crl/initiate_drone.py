# tello_controller_node.py
import rclpy
from std_msgs.msg import String
from djitellopy import Tello

def tello_control_callback(msg):
    command = msg.data
    # Implement security measures and control logic here
    tello.send_command(command)

def tello_node():
    rclpy.init()
    node = rclpy.create_node('tello_node')
    subscriber = node.create_subscription(String, 'tello_control', tello_control_callback, 10)
    tello = Tello()
    tello.connect()
    tello.takeoff()

    tello.move_left(100)
    tello.rotate_counter_clockwise(90)
    tello.move_forward(100)

    tello.land()
   # try:
    #    tello.connect()
     #   tello.takeoff()
      #  node.get_logger().info('Tello connected and taken off.')
       # rclpy.spin(node)
    #finally:
     #   tello.land()
      #  tello.end()"""

if __name__ == '__main__':
    tello = Tello()
    tello_node()
