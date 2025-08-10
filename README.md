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
Now the project will work, no more installation!

## How to use it

Open `script.py` file and go to the last line which contains:

```py
if __name__ == '__main__':
	run()
```

and after `run()` in the next line under it (notice the indetation if you're not familiar with python!) and add one of the following lines or add all of them, each line name is obvious:

```py
	save_to_json()
	save_to_txt()
	save_to_md() # this function has a minor issue we will solve it soon
	save_to_html() # this function has the same minor issue we will solve it soon
``` 

that's it now you know how to use this script!

### License

This project is under [MIT license](https://github.com/omarhossam750/wikipedia-scraper/blob/main/LICENSE)
