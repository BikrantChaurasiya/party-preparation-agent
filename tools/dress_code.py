from smolagents import tool


@tool
def suggest_dress_code(occasion: str) -> str:
    """
    Suggests a dress code for both male and female guests based on the occasion.

    This function acts as a simple recommender system. It checks the occasion
    provided and returns a predefined dress code string suitable for that type of party.

    Args:
        occasion (str): The type of occasion for the party.
            Allowed values:
            - "casual"
            - "formal"
            - "superhero"
            - "wedding"
            - "beach"
            - "festival"
            - "cocktail"
            - "custom"

    Returns:
        str
    """

    if occasion == "casual":
        return "Male: Jeans and T-shirt | Female: Summer dress or casual top with jeans"

    elif occasion == "formal":
        return "Male: Suit and tie | Female: Evening gown or cocktail dress"

    elif occasion == "superhero":
        return "Male: Superhero costume (Batman, Superman) | Female: Superhero costume (Wonder Woman, Catwoman)"

    elif occasion == "wedding":
        return "Male: Sherwani or suit | Female: Saree, lehenga, or gown"

    elif occasion == "beach":
        return "Male: Shorts and linen shirt | Female: Sundress or beachwear"

    elif occasion == "festival":
        return "Male: Kurta with ethnic jacket | Female: Colorful ethnic wear or bohemian dress"

    elif occasion == "cocktail":
        return "Male: Blazer with trousers | Female: Cocktail dress or stylish jumpsuit"

    else:
        return "Male: Custom attire | Female: Custom attire"
