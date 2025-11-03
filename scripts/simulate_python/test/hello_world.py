import time
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.core.channel import ChannelPublisher, ChannelSubscriber
from unitree_sdk2py.idl.default import std_msgs_msg_dds__String_


def HelloHandler(msg):
    print("📩 Received:", msg.data)


if __name__ == "__main__":
    # Ustaw interfejs sieciowy (np. eth0, enp3s0, wlp4s0)
    ChannelFactoryInitialize(1, "wlp4s0")

    # ⚙️ Utwórz typ wiadomości IDL
    String = std_msgs_msg_dds__String_()  # <--- tu były nawiasy!

    # 🔄 Subskrybent
    subscriber = ChannelSubscriber("rt/hello_world", String.__class__)
    subscriber.Init(HelloHandler, 10)

    # 📤 Publisher
    publisher = ChannelPublisher("rt/hello_world", String.__class__)
    publisher.Init()

    msg = String
    counter = 0
    while True:
        msg.data = f"Hello World {counter}"
        publisher.Write(msg)
        print("🚀 Published:", msg.data)
        counter += 1
        time.sleep(1.0)
