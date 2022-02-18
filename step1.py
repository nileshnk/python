import bs4
import requests
import smtplib

getPage = requests.get('https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=recent&distanceType=Mi&radius=24km&latitude=28.63096&longitude=77.21722&loc_group_id=&loc_query=india&base_query=&city=&country=IND&region=&county=&query_options=&')

getPage.raise_for_status()

menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
foods = menu.select('.job-tile')
print(foods)





#https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45#the-process-of-building-the-web-scrapig-script
