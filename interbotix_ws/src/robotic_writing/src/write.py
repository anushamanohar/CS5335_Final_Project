#!/usr/bin/env python3

from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
import numpy as np
from readsvg import get_waypoints
#from waypoints import waypoints_generator
from visualize import Visualizer
import time


class Writer:
    def __init__(self):
        self.arm = InterbotixRobot(robot_name="px150", mrd=mrd)

    def map_y_to_x(self, y, y_min=-0.111, y_max=0.085, x_valley=0.2): #0.106
        y_peak = -0.013   # lowest point of x
        x_edge = 0.199   # highest x value at edges

    # Calculate 'a' so the parabola matches the desired edge height
        a = (x_edge - x_valley) / ((y_min - y_peak) ** 2)

    # Normal parabola: minimum at y_peak
        x = a * (y - y_peak) ** 2 + x_valley
        return np.round(x, 3)

#vis_obj.visualize_waypoints(waypoints)


    def pen_down(self, x_point, y_point, z_point, roll):
        self.arm.set_ee_pose_components(x=x_point, y=y_point,z=z_point, pitch=-1.5, roll=roll)

    def pen_up(self, x_point, y_point, z_point, roll):
        self.arm.set_ee_pose_components(x=x_point, y=y_point, z=z_point, pitch=-1.7, roll=roll)

    def write(self, letter, y_offset, z_offset, last):
        waypoints = get_waypoints(letter)
        last_y = -100
        self.arm.close_gripper()
        self.arm.set_gripper_pressure(0.9)
        print("Sending waypoints to the arm")
        print(waypoints)
        print("Number of strokes", len(waypoints))
        self.arm.set_ee_pose_components(z=0.4, pitch=-1.5)
        roll = 0.0
        for stroke in waypoints:
            self.pen_down(0.15, -(stroke[0][0]+y_offset), stroke[0][1]+z_offset, roll)
            print(stroke)
            for i in range(len(stroke)):
                roll = np.round(-4.26*-(stroke[i][0]+y_offset), 3) #-4.27
                x = self.map_y_to_x(-(stroke[i][0]+y_offset))
                print(x, -np.round(stroke[i][0]+y_offset, 3), stroke[i][1]+z_offset, roll)
                self.arm.set_ee_pose_components(x=x, y=-np.round(stroke[i][0]+y_offset, 3), z=stroke[i][1]+z_offset, roll=roll, pitch=-1.5)
                if last_y < -np.round(stroke[i][0]+y_offset, 3):
                    last_y = -np.round(stroke[i][0]+y_offset, 3)
            self.pen_up(0.15, -(stroke[-1][0]+y_offset), stroke[-1][1]+z_offset, roll)
        print(last)
        if last == True:
            self.arm.set_ee_pose_components(x=0, y=0, z=0.3, pitch=-1.5)
        return last_y

