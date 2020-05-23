from apscheduler.schedulers.background import BackgroundScheduler
import datetime

#Added a function which will be called evry minute
def callThis():
    #Here is where we will make the alphavantage API call
    print(datetime.datetime.now())

#Create a default background(non blocking) schedule object
scheduler = BackgroundScheduler(daemon=True)
