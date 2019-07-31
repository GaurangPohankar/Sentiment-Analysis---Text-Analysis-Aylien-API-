from aylienapiclient import textapi
import pprint

#client = textapi.Client(APP_ID, APP_KEY)
c = textapi.Client("YOUR_APP_ID", "YOUR_APP_KEY")

#s = c.Sentiment({'text': 'John is a very good football player!. I am also happy.'})
text ="Delicious food. Disappointing service."
domain = "restaurants"

s = c.AspectBasedSentiment({'text': text, 'domain': domain})

print(s["sentences"][0]["text"])
print(s["sentences"][1]["text"])
print("---------------------------------------------------------------")
pprint.pprint(s)
#print(s["sentences"][0]["text"])
#print(s["sentences"][1]["text"])
#print(s["sentences"][1]["polarity"])
#print(s["sentences"][1]["aspects"][0]["aspect"])
#print(s["sentences"][0]["aspects"][0]["aspect"])
#print(len(s["sentences"]))

