from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool
)

from config.model import load_model

from tools.menu import suggest_menu
from tools.dress_code import suggest_dress_code
from tools.catering import catering_services_tool


def create_agent(api_key):

    model = load_model(api_key)

    agent = CodeAgent(

        tools=[

            DuckDuckGoSearchTool(),

            suggest_menu,

            suggest_dress_code,

            catering_services_tool

        ],

        model=model,

        additional_authorized_imports=[
            "datetime"
        ]

    )

    return agent
