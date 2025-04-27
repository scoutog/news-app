import openai
from openai import OpenAI
import requests
from datetime import datetime, timedelta
from tqdm import tqdm
import streamlit as st

def get_topical_news_stories(topic):
    """
    """
    from_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&sortBy=relevancy&apiKey={st.secrets["news"]["news_key"]}'

    response = requests.get(url)
    articles = response.json()['articles']
    
    return articles

def get_top_news_stories():
    """
    """
    from_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    url = f'https://newsapi.org/v2/top-headlines?country=us&from={from_date}&apiKey={st.secrets["news"]["news_key"]}'

    response = requests.get(url)
    articles = response.json()['articles']
    
    return articles


def generate_news_summaries(news_content):
    """
    """
    client = OpenAI(api_key=st.secrets["openai"]["openai_key"],)
    if news_content == None:
        output = "EMPTY"
    
    else:
        completion = client.chat.completions.create(
                  model="gpt-4o-mini-2024-07-18",

                  messages=[
                    {"role": "system", 
                     "content": """""Summarize this news story. Try to keep it to 5-8 sentences."""},

                    {"role": "user", 
                     "content": news_content}
                  ]
                )

        output = completion.choices[0].message.content
    
    return output

def do_stuff_on_page_load():
#     st.set_page_config(layout="wide", page_title="Quick News", #centered
#                       page_icon="📰")
    st.markdown(
        """
        <style>
        img {cursor: pointer; transition: all .2s ease-in-out;}
        img:hover {transform: scale(1.1);}
        </style>
        """,unsafe_allow_html=True,
    )
    
    dark = '''
    <style>
        .stApp {
        background-color: dark-gray;
        }
    </style>
    '''
    
    st.markdown(dark, unsafe_allow_html=True)
    
def apa_title_case(title):
    lowercase_words = {
        'a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'so', 'yet',
        'at', 'by', 'in', 'of', 'on', 'per', 'to', 'up', 'via', 'with'
    }
    
    words = title.split()
    if not words:
        return ''
    
    def capitalize(word):
        return word[0].upper() + word[1:] if word else ''
    
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in lowercase_words:
            result.append(capitalize(word))
        else:
            result.append(word.lower())
    
    return ' '.join(result)
