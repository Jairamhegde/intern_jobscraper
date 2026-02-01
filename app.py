def DashBoard(file_path):
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from pathlib import Path
    from queries.analysis import topSkills,roles,topLocations


    BASE_DIR = Path(__file__).resolve().parent
    FILEPATH_DIR = BASE_DIR / f"{file_path}"
    # DATA_FILE = INSIGHTS_DIR / "cleaned.csv"

    datafile=FILEPATH_DIR

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

    # def showInsight(datafile):
    df=topSkills()
    tab1,tab2=st.tabs(
        ["Top Hiring Companies","Average Salary by Job Title"]
    )
    with tab1:
        column1,column2=st.columns(2)
        with column1:
            st.markdown("Top Demanding Skills")
            skills = df['name']
            demand=df['demand']
        
            fig = px.bar(
                x=demand,
                y=skills,
                orientation='h',
                labels={'x': 'Number of Jobs', 'y': 'Skills'},
    
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                showlegend=False,
                height=400,
                margin=dict(l=0, r=0, t=30, b=0)
            )
            st.plotly_chart(fig, use_container_width=True)
        df2=roles()
        with column2:
            st.markdown("Top Demanding Roles")
            job_roles=df2['J_title']
            demandRoles=df2['demand']
            fig=px.bar(
                x=demandRoles,
                y=job_roles,
                labels={'x':'demand','y':'Job '},
                color=job_roles,
                color_continuous_scale='reds',
            )
            fig.update_layout(
                showlegend=False,
                height=400,
                margin=dict(l=0, r=0, t=30, b=0)
            )
            st.plotly_chart(fig,use_container_width=True)

    with tab2:
        column1,column2=st.columns(2)
        with column1:
            pass

DashBoard('D:\java\Python\jobscraper\intern_jobscraper\insights\cleaned.csv')




