from bs4 import BeautifulSoup
import requests


linklist=[]
add_flag = False
url = "https://www.google.com"
r= requests.get(url)
data = r.text
soup = BeautifulSoup(data)
soup.find_all('a')
for link in soup.find_all('a'):
	#print(link.get('href'))
	href = link.get('href')
	if(href.find("http")!=-1):
		r2=requests.get(href)
		if('x-frame-options' in r2.headers):
			print('>>'+href)
			print('x-frame-options:'+r2.headers['x-frame-options'])
		else:
			print("\033[91m {}\033[00m" .format('>>'+href, 1))
