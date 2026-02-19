from leaders_scraper import wikipediaScraper

def main():
    scraper = wikipediaScraper()

    countries = scraper.get_countries()
    print(f"countries: {countries}")

    for country in countries:
        scraper.get_leaders(country)

    scraper.to_json_file("leaders.json")
    print("ok")

if __name__ == "__main__":
    main()
