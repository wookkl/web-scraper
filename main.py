import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup  = BeautifulSoup(indeed_result.text, "html_parser")
pagination = indeed_soup.find("div",{"class": "pagination"})
pages = pagination.find_all('a')
print(pages)