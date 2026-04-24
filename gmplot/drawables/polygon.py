from gmplot.color import _get_hex_color
from gmplot.utility import _format_LatLng

class _Polygon(object):
    def __init__(self, lats, lngs, precision, **kwargs):
        '''
        Args:
            lats ([float]): Latitudes.
            lngs ([float]): Longitudes.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            edge_color (str): Color of the polygon's edge. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            edge_alpha (float): Opacity of the polygon's edge, ranging from 0 to 1.
            edge_width (int): Width of the polygon's edge, in pixels.
            face_color (str): Color of the polygon's face. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            face_alpha (float): Opacity of the polygon's face, ranging from 0 to 1.
        '''
        pass

    def write(self, w):
        '''
        Write the polygon.

        Args:
            w (_Writer): Writer used to write the polygon.
        '''
        pass
