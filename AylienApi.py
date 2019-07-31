from aylienapiclient import textapi
import pprint

#client = textapi.Client(APP_ID, APP_KEY)
c = textapi.Client("9cc0b62f", "289b20a1fbd17af4c6cd277faa4ab720")

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

