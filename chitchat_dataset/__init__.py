"""Chit Chat Challenge dataset."""
import json
import os
from typing import Optional


def _default_dataset_path() -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "dataset.json")


class Dataset(dict):
    """Chit Chat Challenge dataset."""

    def __init__(self, path: Optional[str] = None) -> None:
        """Instantiate a new Dataset object."""
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
