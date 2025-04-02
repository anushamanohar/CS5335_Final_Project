import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='interbotix_keyboard_control',
            executable='keyboard_control.py',
            output='screen'
        )
    ])

