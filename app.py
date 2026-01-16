import streamlit as st
import json
import os

st.set_page_config(page_title="AI News Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center;'>📰 AI-Powered News Dashboard</h1>", unsafe_allow_html=True)

DATA_FILE = "/Users/sarthaksharna/AutoNews/src/news_data.json"

if not os.path.exists(DATA_FILE):
    st.warning("No data found. Run the pipeline first.")
    st.stop()

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

st.success(f"Loaded {len(data)} articles")

# Get unique categories
categories = sorted(set(item["predicted_label"] for item in data))

st.markdown("## Choose a Category")

cols = st.columns(len(categories))
selected_category = None

for col, cat in zip(cols, categories):
    with col:
        if st.button(cat, use_container_width=True):
            selected_category = cat

# If nothing clicked, default
if "selected_category" not in st.session_state:
    st.session_state.selected_category = categories[0]

if selected_category:
    st.session_state.selected_category = selected_category

st.divider()

# Filter articles
filtered_articles = [
    item for item in data
    if item["predicted_label"] == st.session_state.selected_category
]

st.markdown(f"## Articles in **{st.session_state.selected_category}**")

for item in filtered_articles:
    with st.container():
        st.markdown(
            f"""
            <div style="
                padding: 20px;
                border-radius: 12px;
                background: #1e1e1e;
                margin-bottom: 15px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            ">
                <h3>{item['title']}</h3>
                <p><b>Source:</b> {item['source']}</p>
                <p>{item['summary']}</p>
                <a href="{item['url']}" target="_blank">Read Full Article →</a>
            </div>
            """,
            unsafe_allow_html=True
        )
