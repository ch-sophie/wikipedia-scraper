import requests
import re
import json
import time
from bs4 import BeautifulSoup

class wikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        
        self.cookie = None #cookie object
        #session to keep the connection open do it once and not everytime
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})

    def refresh_cookies(self):
        #return a new cookie if the cookie has expired
        try:
            response = self.session.get(f"{self.base_url}{self.cookies_endpoint}")
            response.raise_for_status() #raise error for status codes
            self.cookie = response.cookies
            return self.cookie
        except requests.exceptions.RequestException as e:
            print(f"error: {e}")
            return None
    
    def get_countries(self):
        #return list of supported countries
        try:
            if not self.cookie: #check cookie first
                self.refresh_cookies()
            response = self.session.get(f"{self.base_url}{self.country_endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"error: {e}")
            return [] 
            #if returned None, a loop like for country in countries: would crash with a TypeError. By returning an empty list, the loop simply doesn't run, and the script finishes gracefully.

    def get_first_paragraph(self, wikipedia_url):
        try: 
            res = self.session.get(wikipedia_url)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")

            for p in soup.find_all('p'):
                if p.find('b'):
                    text = p.get_text() #extract text from p
                    #sanitisation
                    text = re.sub(r'\[.*?\]', '', text) #citations [1]
                    for _ in range(2):
                        text = re.sub(r'\s*\([^()]*\)', '', text) #parentheses and double parentheses
                    text = re.sub(r'\s*/.*?/', '', text) #phonetics //
                    text = text.replace('\xa0', ' ') #non breaking space
                    return re.sub(r'\s+', ' ', text).strip()
        except requests.exceptions.RequestException as e:
            print("error: {e}") #failed to scrape wikipedia at url
            return "" #else return ""

    def get_leaders(self, country):
        try:
            if not self.cookie:
                self.refresh_cookies()

            params = {"country": country}
            res = self.session.get(f"{self.base_url}{self.leaders_endpoint}", params=params)

            if res.status_code == 403:
                self.refresh_cookies()
                res = self.session.get(f"{self.base_url}{self.leaders_endpoint}", params=params)
        
            if res.status_code == 200:
                leaders = res.json()
                for leader in leaders:
                    if leader.get("wikipedia_url"):
                        leader['first_paragraph'] = self.get_first_paragraph(leader['wikipedia_url'])
                        time.sleep(0.1)
                self.leaders_data[country] = leaders
        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print("error: {e}") #error processing leaders for {country}

    def to_json_file(self, filepath):
        try:
            with open(filepath, "w", encoding='utf-8') as f:
                json.dump(self.leaders_data, f, indent=4)
            print("data saved successfully")
        except IOError as e:
            print(f"error saving data to {filepath}: {e}")
