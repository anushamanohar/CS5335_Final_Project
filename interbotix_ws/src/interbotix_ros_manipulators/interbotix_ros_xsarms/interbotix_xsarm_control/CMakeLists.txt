cmake_minimum_required(VERSION 3.10)
project(interbotix_xsarm_control)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  interbotix_xs_sdk
  interbotix_xs_modules
  interbotix_xsarm_descriptions
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
catkin_package(
CATKIN_DEPENDS interbotix_xs_sdk interbotix_xs_modules interbotix_xsarm_descriptions
)
