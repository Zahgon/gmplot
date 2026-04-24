from gmplot.drawables.symbols.circle import _Circle
from gmplot.drawables.symbols.plus import _Plus
from gmplot.drawables.symbols.x import _X

class _Symbol(object):
    _SHAPES = {
        'o': _Circle,
        '+': _Plus,
        'x': _X
    }

    def __init__(self, lat, lng, shape, size, precision, **kwargs):
        '''
        Args:
            lat (float): Latitude of the center of the symbol.
            lng (float): Longitude of the center of the symbol.
            shape (str): Shape of the symbol, as 'o', 'x', or '+'.
            size (int): Size of the symbol, in meters.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            edge_color (str): Color of the symbol's edge. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            edge_alpha (float): Opacity of the symbol's edge, ranging from 0 to 1.
            edge_width (int): Width of the symbol's edge, in pixels.
            face_color (str): Color of the symbol's face. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            face_alpha (float): Opacity of the symbol's face, ranging from 0 to 1.
        '''
        pass

    def write(self, w):
        '''
        Write the symbol.

        Args:
            w (_Writer): Writer used to write the symbol.
        '''
        pass
