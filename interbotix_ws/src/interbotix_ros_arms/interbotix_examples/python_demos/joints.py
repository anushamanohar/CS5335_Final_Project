#!/usr/bin/env python3
import rospy
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
from pynput import keyboard
import time

def joint_manual_test():
  
    # Initialize robot
    arm = InterbotixRobot(robot_name="px150", mrd=mrd)

    # Joint control parameters
    global step_size  # Declare it global
    step_size = 0.1  # radians for arm joints
    gripper_step = 2  # mm for gripper

    current_positions = {
        'waist': 0,
        'shoulder': 0,
        'elbow': 0,
        'wrist_angle': 0,
        'wrist_rotate': 0,
        'gripper': 0
    }

    # Display control scheme
    print("""
    PX150 MANUAL JOINT TESTER
    -------------------------
    Controls:
    1/Q - Waist +/-
    2/W - Shoulder +/-
    3/E - Elbow +/-
    4/R - Wrist Angle +/-
    5/T - Wrist Rotate +/-
    G/H - Gripper Open/Close
    Z/X - Increase/Decrease Step Size
    ESC - Exit
    """)

    def on_press(key):
        global step_size  # Declare as global inside the function

        try:
            if key.char == '1':
                current_positions['waist'] += step_size
                arm.set_single_joint_position('waist', current_positions['waist'])
                print(f"Waist: {current_positions['waist']:.2f} rad")

            if key.char == 'q':
                current_positions['waist'] -= step_size
                arm.set_single_joint_position('waist', current_positions['waist'])
                print(f"Waist: {current_positions['waist']:.2f} rad")

            if key.char == '2':
                current_positions['shoulder'] += step_size
                arm.set_single_joint_position('shoulder', current_positions['shoulder'])
                print(f"Shoulder: {current_positions['shoulder']:.2f} rad")

            if key.char == 'w':
                current_positions['shoulder'] -= step_size
                arm.set_single_joint_position('shoulder', current_positions['shoulder'])
                print(f"Shoulder: {current_positions['shoulder']:.2f} rad")

            if key.char == '3':
                current_positions['elbow'] += step_size
                arm.set_single_joint_position('elbow', current_positions['elbow'])
                print(f"Elbow: {current_positions['elbow']:.2f} rad")

            if key.char == 'e':
                current_positions['elbow'] -= step_size
                arm.set_single_joint_position('elbow', current_positions['elbow'])
                print(f"Elbow: {current_positions['elbow']:.2f} rad")

            if key.char == '4':
                current_positions['wrist_angle'] += step_size
                arm.set_single_joint_position('wrist_angle', current_positions['wrist_angle'])
                print(f"Wrist Angle: {current_positions['wrist_angle']:.2f} rad")

            if key.char == 'r':
                current_positions['wrist_angle'] -= step_size
                arm.set_single_joint_position('wrist_angle', current_positions['wrist_angle'])
                print(f"Wrist Angle: {current_positions['wrist_angle']:.2f} rad")

            if key.char == '5':
                current_positions['wrist_rotate'] += step_size
                arm.set_single_joint_position('wrist_rotate', current_positions['wrist_rotate'])
                print(f"Wrist Rotate: {current_positions['wrist_rotate']:.2f} rad")

            if key.char == 't':
                current_positions['wrist_rotate'] -= step_size
                arm.set_single_joint_position('wrist_rotate', current_positions['wrist_rotate'])
                print(f"Wrist Rotate: {current_positions['wrist_rotate']:.2f} rad")

            if key.char == 'g':
                arm.open_gripper()
                print("Gripper Opened")

            if key.char == 'h':
                arm.close_gripper()
                print("Gripper Closed")

            if key.char == 'z':
                step_size = min(0.3, step_size + 0.02)
                print(f"New step size: {step_size:.2f} rad")

            if key.char == 'x':
                step_size = max(0.02, step_size - 0.02)
                print(f"New step size: {step_size:.2f} rad")

        except AttributeError:
            if key == keyboard.Key.esc:
                print("\nExiting...")
                arm.go_to_sleep_pose()
                return False  # Stops the listener

    # Start listening for keyboard input
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    joint_manual_test()

