from bs4 import BeautifulSoup
import urllib.request as urllib2


linklist=[]
add_flag = False
URL = "http://jamsheed.in/down/torrents/Outsourced%20Season%201%20Complete%20720p/"
data = urllib2.urlopen(URL)
soup = BeautifulSoup(data.read())
soup.find_all('a')
for link in soup.find_all('a'):
	#print(link.get('href'))
	href = link.get('href')
	if(".mkv" in href):
		add_flag = True
	if(".avi" in href):
		add_flag = True
	if(".srt" in href):
		add_flag = True
	if(".mp4" in href):
		add_flag = True
	if (add_flag == True):
		item_url = URL + href
		linklist.append(item_url)
print(linklist)

