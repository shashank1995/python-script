import re
import requests
from bs4 import BeautifulSoup

links = []
emails = []
r = requests.get('https://www.google.co.in/search?rlz=1C5CHFA_enIN718IN718&biw=1280&bih=726&ei=oy9nWsvnJIT08QXWrZXACA&q=books+manufacturing+company&oq=books+manu&gs_l=psy-ab.3.0.0l10.2227640.2232901.0.2235332.10.10.0.0.0.0.215.1421.0j2j5.7.0....0...1c.1.64.psy-ab..3.7.1420...0i67k1j0i131k1.0.fFiX0yLU3lg')
soup = BeautifulSoup(r.text,"lxml")
link_list=soup.find_all('div',{"class" : 'g'})
for a in link_list:
	link=a.find_all('h3',{"class" : 'r'})
	for b in link:
		link1=b.find('a')
		link2=link1['href']
		link3=link2.replace("/url?q=","")
		links.append(link3)
for a in links:
	try:
		r = requests.get(a)
		soup = BeautifulSoup(r.text,"lxml")
		all_link = soup.find_all('a')
		for b in all_link:
			try:
				if b['href']:
					links.append(b['href'])
					s = b['href']
					if s[:7] == "mailto:":
						s = s.replace("mailto:","")
						if s in emails:
							pass
						else:
							emails.append(s)
							print (s)
			except KeyError:
				pass
	except requests.exceptions.RequestException as err:
		pass