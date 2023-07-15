from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from typing import Dict
import json
from scraper.types import Job, Company

SEARCH_URL_BASE = "https://www.linkedin.com/jobs/search/?"
FILTERS = {
    "f_JT": "F",
    "geoID": "102257491",
    "keywords": "Software%20Engineer",
    "location": "London%2C%20England%2C%20United%20Kingdom",
    "refresh": "true",
}


def main():
    """
    This program looks on LinkedIn for software engineering jobs in London.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    companies: Dict[str, Company] = {}

    filter_url = "&".join([f"{key}={value}" for key, value in FILTERS.items()])
    search_filter = f"{SEARCH_URL_BASE}{filter_url}"
    print(f"Requesting {search_filter}...")
    driver.get(search_filter)
    time.sleep(3)

    job_result_elements = driver.find_elements(By.CLASS_NAME, "base-search-card__info")
    for element in job_result_elements:
        title = element.find_element(By.CLASS_NAME, "base-search-card__title").text
        company_str = element.find_element(
            By.CLASS_NAME, "base-search-card__subtitle"
        ).text
        metadata = element.find_element(
            By.CLASS_NAME, "base-search-card__metadata"
        ).text

        if company_str not in companies:
            companies[company_str] = Company(company_str)
        company = companies[company_str]
        company.add_job(Job(title, metadata))

    with open("jobs.json", "w", encoding="utf-8") as file:
        json.dump(
            [company for company in companies.values()],
            file,
            indent=2,
            default=lambda o: o.__dict__,
        )


if __name__ == "__main__":
    main()

# 