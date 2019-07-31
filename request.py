import csv
from aylienapiclient import textapi
import pprint
import xlrd
import time
import json

#client = textapi.Client(APP_ID, APP_KEY)
c = textapi.Client("9cc0b62f", "289b20a1fbd17af4c6cd277faa4ab720")

person = {}
aspects = {}
aspect = 0
count = 0

with open('Book1.csv') as file:
  reader = csv.reader(file)
  
  for row in reader:
    
    text =str(row[1])
    domain = "restaurants"
    
    s = c.AspectBasedSentiment({'text': text, 'domain': domain})
    #s = c.Sentiment({'text': text, 'domain': domain})
    #pprint.pprint(s)
    #pprint.pprint(s['aspects'])
    
    if(s['aspects']):
      
      print(len(s['aspects']))
      for i in range(len(s['aspects'])):
        
        user_aspect = s['aspects'][i]['aspect']
        user_aspect_confidence = s['aspects'][i]['aspect_confidence']
        user_polarity = s['aspects'][i]['polarity']
        user_polarity_confidence = s['aspects'][i]['polarity_confidence']
        
        aspects[i] = {
          'aspect': user_aspect,
          'polarity': user_aspect_confidence,
          'aspect_polarity': user_polarity,
          'aspect_polarity_confidence': user_polarity_confidence,
          }
      aspect = aspects
        
    else:
      aspect ='None'
      

    if(s['domain']):
      domain = s['domain']
    else:
      domain ='None' 

    if(s['text']):
      text = s['text']
    else:
      text ='None'

    if(str(row[0])):
      reviewid = str(row[0])
    else:
      reviewid ='None'
    
    person[count] = {
        'reviewid': str(reviewid),
        'aspects': aspect,
        'domain': str(domain),
        'text': str(text),
    }
    
    #print('-----------------------------------------------------')
    count += 1



import json

s = json.dumps(person)

print(s)

with open('data.txt', 'w', encoding='utf8') as json_file:
    json_file.write(s)

  




