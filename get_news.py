import requests
from bs4 import BeautifulSoup

# Getting news, ongoing & recent deaths from Wikipedia Main Page

url = "https://en.wikipedia.org" 
 
response = requests.get(url + "/wiki/Main_Page")
soup = BeautifulSoup(response.text, "html.parser")

mpright = soup.find('div', id="mp-right")
if mpright:
	# news 
	print("")
	ul = mpright.find('ul')
	if ul:
		news_items = ul.find_all("li")
		print("News:")
		print("-----")
		for i, news_item in enumerate(news_items):
			print(f"{i + 1}. {news_item.text.strip()}")
		print("")
	# ongoing
	itnfooter = mpright.find("div", class_="itn-footer")
	if itnfooter:
		containers = itnfooter.find_all("div", recursive=False)
		ongoing = containers[0] if containers else None
		recent_deaths = containers[1] if containers else None
		if ongoing:
			all_ul = itnfooter.find_all("ul")
			ul = all_ul[0] if all_ul else None
			if ul:
				ongoing_items = ul.find_all("li", recursive=False)
				print("Ongoing:")
				print("--------")
				for i, ongoing_item in enumerate(ongoing_items):
					a = ongoing_item.find("a", recursive=False)
					link = url + a['href']
					print(f"{i + 1}. {a.text.strip()} [{link}]")
			print("")
			
		# recent deaths
		print("Recent Deaths:")
		print("--------------")
		if recent_deaths:
			ul = recent_deaths.find("ul")
			deaths = ul.find_all("li", recursive=False)
			for i, death in enumerate(deaths):
				a = death.find("a", recursive=False)
				link = url + a['href']
				print(f"{i + 1}. {a.text.strip()} [{link}]")
		print("")	
	# On this day
	mpotd = mpright.find("div", id="mp-otd")	
	if mpotd:
		print("On this day:")
		print("------------")
		p = mpotd.find("p")
		if p:
			print(p.text.strip() + "\n")
		else: 
			print("Error getting the first paragraph after On this day header*")
		
		all_ul = mpotd.find_all("ul")
		if all_ul:
			for i, ul in enumerate(all_ul):
				if ul:
					if i == len(all_ul) - 1 or i == len(all_ul) - 2:
						break
					items = ul.find_all("li")
					for j, item in enumerate(items):
						print(f"{j + 1}. {item.text.strip()}")
					print("")
