import gradio as gr
from ui.lawbot_ui import get_lawbot_tab
from ui.id_assist_ui import get_id_assist_tab

def get_ui():
    # 📌 Global disclaimer & note
    gr.Markdown(
        """
        <div style="background-color:#2a2a2a; padding: 15px; border-radius: 10px; border: 1px solid #444; 
                    text-align: center; font-size: 14px; color: #ddd; margin-bottom: 30px;">
            ⚠️ <strong>Disclaimer:</strong> This chatbot is intended for <strong>educational and demonstration purposes only</strong>. 
            It is <strong>not a substitute</strong> for professional legal advice or representation.<br><br>
            🕒 <strong>Note:</strong> The chatbot's responses may be slightly slow as the model is 
            <strong>large and runs on limited resources</strong> provided by the hosting environment.
        </div>
        """,
        elem_classes="centered-text"
    )

    # 🛡️ App Title
    gr.Markdown(
        """
        <div align='center' style='font-size: 32px; font-weight: bold; color: #ffffff; margin-top: 10px;'>
            🕊️ Saarthi – Connecting Every Citizen to Justice and Identity Rights with AI
        </div>
        """
    )

    gr.Markdown("---")

    # 📁 Tabs
    get_lawbot_tab()
    get_id_assist_tab()

    gr.Markdown("Made by TEAM AtoM⚡️", elem_classes="centered-text")