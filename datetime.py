from datetime import datetime
now = datetime.now()
def today_date_time():
    my_time= now.strftime("%d/%m/%Y %H:%M:%S")
    return my_time
    
my_time = today_date_time()
print("Hello Harshit. Today is {}".format(my_time))
