import json

class _GroundOverlay(object):
    def __init__(self, url, bounds, **kwargs):
        '''
        Args:
            url (str): URL of image to overlay.
            bounds (dict): Image bounds, as a dict of the form
                ``{'north': float, 'south': float, 'east': float, 'west': float}``.

        Optional:

        Args:
            opacity (float): Opacity of the overlay, ranging from 0 to 1.
        '''
        pass

    def write(self, w):
        '''
        Write the ground overlay.

        Args:
            w (_Writer): Writer used to write the ground overlay.
        '''
        pass
