import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listner():
        def __init__(self):
            self.pub = node.create_subscription(Int16,"countup",self.cd,10)
    def cd(msg):
            global node
            node.get_logger().info("Listen: %d" % msg.data)
def main():
    rclpy.init()
    node = Node("listner")
    rclpy.spin(node)

