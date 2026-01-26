import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Job Market Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">📊 Job Market Insights Dashboard</p>', unsafe_allow_html=True)
st.markdown("---")

# Load data
BASE_DIR = Path(__file__).resolve().parent
INSIGHTS_DIR = BASE_DIR / "insights"
DATA_FILE = INSIGHTS_DIR / "cleaned.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df['avg_salary'] = (df['Min_sal'] + df['Max_sal']) / 2
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
st.sidebar.markdown("---")

# Company filter
# companies = ["All"] + sorted(df['company'].unique().tolist())
# selected_company = st.sidebar.selectbox("Select Company", companies)
selected_company="Internshala"

# # Salary range filter
# min_salary = int(df['Min_sal'].min())
# max_salary = int(df['Max_sal'].max())
# salary_range = st.sidebar.slider(
#     "Salary Range (₹)",
#     min_value=min_salary,
#     max_value=max_salary,
#     value=(min_salary, max_salary)
# )

# Apply filters
filtered_df = df.copy()
# if selected_company != "All":
#     filtered_df = filtered_df[filtered_df['company'] == selected_company]
# filtered_df = filtered_df[
#     (filtered_df['Min_sal'] >= salary_range[0]) & 
#     (filtered_df['Max_sal'] <= salary_range[1])
# ]

# Key Metrics Section
st.markdown("### 📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Jobs",
        value=len(filtered_df),
        delta=f"{len(filtered_df) - len(df)} from total" if selected_company != "All" else None
    )

with col2:
    avg_sal = filtered_df['avg_salary'].mean()
    st.metric(
        label="Avg Salary",
        value=f"₹{avg_sal:,.0f}",
        delta=f"{((avg_sal - df['avg_salary'].mean()) / df['avg_salary'].mean() * 100):.1f}%" if selected_company != "All" else None
    )

with col3:
    st.metric(
        label="Companies",
        value=filtered_df['company'].nunique()
    )

with col4:
    max_sal = filtered_df['Max_sal'].max()
    st.metric(
        label="Highest Salary",
        value=f"₹{max_sal:,.0f}"
    )

st.markdown("---")

# Main visualizations
tab1, tab2, tab3 = st.tabs(["📊 Overview", "💼 Company Analysis", "💰 Salary Insights"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("Top Companies Hiring")
        company_counts = filtered_df['company'].value_counts().head(10)
        
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
    
    with col2:
        st.markdown("#### Job Distribution by Company")
        company_counts_pie = filtered_df['company'].value_counts().head(5)
        
        fig = px.pie(
            values=company_counts_pie.values,
            names=company_counts_pie.index,
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            height=400,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("#### Company Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### Average Salary by Company")
        avg_salary_by_company = (
            filtered_df.groupby('company')['avg_salary']
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )
        
        fig = px.bar(
            x=avg_salary_by_company.values,
            y=avg_salary_by_company.index,
            orientation='h',
            labels={'x': 'Average Salary (₹)', 'y': 'Company'},
            color=avg_salary_by_company.values,
            color_continuous_scale='Greens'
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("##### Salary Range by Top Companies")
        top_companies = filtered_df['company'].value_counts().head(5).index
        salary_range_df = filtered_df[filtered_df['company'].isin(top_companies)]
        
        fig = px.box(
            salary_range_df,
            x='company',
            y='avg_salary',
            color='company',
            labels={'avg_salary': 'Salary (₹)', 'company': 'Company'}
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("#### Salary Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### Overall Salary Distribution")
        fig = px.histogram(
            filtered_df,
            x='avg_salary',
            nbins=30,
            labels={'avg_salary': 'Salary (₹)', 'count': 'Frequency'},
            color_discrete_sequence=['#1f77b4']
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("##### Min vs Max Salary Scatter")
        fig = px.scatter(
            filtered_df.head(50),
            x='Min_sal',
            y='Max_sal',
            color='company',
            size='avg_salary',
            hover_data=['company'],
            labels={'Min_sal': 'Minimum Salary (₹)', 'Max_sal': 'Maximum Salary (₹)'}
        )
        fig.update_layout(
            height=400,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

# Data table
st.markdown("---")
st.markdown("### 📋 Job Listings Data")
st.dataframe(
    filtered_df.style.format({
        'Min_sal': '₹{:,.0f}',
        'Max_sal': '₹{:,.0f}',
        'avg_salary': '₹{:,.0f}'
    }),
    use_container_width=True,
    height=400
)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Data scraped from Internshala | Last updated: Today</p>",
    unsafe_allow_html=True
)