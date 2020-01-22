using HTTP
using JSON

for (_id, convo) in JSON.parse(String(HTTP.get("https://git.io/ccc-dataset").body))
	for message in convo["messages"]
		for utterance in message
			println(utterance["text"])
		end
	end
end