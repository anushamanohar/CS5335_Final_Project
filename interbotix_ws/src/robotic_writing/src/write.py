#!/usr/bin/env python3

from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
import numpy as np
from readsvg import ReadSVG

# The Writer class takes in a letter and send the waypoints to the robot.
class Writer:
    def __init__(self):
        self.arm = InterbotixRobot(robot_name="px150", mrd=mrd)
        self.reader = ReadSVG()

    # A parabolic function to control the x coordinate based on the y coordinate
    def map_y_to_x(self, y, y_min=-0.111, y_max=0.085, x_valley=0.2): #0.106
        y_peak = -0.013   # lowest point of x
        x_edge = 0.199   # highest x value at edges
        a = (x_edge - x_valley) / ((y_min - y_peak) ** 2)
        x = a * (y - y_peak) ** 2 + x_valley
        return np.round(x, 3)

    # Function to pen down (put the marker on to the white board)
    def pen_down(self, x_point, y_point, z_point, roll):
        self.arm.set_ee_pose_components(x=x_point, y=y_point,z=z_point, pitch=-1.5, roll=roll)

    # Function to pen up (lift the marker from the white board)
    def pen_up(self, x_point, y_point, z_point, roll):
        self.arm.set_ee_pose_components(x=x_point, y=y_point, z=z_point, pitch=-1.7, roll=roll)

    # The write function takes in a letter and sends the waypoints to the robot
    def write(self, letter, y_offset, z_offset, last):
        waypoints = self.reader.get_waypoints(letter)
        last_y = -100
        self.arm.close_gripper()
        self.arm.set_gripper_pressure(0.9)
        self.arm.set_ee_pose_components(z=0.4, pitch=-1.5)
        roll = 0.0
        for stroke in waypoints:
            self.pen_down(0.15, -(stroke[0][0]+y_offset), stroke[0][1]+z_offset, roll)
            for i in range(len(stroke)):
                roll = np.round(-4.26*-(stroke[i][0]+y_offset), 3) #-4.27
                x = self.map_y_to_x(-(stroke[i][0]+y_offset))
                print(x, -np.round(stroke[i][0]+y_offset, 3), stroke[i][1]+z_offset, roll)
                self.arm.set_ee_pose_components(x=x, y=-np.round(stroke[i][0]+y_offset, 3), z=stroke[i][1]+z_offset, roll=roll, pitch=-1.5)
                if last_y < -np.round(stroke[i][0]+y_offset, 3):
                    last_y = -np.round(stroke[i][0]+y_offset, 3)
            self.pen_up(0.15, -(stroke[-1][0]+y_offset), stroke[-1][1]+z_offset, roll)
        if last == True:
            self.arm.set_ee_pose_components(x=0, y=0, z=0.3, pitch=-1.5)
        return last_y

