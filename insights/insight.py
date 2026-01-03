import pandas as pd
# from intern_jobscraper.scraper.cleanData import clean_data
# df = pd.read_csv("data/cleaned_data.csv")
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
INSIGHTS_DIR = BASE_DIR / "insights"

INSIGHTS_DIR.mkdir(exist_ok=True)
def generate_insights(dataFile):
    df=pd.read_csv(dataFile);
    # df[['job','company','status',]]=df[['job','company','status',]]
    job_counts=df['job'].value_counts().head()
    print(job_counts)

# df=pd.read_csv(INSIGHTS_DIR/"cleaned.csv");
data=INSIGHTS_DIR/"cleaned.csv"
generate_insights(data)

    