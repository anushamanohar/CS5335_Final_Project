from xml.etree import ElementTree as ET
import numpy as np
import svgpathtools
from svgpathtools import parse_path
from visualize import Visualizer

# Class to extract the waypoints for a specific letter from the SVG file
class ReadSVG:

    def __init__(self):
        self.visualizer = Visualizer()
    # Function to extract the specific glyph from the font svg
    def extract_specific_glyph(self, svg_file, unicode):
        # Parse the SVG file
        tree = ET.parse(svg_file)
        root = tree.getroot()

        # Define the SVG namespace
        namespace = {'svg': 'http://www.w3.org/2000/svg'}

        # Search for the glyph with the specified unicode
        for glyph in root.findall('.//svg:glyph', namespace):
            if glyph.attrib.get('unicode') == unicode:
                d = glyph.attrib.get('d')  # Get the 'd' attribute (path data)
                if d:
                    # Convert the path data into a Path object
                    return parse_path(d)

        return None

    # Function to sort the waypoints to make the y-coordinate strictly increasing
    def sort_waypoints(self, waypoints):
        new_waypoints = []
        c = 0
        for stroke in waypoints:
            val = stroke[0][0]
            for i in range(1, len(stroke)):
                if stroke[i][0] < val:
                    c += 1
                    val = stroke[i][0]
                if c == 3:
                    stroke.reverse()
                    new_waypoints.append(stroke)
                    break
            else:
                new_waypoints.append(stroke)
        return new_waypoints
        

    def generate_adaptive_waypoints(self, path, min_points=3, max_points=10):
        """
        Generate waypoints with adaptive sampling.
        
        Args:
            path: The path object extracted from the SVG file.
            min_points: Minimum points per segment (for straight lines).
            max_points: Maximum points per segment (for curves).

        Returns:
            A list of waypoints as (x, y) tuples.
        """
        waypoints = []

        for segment in path:
            stroke = []
            if isinstance(segment, svgpathtools.Line):
                num_points = min_points
            else:
                num_points = max_points
            
            for t in np.linspace(0, 1, num_points):
                point = segment.point(t)
                p = (np.round(point.real / 15000, 3), np.round(point.imag / 15000, 3)) #15000
                stroke.append(p)
            if len(waypoints) != 0 and waypoints[-1][-1] == stroke[0]:
                for i in range(1, len(stroke)):
                    waypoints[-1].append(stroke[i]) 
            else:
                waypoints.append(stroke)
        #waypoints = self.sort_waypoints(waypoints)
        return waypoints

    # Function to extract the waypoints
    def get_waypoints(self, unicode):
        path = self.extract_specific_glyph('/home/rover/Documents/rss_project/interbotix_ws/src/robotic_writing/src/relief.svg', unicode)  # Replace with the unicode you want to extract
        if path:
            print(f"Extracted glyph for unicode {unicode}: {path}")
            
            # Generate waypoints
            waypoints = self.generate_adaptive_waypoints(path)

            return waypoints
        return None
