import matplotlib.pyplot as plt
import numpy as np


class Graphic:
    def drawPlot(self, years, growth, profit):
        plt.scatter(years, profit, label="net profit percentage", marker="o")
        plt.xlabel("years")
        plt.ylabel("percentage")
        plt.scatter(years[1:], growth, label="growth percentage", marker="o")
        plt.legend()
        plt.show()
