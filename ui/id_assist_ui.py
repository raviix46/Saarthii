import gradio as gr
import os
import pandas as pd
import re

BASE_DIR = "data/ID"

# Utility functions
def get_subfolders(path):
    try:
        return sorted([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    except Exception:
        return []

def get_csv_files(path):
    try:
        return sorted([f for f in os.listdir(path) if f.endswith(".csv")])
    except Exception:
        return []

def get_csv_preview(path):
    try:
        df = pd.read_csv(path)
        df = df.head(1).transpose()
        df.columns = ["Details"]
        df.index.name = "Field"

        # Fields that should display step-wise bullets
        stepwise_fields = {"Step_by_Step_Guide", "Required_Documents", "Eligibility_Criteria"}

        def format_details(text, field_name):  # FIXED indentation
            if not isinstance(text, str):
                return ""

            # Special handling for Direct_Link field
            if field_name == "Direct_Link":
                url = text.strip()
                if url:
                    return f'<a href="{url}" target="_blank" style="color:#33ccff;">{url}</a>'
                else:
                    return ""

            # Step formatting for multi-step fields
            if field_name in stepwise_fields:
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                if len(lines) > 1:
                    cleaned_lines = [re.sub(r'^\d+\.\s*', '', line) for line in lines]
                    return "<br>".join([f"{i+1}. {line}" for i, line in enumerate(cleaned_lines)])
                else:
                    parts = re.split(r'(?<=\d)\.\s+', text)
                    parts = [p.strip() for p in parts if p.strip()]
                    if len(parts) > 1:
                        return "<br>".join([f"{i+1}. {part}" for i, part in enumerate(parts)])
                    else:
                        return text.strip()

            return text.strip()

        # Apply formatting based on field name
        df["Details"] = df.apply(lambda row: format_details(row["Details"], row.name), axis=1)

        # Generate HTML
        html = "<table style='width:100%; border-collapse: collapse;'>"
        html += "<thead><tr><th style='text-align:left; padding:6px; border-bottom:1px solid #ccc;'>Field</th>"
        html += "<th style='text-align:left; padding:6px; border-bottom:1px solid #ccc;'>Details</th></tr></thead><tbody>"

        for index, row in df.iterrows():
            html += "<tr>"
            html += f"<td style='vertical-align: top; padding:6px; font-weight: bold;'>{index}</td>"
            html += f"<td style='white-space: pre-wrap; padding:6px;'>{row['Details']}</td>"
            html += "</tr>"

        html += "</tbody></table>"
        return html

    except Exception as e:
        return f"<div style='color:red;'>⚠️ Error: {str(e)}</div>"

def reset_all():
    return None, None, gr.update(choices=[], visible=False), ""

# Main PehchaanSetu UI tab
def get_id_assist_tab():
    with gr.Tab("🪪 PehchaanSetu"):
        gr.Markdown(
            """
            <div style='font-size: 18px; color: #ffffff; line-height: 1.8; max-width: 850px; padding: 10px 20px; text-align: center; margin: auto;'>
                Get step-by-step guidance for your most essential identity documents <strong>Aadhaar</strong>, <strong>PAN</strong>, <strong>Voter ID</strong><br>
                and more all in one place, simplified and accessible.<br>
                <strong style="color:#ff6600;">Empower yourself, Know the process, Own your identity with PehchaanSetu.</strong>
            </div>
            """
        )

        with gr.Row():
            id_type = gr.Dropdown(label="🗂 ID Type", choices=get_subfolders(BASE_DIR), value=None, interactive=True)
            sub_category = gr.Dropdown(label="🎯 Purpose", choices=[], value=None, interactive=True)
            csv_file = gr.Dropdown(label="📄 CSV File", choices=[], interactive=True, visible=False)

        output_html = gr.HTML(label="📘 Field-Wise Information")
        reset_btn = gr.Button("🔁 Reset", elem_id="id-reset-btn")

        # Dropdown logic
        id_type.change(
            lambda t: gr.update(choices=get_subfolders(f"{BASE_DIR}/{t}"), value=None) if t else gr.update(choices=[], value=None),
            inputs=id_type, outputs=sub_category
        )

        sub_category.change(
            lambda t, s: (
                gr.update(choices=[], visible=False),
                get_csv_preview(f"{BASE_DIR}/{t}/{s}/{files[0]}") if len(files := get_csv_files(f"{BASE_DIR}/{t}/{s}")) == 1 else "",
                gr.update(choices=files, value=None, visible=True) if len(files) > 1 else gr.update(choices=[], visible=False)
            ),
            inputs=[id_type, sub_category],
            outputs=[csv_file, output_html, csv_file]
        )

        csv_file.change(
            lambda t, s, f: get_csv_preview(f"{BASE_DIR}/{t}/{s}/{f}") if t and s and f else "",
            inputs=[id_type, sub_category, csv_file],
            outputs=output_html
        )

        reset_btn.click(
            reset_all,
            inputs=[], outputs=[id_type, sub_category, csv_file, output_html]
        )