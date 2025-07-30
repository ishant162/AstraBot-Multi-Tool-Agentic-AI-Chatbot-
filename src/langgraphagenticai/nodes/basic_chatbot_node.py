from src.langgraphagenticai.state.state import State


class BasiChatbotNode:
    """
    Basic chatbot login implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the state using the LLM model to generate a response.

        """
        return {"messages": self.llm.invoke(state["messages"])}
