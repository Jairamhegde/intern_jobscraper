from queries.analysis import *
import streamlit as st
import plotly.express as px

def Dashboard():
    st.set_page_config(
        page_title="Job Market Analysis",
        layout="wide"
    )

    # ===== TITLE =====
    st.markdown(
        "<h1 style='text-align:center;'> Internship Job Market Analysis</h1>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    # ===== SECTION 1: OVERVIEW =====
    st.subheader("Market Overview")

    col1, col2 = st.columns(2)

    # ---- Top Skills ----
    with col1:
        df = topSkills()
        topskill1=df.iloc[0]['name']
        topskill2=df.iloc[1]['name']
        topskill3=df.iloc[2]['name']

        fig = px.bar(
            df,
            x="demand",
            y="name",
            orientation="h",
            title="Top Demanding Skills",
            color_discrete_sequence=["#4da6ff"]
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            "**Insight:** Python, MySQL, and JavaScript dominate internship requirements, indicating strong demand for backend and data-related skills."
        )

    # ---- Top Roles ----
    with col2:
        df2 = roles()
        topRole1=df2.iloc[0]['J_title']
        topRole2=df2.iloc[1]['J_title']
        

        fig = px.bar(
            df2,
            x="demand",
            y="J_title",
            orientation="h",
            title="Top Demanding Roles",
            color_discrete_sequence=["#ff6666"]
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            f"**Insight:** {topRole1} and {topRole2} account for the majority of openings, suggesting companies prefer versatile engineers at the intern level."
        )

    st.markdown("---")

    # ===== SECTION 2: DEEP INSIGHT =====
    st.subheader("Skill Overlap Across Top Roles")
    
    df3 = commonRoles()
    mostcommonSkill=df3.iloc[0]['skill']

    fig = px.bar(
        df3,
        x="total_occurrences",
        y="skill",
        orientation="h",
        title="Common Skills in Top 2 Demanding Roles",
        color_discrete_sequence=["#66cc99"]
    )
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        f"**Insight:** These skills consistently appear across both top hiring roles which are {topRole1} and {topRole2},and here {mostcommonSkill} is the most common skill."
    )

    st.markdown("---")

    # ===== SECTION 3: FINAL TAKEAWAY =====
    st.subheader("Key Takeaways")
    st.markdown(
        f"""
        - {topRole1} and {topRole2} roles dominate internship hiring.
        - {topskill1}, {topRole2}, and {topskill3} form the core skill set across roles.
        - Skill overlap shows companies value stack-based, not isolated, expertise.
        """
    )

Dashboard()
