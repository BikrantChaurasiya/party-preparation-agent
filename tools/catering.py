from smolagents import tool


@tool
def catering_services_tool(query: str) -> str:
    """
    This is a catering service tool that selects the highest-rated catering service.

    Args:
        query: Search term for finding a catering service.
    """

    services = {
        "Anand Caterings Co.": 4.3,
        "Maa Catering Pvt": 4.9,
        "Priya event planner": 3.9,
    }

    best_services = max(services, key=services.get)

    return best_services
