import math

from gmplot.drawables.polyline import _Polyline

_EARTH_RADIUS_IN_KM = 6378.8 # TODO: Avoid duplicating this constant.

class _Plus(object):
    def __init__(self, lat, lng, size, precision, **kwargs):
        '''
        Args:
            lat (float): Latitude of the center of the '+'.
            lng (float): Longitude of the center of the '+'.
            size (int): Size of the '+', in meters.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            color (str): Color of the '+'. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            alpha (float): Opacity of the '+', ranging from 0 to 1.
            width (int): Width of the '+''s edge, in pixels.
        '''
        pass

    def write(self, w):
        '''
        Write the '+'.

        Args:
            w (_Writer): Writer used to write the '+'.
        '''
        pass
