from aylienapiclient import textapi
import urllib.request
from urllib.parse import quote

#please add your URL to fetch the data into this script and enter that script here 
url = "Your Fetch URL"

#fetched script will now here will be opened to get data 
data = urllib.request.urlopen(url)

#here api client is defined . 
#client = textapi.Client(APP_ID, APP_KEY)
c = textapi.Client("9cc0b62f", "289b20a1fbd17af4c6cd277faa4ab720")

domain = "restaurants"

for text in data :
    s = c.AspectBasedSentiment({'text': text, 'domain': domain})
    print(s)
    #print(s["sentences"][0]["text"])
    #print(s["sentences"][1]["text"])
    #print(s["sentences"][x]["polarity"])
    #print(s["sentences"][1]["aspects"][0]["aspect"])
    #print(s["sentences"][0]["aspects"][0]["aspect"])
    for x in range(0, len(s["sentences"])-1):
        data_insert_url= "YourUrlToUploadData?Text="+urllib.request.quote(str(s["sentences"][x]["text"]))+"&Sentiment="+urllib.request.quote(str(s["sentences"][x]["polarity"]))
        #print(data_insert_url)
        contents = urllib.request.urlopen(data_insert_url).read()
    

