from os import path as osp
from pathlib import Path as Pth

class Path(object):
    def __init__(self, path: str):
        self._path = path
        self._pathlib_obj = Pth(path)
    
    @property
    def name(self):
        return self._pathlib_obj.name
    
    @property
    def stem(self):
        return self._pathlib_obj.stem

    @property
    def suffix(self):
        return self._pathlib_obj.suffix

    @property
    def abspath(self):
        return osp.abspath(self._path)

    @property
    def dirname(self):
        return osp.dirname(self._path)