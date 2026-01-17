

class SentenceHandler():
    def __init__(self)
        self.


    def get_sentence():
        try:
            with open("sentences.json", "r") as f:
                all_sentences - json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            all_sentences = ["JSONDecodeError"]
