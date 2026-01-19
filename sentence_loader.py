import random
import json

class SentenceHandler():
    def __init__(self):
        self.get_sentence()

    def get_sentence(self):
        try:
            with open("sentences.json", "r") as f:
                self.sentences = json.load(f)
        except (FileNotFoundkrror, json.JSONDecodeError):
            self.sentences = ["SentenceHandler"]
    
    def random_sentence(self, difficulty = str):
        """" 
        User clicks "Hard".
        GUI tells the Engine: "Set mode to advanced."
        Engine calls: handler.random_sentence("advanced").
        Handler returns a complex sentence with punctuation and symbols.
        """
        if difficulty not in self.sentences:
            difficulty = "beginner"

        choice = random.choice(self.sentences[difficulty])
        
        print(f"Selected ({difficulty}): {choice}")
        
        return choice

