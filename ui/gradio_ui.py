import gradio as gr

from agent.party_agent import create_agent

# Stores the current agent in memory
current_agent = None


def connect(api_key):
    global current_agent

    try:
        current_agent = create_agent(api_key)
        return "✅ Connected Successfully!"
    except Exception as e:
        return f"❌ {e}"


def chat(message, history):

    global current_agent

    if current_agent is None:
        return "Please connect using your Gemini API Key first."

    try:
        response = current_agent.run(message)
        return str(response)

    except Exception as e:
        return str(e)


with gr.Blocks(title="Party Preparation Agent") as demo:

    gr.Markdown("# 🎉 Party Preparation Agent")

    gr.Markdown(
        "Paste your Gemini API Key below. "
        "The key is used only for this session and is not stored."
    )

    api_key = gr.Textbox(
        label="Gemini API Key",
        type="password",
        placeholder="AIza..."
    )

    connect_btn = gr.Button("Connect")

    status = gr.Textbox(
        label="Status",
        interactive=False
    )

    connect_btn.click(
        connect,
        inputs=api_key,
        outputs=status
    )

    gr.ChatInterface(
        fn=chat,
        title="Ask Alfred Anything"
    )
