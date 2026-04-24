from gmplot.drawables.marker_icon import _MarkerIcon
from gmplot.drawables.raw_marker import _RawMarker

class _MarkerDropper(object):
    '''
    Handler that drops markers on map clicks.

    The markers can be deleted when clicked on.
    '''
    _MARKER_NAME = 'dropped_marker'
    _EVENT_OBJECT_NAME = 'event'

    def __init__(self, color, **kwargs):
        '''
        Args:
            color (str): Color of the markers to be dropped. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').

        Optional:
        
        Args:
            title (str): Hover-over title of the markers to be dropped.
            label (str): Label displayed on the markers to be dropped.
            draggable (bool): Whether or not the markers to be dropped are draggable.
        '''
        pass

    def write(self, w, context):
        '''
        Write the marker dropper.

        Args:
            w (_Writer): Writer used to write the marker dropper.
            context (_Context): Context used to keep track of what was drawn to the map.
        '''
        pass
