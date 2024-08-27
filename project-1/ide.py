import streamlit as st
from streamlit_ace import st_ace

from program.Driver import compiler

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
# st.title("Compiler IDE")

# Spawn a new Ace editor
code = st_ace(
  placeholder='',
  theme='twilight',
  language='python',
  keybinding='vscode',
  height=300,
  min_lines=30,
  max_lines=None,
  font_size=14,
  tab_size=4,
  wrap=False
)

# Display editor's content as you type

def compile(code):
  try:
    result = compiler(code)
    return result
  except Exception as e:
    print("Error compiling code", e)

result, errors = compile(code)

# show the output of the compiler
result

# show the errors
if len(errors) > 0:
  st.write("Errors")
  errors