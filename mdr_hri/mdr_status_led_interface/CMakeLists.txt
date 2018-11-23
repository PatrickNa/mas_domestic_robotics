cmake_minimum_required(VERSION 2.8.3)
project(mdr_status_led_interface)

find_package(catkin REQUIRED
  COMPONENTS
    rospy
)

catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS
    std_msgs
)

#############
## Install ##
#############
install(PROGRAMS
  ros/scripts/status_led_interface
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
