# import the required library
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.service import Service
import datetime
from process_csv import get_top_three, get_top_recommendation


def get_url(r_type, page):
    return f"https://trendlyne.com/research-reports/{r_type}/?page={page}"


def main():
    # instantiate a Chrome options object
    options = webdriver.ChromeOptions()

    # set the options to use Chrome in headless mode
    options.add_argument("--headless=new")

    # Use other driver for lambda or linux os
    service = Service("drivers/chromedriver.exe")

    # initialize an instance of the Chrome driver (browser) in headless mode
    driver = webdriver.Chrome(service=service, options=options)

    data = []

    for r_type in ["buy", "sell"]:

        print(f'Crawler running for type "{r_type}"', )

        for page in range(1, 3):
            driver.get(get_url(r_type, page))

            rows = driver.find_elements(By.CLASS_NAME, "Ltop")

            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                data.append([i.text for i in cells[1:9]])
            print(f"Page {page} completed.")

    driver.quit()

    # Remove Empty Rows
    data.remove([])

    df = pd.DataFrame(data, columns=["Date", "Stock", "Broker", "LTP", "Target", "Price At", "Upside", "Type"])
    df = df.dropna()
    df = df[pd.to_numeric(df['Upside'], errors='coerce').notnull()]
    df['Broker'] = df['Broker'].apply(lambda x: x.split('\n')[0])

    filename = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_csv(f'{filename}.csv', index=False)

    # Find Top Recommendation
    top_df = get_top_recommendation(df)

    # Find Top 3
    res = get_top_three(top_df)

    return res


main()
