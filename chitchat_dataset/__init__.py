"""Chit Chat Challenge dataset."""
import itertools
import json
import os
from typing import Iterable, Iterator, Tuple

_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset.json")


class Dataset(dict):
    """Chit Chat Challenge dataset."""

    def __init__(self, path: str = _PATH) -> None:
        """Instantiates a new Dataset object."""
        self.path = path
        super(Dataset, self).__init__(json.load(open(self.path)))


class ConversationDataset:
    """Chit Chat Challenge dataset.

    The dataset is an iterator over conversations;
    e.g. ``[["message1", "message2", ...], ...]``.
    """

    def __init__(self, path: str = _PATH, end_of_utterance_token: str = " ") -> None:
        """Instantiates a new ConversationDataset object."""
        self.path = path
        self.eou_token = end_of_utterance_token
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator[Iterator]:
        """Iterates over conversations."""
        for conv in self._data.values():
            yield (self.eou_token.join(u["text"] for u in m) for m in conv["messages"])


class CompoundingConversationDataset:
    """Chit Chat Challenge dataset.

    See ``compound_conversation()`` for specifics of the dataset format.
    """

    def __init__(
        self,
        path: str = _PATH,
        first_speaker_token: str = "<speaker1>",
        second_speaker_token: str = "<speaker2>",
        end_of_utterance_token: str = " ",
        prefix: str = "",
    ) -> None:
        """Instantiates a new ConversationDataset object."""
        self.path = path
        self.first_speaker_token = first_speaker_token
        self.second_speaker_token = second_speaker_token
        self.eou_token = end_of_utterance_token
        self.prefix = prefix
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        """Iterates over input/target tuples."""
        for conv in self._data.values():
            conv = [self.eou_token.join(u["text"] for u in m) for m in conv["messages"]]
            for example in compound_conversation(
                conv, self.first_speaker_token, self.second_speaker_token, self.prefix
            ):
                yield example


class MessageDataset:
    """Chit Chat Challenge dataset.

    The dataset is an iterator over messages for all conversation as a flat list;
    e.g. ``["message1", "message2", ...]``.
    """

    def __init__(self, path: str = _PATH, end_of_utterance_token: str = " ") -> None:
        """Instantiates a new MessageDataset object."""
        self.path = path
        self.eou_token = end_of_utterance_token
        self._data = json.load(open(self.path))

    def __iter__(self) -> Iterator:
        """Iterates over messages."""
        for conv in self._data.values():
            for message in conv["messages"]:
                yield self.eou_token.join(u["text"] for u in message)


def compound_conversation(
    convo: Iterable[str],
    first_speaker_token: str,
    second_speaker_token: str,
    prefix: str = "",
) -> Iterator[Tuple[str, str]]:
    """Compounds a single conversation.

    Returns an iterator over compounding input/target example tuples of the
    form (assuming a 4 turn conversation)::

        ("<s1>message1", "<s2>message2")
        ("<s1>message1<s2>message2", "<s1>message3")
        ("<s1>message1<s2>message2<s1>message3", "<s2>message4")

    Where: ``<s1>`` denotes the ``first_speaker_token`` and
    ``<s2>`` denotes the ``second_speaker_token``.
    """
    first_tok = first_speaker_token
    second_tok = second_speaker_token

    convo = list(convo)
    for i in range(1, len(convo)):
        c = "".join(prepend_cycle(convo[:i], [first_tok, second_tok]))
        yield prefix + c, first_tok + convo[i] if i % 2 == 0 else second_tok + convo[i]


# TODO: should this even be a function?  # noqa: W0511
def prepend_cycle(texts: Iterable[str], cycle: Iterable[str]) -> Iterator[str]:
    """Prepends an element of ``cycle`` in order to each element of ``texts``."""
    for token, text in zip(itertools.cycle(cycle), texts):
        yield token + text
