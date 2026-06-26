from smolagents import OpenAIModel


def load_model(api_key):

    model = OpenAIModel(
        model_id="gemini-2.5-flash",
        api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=api_key
    )

    return model
