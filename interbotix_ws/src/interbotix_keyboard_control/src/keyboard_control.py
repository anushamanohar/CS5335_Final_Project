#!/usr/bin/env python3


from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
from pynput import keyboard
import numpy as np

# Initialize the Robot Arm
arm = InterbotixRobot(robot_name="px150", mrd=mrd)

# Movement step size
STEP = 0.01  # Adjust as needed
ROTATION_STEP = 0.05  # Rotation step for pitch/yaw

# Current EE Pose
ee_pose = {"x": 0.3, "y": 0.0, "z": 0.06, "pitch": 0.0}
waist_angle = 0.0

def move_ee(dx=0, dy=0, dz=0, dp=0):
    global ee_pose
    ee_pose["x"] += dx
    ee_pose["y"] += dy
    ee_pose["z"] += dz
    ee_pose["pitch"] += dp
    arm.set_ee_pose_components(x=ee_pose["x"], y=ee_pose["y"], z=ee_pose["z"], pitch=ee_pose["pitch"])
    print(f"EE Position: X={ee_pose['x']:.3f}, Y={ee_pose['y']:.3f}, Z={ee_pose['z']:.3f}, Pitch={ee_pose['pitch']:.2f}")

def move_waist(angle):
    global waist_angle
    waist_angle += angle
    arm.set_single_joint_position("waist", waist_angle)
    print(f"Waist Angle: {waist_angle:.2f} radians")

def on_press(key):
    try:
        if key.char == 'w':  # Move forward
            move_ee(dx=STEP)
        elif key.char == 's':  # Move backward
            move_ee(dx=-STEP)
        elif key.char == 'a':  # Move left
            move_ee(dy=-STEP)
        elif key.char == 'd':  # Move right
            move_ee(dy=STEP)
        elif key.char == 'q':  # Move up
            move_ee(dz=STEP)
        elif key.char == 'e':  # Move down
            move_ee(dz=-STEP)
        elif key.char == 'i':  # Rotate pitch up
            move_ee(dp=ROTATION_STEP)
        elif key.char == 'k':  # Rotate pitch down
            move_ee(dp=-ROTATION_STEP)
        elif key.char == 'j':  # Rotate waist left
            move_waist(-ROTATION_STEP)
        elif key.char == 'l':  # Rotate waist right
            move_waist(ROTATION_STEP)
        elif key.char == 'o':  # Open gripper
            arm.open_gripper()
            print("Gripper Opened")
        elif key.char == 'c':  # Close gripper
            arm.close_gripper()
            print("Gripper Closed")
        elif key.char == 'h':  # Move to Home Position
            arm.go_to_home_pose()
            print("Moved to Home Position")
        elif key.char == 't':  # Move to Sleep Position
            arm.go_to_sleep_pose()
            print("Moved to Sleep Position")
        elif key.char == 'p':
            x_val = input("X coordinate: ")
            z_val = input("Z coordinate: ")
            arm.set_ee__pose_components(x=float(x_val), z=float(z_val))
    except AttributeError:
        if key == keyboard.Key.esc:  # Exit program
            print("Exiting Program...")
            return False

def main():
    print("Keyboard Control for Pincher X150")
    print("Controls:")
    print(" W/S - Move Forward/Backward")
    print(" A/D - Move Left/Right")
    print(" Q/E - Move Up/Down")
    print(" I/K - Rotate Pitch Up/Down")
    print(" J/L - Rotate Waist Left/Right")
    print(" O - Open Gripper")
    print(" C - Close Gripper")
    print(" H - Move to Home Position")
    print(" T - Move to Sleep Position")
    print(" ESC - Quit")

    # Move arm to a safe starting position
    

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    arm.go_to_sleep_pose()  # Move to sleep pose before exiting

if __name__ == "__main__":
    main()


