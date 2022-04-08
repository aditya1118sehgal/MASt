from datetime import datetime
from datetime import timedelta

### Date and Time Utils

def getYesterday():
    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    return yesterday

def calculateEndDate ():
    yesterday = getYesterday()
    return yesterday.strftime('%Y-%m-%d')

def formatDate (date=datetime.today()):
    return date.strftime('%Y-%m-%d')
