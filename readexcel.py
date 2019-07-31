from aylienapiclient import textapi
import pprint
import xlrd
import time

workbook = xlrd.open_workbook('NA.xlsx')
sheet = workbook.sheet_by_index(0)

data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

#client = textapi.Client(APP_ID, APP_KEY)
c = textapi.Client("9cc0b62f", "289b20a1fbd17af4c6cd277faa4ab720")

for i in range(len(data)):
    text =str(data[i][12])
    domain = "restaurants"
    
    s = c.AspectBasedSentiment({'text': text, 'domain': domain})
    print(data[i][12])
    print('          ')
    print(s["sentences"])
    print("---------------------------------------------------------------")
    pprint.pprint(s)
    time.sleep(2)
     
#s = c.Sentiment({'text': 'John is a very good football player!. I am also happy.'})

#print(s["sentences"][0]["text"])
#print(s["sentences"][1]["text"])
#print(s["sentences"][1]["polarity"])
#print(s["sentences"][1]["aspects"][0]["aspect"])
#print(s["sentences"][0]["aspects"][0]["aspect"])
#print(len(s["sentences"]))

