import requests

for _id, convo in requests.get("https://git.io/ccc-dataset").json().items():
    for message in convo["messages"]:
        for utterance in message:
            print(utterance["text"])
