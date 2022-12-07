from datetime import datetime
import pandas as pd
import time

# time based random number genrator in only minutes (based on impractical jokers punishment)

# "why would you want to genrate a random number? your privacy is important to us"
# see @2.17min -> https://www.youtube.com/watch?v=JQVBfcjx6d4

def getRandomNumber():
    now = datetime.now()

    try:
        number = pd.read_csv("already_used.csv")
    except:
        number = pd.DataFrame(columns=["num"])
        number.to_csv("already_used.csv")

    the_number = (int(now.utcnow().timestamp()))  

    if the_number in number["num"]:
        getRandomNumber()
    else:
        number.loc[len(number),"num"] = the_number
        number.to_csv("already_used.csv")
        
        for i in range(60):
            print("Only ",60-i," Seconds left to wait for your random number")
            time.sleep(1)
        
        return the_number

    getRandomNumber()
