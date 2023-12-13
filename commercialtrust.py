from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import undetected_chromedriver as uc
from export import export_one

load_dotenv()

class CommercialtrustScraper:

    def __init__(self) -> None:
        pass

    def start(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.commercialtrust.co.uk/news/")
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article h5 a'))
        )
        i = 0
        j = 0
        while j < 20:
            j += 1
            for i in range(len(elements)):
                element = elements[i]
                link = element.get_attribute("href")
                title = element.text
                try:
                    if title != "":
                        export_one(
                            data={
                                "link": link,
                                "title": title
                            },
                            filename="commercialtrust.xlsx"
                        )
                        print(f"www.commercialtrust.co.uk page {j} article {i} saved")
                except:
                    pass
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#pagelink-next'))
                )
                if element.get_attribute("href").split("=")[-1] == str(j):
                    break
                driver.get(element.get_attribute("href"))
                elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article h5 a'))
                )
            except:
                break
        
        driver.quit()

commercialtrust_scraper = CommercialtrustScraper()