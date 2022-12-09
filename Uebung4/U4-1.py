import json

with open("twitter_small.json", "r", encoding="utf-8") as file:
    data = json.load(file)

topHashtag = {}
tweetCounter = 0
listeUser = []
liteTopTweets = []

class Hashtag():
    hashtagCount = 0

class Tweets():
    tweetCounter = 0

    def __init__(self, name):
        self.name = name
        self.counter = 0

for tweet in range(len(data["tweets"])):

    tweetCounter += 1
    time = data["tweets"][tweet]["time"]
    message = data["tweets"][tweet]["message"]
    user = str(data["tweets"][tweet]["user"]).replace("http://twitter.com", "")


    if "#" in message:
        hashtag = False
        holder = str(message).split(" ")
        for i in holder:
            if i[0] == "#" and len(i) > 2:
                hashtag = True
                if i not in topHashtag:
                    topHashtag[i] = 1
                if i in topHashtag:
                    topHashtag[i] = topHashtag[i] + 1

for key, value in topHashtag.items():
    print(f"{key}, {value}")



print(tweetCounter)

isRuning = True

while isRuning:
    print("Befehl Hilfe")
    commandInput = str(input("Gib einen Befehl ein: ")).lower()
    if commandInput == "tophash":
        topHashtag = sorted(topHashtag.items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(topHashtag)
            if i == 5:
                isRuning = False
                break


