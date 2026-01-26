import requests
from bs4 import BeautifulSoup

# from cleanData import clean_data
# from extractor import scrape_data
def get_soup(url):
        headers={"User-Agent":"Mozilla/5.0"}
        response=requests.get(url,headers=headers)
        html=response.text
        soup=BeautifulSoup(html,"html.parser")
        return soup

# soupp=get_soup("https://internshala.com/jobs/ai-agent-development,backend-development-jobs/")
# scrape=scrape_data(soupp)
# clened=clean_data(scrape)
# print(scrape)
# # print(soupp)