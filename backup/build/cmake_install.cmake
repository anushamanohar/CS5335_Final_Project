# Install script for directory: /home/anusha2631/CS5335_Final_Project/backup/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/anusha2631/CS5335_Final_Project/backup/install")
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

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/anusha2631/CS5335_Final_Project/backup/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/anusha2631/CS5335_Final_Project/backup/install" TYPE PROGRAM FILES "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/_setup_util.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/anusha2631/CS5335_Final_Project/backup/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/anusha2631/CS5335_Final_Project/backup/install" TYPE PROGRAM FILES "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/env.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/anusha2631/CS5335_Final_Project/backup/install/setup.bash;/home/anusha2631/CS5335_Final_Project/backup/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/anusha2631/CS5335_Final_Project/backup/install" TYPE FILE FILES
    "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/setup.bash"
    "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/anusha2631/CS5335_Final_Project/backup/install/setup.sh;/home/anusha2631/CS5335_Final_Project/backup/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/anusha2631/CS5335_Final_Project/backup/install" TYPE FILE FILES
    "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/setup.sh"
    "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/anusha2631/CS5335_Final_Project/backup/install/setup.zsh;/home/anusha2631/CS5335_Final_Project/backup/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/anusha2631/CS5335_Final_Project/backup/install" TYPE FILE FILES
    "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/setup.zsh"
    "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/anusha2631/CS5335_Final_Project/backup/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/anusha2631/CS5335_Final_Project/backup/install" TYPE FILE FILES "/home/anusha2631/CS5335_Final_Project/backup/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/anusha2631/CS5335_Final_Project/backup/build/gtest/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_common_modules/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_common_toolbox/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_ros_xsarms/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_ros_xsarms_examples/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_core/interbotix_ros_xseries/interbotix_ros_xseries/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_toolbox/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_moveit/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_core/interbotix_ros_xseries/interbotix_xs_msgs/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_core/interbotix_ros_xseries/dynamixel_workbench_toolbox/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_keyboard_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_landmark_modules/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_tf_tools/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_core/interbotix_ros_xseries/interbotix_xs_sdk/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_rviz/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_descriptions/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_moveit/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_examples/interbotix_moveit_interface/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_sdk/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_examples/interbotix_diagnostic_tool/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_examples/interbotix_joy_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_examples/interbotix_pid_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_examples/interbotix_puppet_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_examples/interbotix_turret_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_descriptions/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_diagnostic_tool/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_dual/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_joy/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_dual_joy/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_pid/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_puppet/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_arms/interbotix_gazebo/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_ros_control/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_gazebo/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_moveit_interface/cmake_install.cmake")
  include("/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_ros_control/cmake_install.cmake")

endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/anusha2631/CS5335_Final_Project/backup/build/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/anusha2631/CS5335_Final_Project/backup/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
