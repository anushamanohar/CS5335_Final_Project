import matplotlib.pyplot as plt
from svgpathtools import svg2paths

class Visualizer():
    def visualize_waypoints(self, waypoints):
        x_vals = [i[0] for i in waypoints]
        y_vals = [i[1] for i in waypoints]

        plt.figure()

        plt.scatter(x_vals, y_vals, color='r')

        plt.xlabel("x")
        plt.ylabel("y")

        plt.show()

    def visualize_img(self, img):
        plt.imshow(img)

    def plot_x_y(self, x, y):
        plt.plot(x, y, 'o', label="Original Points")
        plt.plot(x, y, '-', label="Smoothed Curve")
        plt.legend()
        plt.axis("equal")
        plt.show()

    def plot_from_path(self, path):
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

    def plot_svg(self, svg_file):
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
