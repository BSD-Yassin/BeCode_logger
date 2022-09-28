import time
import datetime as dt


class Clock():
    def __init__(self):
        pass

    def monitor_datetime(self):
        actual_hour = dt.datetime.now().time()    
        dict_time = {"first_checkin":(dt.time(8,45),dt.time(9,00)), 
                    "first_checkout":(dt.time(12,30),dt.time(13,20)), 
                    "second_checkin":(dt.time(13,20),dt.time(13,30)),
                    "second_checkout":(dt.time(17,00),dt.time(21,00))}
        now = dt.datetime.now()

        # checks if this is a weekday
        if 0 <= now.weekday() <= 4:
        
            if dict_time["first_checkin"][0] <= actual_hour <= dict_time["first_checkin"][1]:
                print("Oh oh oh ! I'm going to check in today !")
                hour_check = "button_9h"
                
                return hour_check 
            
            elif dict_time["first_checkout"][0] <= actual_hour <= dict_time["first_checkout"][1]:
                print("Oh oh oh ! It's time to eat some food !")
                hour_check = "button_12h3"
                
                return hour_check
            
            elif dict_time["second_checkin"][0] <= actual_hour <= dict_time["second_checkin"][1]:
                print(" Yum, that was good, I'm back up now, let me just check in !")
                hour_check = "button_13h3"
                
                return hour_check

            elif dict_time["second_checkout"][0] <= actual_hour <= dict_time["second_checkout"][1]:
                print(" *Accent of a fat mafiosi of New Jersey * Another day, another dollaah !")
                hour_check = "button_17h"

                return hour_check
            else : 
                print("It's " + str(actual_hour.strftime("%H:%M")))
                print("Nothing to check in or check out... Don't call me for nothing, you probably used energy and money on that call...")
        
        else :
            print("Wow, really ? It's not even a weekday. Get a life man... ")
