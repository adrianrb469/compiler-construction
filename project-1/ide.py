import streamlit as st
from streamlit_ace import st_ace

# Custom CSS to make the app full-width
st.markdown("""
<style>
.stApp {
    max-width: 100%;
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Your Streamlit app code
st.title("Compiler IDE")

# Spawn a new Ace editor
content = st_ace(
  placeholder='',
  theme='twilight',
  language='python',
  keybinding='vscode',
  height=600,
  min_lines=40,
  max_lines=None,
  font_size=14,
  tab_size=4,
  wrap=False
)

# Display editor's content as you type
content
