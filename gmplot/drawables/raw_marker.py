class _RawMarker(object):
    def __init__(self, position, icon, **kwargs):
        '''
        Args:
            position (str): JavaScript code that represents the position of the marker.
            icon (str): JavaScript code that represents the icon.

        Optional:

        Args:
            title (str): Hover-over title of the marker.
            label (str): Label displayed on the marker.
            draggable (bool): Whether or not the marker is draggable.
        '''
        pass

    def write(self, w, name=None):
        '''
        Write the raw marker.

        Args:
            w (_Writer): Writer used to write the raw marker.

        Optional:

        Args:
            name (str): JavaScript name of the marker.
        '''
        pass
