from mortgagestrategy import mortgagestrategy_scraper
from independent import independent_scraper
from moneyweek import moneyweek_scraper
from sky import sky_scraper

if __name__ == "__main__":
    mortgagestrategy_scraper.start()
    independent_scraper.start()
    moneyweek_scraper.start()
    sky_scraper.start()