
from scraper.fetcher import get_soup
from scraper.extractor import scrape_data
from scraper.cleanData import clean_data
from insights.insight import generate_insights
from app import DashBoard
from pathlib import Path
import subprocess
import sys

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

def run_streamlit():
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "app.py"
    ])
     
if __name__=='__main__':
    internshala("https://internshala.com/jobs/ai-agent-development,backend-development-jobs/",3)   
    # run_streamlit()
