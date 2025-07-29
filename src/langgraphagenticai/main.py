import streamlit as st
import uuid
from src.langgraphagenticai.ui.streamlitui.load_ui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groq_llm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

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
    
    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.time_frame
    else:
        user_message = st.chat_input("Enter your message here:")
    
    if user_message:
        try:
            # Configure the LLM model based on user input
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Failed to configure the LLM model. Please check your input.")
                return
            
            # Initialize and setup the graph based on use case
            usecase = user_input.get('selected_usecase')
            
            if not usecase:
                st.error("No use case selected. Please select a use case from the sidebar.")
                return
            
            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(
                    usecase, graph, user_message
                ).display_result_on_ui()
            except Exception as e:
                st.error(f"Error building graph: {e}")
                return
            
        except Exception as e:
            st.error(f"Error graph setup failed {e}")
            return