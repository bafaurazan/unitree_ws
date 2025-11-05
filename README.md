
## Links
- [unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco)
- [unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python)

# prepare simulation
```bash

#unitree_sdk2_python installation
cd ~
sudo apt install python3-pip
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd unitree_sdk2_python
pip3 install -e .
pip3 install mujoco
pip3 install pygame

#run simulation
python3 ~/unitree_ws/scripts/simulate_python/unitree_mujoco.py

#test
python3 ~/unitree_ws/scripts/simulate_python/test/test_unitree_sdk2.py 

```

# test simulation with ros2
```bash
colcon build

#run simulation
source ~/unitree_ws/setup_local.sh
python3 ~/unitree_ws/scripts/simulate_python/unitree_mujoco.py

#visualize data
source ~/unitree_ws/setup_local.sh
rqt

#test pure dds hello_world with ros2
source ~/unitree_ws/setup_local.sh
python3 ~/unitree_ws/scripts/simulate_python/test/hello_world.py 

#test moving all motors (only for simulation)
source ~/unitree_ws/setup_local.sh
ros2 run unitree_bringup g1_test.py

#test read data
source ~/unitree_ws/setup_local.sh
ros2 run unitree_ros2_example read_low_state_hg

#test move 
source ~/unitree_ws/setup_local.sh
ros2 run unitree_ros2_example g1_ankle_swing_example 

source ~/unitree_ws/setup_local.sh
ros2 run unitree_ros2_example g1_low_level_example 

```