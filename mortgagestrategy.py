from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import undetected_chromedriver as uc
from export import export_one

load_dotenv()

class MortgagestrategyScraper:

    def __init__(self) -> None:
        pass

    def start(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.mortgagestrategy.co.uk/mortgage-news/")
        # #SHiSO #yel-popup-close
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.content-column article'))
        )
        i = 0
        for i in range(len(elements)):
            element = elements[i]
            link = "Not Found"
            title = ""
            try:
                link = element.find_element(By.CSS_SELECTOR, 'a.entry-thumbnail').get_attribute("href")
            except:
                pass
            try:
                title = element.find_element(By.CSS_SELECTOR, 'div.content header h2').text.strip()        
                if title != "":
                    export_one(
                        data={
                            "link": link,
                            "title": title
                        },
                        filename="mortgagestrategy.xlsx"
                    )
                    print(f"www.mortgagestrategy.co.uk article {i} saved")
            except:
                pass
        driver.quit()

mortgagestrategy_scraper = MortgagestrategyScraper()