import datetime

def fruit_market(data):
    """
    fruit market
    """
    d=datetime.datetime.today()
    f=open("fruit_log.txt","a")
    f.write("\n" +"-"*50+"\n")
    f.write(str(d) + "\n")
    f.write(data)
    f.close()
