# Wikipedia Scraper Python :snake:

This is a python script that scraps data from Wikipedia Main page and save it as json, txt, md and html file formats.

This project is built using:

1. Python
2. BeautifulSoup4 Module
3. Requests Module
4. Json Module

## Installation

Open the terminal in your environment (python venv) or global if you installed pip globally and run the following two commands:

```bash
$ pip install requests
$ pip install beautifulsoup4 
```

And in the project strucutre **create a folder named "storage"**

Now the project will work, no more installation!

## How to use it

Open `script.py` file and go to the last line which contains:

```py
if __name__ == '__main__':
	run()
```

and after `run()` in the next line under it (notice the indetation if you're not familiar with python!) and add one of the following lines, **Don't Add Multiple functions at once** Add one by one so you get the expected file you want without any issues or duplications, each line name is refers to it's job:

```py
	save_to_json() 
	# OR 
	save_to_txt() 
	# OR 
	save_to_md()
	# OR  
	save_to_html() 
	# Finish one then run the script then remove it and add the another one if you want
``` 

that's it now you know how to use this script, if you find any issue don't be shy to tell us in issues tab!

### License

This project is under [MIT license](https://github.com/omarhossam750/wikipedia-scraper/blob/main/LICENSE)

