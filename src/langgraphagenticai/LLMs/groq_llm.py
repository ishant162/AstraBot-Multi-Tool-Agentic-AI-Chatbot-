import streamlit as st

from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls_input: dict):
        """
        Initialize the Groq LLM with the provided user controls input.

        Args:
            user_controls_input (dict): Dictionary containing user controls
            input, including the Groq API key and selected model.
        """
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        """
        Get the Groq LLM model based on user input.

        Returns:
            ChatGroq: An instance of the Groq LLM model.
        """
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get(
                "selected_groq_model"
            )

            if not groq_api_key:
                st.error(
                    "Please enter your Groq API key to proceed. Don't have one?"
                    "Visit https://console.groq.com/ to get started."
                )

            llm = ChatGroq(
                model=selected_groq_model, groq_api_key=groq_api_key
            )

        except Exception as e:
            raise ValueError(
                f"An error occurred while initializing the Groq LLM: {e}"
            )

        return llm
