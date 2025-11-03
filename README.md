cd ~/unitree_ws/scripts/simulate_python
python3 ./unitree_mujoco.py

```bash
colcon build

source ~/unitree_ws/setup_local.sh
python3 ~/unitree_ws/scripts/simulate_python/unitree_mujoco.py

source ~/unitree_ws/setup_local.sh
rqt

#test hello_world
source ~/unitree_ws/setup_local.sh
python3 ~/unitree_ws/scripts/simulate_python/test/hello_world.py 

```