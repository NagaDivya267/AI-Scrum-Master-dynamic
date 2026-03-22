import streamlit as st
import pandas as pd
import csv

# Page config
st.set_page_config(page_title="AI Scrum Assistant", layout="wide", initial_sidebar_state="expanded")

# Define the CSV file path
csv_file = "sprint_data.csv"

# Title and header
st.markdown("# 🚀 AI SCRUM ASSISTANT - SPRINT DATA VIEWER")
st.markdown("---")

def read_from_csv():
    """Read data from CSV file into DataFrame"""
    try:
        df = pd.read_csv(csv_file)
        return df
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        return None

def get_sprint_summary(df):
    """Generate summary statistics from DataFrame"""
    sprints = {}
    for _, row in df.iterrows():
        sprint = row['Sprint']
        status = row['Status']
        story_points = int(row['StoryPoints']) if isinstance(row['StoryPoints'], (int, float)) else 0
        
        if sprint not in sprints:
            sprints[sprint] = {"Done": 0, "In Progress": 0, "To Do": 0, "Total": 0}
        
        sprints[sprint]["Total"] += story_points
        sprints[sprint][status] = sprints[sprint].get(status, 0) + story_points
    
    return sprints

# Read data
df = read_from_csv()

if df is not None:
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["📊 All Data", "📈 Sprint Summary", "🎯 Metrics"])
    
    # Tab 1: All Data
    with tab1:
        st.subheader("Sprint Data Table")
        st.dataframe(df, width='stretch', height=400)
        st.metric("Total Rows", len(df))
    
    # Tab 2: Sprint Summary
    with tab2:
        st.subheader("Sprint Completion Status")
        sprints_summary = get_sprint_summary(df)
        
        cols = st.columns(len(sprints_summary))
        for idx, (sprint_name, stats) in enumerate(sorted(sprints_summary.items())):
            with cols[idx]:
                completion = (stats["Done"] / stats["Total"] * 100) if stats["Total"] > 0 else 0
                st.metric(
                    label=sprint_name,
                    value=f"{completion:.0f}%",
                    delta=f"{stats['Done']}/{stats['Total']} pts"
                )
        
        # Detailed summary
        st.subheader("Detailed Sprint Breakdown")
        for sprint_name, stats in sorted(sprints_summary.items()):
            with st.expander(f"{sprint_name} - {stats['Done']}/{stats['Total']} pts"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Points", stats["Total"])
                with col2:
                    st.metric("✅ Done", stats["Done"])
                with col3:
                    st.metric("🔄 In Progress", stats["In Progress"])
                with col4:
                    st.metric("⏳ To Do", stats["To Do"])
    
    # Tab 3: Metrics
    with tab3:
        st.subheader("Key Metrics")
        
        # Calculate overall metrics
        sprints_summary = get_sprint_summary(df)
        total_story_points = sum(s["Total"] for s in sprints_summary.values())
        total_completed = sum(s["Done"] for s in sprints_summary.values())
        total_in_progress = sum(s["In Progress"] for s in sprints_summary.values())
        total_todo = sum(s["To Do"] for s in sprints_summary.values())
        
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total Story Points", total_story_points)
        with m2:
            st.metric("Completed", f"{total_completed}/{total_story_points}")
        with m3:
            st.metric("In Progress", total_in_progress)
        with m4:
            st.metric("To Do", total_todo)
        
        # Completion rate
        overall_completion = (total_completed / total_story_points * 100) if total_story_points > 0 else 0
        st.metric("Overall Completion Rate", f"{overall_completion:.1f}%")
        
        # Status distribution
        st.subheader("Status Distribution")
        status_count = df['Status'].value_counts()
        st.bar_chart(status_count)
        
        # Blocked items
        st.subheader("Blocked Items")
        blocked_df = df[df['Blocked'] == 'Yes']
        if len(blocked_df) > 0:
            st.warning(f"⚠️ {len(blocked_df)} items are blocked")
            st.dataframe(blocked_df[['Sprint', 'Story', 'Status', 'StoryPoints']], width='stretch')
        else:
            st.success("✅ No blocked items")
    
    st.markdown("---")
    st.markdown("*Last updated: Real-time from sprint_data.csv*")
