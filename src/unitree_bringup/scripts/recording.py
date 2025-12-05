#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import yaml
import threading

class MotionRecorder(Node):
    def __init__(self):
        super().__init__('motion_recorder')

        self.joint_history = []
        self.lock = threading.Lock()

        self.sub = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_callback,
            10
        )

        self.get_logger().info(">>> Rozpoczęto nagrywanie /joint_states ...")

    def joint_callback(self, msg):
        with self.lock:
            # kopiujemy dane aby uniknąć problemów z mutacją list
            self.joint_history.append(list(msg.position))

    def save_to_yaml(self, filename="motion_seq.yaml"):
        if len(self.joint_history) == 0:
            self.get_logger().warn("Brak nagranych danych – plik nie został zapisany.")
            return

        data = {
            'type': 'CompositeSeq',
            'content': 'BodyMotion',
            'frame_rate': 50,
            'num_frames': len(self.joint_history),
            'components': [
                {
                    'type': 'MultiValueSeq',
                    'content': 'JointDisplacement',
                    'frame_rate': 50,
                    'num_frames': len(self.joint_history),
                    'num_parts': len(self.joint_history[0]),
                    'frames': self.joint_history
                }
            ]
        }

        with open(filename, 'w') as f:
            yaml.dump(data, f)

        self.get_logger().info(f">>> Zapisano plik: {filename}")

def main():
    rclpy.init()
    node = MotionRecorder()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\n>>> Nagrywanie zatrzymane (CTRL+C)")
    finally:
        # zapis po przerwaniu
        node.save_to_yaml("motion_seq.yaml")
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
