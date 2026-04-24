from gmplot.utility import _get, _format_LatLng

class _Route(object):
    '''For more info, see Google Maps' `Directions Service https://developers.google.com/maps/documentation/javascript/directions`_.'''
    
    def __init__(self, origin, destination, precision, **kwargs):
        '''
        Args:
            origin ((float, float)): Origin, as a latitude/longitude tuple.
            destination ((float, float)): Destination, as a latitude/longitude tuple.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            travel_mode (str): Travel mode.
            waypoints ([(float, float)]): Waypoints.
        '''
        pass

    def write(self, w):
        '''
        Write the route.

        Args:
            w (_Writer): Writer used to write the route.
        '''
        pass
