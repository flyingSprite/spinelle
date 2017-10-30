

# plot a sine wave from 0 to 4pi
import pylab as lib


class DifferentCharts(object):

    @staticmethod
    def draw_sin_chart():
        x_values = lib.arange(0.0, lib.math.pi * 4, 0.01)
        y_values = lib.sin(x_values)
        lib.plot(x_values, y_values, linewidth=1.0)
        lib.xlabel('x')
        lib.ylabel('sin(x)')
        lib.title('Simple plot')
        # If show grid lines in chart
        lib.grid(True)
        lib.savefig("sin.png")
        lib.show()

    @staticmethod
    def draw_cos_chart():
        x_values = lib.arange(0.0, lib.math.pi * 4, 0.01)
        y_values = lib.cos(x_values)
        lib.plot(x_values, y_values, linewidth=1.0)
        lib.xlabel('x')
        lib.ylabel('sin(x)')
        lib.title('Simple plot')
        # If show grid lines in chart
        lib.grid(True)
        lib.savefig("sin.png")
        lib.show()


DifferentCharts.draw_sin_chart()
DifferentCharts.draw_cos_chart()

