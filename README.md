# Wikipedia Scraper 

- Repository: `wikipedia-scraper`
- Type: `Consolidation`
- Duration: `3 days`
- Team: `solo project`

## Mission Objectives

1. Creating a self-contained development environment (virtual environment)
2. Retrieving some information from an API
3. Leveraging your knowledge to scrape a website that does not provide an API
4. Saving the output for later processing

More specifically, in this project we will query an API to obtain a list of countries and their past political leaders. We then extract and sanitize their short bio from Wikipedia. Finally, we save the data.

## Learning Objectives

- Use [venv](https://docs.python.org/3/library/venv.html) to isolate your Python environment
- Use [requests](https://requests.readthedocs.io/en/latest/) to call an external API are any internet link
- Use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to extract text from HTML
- Use proper exception handling
- Get comfortable with JSON 
- (_Optional_) Use OOP to split functionalities into classes and methods
- (_Optional_) Use regex to clean text data
- (_Optional_) Use multiprocessing to speedup your code

## The Mission

Create a scraper that builds a JSON file with the political leaders of each country you get from [this API](https://country-leaders.onrender.com/docs).

Include in this file the first paragraph of the Wikipedia page of these leaders (you'll retrieve the Wikipedia page URL from the API, which you then have to scrape yourself).

### Must-have features (MVP)

- You should have a working `wikipedia_scraper.ipynb` notebook that calls the API and creates a JSON file
- Create your own exception to include proper exception handling
- Have a nice README that explains your project.
