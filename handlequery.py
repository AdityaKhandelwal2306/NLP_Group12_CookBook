from nltk.tokenize import word_tokenize

def handle_question(question, platform):
    tokens = word_tokenize(question.lower())
    base_url = "https://www.youtube.com/results?search_query=" if platform == "YouTube" else "https://www.google.com/search?q="
    search_query = "+".join(tokens)
    search_url = f"{base_url}{search_query}"
    return search_url
