import requests
from bs4 import BeautifulSoup
def get_soup(url):
        headers={"User-Agent":"Mozilla/5.0"}
        response=requests.get(url,headers=headers)
        html=response.text
        soup=BeautifulSoup(html,"html.parser")
        return soup