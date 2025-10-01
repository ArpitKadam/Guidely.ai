from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from src.logger import logger
from src.exception import CustomException
from src.utils.models import ModelLoader
from src.prompts.system_prompt import SYSTEM_PROMPT
from src.tools.weather_info_tool import WeatherInfoTool
from src.tools.place_search_tool import PlaceSearchTool
from src.tools.expense_calculator_tool import CalculatorTool
from src.tools.currency_converter_tool import CurrencyConverterTool


class GraphBuilder:
    """
    Builds a LangGraph agent pipeline for a travel planner with integrated tools:
    
    Tools included:
    - Weather information
    - Place search (attractions, restaurants, activities, transport)
    - Currency conversion
    - Expense calculation
    
    The agent uses a system prompt for structured travel planning responses.
    """

    def __init__(self, model_provider: str = "groq"):
        """
        Initialize the GraphBuilder with LLM and integrated tools.

        Parameters
        ----------
        model_provider : str, optional
            The LLM provider to load, by default "groq".
        """
        try:
            logger.info("Initializing GraphBuilder...")

            # Load LLM
            self.model_loader = ModelLoader(model_provider=model_provider)
            self.llm = self.model_loader.load_llm()

            # Initialize tools
            self.weather_tools = WeatherInfoTool()
            self.place_search_tools = PlaceSearchTool()
            self.calculator_tools = CalculatorTool()
            self.currency_converter_tools = CurrencyConverterTool()

            # Merge all tools
            self.tools = [
                *self.weather_tools.weather_tool_list,
                *self.place_search_tools.place_search_tool_list,
                *self.calculator_tools.calculator_tool_list,
                *self.currency_converter_tools.currency_converter_tool_list,
            ]

            # Bind tools to LLM
            self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
            self.graph = None
            self.system_prompt = SYSTEM_PROMPT

            logger.info("GraphBuilder initialized successfully.")

        except Exception as e:
            logger.exception("GraphBuilder initialization failed.")
            raise CustomException(f"GraphBuilder init failed: {e}")

    def agent_function(self, state: MessagesState) -> dict:
        """
        Main agent function. Receives user messages, prepends system prompt, 
        and invokes the LLM with tools.

        Parameters
        ----------
        state : MessagesState
            Current messages state in the LangGraph.

        Returns
        -------
        dict
            Dictionary containing the response messages.
        """
        try:
            logger.info("Agent function invoked.")
            user_question = state["messages"]

            # Prepend system prompt
            input_question = [self.system_prompt] + user_question

            # Invoke LLM with tools
            response = self.llm_with_tools.invoke(input_question)
            logger.debug(f"Agent response generated: {response}")
            return {"messages": [response]}

        except Exception as e:
            logger.exception("Agent function execution failed.")
            raise CustomException(f"Agent function failed: {e}")

    def build_graph(self):
        """
        Build and compile the LangGraph execution pipeline with tools and agent.

        Returns
        -------
        Compiled LangGraph object
        """
        try:
            logger.info("Building LangGraph pipeline...")

            graph_builder = StateGraph(MessagesState)
            graph_builder.add_node("agent", self.agent_function)
            graph_builder.add_node("tools", ToolNode(tools=self.tools))

            # Define edges
            graph_builder.add_edge(START, "agent")
            graph_builder.add_conditional_edges("agent", tools_condition)
            graph_builder.add_edge("tools", "agent")
            graph_builder.add_edge("agent", END)

            # Compile graph
            self.graph = graph_builder.compile()
            logger.info("LangGraph pipeline built successfully.")
            return self.graph

        except Exception as e:
            logger.exception("Graph build failed.")
            raise CustomException(f"Graph build failed: {e}")

    def __call__(self):
        """
        Callable interface. Returns the compiled graph.

        Returns
        -------
        Compiled LangGraph object
        """
        return self.build_graph()
