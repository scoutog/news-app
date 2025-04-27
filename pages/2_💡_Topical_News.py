import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from streamlit_functions import *

st.set_page_config(page_title="The Brief", page_icon="📰", layout="centered")

st.subheader("📰 Topical News - Made Just for You")

st.write("Choose a topic and we'll find and summarize news stories.")

text_input = st.text_input(
    "👇",
    placeholder ='What type of news would you like to see?',
)

if text_input:
#     st.write("You entered: ", text_input)
    
    with st.spinner("Finding stories...", show_time=True):
        articles = get_topical_news_stories(text_input)
    articles = articles[0:8]
    
    # Add if all articles are blank a response that nothing came out

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
            st.header(f"[🔗]({url}) {apa_title_case(title)}")
            st.subheader(f"By {author} {name}, {formatted_date}")
    #         st.image(image_url)
    #         st.write(summary)
            st.markdown(
                f"""
                <div style="overflow: auto;">
                    <img src="{image_url}" style="float: left; width: 25%; margin-right: 20px; margin-bottom: 10px;" />
                    <p style="text-align: justify;">{summary}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("---")


