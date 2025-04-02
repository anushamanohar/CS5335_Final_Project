#!/usr/bin/env python3

from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
import numpy as np
from readsvg import get_waypoints
from waypoints import waypoints_generator

text = "A"

print("Generating waypoints")
#obj = waypoints_generator()

#waypoints = obj.get_waypoints(text)
waypoints = get_waypoints("a")
print(waypoints)
print("Waypoints generated")
arm = InterbotixRobot(robot_name="px150", mrd=mrd)
print("Sending waypoints to the arm")
print("Number of waypoints", len(waypoints))
for i in waypoints[:10]:
    print(i[0]/1000)
    print(i[1]/1000)
    arm.set_ee_pose_components(x=i[0]/1000, y=i[1]/1000)

