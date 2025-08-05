# 🧠 Saarthi – Connecting Every Citizen to Justice and Identity Rights with AI

Saarthi is an open-source AI-powered web assistant designed to simplify **legal awareness** and **identity document assistance** for the common man. Built using Gradio, Sentence Transformers, and local knowledge bases, Saarthi bridges the gap between complex legal processes and everyday citizens.

> ⚖️ Whether you're confused about your rights or unsure where to begin your ID application, Saarthi is here to guide you — anytime, anywhere.

---

## 🧭 Why Saarthi Matters

In India, many citizens don’t know where to begin when it comes to legal rights or ID corrections. Saarthi makes complex legal and bureaucratic processes understandable and accessible — especially for underrepresented communities.

It’s not just an AI project. It’s a public good.

---

## 🔍 Features

### 🟠 NyaySetu – Legal Q&A Chatbot
> _"Accurate, easy-to-understand legal help — anytime, anywhere."_

- Ask natural language questions about Indian laws (e.g., _"What is Section 498A?"_)
- Powered by **semantic retrieval** using MiniLM embeddings
- Trained on curated legal Q&A datasets
- Instant responses from offline-embedded knowledge (no API needed)
  
### 🪪 PehchaanSetu – Identity Document Guide
> _"Empower yourself. Know the process. Own your identity."_

- Get step-by-step guidance for applying, correcting, or reprinting:
  - Aadhaar
  - PAN Card
  - Voter ID
  - Caste Certificate
  - Driving License
  - Passport
  - Ration Card
- All guidance is loaded dynamically from local folders
- Dropdown-based interface with **zero typing needed**

---

## 🧠 How it Works

### 🔹 Legal Q&A Flow
1. Load precomputed MiniLM embeddings from `qa_embeddings.pkl`
2. Compute embedding for user query
3. Use cosine similarity to find the best match
4. Return the legally accurate, beginner-friendly response

### 🔹 ID Assistance Flow
1. User selects ID Type and Purpose
2. `id_assist_interface.py` dynamically constructs path
3. Loads `.txt` or `.md` from corresponding folder
4. Renders guidance with basic formatting

---

## 🚀 Try it Out (Hugging Face Space)

> 👉 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/raviix46/Saarthi)

---

## ⚙️ Installation (For Local Development)

```bash
git clone https://github.com/raviix46/Saarthi.git
cd Saarthi
pip install -r requirements.txt
python app.py
