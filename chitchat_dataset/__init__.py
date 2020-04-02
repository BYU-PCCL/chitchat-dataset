"""Chit Chat Challenge dataset."""
import json
import os
from typing import Iterator, Optional


def _default_dataset_path() -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "dataset.json")


class Dataset(dict):
    """Chit Chat Challenge dataset."""

    def __init__(self, path: Optional[str] = None) -> None:
        """Instantiate a new Dataset object."""
        self.path = path if path is not None else _default_dataset_path()
        super(Dataset, self).__init__(json.load(open(self.path)))


class ConversationDataset:
    """Chit Chat Challenge dataset.

    The dataset is an iterator over conversations;
    e.g. `[["message1", "message2", ...], ...]`.
    """

    def __init__(self, path: str = None, end_of_utterance_token: str = " ") -> None:
        """Instantiate a new ConversationDataset object."""
        self.path = path if path is not None else _default_dataset_path()
        self.eou_token = end_of_utterance_token
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator[Iterator]:
        """Iterate over conversations."""
        for conv in self._data.values():
            yield (self.eou_token.join(u["text"] for u in m) for m in conv["messages"])


class MessageDataset:
    """Chit Chat Challenge dataset.

    The dataset is an iterator over messages for all conversation as a flat list;
    e.g. `["message1", "message2", ...]`.
    """

    def __init__(
        self,
        path: str = None,
        end_of_utterance_token: str = " ",
        end_of_message_token: str = "<EOM>",
    ) -> None:
        """Instantiate a new MessageDataset object."""
        self.path = path if path is not None else _default_dataset_path()
        self.eou_token = end_of_utterance_token
        self.eom_token = end_of_message_token
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator:
        """Iterate over messages."""
        for conv in self._data.values():
            for message in conv["messages"]:
                yield self.eou_token.join(u["text"] for u in message)
