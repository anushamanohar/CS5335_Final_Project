import matplotlib.pyplot as plt
from svgpathtools import svg2paths
from xml.etree import ElementTree as ET

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

def generate_waypoints(path, num_points=100):
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
            waypoints.append((point.real, point.imag))  # Convert complex to (x, y)
    return waypoints

def get_waypoints(unicode):
    path = extract_specific_glyph('/home/rover/Documents/rss_project/interbotix_ws/src/interbotix_keyboard_control/src/regularfont.svg', unicode)  # Replace with the unicode you want to extract
    if path:
        print(f"Extracted glyph for unicode {unicode}: {path}")
        
        # Generate waypoints
        waypoints = generate_waypoints(path, num_points=100)
        print(f"Generated waypoints: {waypoints}")

        return waypoints
    return None

# Example usage
#if __name__ == "__main__":
    svg_file = 'regularfont.svg'  # Replace with your SVG file path
    unicode = "c"
    path = extract_specific_glyph(svg_file, unicode)  # Replace with the unicode you want to extract
    if path:
        print(f"Extracted glyph for unicode {unicode}: {path}")
        
        # Generate waypoints
        waypoints = generate_waypoints(path, num_points=100)
        print(f"Generated waypoints: {waypoints}")
        
        # Plot the path
        #plot_from_path(path)
    else:
        print(f"No glyph found for unicode {unicode}")