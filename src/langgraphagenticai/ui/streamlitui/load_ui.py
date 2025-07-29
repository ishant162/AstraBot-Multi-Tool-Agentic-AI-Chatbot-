import os
import streamlit as st

from src.langgraphagenticai.ui.ui_config_file import Config

class LoadStreamlitUI:
    def __init__(self, ):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self, session_id=None):
        st.set_page_config(
            page_title=self.config.get_page_title(),
            layout="wide"
        )
        st.header(self.config.get_page_title())
        st.session_state.time_frame = ""
        st.session_state.IsFetchButtonClicked = False
        
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls['selected_llm'] = st.selectbox(
                "Select LLM",
                llm_options,
                key=f"llm_selectbox_{session_id}"
            )
            
            if self.user_controls['selected_llm'] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox(
                    "Select Groq Model",
                    model_options,
                    key="groq_model_selectbox"
                )
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API KEY", type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API key to proceed. Don't have one? Visit https://console.groq.com/ to get started.")
                    
            # Usecase selection
            self.user_controls['selected_usecase'] = st.selectbox(
                "Select Use Cases",
                usecase_options,
                key="usecase_selectbox"
            )
            
            if self.user_controls['selected_usecase'] in ["Chatbot with WebSearch", "AI News"]:
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY_API_KEY", type="password")
                
                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API key to proceed. Don't have one? Visit https://tavily.com/ to get started.")
            
            if self.user_controls['selected_usecase'] == "AI News":
                st.subheader("AI News Explorer")
                
                with st.sidebar:
                    time_frame = st.selectbox(
                        "Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0,
                    )
                if st.button("Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.time_frame = time_frame
               
        return self.user_controls