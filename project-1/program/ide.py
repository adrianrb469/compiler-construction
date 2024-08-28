import streamlit as st
from streamlit_ace import st_ace

from program.Driver import compilador

# Custom CSS to make the app full-width
st.markdown(
    """
<style>
.stApp {
    max-width: 100%;
    padding-top: 2rem;
}
</style>
""",
    unsafe_allow_html=True,
)

# Your Streamlit app code
st.title("Compiler IDE")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # Spawn a new Ace editor
    code = st_ace(
        placeholder="",
        theme="twilight",
        language="python",
        keybinding="vscode",
        height=500,
        min_lines=35,
        max_lines=None,
        font_size=14,
        tab_size=4,
        wrap=False,
    )


def compile(code):
    try:
        result = compilador(code)
        return result
    except Exception as e:
        return f"Error compiling code: {e}"


with col2:
    result = compile(code)
    st.write(result)
