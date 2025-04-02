#!/usr/bin/env python3

from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd


arm = InterbotixRobot(robot_name="px150", mrd=mrd)
#arm.open_gripper()
#arm.close_gripper()
arm.set_ee_pose_components(0.3, 0.3)

for i in range(50):
    x = input("Input the x-coordinate: ")
    #y = input("Input the y coordinate: ")
    z = input("Input the z coordinate: ")
    #z = input("Input the z coordinate: ")
    if x == '0' and z == '0':
        arm.go_to_sleep_pose()

    arm.set_ee_cartesian_trajectory(x=float(x), z=float(z))
