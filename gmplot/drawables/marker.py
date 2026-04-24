from gmplot.utility import _format_LatLng
from gmplot.drawables.marker_icon import _MarkerIcon
from gmplot.drawables.marker_info_window import _MarkerInfoWindow
from gmplot.drawables.raw_marker import _RawMarker

class _Marker(object):
    def __init__(self, lat, lng, color, precision, **kwargs):
        '''
        Args:
            lat (float): Latitude of the marker.
            lng (float): Longitude of the marker.
            color (str): Marker color. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            title (str): Hover-over title of the marker.
            label (str): Label displayed on the marker.
            info_window (str): HTML content to be displayed in a pop-up `info window`_.
            draggable (bool): Whether or not the marker is `draggable`_.

        .. _info window: https://developers.google.com/maps/documentation/javascript/infowindows
        .. _draggable: https://developers.google.com/maps/documentation/javascript/markers#draggable
        '''
        pass

    def write(self, w, context):
        '''
        Write the marker.

        Args:
            w (_Writer): Writer used to write the marker.
            context (_Context): Context used to keep track of what was drawn to the map.
        '''
        pass
