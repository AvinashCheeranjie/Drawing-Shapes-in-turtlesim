import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleCircle(Node):
    """To draw a circle in turtlesim"""
    def __init__(self):
        super().__init__('turtle_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_circle()

    def draw_circle(self):
        vel_msg = Twist()
        vel_msg.linear.x = 2.0  # Set linear velocity to 2.0
        vel_msg.angular.z = 1.0  # Set angular velocity to 1.0 rad/s

        self.get_logger().info('Drawing a circle...')

        start_time = time.time()
        while time.time() - start_time < 8:
            self.publisher_.publish(vel_msg)
            time.sleep(0.1)  # Sleep for a short period

        # Stop the turtle after 8 seconds
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        self.publisher_.publish(vel_msg)
        self.get_logger().info('Circle drawn!')

def main(args=None):
    rclpy.init(args=args)
    turtle_circle = TurtleCircle()
    rclpy.spin(turtle_circle)
    turtle_circle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
