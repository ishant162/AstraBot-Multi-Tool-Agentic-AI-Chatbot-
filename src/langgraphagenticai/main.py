import streamlit as st
import uuid
from src.langgraphagenticai.ui.streamlitui.load_ui import LoadStreamlitUI

def load_langgraph_agentic_app():
    """
    Load and runs AgenticAI Application using Streamlit UI.
    This function initializes the Streamlit UI, handles user input, configures the LLM model.
    sets up the graph bases on the selected use case, and displays the output while implementing
    exception handling for robustness.
    """
    
    # Generate a unique ID for this session if not already present
    if "ui_session_id" not in st.session_state:
        st.session_state.ui_session_id = str(uuid.uuid4())[:8]
    session_id = st.session_state.ui_session_id

    # LoadUI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui(session_id=session_id)

    if not user_input:
        st.error("No user input provided. Please select options from the sidebar.")
        return
    
    user_message = st.chat_input("Enter your message here:")
    