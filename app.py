import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INSIGHTS_DIR = BASE_DIR / "insights"
DATA_FILE = INSIGHTS_DIR / "cleaned.csv"

data="insights\cleaned.csv"

st.set_page_config(
    page_title="Job Market Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"  
)
st.markdown("""<style>
.main-title{
            text-align:center;
            color:white;
            font-size:5rem;
            font-weight:bold;
            }
</style>""",unsafe_allow_html=True)

st.markdown("<p class='main-title'>Job Market Analysis</p>",unsafe_allow_html=True)
st.markdown("--------")

def showInsight(datafile):
    df=pd.read_csv(datafile)
    tab1,tab2=st.tabs(
        ["Top Hiring Companies","Average Salary by Job Title"]
    )
    with tab1:
        column1,column2=st.columns(2)
        with column1:
            st.markdown("Top Companies Hiring")
            company_counts = df['company'].value_counts().head(10)
        
            fig = px.bar(
                x=company_counts.values,
                y=company_counts.index,
                orientation='h',
                labels={'x': 'Number of Jobs', 'y': 'Company'},
                color=company_counts.values,
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                showlegend=False,
                height=400,
                margin=dict(l=0, r=0, t=30, b=0)
            )
            st.plotly_chart(fig, use_container_width=True)

        with column2:
            st.markdown("Average Salary asper Job Title")
            df['average']=(df['Min_sal']+df['Max_sal'])/2
            fig=px.bar(
                df.groupby('job')['average'].mean().sort_values(ascending=False).head(10),
                labels={'value':'Average Salary','job':'Job Title'},
                color=df.groupby('job')['average'].mean().sort_values(ascending=False).head(10).values,
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig,use_container_width=True)

    with tab2:
        column1,column2=st.columns(2)
        with column1:
            pass
            

showInsight(DATA_FILE)




