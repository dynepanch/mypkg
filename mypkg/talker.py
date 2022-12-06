#!/user/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self,node_ref):   
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n=0
        node_ref.create_timer(0.5,self.cb)

    def cd(self):
        msg=Int16()
        msd.data =taker.n
        self.pub.publish(meg)
        self.n+=1
def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)
if __name__ == '__main__':
    main()
