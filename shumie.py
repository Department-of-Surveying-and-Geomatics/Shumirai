import pandas as pd
import matplotlib.pyplot as plt


class Point:
    """
    A class representing a point with x,y coordinates.
    """

    def __init__(self, x, y):
        """
        Initialize the Point object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = float(x)  # Convert x to float
        self.y = float(y)  # Convert y to float

    def translate(self, dx, dy):
        """
        translate the point by a given dy and dx values.

        Args:
            dx (float): The displacement in the x direction.
            dy (float): The displacement in the y direction.
        """
        self.x += dx
        self.y += dy


def plot_points(points, color='green'):
    """
    Plot a list of points on a scatterplot.
     Reads the coordinates from a text file, plots them on a scatterplot,
    moves the points, and replots them in a different color.
    Args:
        points (list): List of Point objects.
        color (str): Color of the plotted points. Default is 'green'.
    """
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]

    plt.scatter(x_values, y_values, color=color)


# import coordinates from csv file
file_path = 'coordinate_file.csv'

# Read the data from the file using pandas, skipping the header row
data = pd.read_csv(file_path, skiprows=1, names=['x', 'y'], delimiter=', ')

# Create Point objects from the data
points = [Point(row['x'], row['y']) for _, row in data.iterrows()]

# Plotting the points
plot_points(points, color='green')

# Translate the points by a given dy and dx values
dx = 5
dy = 1
translated_points = [Point(point.x + dx, point.y + dy) for point in points]

# Plotting the translated points in different color
plot_points(translated_points, color='purple')

# customize scatter plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')

# Display the plot
plt.show()