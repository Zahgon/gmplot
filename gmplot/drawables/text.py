from gmplot.color import _get_hex_color
from gmplot.utility import _COLOR_ICON_PATH, _format_LatLng, _get_embeddable_image

class _Text(object):    
    def __init__(self, lat, lng, text, precision, **kwargs):
        '''
        Args:
            lat (float): Latitude of the text label.
            lng (float): Longitude of the text label.
            text (str): Text to display.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            color (str): Text color. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            font_size (int): Font size in pixels.
        '''
        pass

    def write(self, w):
        '''
        Write the text.

        Args:
            w (_Writer): Writer used to write the text.
        '''
        pass
