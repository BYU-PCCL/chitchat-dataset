"""Chit Chat Challenge dataset."""

__version__ = "0.2.0"

import json
import os


def _default_dataset_path():
    here = os.path.abspath(os.path.dirname(__file__))
    # due to python's package management, this has a `.py` extension
    return os.path.join(here, "dataset.py")


class Dataset(dict):
    """Chit Chat Challenge dataset."""

    def __init__(self, path=None):
        self.path = path if path is not None else _default_dataset_path()
        super(Dataset, self).__init__(json.load(open(self.path)))


class FlatDataset:
    """
    Chit Chat Challenge dataset as a flat iterator over conversations, with
    optional end of utterance and end of message tokens.
    """

    def __init__(
        self, path=None, end_of_utterance_token="<EOU>", end_of_message_token="<EOM>"
    ):
        self.path = path if path is not None else _default_dataset_path()
        self.eou_token = end_of_utterance_token
        self.eom_token = end_of_message_token
        self._data = json.load(open(self.path))

    def __iter__(self):
        for conv in self._data.values():
            yield self.eom_token.join(
                self.eou_token.join(u["text"] for u in m) for m in conv["messages"]
            )
