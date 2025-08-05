import gradio as gr
from modules.lawbot.interface import lawbot_interface

def get_lawbot_tab():
    with gr.Tab("⚖️ NyaySetu"):
        gr.Markdown(
            """
            <div style='font-size: 18px; color: #ffffff; line-height: 1.8; max-width: 850px; padding: 10px 20px; text-align: center; margin: auto;'>
                Whether you’re confused about your rights or unsure where to begin,<br>
                <strong style="color:#ff6600;">NyaySetu gives you accurate, easy-to-understand legal help — anytime, anywhere.</strong>
            </div>
            """
        )

        with gr.Row():
            with gr.Column(scale=1):
                question = gr.Textbox(
                    label="Ask a Question",
                    placeholder="e.g., What is Section 498A?"
                )
                get_answer_btn = gr.Button("Get Answer", elem_id="lawbot-submit-btn")
                clear_btn = gr.Button("Clear", elem_id="lawbot-clear-btn")

            with gr.Column(scale=1):
                answer = gr.Textbox(
                    label="Answer",
                    interactive=False,
                    lines=7
                )

        # Connect buttons to functions
        get_answer_btn.click(fn=lawbot_interface, inputs=question, outputs=answer)
        clear_btn.click(fn=lambda: ("", ""), inputs=[], outputs=[question, answer])