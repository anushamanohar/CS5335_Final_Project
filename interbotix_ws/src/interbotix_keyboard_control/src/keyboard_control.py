#!/usr/bin/env python3


from pynput import keyboard
import rospy
from std_msgs.msg import Float64

# Define publishers for each joint
waist_pub = rospy.Publisher('/px150/joint_commands/waist', Float64, queue_size=10)
shoulder_pub = rospy.Publisher('/px150/joint_commands/shoulder', Float64, queue_size=10)
elbow_pub = rospy.Publisher('/px150/joint_commands/elbow', Float64, queue_size=10)
wrist_angle_pub = rospy.Publisher('/px150/joint_commands/wrist_angle', Float64, queue_size=10)
wrist_rotate_pub = rospy.Publisher('/px150/joint_commands/wrist_rotate', Float64, queue_size=10)

def on_press(key):
    try:
        if key.char == 'w':  # Move waist clockwise
            waist_pub.publish(0.1)
        elif key.char == 's':  # Move waist counterclockwise
            waist_pub.publish(-0.1)
        elif key.char == 'a':  # Move shoulder up
            shoulder_pub.publish(0.1)
        elif key.char == 'd':  # Move shoulder down
            shoulder_pub.publish(-0.1)
        elif key.char == 'q':  # Move elbow up
            elbow_pub.publish(0.1)
        elif key.char == 'e':  # Move elbow down
            elbow_pub.publish(-0.1)
        elif key.char == 'r':  # Move wrist angle up
            wrist_angle_pub.publish(0.1)
        elif key.char == 'f':  # Move wrist angle down
            wrist_angle_pub.publish(-0.1)
        elif key.char == 't':  # Move wrist rotate clockwise
            wrist_rotate_pub.publish(0.1)
        elif key.char == 'g':  # Move wrist rotate counterclockwise
            wrist_rotate_pub.publish(-0.1)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
rospy.init_node('keyboard_control', anonymous=True)
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
