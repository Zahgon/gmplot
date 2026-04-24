from gmplot.color import _get_hex_color
from gmplot.utility import _format_LatLng

class _Polyline(object):
    def __init__(self, lats, lngs, precision, **kwargs):
        '''
        Args:
            lats ([float]): Latitudes.
            lngs ([float]): Longitudes.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            color (str): Color of the polyline. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            alpha (float): Opacity of the polyline, ranging from 0 to 1.
            width (int): Width of the polyline, in pixels.
        '''
        pass

    def write(self, w):
        '''
        Write the polyline.

        Args:
            w (_Writer): Writer used to write the polyline.
        '''
        pass
