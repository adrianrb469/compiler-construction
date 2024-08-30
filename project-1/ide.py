import streamlit as st
from streamlit_ace import st_ace
from program.Driver import compiler

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
        language="python",
        keybinding="vscode",
        height=700,
        min_lines=35,
        max_lines=None,
        font_size=14,
        tab_size=4,
        wrap=False,
    )

with col2:
    result, errors = compiler(code)

    if result:
        st.subheader("Parse Tree")
        with st.container(height=200, border=False):

            st.code(result, language="text")
    else:
        st.markdown(
            '<div class="output-content">No output</div>', unsafe_allow_html=True
        )

    if errors:

        st.subheader("Errors")
        with st.container(height=500, border=False):

            for error in errors:
                st.error(error)

    st.markdown("</div>", unsafe_allow_html=True)
