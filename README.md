# Wikipedia Scraper 

- Repository: `wikipedia-scraper`
- Type: `Consolidation`
- Duration: `3 days`
- Team: `solo project`

## Mission Objectives

1. Creating a self-contained development environment (virtual environment)
2. Retrieving some information from an API
3. Leveraging my knowledge to scrape a website that does not provide an API
4. Saving the output for later processing

More specifically, in this project we will query an API to obtain a list of countries and their past political leaders. We then extract and sanitize their short bio from Wikipedia. Finally, we save the data.

## Learning Objectives

- Use [venv](https://docs.python.org/3/library/venv.html) to isolate the Python environment
- Use [requests](https://requests.readthedocs.io/en/latest/) to call an external API on any internet link
- Use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to extract text from HTML
- Get comfortable with JSON 
- (_Optional_) Use OOP to split functionalities into classes and methods
- (_Optional_) Use regex to clean text data
- (_Optional_) Use multiprocessing to speedup your code

## The Mission

Create a scraper that builds a JSON file with the political leaders of each country I get from [this API](https://country-leaders.onrender.com/docs).

Include in this file the first paragraph of the Wikipedia page of these leaders.

### Must-have features (MVP)

- Have a working `wikipedia_scraper.ipynb` notebook that calls the API and creates a JSON file
- Create exception to include proper exception handling

### Nice-to-have features

- Use [Session()](https://requests.readthedocs.io/en/latest/user/advanced/) from the `requests` library instead of `get()`
- A switch to store the output as CSV instead of JSON
- Speed up the execution using multiprocessing

### Steps

#### 0. Setup and preparation
- Create a GitHub repo with a name that makes sense (for example, `wikipedia-scraper`)
- Create a virtual environment using [venv](https://docs.python.org/3/library/venv.html). Don't forget to add it to the `.gitignore` file.
- **Read the docs from the [API](https://country-leaders.onrender.com/docs)!**
- Copy the `wikipedia_scraper.ipynb` file from your fork into your new project repo.

#### 1. Complete the first MVP (Notebook)
- Activate the environment and install the required modules (e.g. request, and beautifulsoup). 
- Complete the Notebook.

#### 2a. A `scraper.py` module (Second MVP - OOP)

- Code up a `WikipediaScraper` scraper object that allows you to structurally retrieve data from the API.

The object should contain at least these six attributes: 
- `base_url: str` containing the base url of the API (https://country-leaders.onrender.com)
- `country_endpoint: str` → `/countries` endpoint to get the list of supported countries
- `leaders_endpoint: str` → `/leaders` endpoint to get the list of leaders for a specific country
- `cookies_endpoint: str` → `/cookie` endpoint to get a valid cookie to query the API
- `leaders_data: dict` is a dictionary where you store the data you retrieve before saving it into the JSON file
- `cookie: object` is the cookie object used for the API calls

The object should contain at least these five methods:
- `refresh_cookie() -> object` returns a new cookie if the cookie has expired
- `get_countries() -> list` returns a list of the supported countries from the API
- `get_leaders(country: str) -> None` populates the `leader_data` object with the leaders of a country retrieved from the API
- `get_first_paragraph(wikipedia_url: str) -> str` returns the first paragraph (defined by the HTML tag `<p>`) with details about the leader
- `to_json_file(filepath: str) -> None` stores the data structure into a JSON file

#### 2b. A `main.py` script

Bundle everything together in a `main.py` file that calls the `WikipediaScraper` object and saves the data into a JSON file.