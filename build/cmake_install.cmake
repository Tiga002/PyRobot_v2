# Install script for directory: /home/developer/low_cost_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/developer/low_cost_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/developer/low_cost_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/developer/low_cost_ws/install" TYPE PROGRAM FILES "/home/developer/low_cost_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/developer/low_cost_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/developer/low_cost_ws/install" TYPE PROGRAM FILES "/home/developer/low_cost_ws/build/catkin_generated/installspace/env.sh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/developer/low_cost_ws/install/setup.bash;/home/developer/low_cost_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/developer/low_cost_ws/install" TYPE FILE FILES
    "/home/developer/low_cost_ws/build/catkin_generated/installspace/setup.bash"
    "/home/developer/low_cost_ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/developer/low_cost_ws/install/setup.sh;/home/developer/low_cost_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/developer/low_cost_ws/install" TYPE FILE FILES
    "/home/developer/low_cost_ws/build/catkin_generated/installspace/setup.sh"
    "/home/developer/low_cost_ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/developer/low_cost_ws/install/setup.zsh;/home/developer/low_cost_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/developer/low_cost_ws/install" TYPE FILE FILES
    "/home/developer/low_cost_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/developer/low_cost_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/developer/low_cost_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/developer/low_cost_ws/install" TYPE FILE FILES "/home/developer/low_cost_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/developer/low_cost_ws/build/gtest/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/create_autonomy/ca_tools/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/create_autonomy/create_autonomy/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench/dynamixel_workbench/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/ros_control/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/rqt_controller_manager/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/create_autonomy/ca_msgs/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/controller_manager_msgs/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench-msgs/dynamixel_workbench_msgs/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ar_track_alvar/ar_track_alvar_msgs/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/DynamixelSDK/ros/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench/dynamixel_workbench_toolbox/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench/dynamixel_workbench_single_manager/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench/dynamixel_workbench_single_manager_gui/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/create_autonomy/ca_description/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/hardware_interface/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/combined_robot_hw/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/controller_interface/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/controller_manager/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_description/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/controller_manager_tests/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/combined_robot_hw_tests/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench/dynamixel_workbench_controllers/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/dynamixel-workbench/dynamixel_workbench_operators/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_calibration/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_control/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/pyrobot_bridge/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/create_autonomy/ca_driver/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_gazebo/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_navigation/orb_slam2_ros/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ar_track_alvar/ar_track_alvar/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/transmission_interface/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/thirdparty/ros_control/joint_limits_interface/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_lite_moveit_config/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_moveit_config/cmake_install.cmake")
  include("/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_navigation/base_navigation/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/developer/low_cost_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
