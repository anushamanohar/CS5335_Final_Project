execute_process(COMMAND "/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_landmark_modules/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/anusha2631/CS5335_Final_Project/backup/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_landmark_modules/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
