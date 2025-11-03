#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from unitree_hg.msg import LowCmd, MotorCmd

class LowCmdPublisher(Node):
    def __init__(self):
        super().__init__('lowcmd_pub')
        self.publisher_ = self.create_publisher(LowCmd, '/lowcmd', 10)
        self.timer = self.create_timer(0.01, self.publish_lowcmd)  # 100 Hz

    def publish_lowcmd(self):
        msg = LowCmd()
        msg.mode_pr = 0
        msg.mode_machine = 0

        # motor_cmd ma już 35 elementów – trzeba przypisać po indeksach
        for i in range(35):
            msg.motor_cmd[i].mode = 3   # tryb momentu
            msg.motor_cmd[i].q = 0.0
            msg.motor_cmd[i].dq = 0.0
            msg.motor_cmd[i].tau = 0.0  # mocny moment
            msg.motor_cmd[i].kp = 0.0
            msg.motor_cmd[i].kd = 0.0
            msg.motor_cmd[i].reserve = 0
        for i in range(1):
            msg.motor_cmd[i].mode = 3   # tryb momentu
            msg.motor_cmd[i].q = 0.0
            msg.motor_cmd[i].dq = 0.0
            msg.motor_cmd[i].tau = 5.0  # mocny moment
            msg.motor_cmd[i].kp = 10.0
            msg.motor_cmd[i].kd = 0.5
            msg.motor_cmd[i].reserve = 0

        msg.reserve = [0, 0, 0, 0]
        msg.crc = 0

        self.publisher_.publish(msg)
        self.get_logger().info('Published strong LowCmd')

def main(args=None):
    rclpy.init(args=args)
    node = LowCmdPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
