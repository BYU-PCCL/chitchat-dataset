# chitchat-dataset

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chitchat_dataset)](https://pypi.org/project/chitchat-dataset/)
[![PyPI](https://img.shields.io/pypi/v/chitchat_dataset)](https://pypi.org/project/chitchat-dataset/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/chitchat_dataset)](https://pypi.org/project/chitchat-dataset/)

[![CI](https://github.com/BYU-PCCL/chitchat-dataset/workflows/CI/badge.svg)](https://github.com/BYU-PCCL/chitchat-dataset/actions?query=workflow%3ACI)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Open-domain conversational dataset from the BYU
[Perception, Control & Cognition] lab's [Chit-Chat Challenge].

## install

```bash
pip3 install chitchat_dataset
```

_or_ simply download the raw dataset:

```bash
curl -LO https://raw.githubusercontent.com/BYU-PCCL/chitchat-dataset/master/chitchat_dataset/dataset.json
```

## usage

```python
import chitchat_dataset as ccc

dataset = ccc.Dataset()

# Dataset is a subclass of dict()
for convo_id, convo in dataset.items():
    print(convo_id, convo)
```

See [`examples/`] for other languages.

## stats

- 7,168 conversations
- 258,145 utterances
- 1,315 unique participants

## format

The [dataset] is a mapping from conversation [UUID] to a conversation:

```json
{
  "prompt": "What's the most interesting thing you've learned recently?",
  "ratings": { "witty": "1", "int": 5, "upbeat": 5 },
  "start": "2018-04-20T01:57:41",
  "messages": [
    [
      {
        "text": "Hello",
        "timestamp": "2018-04-19T19:57:51",
        "sender": "22578ac2-6317-44d5-8052-0a59076e0b96"
      }
    ],
    [
      {
        "text": "I learned that the Queen of England's last corgi died",
        "timestamp": "2018-04-19T19:58:14",
        "sender": "bebad07e-15df-48c3-a04f-67db828503e3"
      }
    ],
    [
      {
        "text": "Wow that sounds so sad",
        "timestamp": "2018-04-19T19:58:18",
        "sender": "22578ac2-6317-44d5-8052-0a59076e0b96"
      },
      {
        "text": "was it a cardigan welsh corgi",
        "timestamp": "2018-04-19T19:58:22",
        "sender": "22578ac2-6317-44d5-8052-0a59076e0b96"
      },
      {
        "text": "?",
        "timestamp": "2018-04-19T19:58:24",
        "sender": "22578ac2-6317-44d5-8052-0a59076e0b96"
      }
    ]
  ]
}
```

[perception, control & cognition]: https://pcc.cs.byu.edu
[chit-chat challenge]: https://pcc.cs.byu.edu/2018/04/18/the-chit-chat-challenge/
[dataset]: chitchat_dataset/dataset.py
[dataset.json]: chitchat_dataset/dataset.py
[`dataset.json`]: chitchat_dataset/dataset.py
[uuid]: https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)
[requests]: https://2.python-requests.org/en/master/
[examples]: examples/
[`examples/`]: examples/
