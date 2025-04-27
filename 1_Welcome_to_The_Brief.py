import streamlit as st
from streamlit_functions import do_stuff_on_page_load

st.set_page_config(page_title="The Brief", page_icon="📰", layout="centered")

do_stuff_on_page_load()

# st.title("📰 The Brief")

left_co, cent_co,last_co = st.columns([1,3,1])

with cent_co:
    st.image("data/logo_2.png", use_container_width=True)
    
st.subheader("When a headline isn’t enough and an article is too much")

st.write("---")

st.markdown("""

### 👋 Welcome to **The Brief** - News that fits your attention span

We scan the top new stories of the day and summarize them, giving you clean, readable updates on the world’s biggest stories — without the endless scrolling, clickbait, or noise. 

---

### 🧠 Why use The Brief?

- **Save time** – No need to sift through dozens of tabs or paywalls.
- **Stay informed** – Get the essence of each story in seconds.
- **Dig deeper only if you want to** – Each summary includes a link to the full article.

---

### 🚀 How to use The Brief

Use the **sidebar** on the left to explore:

- **Top News** – A daily roundup of major headlines with AI-generated summaries and links.
- **Topical News** – Focused news grouped by themes or user-selected topics (coming soon!).

Whether you're catching up on your commute, during lunch, or in line for coffee — The Brief helps you stay sharp, fast.

---

""")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("### Ready to dive in?")

with col2:
    if st.button("📈 Top News"):
        st.switch_page("pages/1_📈_Top_News.py")

with col3:
    if st.button("💡 Topical News"):
        st.switch_page("pages/2_💡_Topical_News.py")
        
st.write("---")

st.markdown(
    """
    <div style='text-align: center; font-size: 16px; margin-top: 20px;'>
        Made by <strong>Scout Oatman-Gaitan</strong> ·
        <a href="https://www.linkedin.com/in/scout-og/" target="_blank">LinkedIn</a> ·
        <a href="https://github.com/scoutog" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)



# The Brief
# Daily Drip
# Bite-Sized News
# CliffNotes Daily
# Skimline