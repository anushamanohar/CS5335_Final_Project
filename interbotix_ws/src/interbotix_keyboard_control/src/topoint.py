#!/usr/bin/env python3

from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd


arm = InterbotixRobot(robot_name="px150", mrd=mrd)
#arm.open_gripper()
#arm.close_gripper()
#arm.set_ee_pose_components(0.3, 0.3)
#arm.set_joint_positions([0, 0, 0, 1.5, 0]) 
#l = [0.496, -0.251, -0.389, 1.637, -0.345]
#arm.set_joint_positions(l)
l = arm.get_joint_positions()
print(l)
for i in range(50):
    x = float(input("Input the x-coordinate: "))
    y = float(input("Input the y coordinate: "))
    z = float(input("Input the z coordinate: "))
    p = float(input("Input the pitch"))
    arm.set_ee_pose_components(x=x, y=y, z=z, pitch=p)
    #if x == '0' and z == '0' and y == '0':
        #arm.go_to_sleep_pose()
        #break

    #arm.set_ee_pose_components(x=float(x), y=float(y), z=float(z), pitch=float(p))
    #arm.set_single_joint_position('wrist_angle', 1.7)
    

    #0.3 0.0 0.06
    #0.27 0.0 0.08
