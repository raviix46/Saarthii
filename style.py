# style.py
custom_css = """
body {
    background-color: #121212;
    color: white;
}

.centered-text {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
}


/* 🔵 Primary LawBot buttons (Get Answer) */
#lawbot-submit-btn {
    background-color: #1a237e !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px !important;
    padding: 10px 20px;
}

#lawbot-submit-btn:hover {
    background-color: #0f1a5e !important;
    cursor: pointer;
}

/* ⚪ Secondary button (Clear) */
#lawbot-clear-btn {
    background-color: #444444 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px !important;
    padding: 10px 20px;
}

#lawbot-clear-btn:hover {
    background-color: #333333 !important;
    cursor: pointer;
}

/* 📄 Tab highlight */
.tabitem.selected {
    color: #1a237e !important;
    border-bottom: 3px solid #1a237e !important;
}

/* 🔁 Reset Button Styling */
#id-reset-btn {
    background-color: #1a237e !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}

#id-reset-btn:hover {
    background-color: #0f1a5e !important;
    cursor: pointer;
}

/* 📄 Markdown cleanup */
.gr-markdown > div {
    background: transparent !important;
}
"""