from gmplot.color import _get_hex_color
from gmplot.utility import _format_LatLng

class _Circle(object):
    def __init__(self, lat, lng, radius, precision, **kwargs):
        '''
        Args:
            lat (float): Latitude of the center of the circle.
            lng (float): Longitude of the center of the circle.
            radius (int): Radius of the circle, in meters.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            edge_color (str): Color of the circle's edge. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            edge_alpha (float): Opacity of the circle's edge, ranging from 0 to 1.
            edge_width (int): Width of the circle's edge, in pixels.
            face_color (str): Color of the circle's face. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            face_alpha (float): Opacity of the circle's face, ranging from 0 to 1.
        '''
        pass

    def write(self, w):
        '''
        Write the circle.

        Args:
            w (_Writer): Writer used to write the circle.
        '''
        pass
