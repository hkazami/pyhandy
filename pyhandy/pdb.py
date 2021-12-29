"""
    Utility functions for better development experience.

    Usage:
        - Import this file to the main program:
            `from CameramanRemover.utils.pdb import register_pdb_hook`
        - Activate the pdb hook:
            `register_pdb_hook()`
"""
import sys


def _info(etype, value, tb):
    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
        sys.__excepthook__(etype, value, tb)
    else:
        import pdb
        import traceback
        # we are NOT in interactive mode, print the exception...
        traceback.print_exception(etype, value, tb)
        print()
        # ...then start the debugger in post-mortem mode.
        pdb.post_mortem(tb)


def register_pdb_hook():
    """
        Utility function for automatically calling python 
        debugger when the program encounters error.
    """
    sys.excepthook = _info
