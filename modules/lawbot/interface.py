from modules.lawbot.retriever import get_best_match

def lawbot_interface(query):
    if not query.strip():
        return "⚠️ Please enter a valid legal question."
    return get_best_match(query)