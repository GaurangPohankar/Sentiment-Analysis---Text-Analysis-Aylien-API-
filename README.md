# Sentiment-Analysis---Text-Analysis-Aylien-API-

This Package includes the three files. 

Each are essential to the task . 

----------------------------------------------------------------------------------------
1. AylienApi.py 
--> Aylien Api is the api we are going to use in our system for sentiment analysis
--> To run this file you will need 'python 3' installed on your system.
--> After installing 'python 3' you will need to install following packages 
--> Aylien Api client , pprint. To install them
	--> open your terminal . 
	--> run this command= 'pip3 install aylien-apiclient' or 'pip install aylien-apiclient' 
 	--> run this command= 'pip3 install pprint' or 'pip install pprint'
	--> run this command= 'pip3 install urllib3'
	--> run this command= 'pip install requests'  
--> Now run the script . The json data of the demo text will be visible and required aspects accordingly.
--> You can now change the text to test it. 
--> Every aspect position is given so that data uploading will be easier.


-----------------------------------------------------------------------------------------
2. AylienApi_Final.py

--> Now here we will fetch the data and upload analyzed data.
--> Data array will be put in the the for loop and each answer will be analyzed one by one. 
--> Now each answer may have multiple sentence and requirement stated was that accordingly generate analyzed per sentence data.  
--> now in nested for loop you can add variables as json data is generated and upload it using the url .
--> Understand that 'urllib.request.urlopen' this command uploads the data.  

-----------------------------------------------------------------------------------------
3. request.py

--> It is simple file with which data upload opeartion is performed . 
--> you can analyze the code fr better understaning. 
