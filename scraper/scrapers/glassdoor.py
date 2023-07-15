from bs4 import BeautifulSoup
import re
import requests

URL_PREFIX = (
    "https://www.glassdoor.co.uk/Salaries/software-engineer-salary-SRCH_KO0,17_IP"
)
URL_SUFFIX = ".htm"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
}

if __name__ == "__main__":
    index = 1
    url = f"{URL_PREFIX}{index}{URL_SUFFIX}"
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.content, "html.parser")
    posts = soup.find_all("div", {"data-test": re.compile(r"^salaries-list-item-")})
    soup.find()
    for post in posts:
        company = post.find(
            "h3", {"data-test": re.compile(r"^salaries-list-item-.*-employer-name$")}
        )
        salary = post.find(
            "div", {"data-test": re.compile(r"^salaries-list-item-.*-salary-info$")}
        )
        if company and salary:
            print(company.text.strip(), salary.text.strip())
