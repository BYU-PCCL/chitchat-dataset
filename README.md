# chitchat-dataset

Conversational dataset from the Chit-Chat Challenge.

## download

```
curl -L git.io/ccc-dataset-json -o dataset.json
```

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

## examples

A Python example using the [Requests] library:

```python
import requests

for _id, convo in requests.get("https://git.io/ccc-dataset-json").json().items():
    for message in convo["messages"]:
        for utterance in message:
            print(utterance["text"])
```

For more examples see [`examples/`].


[dataset]: dataset.json
[dataset.json]: dataset.json
[`dataset.json`]: dataset.json
[UUID]: https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)
[Requests]: https://2.python-requests.org/en/master/
[examples]: examples/
[`examples/`]: examples/