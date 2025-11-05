cmake_minimum_required(VERSION 3.5)
project(unitree_ros2_example)

if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

include_directories(include include/common include/nlohmann)
link_directories(src)

set(
  DEPENDENCY_LIST
  unitree_go
  unitree_hg
  unitree_api
  rclcpp
  std_msgs
  rosbag2_cpp
)

find_package(ament_cmake REQUIRED)
find_package(unitree_go REQUIRED)
find_package(unitree_hg REQUIRED)
find_package(unitree_api REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosbag2_cpp REQUIRED)
find_package(Eigen3 REQUIRED)

# --- EXECUTABLES ---
add_executable(low_level_ctrl src/low_level_ctrl.cpp src/common/motor_crc.cpp)
add_executable(low_level_ctrl_hg src/h1-2/lowlevel/low_level_ctrl_hg.cpp src/common/motor_crc_hg.cpp)
add_executable(g1_low_level_example src/g1/lowlevel/g1_low_level_example.cpp src/common/motor_crc_hg.cpp)
add_executable(read_low_state src/read_low_state.cpp)
add_executable(read_low_state_hg src/read_low_state_hg.cpp)
add_executable(read_motion_state src/read_motion_state.cpp)
add_executable(read_wireless_controller src/read_wireless_controller.cpp)

add_executable(go2_sport_client src/go2/go2_sport_client.cpp src/common/ros2_sport_client.cpp)
target_compile_features(go2_sport_client PRIVATE cxx_std_20)
add_executable(go2_stand_example src/go2/go2_stand_example.cpp src/common/motor_crc.cpp)
target_compile_features(go2_stand_example PRIVATE cxx_std_20)
add_executable(go2_robot_state_client src/go2/go2_robot_state_client.cpp src/common/motor_crc.cpp)
target_compile_features(go2_robot_state_client PRIVATE cxx_std_20)

add_executable(g1_arm_sdk_dds_example src/g1/high_level/g1_arm_sdk_dds_example.cpp src/common/motor_crc.cpp)
target_compile_features(g1_arm_sdk_dds_example PRIVATE cxx_std_20)
add_executable(g1_arm_action_example src/g1/high_level/g1_arm_action_example.cpp src/common/motor_crc.cpp)
target_compile_features(g1_arm_action_example PRIVATE cxx_std_20)
add_executable(g1_dex3_example src/g1/dex3/g1_dex3_example.cpp src/common/motor_crc.cpp)
target_compile_features(g1_dex3_example PRIVATE cxx_std_20)
add_executable(g1_loco_client_example src/g1/high_level/loco_client_example.cpp src/common/motor_crc.cpp)
target_compile_features(g1_loco_client_example PRIVATE cxx_std_20)
add_executable(g1_ankle_swing_example src/g1/lowlevel/g1_ankle_swing_example.cpp src/common/motor_crc_hg.cpp)
target_compile_features(g1_ankle_swing_example PRIVATE cxx_std_20)
add_executable(g1_audio_client_example src/g1/audio_client/g1_audio_client_example.cpp)
target_compile_features(g1_audio_client_example PRIVATE cxx_std_20)

add_executable(b2w_sport_client src/b2w/b2w_sport_client.cpp src/common/ros2_b2_sport_client.cpp)
target_compile_features(b2w_sport_client PRIVATE cxx_std_20)
add_executable(b2w_stand_example src/b2w/b2w_stand_example.cpp src/common/motor_crc.cpp)
target_compile_features(b2w_stand_example PRIVATE cxx_std_20)
add_executable(b2_stand_example src/b2/b2_stand_example.cpp src/common/motor_crc.cpp)
target_compile_features(b2_stand_example PRIVATE cxx_std_20)
add_executable(b2_sport_client src/b2/b2_sport_client.cpp src/common/ros2_b2_sport_client.cpp)
target_compile_features(b2_sport_client PRIVATE cxx_std_20)

# --- DEPENDENCJE ---
foreach(target
  low_level_ctrl
  low_level_ctrl_hg
  g1_low_level_example
  read_low_state
  read_low_state_hg
  read_motion_state
  read_wireless_controller
  go2_sport_client
  go2_stand_example
  go2_robot_state_client
  g1_arm_sdk_dds_example
  g1_arm_action_example
  g1_dex3_example
  g1_loco_client_example
  g1_ankle_swing_example
  g1_audio_client_example
  b2w_sport_client
  b2w_stand_example
  b2_sport_client
  b2_stand_example
)
  ament_target_dependencies(${target} ${DEPENDENCY_LIST})
endforeach()

target_include_directories(g1_dex3_example PRIVATE ${EIGEN3_INCLUDE_DIR})

# --- YAML-CPP OPCJONALNY ---
find_package(yaml-cpp QUIET)
if(yaml-cpp_FOUND AND ${yaml-cpp_VERSION} VERSION_GREATER_EQUAL "0.6")
  message(STATUS "Found yaml-cpp version ${yaml-cpp_VERSION}")
  add_executable(g1_dual_arm_example src/g1/lowlevel/g1_dual_arm_example.cpp src/common/motor_crc_hg.cpp)
  target_compile_features(g1_dual_arm_example PRIVATE cxx_std_20)
  ament_target_dependencies(g1_dual_arm_example yaml-cpp ${DEPENDENCY_LIST})
  install(TARGETS g1_dual_arm_example
    DESTINATION lib/${PROJECT_NAME})
else()
  message(STATUS "yaml-cpp too old or not found, skipping dual arm example.")
endif()

# --- INSTALACJA WSZYSTKICH NODEÓW ---
install(TARGETS
  low_level_ctrl
  low_level_ctrl_hg
  g1_low_level_example
  read_low_state
  read_low_state_hg
  read_motion_state
  read_wireless_controller
  go2_sport_client
  go2_stand_example
  go2_robot_state_client
  g1_arm_sdk_dds_example
  g1_arm_action_example
  g1_dex3_example
  g1_loco_client_example
  g1_ankle_swing_example
  g1_audio_client_example
  b2w_sport_client
  b2w_stand_example
  b2_sport_client
  b2_stand_example
  DESTINATION lib/${PROJECT_NAME}
)

# --- TESTY ---
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
