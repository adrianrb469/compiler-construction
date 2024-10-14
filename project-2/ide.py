import streamlit as st
from streamlit_ace import st_ace
from program.compiler import compile

# Streamlit configuration
st.set_page_config(layout="wide")


# Helper function to display the editor
def show_editor(default_code=""):
    return st_ace(
        placeholder="Type your Compiscript code here...",
        theme="dracula",  # Changed theme to 'dracula' for better color contrast
        language="java",  # Still using 'java' as it’s close to Compiscript
        keybinding="vscode",
        height=1000,
        min_lines=35,
        font_size=14,
        tab_size=4,
        wrap=False,
    )


# Helper function to display TAC and errors
def display_compilation_output(tac, errors):
    if errors is None:
        st.subheader("Compiled Three-Address Code")
        # Display the formatted TAC code with correct language (text or other)
        with st.container(height=1000, border=False):
            st.code(tac, language="text", line_numbers=True)

    else:
        st.subheader("Compilation Errors")
        st.error("The following errors were found during compilation:")
        for error in errors:
            st.error(f"• {error}")


# App Layout
st.title("Compiscript IDE")

# Two-column layout
col1, col2 = st.columns([1, 1])  # Keeping equal width for editor and output

with col1:
    st.subheader("Code Editor")
    code = show_editor()

with col2:

    if code:
        tac, table, errors, _ = compile(code)

        # Create tabs for the TAC output and Symbol Table
        tab1, tab2 = st.tabs(["Three-Address Code", "Symbol Table"])

        with tab1:
            display_compilation_output(tac, errors)

        with tab2:
            # Display Symbol Table if no errors
            if errors is None:
                st.subheader("Symbol Table")
                st.json(table)

# Footer with some credits or description
st.markdown(
    """
    <hr>
    <small>Created with Streamlit & Ace Editor</small>
    """,
    unsafe_allow_html=True,
)
