import matplotlib.pyplot as plt

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