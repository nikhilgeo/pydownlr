#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import telepot
import datetime

now = datetime.datetime.now()

print(now)
tel_bot_token = 'XXXXXX' #telegram bot auth tokens
bmsurl ="https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426"
paytmurl ="https://paytm.com/movies/bengaluru/avengers-endgame-m/o9otdt?fromdate=2019-04-26"
tel_users = ['userid1','userid2'] #ID of users to send alert to
bms_checkTheatres = ['PVR: Vega City,  Bannerghatta Road','PVR: Gold, Vega City, Bannerghatta Road']
paytm_checkTheatres =['PVR VEGA, Bannerghatta Road','PVR VEGA Gold, Bannerghatta Road']

def send_tel_msg(msg):
    bot = telepot.Bot(tel_bot_token)
    for user in tel_users:
        print ("Sending telegram msg..")
        bot.sendMessage(user, msg)


print("Making request to BookMyShow..")
r= requests.get(bmsurl)
data = r.text
#print(data)
print("making soup..")
soup = BeautifulSoup(data,'lxml')
soup.find_all('a')
print("searching for venue..")
for link in soup.find_all('a',{'class':'__venue-name'}):
    cinema = link.getText()
    #print("cinema",cinema)
    for theatre in bms_checkTheatres:
        #print("theatre", theatre)
        if(cinema.strip(' \t\n\r') == theatre):
            msg = "ALERT: BookMyShow-Booking open in " + theatre
            print("Booking open in ",theatre)
            send_tel_msg(msg)

print("Making request to paytm..")
r= requests.get(paytmurl)
data = r.text
#print(data)
print("making soup..")
soup = BeautifulSoup(data,'lxml')
soup.find_all('a')
print("searching for venue..")
for link in soup.find_all('div',{'class':'_2tt5'}):
    cinema = link.getText()
    print("cinema",cinema)
    for theatre in paytm_checkTheatres:
        #print("theatre", theatre)
        if(cinema.strip(' \t\n\r') == theatre):
            msg = "ALERT: Paytm-Booking open in " + theatre
            print("Booking open in ",theatre)
            send_tel_msg(msg)
