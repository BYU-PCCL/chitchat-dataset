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
        odd_speaker_token: str = "<speaker1>",
        even_speaker_token: str = "<speaker2>",
        end_of_utterance_token: str = " ",
        prefix: str = "",
    ) -> None:
        """Instantiate a new ConversationDataset object."""
        self.path = path
        self.odd_speaker_token = odd_speaker_token
        self.even_speaker_token = even_speaker_token
        self.eou_token = end_of_utterance_token
        self.prefix = prefix
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        """Iterate over input/target tuples."""
        for conv in self._data.values():
            conv = [self.eou_token.join(u["text"] for u in m) for m in conv["messages"]]
            for example in compound_conversation(
                conv, self.odd_speaker_token, self.even_speaker_token, self.prefix
            ):
                yield example


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
    convo: Iterable[str],
    odd_speaker_token: str,
    even_speaker_token: str,
    prefix: str = "",
) -> Iterator[Tuple[str, str]]:
    """Compounds a single conversation.

    Returns an iterator over compounding input/target example tuples of the
    form (assuming a 4 turn conversation)::

        ("<s1>message1", "<s2>message2")
        ("<s1>message1<s2>message2", "<s1>message3")
        ("<s1>message1<s2>message2<s1>message3", "<s2>message4")

    Where:
        * ``<s1>`` denotes the ``odd_speaker_token``
        * ``<s2>`` denotes the ``even_speaker_token``
    """
    # NB: switch even and odd tokens because we start at 1
    even_token = odd_speaker_token
    odd_token = even_speaker_token

    convo = list(convo)
    for i in range(1, len(convo)):
        c = "".join(add_alternating_tokens(convo[:i], odd_token, even_token))
        yield prefix + c, even_token + convo[i] if i % 2 == 0 else odd_token + convo[i]


def add_alternating_tokens(
    convo: Iterable[str], odd_token: str, even_token: str,
) -> Iterator[str]:
    """Adds alternating tokens to an iterable (list) of strings."""
    for i, s in enumerate(convo):
        yield even_token + s if i % 2 == 0 else odd_token + s
