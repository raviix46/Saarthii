import gradio as gr
from ui.gradio_ui import get_ui       # Main UI structure
from style import custom_css          # Custom CSS for styling

# Gradio app with custom CSS and UI
with gr.Blocks(css=custom_css) as demo:
    get_ui()  # Loads all tabs including PehchaanSetu and others

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()