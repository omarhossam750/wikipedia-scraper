import requests, json
from bs4 import BeautifulSoup

# Getting news, ongoing & recent deaths from Wikipedia Main Page

url = "https://en.wikipedia.org" 
response = requests.get(url + "/wiki/Main_Page")
soup = BeautifulSoup(response.text, "html.parser")

data = { 
	"news": [], 
	"ongoing": [], 
	"recent_deaths": [], 
	"on_this_day": [] 
}
links = {
	"ongoing": [],
	"recent_deaths": []
}

def save_to_json():
	try:
		with open("./storage/data.json", "w", encoding='utf-8') as file:
			
			for i, link in enumerate(links["ongoing"]):
				data["ongoing"][i] = data["ongoing"][i] + f" [ {link} ]"
			for i, link in enumerate(links["recent_deaths"]):
				data["recent_deaths"][i] = data["recent_deaths"][i] + f" [ {link} ]"
			
			json.dump(data, file, indent=4, ensure_ascii=False)
		print("Data saved in \"storage/data.json\"!")
	except:
		print("An error eccoured while saving to json!")
	
def save_to_txt():
	try:
		with open("./storage/data.txt", "w", encoding='utf-8') as file:
			for key, values in data.items():
				if key == "news":
					file.write("News:\n")
					file.write("-----\n")
				elif key == "ongoing":
					file.write("Ongoing:\n")
					file.write("--------\n")
				elif key == "recent_deaths":
					file.write("Recent Deaths:\n")
					file.write("--------------\n")
				if key == "on_this_day":
					file.write("On this day:\n")
					file.write("------------\n")
					file.write(values[0] + "\n\n")
					for j, item in enumerate(values[1: len(values)]): 
						file.write(f"{j + 1}. {item}\n")
					file.write("\n")
					
				else:
					for j, item in enumerate(values): 
						if key == "recent_deaths" or key == "ongoing":
							file.write(f"{j + 1}. {item} [ {links[key][j]} ]\n")
						else:
							file.write(f"{j + 1}. {item}\n")
						
					file.write("\n")
					
		print("Data saved in \"storage/data.txt\"!")
	except:
		print("An error eccoured while saving to txt!")

def save_to_md():
	try:
		with open("./storage/data.md", "w", encoding='utf-8') as file:
			file.write("# Wikipedia Scraper\n\n")
			for key, values in data.items():
				if key == "news":
					file.write("## News:\n\n")
				elif key == "ongoing":
					file.write("## Ongoing: \n\n")
				elif key == "recent_deaths":
					file.write("## Recent Deaths:\n\n")
				if key == "on_this_day":
					file.write("## On this day:\n\n")
					file.write(f"**{values[0]}** \n\n")
				
					for j, item in enumerate(values[1: len(values)]): 
						file.write(f"{j + 1}. {item}\n")
					file.write("\n")
				else:
					for j, item in enumerate(values): 
						if key == "ongoing" or key == "recent_deaths":
							file.write(f"{j + 1}. [{item}]({links[key][j]})\n")
						else:
							file.write(f"{j + 1}. {item}\n")
					file.write("\n")
				
		print("Data saved in \"storage/data.md\"!")
	except:
		print("An error eccoured while saving to md!")

def save_to_html():
	try:
		with open("./storage/data.html", "w", encoding="utf-8") as file:
			file.write('<!DOCTYPE html>\n')
			file.write('  <html lang="en">\n')
			file.write('  	<head>\n')
			file.write('  	  <title>Wikipedia Data Scraper</title>\n')
			file.write('  	  <meta charset="UTF-8">\n')
			file.write('  	  <meta name="viewport" content="width=device-width, initial-scale=1">\n')
			file.write('  	</head>\n')
			file.write('  	<body>\n')
			file.write('  	  <h1>Wikipedia Web Scraper</h1><hr />\n')
			for key, values in data.items():
				if key == "news":
					file.write("  	  <h2>News</h2>\n")
				elif key == "ongoing":
					file.write("  	  <h2>Ongoing</h2>\n")
				elif key == "recent_deaths":
					file.write("  	  <h2>Recent Deaths</h2>\n")
				if key == "on_this_day":
					file.write("  	  <h2>On This Day</h2>\n")
					file.write(f"	  <p>{values[0]}</p>\n")
					file.write("  	  <ol>\n")
					for j, item in enumerate(values[1: len(values)]): 
							file.write(f"  	    <li>{item}</li>\n")
					file.write("  	  </ol>\n\n")
				else:
					file.write("  	  <ol>\n")
					for j, item in enumerate(values): 
						if key == "ongoing" or key == "recent_deaths":
							file.write(f"  	    <li><a href='{links[key][j]}' target='_blank'>{item}</a></li>\n")
						else:
							file.write(f"  	    <li>{item}</li>\n")
					file.write("  	  </ol>\n\n")
			file.write('  	</body>\n')
			file.write('  </html>\n')
		print("Data saved in \"storage/data.html\"!")
	except:
		print("An error eccoured while saving to html.")

def print_data(): # for console/terminal
	print("")
	for key, values in data.items():
		if key == "news":
			print("News:")
			print("-----")
		elif key == "ongoing":
			print("Ongoing:")
			print("--------")
		elif key == "recent_deaths":
			print("Recent Deaths:")
			print("--------------")
		elif key == "on_this_day":
			print("On this day:")
			print("------------")
			
		for j, item in enumerate(values): 
			print(f"{j + 1}. {item}")
		print("")
		
def run():
	mpright = soup.find('div', id="mp-right")
	if mpright:
		# news 
		ul = mpright.find('ul')
		if ul:
			news_items = ul.find_all("li")
			for i, news_item in enumerate(news_items):
				data["news"].append(news_item.text.strip())
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
					for i, ongoing_item in enumerate(ongoing_items):
						a = ongoing_item.find("a", recursive=False)
						link = url + a['href']
						links["ongoing"].append(link)
						data["ongoing"].append(a.text.strip())
				
			# recent deaths
			if recent_deaths:
				ul = recent_deaths.find("ul")
				deaths = ul.find_all("li", recursive=False)
				for i, death in enumerate(deaths):
					a = death.find("a", recursive=False)
					link = url + a['href']
					links["recent_deaths"].append(link)
					data["recent_deaths"].append(a.text.strip())	
		# On this day
		mpotd = mpright.find("div", id="mp-otd")	
		if mpotd:
			p = mpotd.find("p")
			if p:
				data["on_this_day"].append(p.text.strip())
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
							data["on_this_day"].append(item.text.strip())

if __name__ == '__main__':
	run()
	# Add the function below in the same indentaion! 
	save_to_json()
