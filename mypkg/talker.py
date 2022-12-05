#!/user/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self):   
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n=0
        node.create_timer(0.5,self.cb)

    def cd():
        msg=Int16()
        msd.data =taker.n
        self.pub.publish(meg)
        self.n+=1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)

