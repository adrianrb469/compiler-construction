import streamlit as st
from streamlit_ace import st_ace
from program.compiler import compile

st.set_page_config(layout="wide")

# Your Streamlit app code
st.title("Compiscript")

# Create two columns with equal width
col1, col2 = st.columns(2)

with col1:
    # Spawn a new Ace editor
    code = st_ace(
        placeholder="",
        theme="twilight",
        language="java",
        keybinding="vscode",
        height=500,
        min_lines=35,
        max_lines=None,
        font_size=14,
        tab_size=4,
        wrap=False,
    )

with col2:
    tac, table, errors = compile(code)

    if errors is None:
        st.subheader("Compiled code")
        with st.container(height=200, border=False):
            st.code(tac, language="text")

    else:
        st.subheader("Errors")
        with st.container(height=500, border=False):

            for error in errors:
                st.error(error)

    st.markdown("</div>", unsafe_allow_html=True)

if errors is None:
    st.title("Symbol Table")
    st.json(table)
