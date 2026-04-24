class _MarkerInfoWindow(object):
    def __init__(self, content):
        '''
        Args:
            content (str): HTML content to be displayed in this info window.
        '''
        pass

    def write(self, w, context, marker_name):
        '''
        Write the info window that attaches to the given marker on click.

        Args:
            w (_Writer): Writer used to write the info window.
            context (_Context): Context used to keep track of what was drawn to the map.
            marker_name (str): JavaScript name of the marker that should display this info window.
        '''
        pass
