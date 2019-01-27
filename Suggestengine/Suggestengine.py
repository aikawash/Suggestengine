import requests
import bs4
import RandomHeaders
import sys
import array as arr
import easygui as eg
import random
import datetime

now = datetime.datetime.now()

URL = "https://calendar.clemson.edu/"
SECTION_CSS = ".vevent"
TIME = ".dtstart"
LOCATION = ".event_item_venue"
EVENT = ".summary a"

def grab_site(url):
	# Pulls the site
	headers = RandomHeaders.LoadHeader()
	# This is a non-Python user agent, which prevents Amazon from blocking the request
	return requests.get(url, headers=headers)

event_list = []
place_list = []
when_list = []
if __name__ == '__main__':
    res = grab_site(URL)
    page = bs4.BeautifulSoup(res.text, 'lxml')

    #print(page.title.string)

    try:
        for section in page.select(SECTION_CSS):
            event = section.select(EVENT)
            time = section.select(TIME)
            location = section.select(LOCATION)

            event = event[0].getText()
            time = time[0].getText()
            location = location[0].getText()

            time = time.translate({ord(c): None for c in '\n'})

            time = time[4:]

            event_list.append(event)
            #
            place_list.append(location)
            when_list.append(time)
            #print("Event: {} | Time: {} | Location: {}".format(event, time, location)


        print(1)


    except:
        #print (when_list, sep = "\n")
        pass



string = "HELLO"
x = 4
sys.path.append('..')

reply = eg.msgbox("Hi. What kind of events are you looking for?")
if reply is None:
    exit()
else:
    choices = ["Clemson Event", "Spontaneous"]
    reply = eg.buttonbox("Choose one.", choices  = ['One Time Events', 'Anytime Events'])

    if reply is None or reply == 'One Time Events':
        choices = ["This Month", "This Week", "Right Now", "Cancel"]
        reply = eg.buttonbox("When would you like to attend this event?", choices = ['This Month','This Week', 'Right Now', 'Cancel'])
        #print(reply)
        if reply is None or reply == 'Cancel':
            exit()
        elif reply == 'This Month':
            x = random.randint(0, len(event_list)-1)
            eg.msgbox("Sure thing. Here's someething I've found: "+str(event_list[x]) +" at "+str(place_list[x]) + " " +str(when_list[x]))

        elif reply == 'This Week':
            today = now.day
            month = now.month
            date = str(month) + "/" + str(today)

            todayEvents = []
            tEvTime = []
            tEvLoc = []

            for y in range(0,6):
                for x in range(len(event_list)):
                    if str(month) + "/" + str(today+y) in when_list[x]:
                        todayEvents.append(event_list[x])
                        tEvLoc.append(place_list[x])
                        tEvTime.append(when_list[x])

            if len(todayEvents) != 0:
                x = random.randint(0, len(todayEvents)-1)
                date = todayEvents[x]
            eg.msgbox("OK, I've got something you might be interested in, " +str(date) + " at " + str(tEvLoc[x]) + ", " + str(tEvTime[x]) )

        elif reply == 'Right Now':
            today = now.day
            month = now.month
            date = str(month) + "/" + str(today)

            todayEvents = []
            tEvTime = []
            tEvLoc = []
            for x in range(len(event_list)):
                if date in when_list[x]:
                    todayEvents.append(event_list[x])
                    tEvLoc.append(place_list[x])
                    tEvTime.append(when_list[x])

            if len(todayEvents) != 0:
                x = random.randint(0, len(todayEvents)-1)
                date = todayEvents[x]
                eg.msgbox("Alright. Here's what I've found for you:"+ str(date) + " at " + str(tEvLoc[x]) + ", " + str(tEvTime[x]))
            else:
                eg.msgbox("Sorry, I found no events for today, perhaps you want to try later on")



    elif reply is None or reply == 'Anytime Events':
        choices = [ "Food", "Outdoors", "Sports", "etc.", "Cancel"]
        reply = eg.buttonbox("Choose an activity.", choices = ['Clubs','Food', 'Outdoors', 'Sports', 'Shopping', 'Etc.', 'Cancel'])

        if reply is None or reply == 'Cancel':
            exit()
        elif reply =='Food':
            edible = ["try a bite at douthit dining hall", "take a trip to core dining hall", "downtown's many fine dining locations",
            "take a trip to Greenville", "TDs", "take a car ride to Anderson"]
            x = random.randint(0, len(edible)-1)
            eg.msgbox("If you want to do something of an edible nature, you could "+str(edible[x]))

        elif reply == 'Outdoors':
            outdoorsy = ["going to a park", "walking the dog", " taking a hike to the botanical gardens for the museum and garden", "visiting Lake Hartwell"]
            #"visiting the twin lakes" , "visiting y beach" ,"going to the dam", "experimenting with new forest hiking trails"]
            x = random.randint(0, len(outdoorsy)-1)
            eg.msgbox("If you want to do something outdoorsy, you could try " +str(outdoorsy[x]))
            exit()

        elif reply == 'Sports':
            sporty = ["going to bownam with friends", "going to union game center"]
            x = random.randint(0, len(sporty)-1)
            eg.msgbox("If you want to do something sporty, you could try " +str(sporty[x]))
            exit()

        elif reply == 'Shopping':
            money = ["going to the Walmart", "going to the Anderson mall", "going downtown Clemson"]
            x = random.randint(0, len(money)-1)
            eg.msgbox("If you have money burning a hole in your pocket, you could spend it by" +str(money[x]))
            exit()

        elif reply == 'Clubs':
            money = ["going to the chess club", " going to the boxing club"]
            x = random.randint(0, len(money)-1)
            eg.msgbox("Want to spend time with some like-minded people? Try " +str(money[x]))
            exit()

        elif reply == 'Etc.':
            chaos = ["going to the chess club", " going to the boxing club", "going to the Walmart", "going to the Anderson mall", "going downtown Clemson",
            "going to bownam with friends", "going to union game center", "going to a park", "walking the dog", " taking a hike to the botanical gardens for the museum and garden", "visiting Lake Hartwell"
             "visiting the twin lakes" , "visiting y beach" ,"going to the dam", "experimenting with new forest hiking trails", "a bite at douthit dining hall", "taking a trip to core dining hall", "downtown's many fine dining locations",
             "taking a trip to Greenville", "TDs", "take a car ride to Anderson"]
            x = random.randint(0, len(chaos)-1)
            eg.msgbox("Try " +str(chaos[x]))
            exit()
