
#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


linklist=[]
add_flag = False
url = "https://in.bookmyshow.com/buytickets/kabali-bengaluru/movie-bang-ET00039091-MT/20160722"
r= requests.get(url)
data = r.text
soup = BeautifulSoup(data)
soup.find_all('a')
for link in soup.find_all('a',{'class':'__venue-name'}):
                theater = link.getText()
                if(theater.strip(' \t\n\r') == "Cinepolis: Bannerghatta Road"):
                        print "adasdasdA"
                        fromaddr = "tcheck@domain.com"
                        toaddr = "abc@domain.com,cde@domain.com"
                        msg = MIMEMultipart()
                        msg['From'] = fromaddr
                        msg['To'] = toaddr
                        msg['Subject'] = "KCBR"
                        body = "Kabali !!"
                        msg.attach(MIMEText(body, 'plain'))
                        s = smtplib.SMTP('localhost')
                        s.sendmail(fromaddr,toaddr.split(','), msg.as_string())
                        s.quit()
