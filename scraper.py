import bs4
from urllib.request import urlopen
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://www.bu.edu/innovate/events/"

uClient = uReq(my_url)
raw_data = uClient.read()
uClient.close()

page_soup = soup(raw_data,"html.parser")

#event_list = page_soup.findAll("div",{"class":"event-list"})
events = page_soup.findAll("div",{"class":"events"})
print(events)

