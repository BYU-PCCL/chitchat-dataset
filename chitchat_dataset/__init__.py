"""Chit Chat Challenge dataset."""

__version__ = "0.1.3"

import json
import os


class Dataset(dict):
    """Chit Chat Challenge dataset."""

    def __init__(self, path=None):
        if path is None:
            here = os.path.abspath(os.path.dirname(__file__))
            # due to python's package management, this has a `.py` extension
            path = os.path.join(here, "dataset.py")
        self.path = path
        super(Dataset, self).__init__(json.load(open(self.path)))
