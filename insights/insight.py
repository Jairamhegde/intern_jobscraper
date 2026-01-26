import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
INSIGHTS_DIR = BASE_DIR / "insights"

INSIGHTS_DIR.mkdir(exist_ok=True)
def generate_insights(dataFile):
    df = pd.read_csv(dataFile)
    job_counts = df['job'].value_counts().head()
    df['avg_sal'] = (df['Min_sal'] + df['Max_sal']) / 2
    avg_sal_perjob = df.groupby('job')['avg_sal'].mean().sort_values(ascending=False).head(5)
    plt.figure(figsize=(14,5))
    plt.subplot(1,2,1)
    plt.pie(job_counts.values,labels=job_counts.index)
    plt.title("Most Hiring companies")
   
    plt.subplot(1,2,2)
    avg_sal_perjob.plot(kind='bar')
    plt.title("Average salary")
    plt.ylabel("Average Salary")
    plt.xlabel("Job Title")
    plt.xticks(rotation=45)
    plt.show()


data = INSIGHTS_DIR / "cleaned.csv"

# generate_insights(data)


    