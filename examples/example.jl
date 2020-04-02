using HTTP
using JSON

for (_id, convo) in JSON.parse(String(HTTP.get("https://raw.githubusercontent.com/BYU-PCCL/chitchat-dataset/master/chitchat_dataset/dataset.json").body))
	for message in convo["messages"]
		for utterance in message
			println(utterance["text"])
		end
	end
end
