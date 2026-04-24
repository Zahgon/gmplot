import warnings
import inspect
from .utility import _INDENT

class _Writer(object):
    '''Writer used to format content with consistent indentation.'''

    def __init__(self, file):
        '''
        Args:
            file (handle): File to write to.
        '''
        pass

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        '''
        Args:
            exception_type: Type of exception that triggered the exit. 
            exception_value: Value of exception that triggered the exit.
            traceback: Traceback when exit was triggered.
        '''
        # Clear the file if an uncaught exception occured while writing:
        if exception_type:
            self._file.truncate(0)

    def indent(self):
        '''Indent the writer by one level.'''
        pass

    def dedent(self):
        '''Dedent the writer by one level.'''
        pass

    def write(self, content='', end_in_newline=True):
        '''
        Write content.

        Optional:

        Args:
            content (str): Content to write, as a string.
                Content is cleaned using the same rules as Python's ``inspect.cleandoc()``:
                - Leading and trailing empty lines are removed.
                - Any leading whitespace common to all lines is removed.
                - All tabs are expanded to spaces.
            end_in_newline (bool): Whether or not to write a newline at the end. Defaults to True.
        '''
        pass
