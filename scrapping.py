import urllib.request
from bs4 import BeautifulSoup
import re
wiki = "http://dir.indiamart.com/search.mp?ss=notebook"
companies = []
other_links = []
details = []

def print_them_all():
    i = 1
    for detail in details:
        print (i)
        print ("Company Name: ", detail['Company name'])
        print ("Phone Number: ", detail['Phone Number'])
        i = i + 1

def get_to_next_link(curr_link,details,other_links):
    wiki = curr_link
    if wiki!="":
        print (wiki)
    else:
        print ("No link found")
    page = urllib.request.urlopen(wiki)
    soup = BeautifulSoup(page,"lxml")
    print (soup.title.string)
    companies = []
    all_company=soup.find_all('div',class_=re.compile('normal-listing-color'))
    for company in all_company:
        link=company.find('span',{"class" : 'company-name'})
        dict = {}
        dict['Company name'] = link.text
        all_links=company.find('span',{"class" : 'listing-contact phone-block'})
        abc = all_links.text
        abcd = abc.split( )
        dict['Phone Number'] = abcd[0]
        details.append(dict)
    all_company=soup.find_all('div',class_=re.compile('star-listing-color'))
    for company in all_company:
            link=company.find('span',{"class" : 'company-name'})
            dict = {}
            dict['Company name'] = link.text
            all_links=company.find('span',{"class" : 'listing-contact phone-block'})
            abc = all_links.text
            abcd = abc.split( )
            dict['Phone Number'] = abcd[0]
            details.append(dict)
    all_links=soup.find('div',class_='rf-sch')
    links=all_links.find_all("a")
    if len(other_links)<=50:
            for link in links:
                ab = str(link.get("href"))
                if ab == 'None':
                    pass
                else:
                    ab = "http:" + ab
                    other_links.append(ab)
            link_site = other_links[0]
            del other_links[0]
            get_to_next_link(link_site,details,other_links)
    else:
            print_them_all()

get_to_next_link(wiki,details,other_links)


