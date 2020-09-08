# STEPS TO Execute the Flask Appication

1) Clone the Code to the local 
2) Import all the required libraried in requirement.tt
3) Run Flask.py  either from cmd or IDE
Open http://localhost:5000
web application is ready to use, Use Customer ID : 1 in search bar to make prediction

# Behind the Scenes (after Search hit)

1) databas.py file is called and for the  entered id. It fetches the records from  Elephantsqlnstance (POstGres as Service) and returns as list
2) The list is passed to Apicall.py to hit the model deployed in Watson machine Learning Studio and get the predictions.
3) Predictionms are displayed in Website for different products

