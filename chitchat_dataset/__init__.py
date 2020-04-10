"""Chit Chat Challenge dataset."""
import json
import os
from typing import Iterable, Iterator, Tuple

_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset.json")


class Dataset(dict):
    """Chit Chat Challenge dataset."""

    def __init__(self, path: str = _PATH) -> None:
        """Instantiate a new Dataset object."""
        self.path = path
        super(Dataset, self).__init__(json.load(open(self.path)))


class ConversationDataset:
    """Chit Chat Challenge dataset.

    The dataset is an iterator over conversations;
    e.g. `[["message1", "message2", ...], ...]`.
    """

    def __init__(self, path: str = _PATH, end_of_utterance_token: str = " ") -> None:
        """Instantiate a new ConversationDataset object."""
        self.path = path
        self.eou_token = end_of_utterance_token
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator[Iterator]:
        """Iterate over conversations."""
        for conv in self._data.values():
            yield (self.eou_token.join(u["text"] for u in m) for m in conv["messages"])


class CompoundingConversationDataset:
    """Chit Chat Challenge dataset.

    See `compound_conversation()` for specifics of the dataset format.
    """

    def __init__(
        self,
        path: str = _PATH,
        end_of_message_token: str = "<EOM>",
        end_of_utterance_token: str = " ",
        prefix: str = "",
    ) -> None:
        """Instantiate a new ConversationDataset object."""
        self.path = path
        self.eom_token = end_of_message_token
        self.eou_token = end_of_utterance_token
        self.prefix = prefix
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        """Iterate over input/target tuples."""
        for conv in self._data.values():
            conv = [self.eou_token.join(u["text"] for u in m) for m in conv["messages"]]
            for m in compound_conversation(conv, self.prefix, self.eom_token):
                yield m


class MessageDataset:
    """Chit Chat Challenge dataset.

    The dataset is an iterator over messages for all conversation as a flat list;
    e.g. `["message1", "message2", ...]`.
    """

    def __init__(self, path: str = _PATH, end_of_utterance_token: str = " ") -> None:
        """Instantiate a new MessageDataset object."""
        self.path = path
        self.eou_token = end_of_utterance_token
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator:
        """Iterate over messages."""
        for conv in self._data.values():
            for message in conv["messages"]:
                yield self.eou_token.join(u["text"] for u in message)


def compound_conversation(
    convo: Iterable[str], prefix: str, eom_token: str
) -> Iterator[Tuple[str, str]]:
    """Compounds a single conversation.

    Returns an iterator over compounding input/target example tuples of the
    form (assuming a 4 turn conversation and an `end_of_message_token` of `<TURN>`):
    ```
    ("message1", "message2")
    ("message1<TURN>message2", "message3")
    ("message1<TURN>message2<TURN>message3", "message4")
    ```
    """
    convo = list(convo)
    for i in range(1, len(convo)):
        yield prefix + eom_token.join(convo[:i]), convo[i]
