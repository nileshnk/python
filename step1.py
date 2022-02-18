import bs4
import requests
import smtplib

getPage = requests.get('http://www.google.com/images')

getPage.raise_for_status()

menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
foods = menu.select('.gb1')
print(foods)

#https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45#the-process-of-building-the-web-scrapig-script
