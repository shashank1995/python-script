import re
import requests
from bs4 import BeautifulSoup

data = {}
r = requests.get('https://www.google.co.in/search?q=dtu&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiqkvaPlufgAhVqGTQIHfOCAgsQ_AUIECgD&biw=1280&bih=690&dpr=2')
soup = BeautifulSoup(r.text,"lxml")
data['title'] = [ span.text for span in soup.select('cite')]
summ = 1
for a in data['title']:
	if a[:4] != 'http':
		a = "http://" + a
	r = requests.get(a)
	soup = BeautifulSoup(r.text,"lxml")
	img_tags = soup.findAll('img',{"src":True})
	urls = [img['src'] for img in img_tags]
	for url in urls:
		if url:
			if url[:4] == 'http':
				filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
				if filename:
					with open(filename.group(1), 'wb') as f:
						response = requests.get(url)
						f.write(response.content)
						print (("Image downloaded: No.%d") % (summ))
						summ = summ + 1

