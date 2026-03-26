import streamlit as st
import random

st.set_page_config(page_title="AI Scrum Master", layout="wide")

st.title("🤖 AI Scrum Master Retrospective Tool")

# Create Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "😊 Mood",
    "📊 Sprint Insights",
    "🎯 AI Questions",
    "✅ Action Tracker"
])
with tab1:
    st.subheader("Team Mood Check")

    st.write("Select your mood:")

    col1, col2, col3, col4, col5 = st.columns(5)

    moods = {
        "😡": 1,
        "😟": 2,
        "😐": 3,
        "😊": 4,
        "🚀": 5
    }

    selected_mood = None

    for i, (emoji, value) in enumerate(moods.items()):
        if [col1, col2, col3, col4, col5][i].button(emoji):
            selected_mood = value
            st.session_state["last_mood"] = value

    if "last_mood" in st.session_state:
        mood = st.session_state["last_mood"]

        if mood <= 2:
            st.error("⚠️ Team morale is low")
        elif mood == 3:
            st.warning("🙂 Neutral mood")
        else:
            st.success("🚀 Positive team energy")
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

if selected_mood:
    st.session_state.mood_history.append(selected_mood)
  if st.session_state.mood_history:
    avg_mood = sum(st.session_state.mood_history) / len(st.session_state.mood_history)

    st.metric("Average Mood", f"{avg_mood:.2f}")

    if avg_mood < 2.5:
        st.error("Team is struggling 😟")
    elif avg_mood < 4:
        st.warning("Team is okay but needs improvement")
    else:
        st.success("Team is performing great 🚀")
import pandas as pd
import os

FILE_NAME = "sprint_data.csv"

with tab2:
    st.subheader("Sprint Insights Tracker")

    # Load existing data
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Sprint", "Committed", "Completed", "Scope Added"])

    # Input fields
    sprint_name = st.text_input("Sprint Name")
    committed = st.number_input("Committed Story Points", min_value=0)
    completed = st.number_input("Completed Story Points", min_value=0)
    scope_added = st.number_input("Scope Added During Sprint", min_value=0)

    # Add data
    if st.button("Add Sprint Data"):
        if sprint_name:
            new_row = pd.DataFrame([{
                "Sprint": sprint_name,
                "Committed": committed,
                "Completed": completed,
                "Scope Added": scope_added
            }])

            df = pd.concat([df, new_row], ignore_index=True)

            # Keep only last 6 sprints
            df = df.tail(6)

            # Save to CSV
            df.to_csv(FILE_NAME, index=False)

            st.success("Sprint data saved!")

    # Show data
    if not df.empty:
        st.write("### Last 6 Sprints")
        st.dataframe(df)
              st.write("### Trends")
st.line_chart(df.set_index("Sprint")[["Completed"]])
        avg_velocity = df["Completed"].mean()
        predictability = (df["Completed"].sum() / df["Committed"].sum()) * 100 if df["Committed"].sum() > 0 else 0
        scope_change = (df["Scope Added"].sum() / df["Committed"].sum()) * 100 if df["Committed"].sum() > 0 else 0

        col1, col2, col3 = st.columns(3)

        col1.metric("Avg Velocity", f"{avg_velocity:.2f}")
        col2.metric("Predictability %", f"{predictability:.2f}%")
        col3.metric("Scope Change %", f"{scope_change:.2f}%")
