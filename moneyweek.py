from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import undetected_chromedriver as uc
from export import export_one

load_dotenv()

class MoneyweekScraper:

    def __init__(self) -> None:
        pass

    def start(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://moneyweek.com/personal-finance/mortgages")
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'section.listing .listing__item a.listing__link'))
        )
        i = 0
        j = 1
        for i in range(len(elements)):
            element = elements[i]
            link = element.get_attribute("href")
            title = ""
            try:
                title = element.find_element(By.CSS_SELECTOR, 'h2').text.strip()
                if title != "":
                    export_one(
                        data={
                            "link": link,
                            "title": title
                        },
                        filename="moneyweek.xlsx"
                    )
                    print(f"moneyweek.com page {j} article {i} saved")
            except:
                pass
        pages = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.flexi-pagination a'))
        )
        for page in pages:
            j += 1
            driver.get(page.get_attribute("href"))
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'section.listing .listing__item a.listing__link'))
            )
            i = 0
            for i in range(len(elements)):
                element = elements[i]
                link = element.get_attribute("href")
                title = ""
                try:
                    title = element.find_element(By.CSS_SELECTOR, 'h2').text.strip()
                    if title != "":
                        export_one(
                            data={
                                "link": link,
                                "title": title
                            },
                            filename="moneyweek.xlsx"
                        )
                        print(f"moneyweek.com page {j} article {i} saved")
                except:
                    pass
        driver.quit()

moneyweek_scraper = MoneyweekScraper()