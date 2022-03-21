"""
Configuration for Graph class.
mathplotlib is a library enabling creating graphs in python.
"""
import matplotlib.pyplot as plt

x = '4,5'
print(x.replace(",", "."))
class Graph:
    """Method responsible initialising object"""

    def __init__(self, x, y):
        self.x = self.replace_signs(x)
        self.y = self.replace_signs(y)

    def replace_signs(self, value):
        """Method responsible for ensuring proper input data"""
        if type(value) != str:
            return value
        val = []
        if type(value)==str:
            for ele in value:
                if ele == ',':
                    val.append('.')
                else:
                    val.append(ele)
        return float(value)

    def plot_graph(self):
        """Method responsible for drawing graphs"""
        return plt.plot(self.x, self.y)

    def name_the_x_axis(self, name):
        """Method responsible for naming the x axis of a given graph"""
        return plt.xlabel(name)

    def name_the_y_axis(self, name):
        """Method responsible for naming the y axis of a given graph"""
        return plt.ylabel(name)

    def title_the_graph(self, title):
        """Method responsible for assigning a graph title"""
        return plt.title(title)

    def show_the_plot(self):
        """Method responsible for displaying graph"""
        return plt.show()
