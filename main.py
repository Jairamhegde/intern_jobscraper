
from scraper.fetcher import get_soup
from scraper.extractor import scrape_data
from scraper.cleanData import clean_data
from insights.insight import generate_insights
from pathlib import Path

def internshala(url,pages):
        
        newl=[]
        for i in range(1,pages+1):
            if i==1:
                link=url
            else:
                link=url+f'page-{i}'
            g=get_soup(link)
            s=scrape_data(g)
            newl.extend(s)
        clean_data(newl)

if __name__=='__main__':
    internshala("https://internshala.com/jobs/",3)
    generate_insights("insights//cleaned.csv")
