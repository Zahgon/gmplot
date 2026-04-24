import math

from gmplot.drawables.polyline import _Polyline

class _Grid(object):
    def __init__(self, bounds, lat_increment, lng_increment, precision, **kwargs):
        '''
        Args:
            bounds (dict): Grid bounds, as a dict of the form
                ``{'north': float, 'south': float, 'east': float, 'west': float}``.
            lat_increment (float): Distance between latitudinal divisions.
            lng_increment (float): Distance between longitudinal divisions.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            color (str): Grid color. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            alpha (float): Opacity of the grid, ranging from 0 to 1.
            width (int): Width of the grid lines, in pixels.
        '''
        pass

    def write(self, w):
        '''
        Write the grid.

        Args:
            w (_Writer): Writer used to write the grid.
        '''
        pass
