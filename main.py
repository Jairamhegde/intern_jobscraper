from scraper.fetcher import get_soup
from scraper.scape import scrape_data
from data.cleanData import clean_data
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

print("This is just for sample..")