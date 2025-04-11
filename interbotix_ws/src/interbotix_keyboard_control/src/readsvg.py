import matplotlib.pyplot as plt
from svgpathtools import svg2paths
from xml.etree import ElementTree as ET
from visualize import Visualizer
import numpy as np
import svgpathtools

def extract_glyphs(svg_file):
    # Load SVG paths
    paths, attributes = svg2paths(svg_file)

    # Extract glyphs
    glyphs = []
    for path in paths:
        for segment in path:
            glyphs.append(segment)

    return glyphs

def extract_specific_glyph(svg_file, unicode):
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
                from svgpathtools import parse_path
                return parse_path(d)

    return None

def plot_from_path(path):
    # Create a new figure
    plt.figure()

    # Iterate through each segment in the path and plot it
    for segment in path:
        plt.plot([segment.start.real, segment.end.real], 
                 [segment.start.imag, segment.end.imag], color='black')

    # Set equal aspect ratio
    plt.axis('equal')
    
    # Show the plot
    plt.show()

def plot_svg(svg_file):
    # Load SVG paths
    paths, attributes = svg2paths(svg_file)

    # Create a new figure
    plt.figure()

    # Iterate through each path and plot it
    for path in paths:
        for segment in path:
            plt.plot([segment.start.real, segment.end.real], 
                 [segment.start.imag, segment.end.imag], color='black')

    # Set equal aspect ratio
    # plt.axis('equal')
    
    # Show the plot
    plt.show()

def generate_waypoints(path, num_points=50):
    """
    Generate waypoints from a path object.
    
    Args:
        path: The path object extracted from the SVG file.
        num_points: Number of waypoints to generate along the path.

    Returns:
        A list of waypoints as (x, y) tuples.
    """
    waypoints = []
    for segment in path:
        # Sample points along the segment
        for t in [i / num_points for i in range(num_points + 1)]:
            point = segment.point(t)
            waypoints.append((point.real/6000, point.imag/6000))  # Convert complex to (x, y)
    return waypoints

def sort_waypoints(waypoints):
    new_waypoints = []
    for stroke in waypoints:
        print(stroke)
        c = 0
        val = stroke[0][0]
        for i in range(1, len(stroke)):
            if stroke[i][0] < val:
                c += 1
                val = stroke[i][0]
            if c == 5:
                stroke.reverse()
                new_waypoints.append(stroke)
                break
        else:
            new_waypoints.append(stroke)
    return new_waypoints
    

def generate_adaptive_waypoints(path, min_points=4, max_points=20, curvature_threshold=0.01):
    """
    Generate waypoints with adaptive sampling.
    
    Args:
        path: The path object extracted from the SVG file.
        min_points: Minimum points per segment (for straight lines).
        max_points: Maximum points per segment (for curves).
        curvature_threshold: Threshold to decide if a segment is curved.

    Returns:
        A list of waypoints as (x, y) tuples.
    """
    waypoints = []

    def curvature(p0, p1, p2):
        """Compute the curvature given three points."""
        a = np.array([p0.real, p0.imag])
        b = np.array([p1.real, p1.imag])
        c = np.array([p2.real, p2.imag])

        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(np.clip(cosine_angle, -1, 1))  # Avoid numerical errors

        return angle  # Large angle means higher curvature

    for segment in path:
        stroke = []
        if isinstance(segment, svgpathtools.Line):
            num_points = min_points
        else:
            num_points = max_points
            #segment_points = [segment.point(t) for t in np.linspace(0, 1, 3)]
        
        # Compute curvature at the middle of the segment
            #k = curvature(segment_points[0], segment_points[1], segment_points[2])
        
        # Decide number of points based on curvature
            #if k < curvature_threshold:
                #num_points = min_points  # Straight lines get fewer points
            #else:
                #num_points = max_points  # Curved sections get more points
        
        for t in np.linspace(0, 1, num_points):
            point = segment.point(t)
            p = (np.round(point.real / 15000, 3), np.round(point.imag / 15000, 3))
            stroke.append(p)
        if len(waypoints) != 0 and waypoints[-1][-1] == stroke[0]:
            for i in range(1, len(stroke)):
                waypoints[-1].append(stroke[i]) 
        else:
            waypoints.append(stroke)
    waypoints = sort_waypoints(waypoints)
    print(waypoints)
    return waypoints

def get_waypoints(unicode):
    path = extract_specific_glyph('/home/rover/Documents/rss_project/interbotix_ws/src/interbotix_keyboard_control/src/relief.svg', unicode)  # Replace with the unicode you want to extract
    if path:
        print(f"Extracted glyph for unicode {unicode}: {path}")
        
        # Generate waypoints
        waypoints = generate_adaptive_waypoints(path)
        #print(f"Generated waypoints: {waypoints}")

        return waypoints
    return None

# Example usage
if __name__ == "__main__":
    svg_file = 'relief.svg'  # Replace with your SVG file path
    unicode = "N" # Replace with the unicode you want to extract
    visualizer = Visualizer()
    
    # Generate waypoints
    waypoints = get_waypoints(unicode)
    #print(f"Generated waypoints: {waypoints}")
    #f = 1000
    #for i in range(len(waypoints)):
        #waypoints[i] = (waypoints[i][0]/f, waypoints[i][1]/f)
    visualizer.visualize_waypoints(waypoints)
        
        # Plot the path
        #plot_from_path(path)