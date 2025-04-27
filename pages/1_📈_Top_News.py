import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from streamlit_functions import *

# do_stuff_on_page_load()
st.set_page_config(page_title="The Brief", page_icon="📰", layout="centered")

st.subheader("📰 Today's Top Stories - Summarized")

st.write("---")

with st.spinner("Finding stories...", show_time=True):
    articles = get_top_news_stories()
articles = articles[0:8]

with st.spinner("Generating summaries...", show_time=True):
    for article in articles:
        summary = generate_news_summaries(article['content'])
        article['summary'] = summary

    
for article in articles:
    if article['content'] == None:
        pass
    
    else:
        name = article['source']['name']
        author = article['author']
        if author == None:
            author = ''
        url = article['url']
        publish_date = article['publishedAt']
        title = article['title']
        summary = article['summary']
        image_url = article['urlToImage']
        formatted_date = datetime.strptime(publish_date, '%Y-%m-%dT%H:%M:%SZ').strftime('%m-%d-%Y')
        
        # Display content
        st.subheader(f"{apa_title_case(title)}")
        st.caption(f"By {author} {name}, {formatted_date}")
#         st.image(image_url)
#         st.write(summary)
        st.markdown(
            f"""
            <div style="overflow: auto;">
                <img src="{image_url}" style="float: left; width: 25%; margin-right: 20px; margin-bottom: 10px;" />
                <p style="text-align: justify;">{summary}\n</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write(f"\n\n🔗 _Want to read more?_ [_Click here_]({url})")
        st.markdown("---")

