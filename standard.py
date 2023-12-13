from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import undetected_chromedriver as uc
from export import export_one

load_dotenv()

class StandardScraper:

    def __init__(self) -> None:
        pass

    def start(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.standard.co.uk/topic/mortgages")
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.section-content a[data-testid="link-data-testid"] p'))
        )
        i = 0
        for i in range(len(elements)):
            element = elements[i]
            link = ""
            try:
                link = element.find_element(By.XPATH, '..').get_attribute("href")
            except:
                pass
            title = element.text
            try:
                if title != "":
                    export_one(
                        data={
                            "link": link,
                            "title": title
                        },
                        filename="standard.xlsx"
                    )
                    print(f"www.standard.co.uk article {i} saved")
            except:
                pass
        
        driver.quit()

standard_scraper = StandardScraper()