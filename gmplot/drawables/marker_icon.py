import os
import warnings

from gmplot.color import _get_hex_color
from gmplot.utility import _COLOR_ICON_PATH, _get_embeddable_image

class _MarkerIcon(object):
    def __init__(self, color):
        '''
        Args:
            color (str): Marker icon color. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
        '''
        pass

    def get_name(self):
        '''Get the name of the marker icon.'''
        pass
    
    def write(self, w, context):
        '''
        Write the marker icon (if it isn't already written).

        Args:
            w (_Writer): Writer used to write the marker icon.
            context (_Context): Context used to keep track of what was drawn to the map.
        '''
        pass
