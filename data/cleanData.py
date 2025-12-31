import pandas as pd
def clean_data(dataset):
    df=pd.DataFrame(dataset)
    df['Salary']=df['Salary'].str.replace("₹","",regex=False)
    df['Salary']=df['Salary'].str.replace(",","",regex=False)
    sal=df['Salary'].str.split("-",expand=True)
    df['Min_sal']=sal[0]
    df['Max_sal']=sal[1]
    
    df['Min_sal']=pd.to_numeric(df['Min_sal'],errors='coerce')
    df['Max_sal']=pd.to_numeric(df['Max_sal'],errors='coerce')
    df.to_csv("cleaned.csv",index=False)
    