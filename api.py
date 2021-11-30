from tkinter import *
from typing import ValuesView

import requests
import json


# Creating wellcome root. you can use just root too
wellcomeroot =Tk ()
# Tittle of the page
wellcomeroot.title ("Syed Murad's Employee Registation")
# putting size of the wellcomepage
wellcomeroot.geometry("480x100")

Label(wellcomeroot, text="Syed Murad's Employee Registation", font=("Arial", 15, "bold"), bg="#00376b", fg="#FFFCF9").place(x=60, y=30)


try:
    #To get API data 
    api_requeat = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=CFD0BB59-E61A-437F-91FF-8F31BA883474")
# loading data from API
    api = json.loads(api_requeat.content)   
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    catagory = api[0]['Category']['Name']
except Exception as e:
    api = "error"
viewdata = Label(wellcomeroot,text= city + "Air Quality" + str(quality) +  catagory + "", font=("Arial", 15, "bold") )
viewdata.pack()

button_exit = Button(wellcomeroot, text="Exit Program", command=wellcomeroot.quit).place(x=200, y=65)
#button_exit.pack()



wellcomeroot.mainloop()

