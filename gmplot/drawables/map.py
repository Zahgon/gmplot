import json

from gmplot.utility import _INDENT_LEVEL, _format_LatLng

class _Map(object):
    def __init__(self, lat, lng, zoom, precision, **kwargs):
        '''
        Args:
            lat (float): Latitude of the center of the map.
            lng (float): Longitude of the center of the map.
            zoom (int): `Zoom level`_, where 0 is fully zoomed out.
            precision (int): Number of digits after the decimal to round to for the lat/lng center.

        Optional:

        Args:
            map_type (str): `Map type`_.
            map_styles ([dict]): `Map styles`_. Requires `Maps JavaScript API`_.
            tilt (int): `Tilt`_ of the map upon zooming in.
            scale_control (bool): Whether or not to display the `scale control`_.
            fit_bounds (dict): Fit the map to contain the given bounds, as a dict of the form
                ``{'north': float, 'south': float, 'east': float, 'west': float}``.

        .. _Zoom level: https://developers.google.com/maps/documentation/javascript/tutorial#zoom-levels
        .. _Map type: https://developers.google.com/maps/documentation/javascript/maptypes
        .. _Map styles: https://developers.google.com/maps/documentation/javascript/style-reference
        .. _Maps JavaScript API: https://console.cloud.google.com/marketplace/details/google/maps-backend.googleapis.com
        .. _Tilt: https://developers.google.com/maps/documentation/javascript/reference/map#MapOptions.tilt
        .. _scale control: https://developers.google.com/maps/documentation/javascript/reference/map#MapOptions.scaleControl
        '''
        pass

    def write(self, w):
        '''
        Write the map.

        Args:
            w (_Writer): Writer used to write the map.
        '''
        pass
