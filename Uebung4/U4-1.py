import json

with open("twitter_small.json", "r", encoding="utf-8") as f:
    daten = f.readlines()
    print(f"Anzahl Tweets: {len(daten)}")
    #for i in daten:
    #    print(i)

class Tweets:

    def __init__(self, username, message, datum):
        self.username = username
        self.message = message
        self.datum = datum

