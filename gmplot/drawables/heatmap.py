from collections import namedtuple

from gmplot.utility import _get, _format_LatLng

class _Heatmap(object):
    _DEFAULT_WEIGHT = 1

    _Point = namedtuple('Point', ['location', 'weight'])

    def __init__(self, lats, lngs, precision, **kwargs):
        '''
        Args:
            lats ([float]): Latitudes.
            lngs ([float]): Longitudes.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            radius (int): Radius of influence for each data point, in pixels.
            gradient ([(int, int, int, float)]): Color gradient of the heatmap, as a list of `RGBA`_ colors.
                The color order defines the gradient moving towards the center of a point.
            opacity (float): Opacity of the heatmap, ranging from 0 to 1.
            max_intensity (int): Maximum intensity of the heatmap.
            dissipating (bool): True to dissipate the heatmap on zooming, False to disable dissipation.
            weights ([float]): List of weights corresponding to each data point. Each point has a weight
                of 1 by default. Specifying a weight of N is equivalent to plotting the same point N times.
        
        .. _RGBA: https://www.w3.org/TR/css-color-3/#rgba-color
        '''
        pass

    def write(self, w):
        '''
        Write the heatmap.

        Args:
            w (_Writer): Writer used to write the heatmap.
        '''
        pass
