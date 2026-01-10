import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from pathlib import Path


st.set_page_config(page_title="Job Market Insights", layout="centered")
st.title("Job Market Insights Dashboard")
BASE_DIR = Path(__file__).resolve().parent
INSIGHTS_DIR = BASE_DIR / "insights"
DATA_FILE = INSIGHTS_DIR / "cleaned.csv"

df = pd.read_csv(DATA_FILE)

column1,locumn2 = st.columns(2)
with column1:
    st.subheader("Top Companies Hiring the Most")

    company_counts = df['company'].value_counts().head(5)

    fig1, ax1 = plt.subplots(figsize=(6,6))
    ax1.pie(
        company_counts.values,
        labels=company_counts.index,
        autopct='%1.1f%%',
        startangle=140)
    ax1.set_title("Top 5 Companies by Job Count")
    st.pyplot(fig1)
with locumn2:
    st.subheader("Average Salary by Company")
    df['avg_salary'] = (df['Min_sal'] + df['Max_sal']) / 2
    avg_salary = (
        df.groupby('company')['avg_salary']
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )
    fig2, ax2 = plt.subplots(figsize=(6,6))
    sns.barplot(x=avg_salary.index, y=avg_salary.values, ax=ax2)
    ax2.set_xlabel("Company")
    ax2.set_ylabel("Average Salary")
    ax2.set_title("Top 5 Companies by Average Salary")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
